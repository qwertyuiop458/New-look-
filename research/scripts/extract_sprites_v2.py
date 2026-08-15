#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_sprites_v2.py — экспорт реальных спрайт-листов по формату a.java.

Формат (a.java a(byte[],int), восстановлен статически):
  [0..1]      2 байта пропускаются (++n)
  [2..5]      f = u32 LE
  [6..7]      c = u16 LE — число объектов
  объекты:    k=0: a u16, b u16, c u16, d u16 (8 Б)
              k=1/2: e u32, c u8, d u8 (6 Б)
  палитры:    n8 u16 записей: tag u8, f u16, g u16, d u8 (6 Б)
  [f&0x8000]: n10 u16 палитр: a[n10][4]
  b-записи:   n6 u16: tag u8, e u16 (, i u8 + k u16 если f&0x8000)
  f-записи:   n5 u16: f u8, g u8, i u16, j u16, h u8 (7 Б)
  e-записи:   n4 u16: e u8, h u16 (3 Б)
  FORMAT:     n10 u16 — пиксельный формат: 0x8888=ARGB32, 0x4444=ARGB4444, 0x6505=RGB565(+0xF81F alpha)
  g u8: число кадров; h u8 (0->256): пикселей на кадр
  a[g][h]     пиксели
  магия       25840 (0x64F0) u16 — анимационный лист (опционально)
  блоки:      c u16: число блоков, длины u16, данные

