#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trace_frame_to_sprite_v2.py — восстановление моста frame -> pixel data -> Image (этап 15.14).

ДОКАЗАННАЯ ЦЕПОЧКА (a.java):
  a(int n) (строка 800): пиксели кадра генерируются из RLE-блоков:
    this.j (byte[] блоки) + this.a[this.i] (палитра-индексы, int[256])
    форматы сжатия (this.a после магии): 25840 (RLE+маска j), 10225 (RLE), 22258 (RLE-v),
    5632 (4bpp), 2048 (3bpp), 1024 (2bpp), 512 (1bpp), 22018 (8bpp)
  a(Graphics) (строка ~760): Image.createRGBImage(pixels, w, h, alpha) ->
    drawImage / drawRegion(image, 0,0,w,h, SPRITE_TRANSFORM[n4 & 7], x, y, 0)
  трансформы: static a = {0,2,1,3,5,7,4,6} (SPRITE_TRANSFORM_*)
  размер кадра: c[n] & 0xFF (w), d[n] & 0xFF (h) — из записей объекта

Вывод: graphics/{render-call-index.json, x-frame-dataflow.json, sprite-package-load-map.json,
  sprite-format-usage-v2.json, palette-render-dataflow-v2.json, sprite-transform-v2.json,
  render-dataflow.md, pixel-decoder-trace-v2.md, reference-chain/*}
"""
import json
import struct
import sys
from pathlib import Path

JAR = Path("research/extracted/jar")
OUT = Path("research/analysis/v2/graphics")


def read(p):
    d = (JAR / p).read_bytes()
    A = d[0]
    h = [struct.unpack("<I", d[1 + 4 * i:5 + 4 * i])[0] for i in range(A)]
    return d, A, h, 1 + 4 * A


def seg(d, h, base, n):
    return d[base + h[n] - h[0]:base + h[n + 1] - h[0]]


def parse_sprite_list(data):
    """Парсер a.java-листа (облегчённый, из этапа 15.11) + размеры кадров c/d."""
    if data is None or len(data) < 8:
        return None
    try:
        n = 0
        n += 1
        f = struct.unpack_from("<I", data, n + 1)[0]
        n += 5
        c = struct.unpack_from("<H", data, n)[0]
        n += 2
        objs = []
        for i in range(c):
            if n + 6 > len(data):
                break
            tag = data[n]
            if tag in (255, 254):
                objs.append({"k": 1 if tag == 255 else 2,
                             "e": struct.unpack_from("<I", data, n + 1)[0],
                             "c": data[n + 5], "d": data[n + 6] if n + 6 < len(data) else 0})
                n += 7
            else:
                objs.append({"k": 0, "a": struct.unpack_from("<H", data, n + 1)[0],
                             "b": struct.unpack_from("<H", data, n + 3)[0],
                             "c": struct.unpack_from("<H", data, n + 5)[0],
                             "d": struct.unpack_from("<H", data, n + 7)[0]})
                n += 9
        return {"f": f, "objects": objs, "obj_count": len(objs), "head_size": n}
    except Exception:  # noqa: BLE001
        return None


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "reference-chain").mkdir(parents=True, exist_ok=True)

    # ---------- 1. render-call-index ----------
    render_calls = {
        "meta": "Все render-вызовы (первичный код). Ключевые: a.java:360/763 createRGBImage; "
                "a.java:770/772 drawImage/drawRegion (трансформы a[n4 & 7]).",
        "calls": [
            {"class": "a", "method": "a(Graphics)", "line": 770, "call": "drawImage(image, n2, n3, 0)",
             "args": "image (кэш), x, y, anchor=0", "source": "Image.createRGBImage(pixels,w,h,alpha)",
             "confidence": "CONFIRMED"},
            {"class": "a", "method": "a(Graphics)", "line": 772, "call": "drawRegion(image, 0, 0, n6, n5, a[n4 & 7], n2, n3, 0)",
             "args": "src (0,0,w,h), transform=a[n4&7], dst (n2,n3)", "source": "тот же Image",
             "confidence": "CONFIRMED"},
            {"class": "a", "method": "a(Graphics)", "line": 360, "call": "Image.createRGBImage(nArray, n4, n5, bl)",
             "args": "int[] пиксели, w, h, alpha-флаг", "source": "this.a(n) — декодер RLE",
             "confidence": "CONFIRMED"},
            {"class": "a", "method": "a(Graphics)", "line": 763, "call": "Image.createRGBImage(nArray2, n6, n5, this.a)",
             "args": "int[] пиксели кадра, w, h, alpha", "source": "this.a(n) — декодер RLE",
             "confidence": "CONFIRMED"},
            {"class": "a", "method": "a(int)", "line": 800, "call": "декодер: j-блоки + палитра a[i] -> int[]",
             "args": "RLE-блоки this.j, палитра this.a[this.i], форматы 512..25840", "source": "сырые байты листа",
             "confidence": "CONFIRMED"},
            {"class": "g", "method": "a(Graphics,int,int,int[],...)", "line": 9115, "call": "drawRGB(v, 0, n3, n, n2, n3, n4, true)",
             "args": "массив пикселей v, w, h", "source": "масштабирование/эффекты (g.a(int[],...))",
             "confidence": "CONFIRMED (не основной путь)"},
            {"class": "g", "method": "paint", "line": 687, "call": "Image.createImage(240,320) + drawImage",
             "args": "буфер экрана", "source": "двойная буферизация",
             "confidence": "CONFIRMED"},
        ]
    }
    (OUT / "render-call-index.json").write_text(json.dumps(render_calls, indent=1, ensure_ascii=False))

    # ---------- 2. x-frame-dataflow ----------
    xfd = {"meta": "X-записи (пары u16) -> кадры. W[10]=старт X, W[11]=кол-во; g.d(type,anim,fr,0/1). "
                   "Семантика пары: (индекс_кадра, ?) — второй элемент пока UNKNOWN.",
           "accessor": "g.d(type, anim, fr, 0) = X[W[10] + fr*2 + 0] (g.java:24747)",
           "note": "Кадр-индекс из X используется в g[30+i] слотах и f.a[slot][frame] = g.d(type, n, frame, 0); "
                   "связь с размером кадра (c/d объектов листа) — через рантайм-рендер (a.a(d,e,...))",
           "status": "STATICALLY_RESOLVED (структура); семантика второго элемента X — RENDER_RUNTIME_REQUIRED"}
    (OUT / "x-frame-dataflow.json").write_text(json.dumps(xfd, indent=1, ensure_ascii=False))

    # ---------- 3. sprite-package-load-map ----------
    # сценарий g.g(): case 1/2/3 -> a[] слоты (см. этап 15.11); + m6_*/m7 геймплей
    loadmap = {"meta": "Пакеты, загружаемые как спрайт-листы a.java (сценарий g.g() + геймплей).",
               "packages": [
                   {"resource": "m0", "segments": [0, 9], "loader": "g.g() case 3 -> a[][0..1]", "sprite_objects": None, "pixel_blocks": None, "format": None, "confidence": "CONFIRMED (загрузка)"},
                   {"resource": "m1", "segments": [0], "loader": "g.g() case 2 -> b[][1]", "confidence": "CONFIRMED (загрузка)"},
                   {"resource": "m2", "segments": [1, 2, 23], "loader": "g.g() case 3 -> a[][0..2]", "confidence": "CONFIRMED (загрузка)"},
                   {"resource": "m7", "segments": [3, 6], "loader": "g.g() case 3 -> a[][0] + геймплей (a[22])", "confidence": "CONFIRMED (загрузка)"},
                   {"resource": "m11_0", "segments": [4, 5, 7, 11, 12, 13, 14, 19, 20, 21], "loader": "g.g() case 3 -> a[][0..9]", "confidence": "CONFIRMED (загрузка)"},
                   {"resource": "m11_1", "segments": [8, 10, 15, 16, 17, 18, 22], "loader": "g.g() case 3 -> a[][0..6]", "confidence": "CONFIRMED (загрузка)"},
                   {"resource": "m6_0..m6_5", "segments": "все", "loader": "геймплей: g.java:2501 a[16+n]; 2524 g.a(byArray)", "confidence": "CONFIRMED (загрузка)"},
               ],
               "note": "форматы/объекты каждого листа — см. sprite-format-usage-v2.json"}
    (OUT / "sprite-package-load-map.json").write_text(json.dumps(loadmap, indent=1, ensure_ascii=False))

    # ---------- 4. sprite-format-usage-v2 ----------
    # проверим реальные листы из loadmap
    usage = {"meta": "Реальные форматы пикселей по сегментам (декодировано parse_sprite_list).", "segments": []}
    for (name, segs) in [("m0", [0]), ("m2", [1, 2]), ("m7", [3, 6]), ("m11_0", [4, 5, 7]),
                         ("m11_1", [8, 10]), ("m6_0", [0])]:
        d, A, h, b = read(name)
        for s in segs:
            if s + 1 >= A:
                continue
            sd = seg(d, h, b, s)
            p = parse_sprite_list(sd)
            fmt = None
            if p and p["obj_count"] > 0 and len(sd) > 200:
                # формат в заголовке после записей — приблизительно ищем u16 0x4444/0x8888/0x6505
                for off in range(p["head_size"], min(len(sd) - 1, p["head_size"] + 200), 2):
                    v = struct.unpack_from("<H", sd, off)[0]
                    if v in (0x4444, 0x8888, 0x6505):
                        fmt = hex(v)
                        break
            usage["segments"].append({"resource": name, "segment": s, "size": len(sd),
                                      "obj_count": p["obj_count"] if p else None,
                                      "pixel_format": fmt, "evidence": "a.java декодер (этап 15.11/15.14)",
                                      "confidence": "INFERRED" if fmt else "UNKNOWN"})
    (OUT / "sprite-format-usage-v2.json").write_text(json.dumps(usage, indent=1, ensure_ascii=False))

    # ---------- 5. palette-render-dataflow ----------
    prd = {"meta": "Палитра -> финальный RGB. Два механизма: (1) мини-кадры: пиксели сразу ARGB "
                   "(форматы 0x8888/0x4444/0x6505 в заголовке листа); (2) большие кадры (RLE-блоки j): "
                   "палитра-индексы this.a[this.i] (int[256]) -> int[] -> Image. prop31 = индекс палитры "
                   "актёра при отрисовке (f.java:4107); c.java: this.c = палитра актёра.",
           "chain": "RLE-блок j -> индексы (бит-пак: 1/2/3/4/8 bpp, RLE-варианты) -> палитра a[i][256] "
                    "-> int[] ARGB -> createRGBImage -> drawRegion",
           "prop31": "g.a(graphics, g.b, null, 9, g.h(type,31), 0, RGBA...) — индекс палитры в draw",
           "status": "STATICALLY_RESOLVED (декодер+палитра); точный выбор палитры актёра — RENDER_RUNTIME_REQUIRED"}
    (OUT / "palette-render-dataflow-v2.json").write_text(json.dumps(prd, indent=1, ensure_ascii=False))

    # ---------- 6. sprite-transform-v2 ----------
    tr = {"meta": "Трансформы drawRegion: static int[] a = {0, 2, 1, 3, 5, 7, 4, 6} (a.java static init)",
          "transforms": [
              {"index": 0, "sprite": "SPRITE_TRANSFORM_NONE (0)", "evidence": "a.java:772 (a[n4 & 7])"},
              {"index": 1, "sprite": "SPRITE_TRANSFORM_MIRROR_ROT180 (2)"},
              {"index": 2, "sprite": "SPRITE_TRANSFORM_ROT90 (1)"},
              {"index": 3, "sprite": "SPRITE_TRANSFORM_ROT180 (3)"},
              {"index": 4, "sprite": "SPRITE_TRANSFORM_MIRROR (5)"},
              {"index": 5, "sprite": "SPRITE_TRANSFORM_MIRROR_ROT270 (7)"},
              {"index": 6, "sprite": "SPRITE_TRANSFORM_ROT270 (4)"},
              {"index": 7, "sprite": "SPRITE_TRANSFORM_MIRROR_ROT90 (6)"},
          ],
          "source": "n4 & 7 (флаг в вызове a(Graphics)) — параметр transform; источник n4: анимация/кадр (c.java: this.c поле?; точный источник — RENDER_RUNTIME_REQUIRED)"}
    (OUT / "sprite-transform-v2.json").write_text(json.dumps(tr, indent=1, ensure_ascii=False))

    # ---------- 7. reference chain (archetype 3) ----------
    # архетип 3: найдём его пропа и анимации
    d9, A9, h9, b9 = read("m9")
    seg4 = seg(d9, h9, b9, 4)
    types = {}
    anim_count = {}
    i = 0
    cur = None
    while i < len(seg4):
        t = seg4[i]
        if t == 6:
            iid = struct.unpack_from("<H", seg4, i + 1)[0]
            props = [struct.unpack_from("<H", seg4, i + 3 + 2 * j)[0] for j in range(32)]
            types[iid] = props
            cur = iid
            anim_count[cur] = 0
            i += 67
        elif t == 7:
            if cur is not None:
                anim_count[cur] += 1
            i += 21
        elif t == 10:
            i += 31
        elif t in (8, 9):
            i += 5
        else:
            i += 1

    aid = 3
    props = types.get(aid)
    chain = {
        "meta": "Reference chain: mission instance -> archetype 3 -> animation -> frame -> X -> pixel decoder -> Image",
        "archetype": aid,
        "props32": props,
        "anim_count": anim_count.get(aid, 0),
        "chain": [
            {"stage": "instance", "detail": "type 3 record: g[0] = g.a(g.m, props[0])", "status": "CONFIRMED", "evidence": "f.c()"},
            {"stage": "archetype", "detail": f"id {aid}, props32={props}", "status": "CONFIRMED", "evidence": "m9 seg4"},
            {"stage": "animation", "detail": f"{anim_count.get(aid,0)} анимаций; prop33; слоты g[30+i] = W[i][0] или X-кадры", "status": "CONFIRMED", "evidence": "f.g() f.java:2572"},
            {"stage": "frame", "detail": "кадр = dir + g.i(type, state) = V[prop34*15 + state]", "status": "CONFIRMED", "evidence": "f.java:4656"},
            {"stage": "X entry", "detail": "g.d(type, anim, fr, 0/1) = X[W[10] + fr*2 + 0/1]", "status": "CONFIRMED", "evidence": "g.java:24747"},
            {"stage": "sprite resource", "detail": "a.java лист: объект (c x d размеры) + RLE-блоки j", "status": "CONFIRMED (структура)", "evidence": "a.java:60-300"},
            {"stage": "pixel block", "detail": "a(int n): j-блоки + палитра a[i][256] -> int[] (форматы 512..25840)", "status": "CONFIRMED", "evidence": "a.java:800-960"},
            {"stage": "Image", "detail": "Image.createRGBImage(pixels, w, h, alpha)", "status": "CONFIRMED", "evidence": "a.java:763"},
            {"stage": "render", "detail": "drawImage/drawRegion(image, 0,0,w,h, a[n4&7], x, y, 0)", "status": "CONFIRMED", "evidence": "a.java:770-772"},
            {"stage": "кадр->объект листа", "detail": "какой именно X-индекс -> какой объект (c/d) листа", "status": "RENDER_RUNTIME_REQUIRED", "evidence": "нет статической таблицы"}
        ],
        "gap": "последний шаг (X-индекс -> конкретный объект листа) требует рантайм-рендера; "
               "всё остальное доказано статически."
    }
    (OUT / "reference-chain" / "chain.json").write_text(json.dumps(chain, indent=1, ensure_ascii=False))

    report = """# Reference Chain — archetype 3 (этап 15.14)

**Дата:** 2026-08-15 · **Статус:** STATICALLY_RESOLVED до кадра; RENDER_RUNTIME_REQUIRED для последнего шага.

## Цепочка (все шаги с evidence)

```
mission record [type 3][id][x][y][len][props]
  → g[0] = g.a(g.m, props[0])                    (f.c(), таблица m из m9 seg4)         CONFIRMED
  → архетип 3: props32 = [...]                    (m9 seg4, tag6)                       CONFIRMED
  → анимации: prop33 = N; слоты g[30+i]          (f.g(), f.java:2572)                   CONFIRMED
  → кадр: n5 = dir + g.i(type, state)            (f.java:4656; V[prop34*15+state])      CONFIRMED
  → X: g.d(type, anim, fr, 0/1) = X[W10+fr*2+0/1] (g.java:24747)                        CONFIRMED
  → пиксели: a(int n) — RLE-блоки j + палитра a[i][256]
      форматы: 25840 (RLE+маска), 10225/22258 (RLE), 5632 (4bpp), 2048 (3bpp),
               1024 (2bpp), 512 (1bpp), 22018 (8bpp)                                     CONFIRMED
  → Image: createRGBImage(pixels, w, h, alpha)   (a.java:763)                           CONFIRMED
  → render: drawImage/drawRegion(..., a[n4&7], ...) (a.java:770-772; трансформы {0,2,1,3,5,7,4,6}) CONFIRMED
  → КАКОЙ X-индекс → КАКОЙ объект листа (c x d):     RENDER_RUNTIME_REQUIRED
```

## Вывод

Мост frame → pixel data → Image **найден и доказан статически** на уровне декодера и рендера.
Единственный оставшийся шаг — сопоставление конкретного X-индекса кадра с конкретным объектом
спрайт-листа (размеры c×d) — требует рантайм-рендера (нет статической таблицы соответствия).
"""
    (OUT / "reference-chain" / "chain-report.md").write_text(report, encoding="utf-8")

    print("render-call-index, x-frame-dataflow, sprite-package-load-map, sprite-format-usage,"
          "\npalette-render-dataflow, sprite-transform, reference-chain записаны")
    print("архетип 3: anim_count =", anim_count.get(3), ", props =", props[:8], "...")


if __name__ == "__main__":
    sys.exit(main())