Запуск: python3 research/scripts/extract_sprites_v2.py
"""
import json
import struct
import sys
from pathlib import Path

JAR = Path("research/extracted/jar")
OUT = Path("research/analysis/v2/graphics/sprites")
PNG = Path("research/analysis/v2/graphics/png")

# (ресурс, сегмент, слот/назначение) из статического сценария g.g()
SPRITE_SOURCES = [
    ("m0", 0, "a[][0] menu/hero"), ("m0", 9, "a[][1]"), ("m2", 1, "a[][0]"),
    ("m2", 2, "a[][1]"), ("m2", 23, "a[][2]"), ("m7", 3, "a[][0]"),
    ("m7", 6, "a[][-1]"), ("m11_0", 4, "a[][0]"), ("m11_0", 5, "a[][5]"),
    ("m11_0", 7, "a[][1]"), ("m11_0", 11, "a[][2]"), ("m11_0", 12, "a[][3]"),
    ("m11_0", 13, "a[][4]"), ("m11_0", 14, "a[][6]"), ("m11_0", 19, "a[][8]"),
    ("m11_0", 20, "a[][9]"), ("m11_0", 21, "a[][7]"),
    ("m11_1", 8, "a[][0]"), ("m11_1", 10, "a[][1]"), ("m11_1", 15, "a[][2]"),
    ("m11_1", 16, "a[][3]"), ("m11_1", 17, "a[][4]"), ("m11_1", 18, "a[][5]"),
    ("m11_1", 22, "a[][6]"),
]


def read(p):
    d = (JAR / p).read_bytes()
    A = d[0]
    h = [struct.unpack("<I", d[1 + 4 * i:5 + 4 * i])[0] for i in range(A)]
    return d, A, h, 1 + 4 * A


def segof(name, n):
    d, A, h, base = read(name)
    if n + 1 >= A:
        return None
    return d[base + h[n] - h[0]:base + h[n + 1] - h[0]]


def parse_sprite_list(data):
    """Полный парсер a.java-листа. Возвращает dict."""
    if data is None or len(data) < 8:
        return None
    try:
        n = 0
        n += 1  # пропуск
        f = struct.unpack_from("<I", data, n + 1)[0]
        n += 5
        c = struct.unpack_from("<H", data, n)[0]
        n += 2
        objs = []
        for i in range(c):
            if n + 6 > len(data):
                return {"error": "truncated objects", "parsed_objs": len(objs)}
            tag = data[n]
            if tag == 255 or tag == 254:
                e = struct.unpack_from("<I", data, n + 1)[0]
                cc = data[n + 5]
                dd = data[n + 6] if n + 6 < len(data) else 0
                objs.append({"k": 1 if tag == 255 else 2, "e": e, "c": cc, "d": dd})
                n += 7
            else:
                a = struct.unpack_from("<H", data, n + 1)[0]
                b = struct.unpack_from("<H", data, n + 3)[0]
                cc = struct.unpack_from("<H", data, n + 5)[0]
                dd = struct.unpack_from("<H", data, n + 7)[0]
                objs.append({"k": 0, "a": a, "b": b, "c": cc, "d": dd})
                n += 9
        # палитра
        n8 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        pals = []
        for i in range(n8):
            if n + 6 > len(data):
                break
            pals.append({"tag": data[n], "f": struct.unpack_from("<H", data, n + 1)[0],
                         "g": struct.unpack_from("<H", data, n + 3)[0], "d": data[n + 5]})
            n += 6
        if (f & 0x8000) != 0:
            n10 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
            n += 2
            for i in range(n10):
                n += 4
        n6 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        brecs = []
        for i in range(n6):
            if n + 3 > len(data):
                break
            brecs.append({"tag": data[n], "e": struct.unpack_from("<H", data, n + 1)[0]})
            n += 3
            if (f & 0x8000) != 0:
                n += 1 + 2
        n5 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        frecs = []
        for i in range(n5):
            if n + 7 > len(data):
                break
            frecs.append({"f": data[n], "g": data[n + 1],
                          "i": struct.unpack_from("<H", data, n + 2)[0],
                          "j": struct.unpack_from("<H", data, n + 4)[0], "h": data[n + 6]})
            n += 7
        n4 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        erecs = []
        for i in range(n4):
            if n + 3 > len(data):
                break
            erecs.append({"e": data[n], "h": struct.unpack_from("<H", data, n + 1)[0]})
            n += 3
        # формат пикселей
        fmt = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        g = data[n] if n < len(data) else 0
        n += 1
        h = data[n] if n < len(data) else 0
        n += 1
        if h == 0:
            h = 256
        frames = []
        for fr in range(g):
            if n + h * (2 if fmt != 0x8888 else 4) > len(data):
                break
            px = []
            alpha = False
            for p in range(h):
                if fmt == 0x8888:
                    v = struct.unpack_from("<I", data, n)[0]
                    n += 4
                    px.append(v)
                    if (v & 0xFF000000) != 0xFF000000:
                        alpha = True
                elif fmt == 0x4444:
                    v = struct.unpack_from("<H", data, n)[0]
                    n += 2
                    a = (v >> 12) & 0xF
                    r = (v >> 8) & 0xF
                    gg = (v >> 4) & 0xF
                    b = v & 0xF
                    argb = (a << 28) | (r << 20) | (gg << 12) | (b << 4)
                    px.append(argb | (argb >> 4) & 0x0F0F0F0F)
                    if a != 0xF:
                        alpha = True
                elif fmt == 0x6505:
                    v = struct.unpack_from("<H", data, n)[0]
                    n += 2
                    if v == 0xF81F:
                        px.append(0)
                        alpha = True
                    else:
                        r = (v >> 11) & 0x1F
                        gg = (v >> 5) & 0x3F
                        b = v & 0x1F
                        px.append(0xFF000000 | (r << 19) | (gg << 10) | (b << 3))
                else:
                    return {"error": f"unknown pixel format 0x{fmt:04x}",
                            "objects": objs, "pos": n, "g": g, "h": h}
            frames.append({"frame": fr, "pixels": px, "alpha": alpha})
        magic = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        blocks = []
        if magic == 25840:
            bc = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
            n += 2
            for i in range(bc):
                if n + 2 > len(data):
                    break
                bl = struct.unpack_from("<H", data, n)[0]
                n += 2 + bl
                blocks.append(bl)
        return {"f": f, "objects": objs, "palettes": pals, "b_records": brecs,
                "f_records": frecs, "e_records": erecs, "pixel_format": fmt,
                "frames_count": g, "pixels_per_frame": h, "frames": frames,
                "magic": magic, "blocks": blocks, "end_pos": n, "size": len(data)}
    except Exception as e:  # noqa: BLE001
        return {"error": str(e)}


def write_png(path, frames, w, h, fmt_name):
    """Простой PNG-энкодер (RGBA). Кадры выкладываются в ряд."""
    try:
        import zlib
        import struct as st
    except Exception:
        return False
    total_w = w * len(frames)
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        for fr in frames:
            for x in range(w):
                px = fr["pixels"][y * w + x]
                raw += bytes([(px >> 16) & 0xFF, (px >> 8) & 0xFF, px & 0xFF, (px >> 24) & 0xFF])
    def chunk(tag, data):
        c = st.pack(">I", len(data)) + tag + data
        return c + st.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", st.pack(">IIBBBBB", total_w, h, 8, 6, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    png += chunk(b"IEND", b"")
    path.write_bytes(png)
    return True


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    PNG.mkdir(parents=True, exist_ok=True)
    results = []
    for (name, seg, slot) in SPRITE_SOURCES:
        data = segof(name, seg)
        if data is None:
            results.append({"resource": name, "segment": seg, "slot": slot, "error": "UNREACHABLE"})
            continue
        parsed = parse_sprite_list(data)
        if parsed is None or "error" in parsed:
            results.append({"resource": name, "segment": seg, "slot": slot,
                            "error": parsed.get("error") if parsed else "TOO_SHORT",
                            "head": data[:16].hex()})
            continue
        # сохранить метаданные
        meta = {k: v for k, v in parsed.items() if k != "frames"}
        meta.update({"resource": name, "segment": seg, "slot": slot,
                     "size": len(data), "sha256": __import__("hashlib").sha256(data).hexdigest()})
        results.append(meta)
        # PNG
        frames = parsed["frames"]
        w = 16
        h = parsed["pixels_per_frame"]
        if h % 16 == 0:
            pass
        if len(frames) and len(frames[0]["pixels"]) == h:
            w = 16 if h % 16 == 0 and h >= 16 else (h if h < 16 else 1)
            try:
                ok = write_png(PNG / f"{name}_seg{seg}.png", frames, w, h,
                               hex(parsed["pixel_format"]))
            except Exception as e:
                ok = False
                meta["png_error"] = str(e)
            meta["png"] = str(PNG / f"{name}_seg{seg}.png") if ok else None
            meta["png_w"] = w
        print(f"{name} seg{seg}: fmt={parsed['pixel_format']:#06x} frames={parsed['frames_count']} "
              f"px/frame={parsed['pixels_per_frame']} objs={len(parsed['objects'])} "
              f"err={parsed.get('error')}")
    (OUT / "extracted-metadata.json").write_text(
        json.dumps({"sources": results}, indent=1, ensure_ascii=False))
    print("готово:", len(results), "ресурсов; PNG:", len(list(PNG.glob('*.png'))))


if __name__ == "__main__":
    sys.exit(main())
