#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_x_to_sprite_map_v2.py — мост X-индекс -> sprite-list (этап 15.15).

ДОКАЗАННАЯ ЦЕПОЧКА (a.java):
  c.java:117: this.a.a(this.d, this.e, n, n2, this.c)   // d=анимация, e=КАДР
  a.java:570 a(n,n2,n3,n4): n5 = b[n] & 0xFF; цикл b(n, i, n2, n3, n4)   // b[n] = число компонентов
  a.java:574 b(n,i,n2,n3,n4): n13 = e[n] + i          // n13 = индекс записи
                            n7 = d[n13] & 0xFF       // флаги/высота
                            n6 = c[n13] & 0xFF | (n7 & 0xC0) << 2   // ИНДЕКС ОБЪЕКТА листа
                            f[n13], g[n13]           // смещения (x, y)
  → b(n6, n3, n4, n5 ^ n7 & 0xF)  (или a(n6,...))    // рендер объекта n6 листа
  → декодер a(n6): j-блоки + палитра -> пиксели; c[n6]&0xFF x d[n6]&0xFF размеры

ИТОГ: кадр (e из c.java) -> e[n] таблица -> c[n13] = ОБЪЕКТ ЛИСТА -> пиксели.
X-индекс (из X-пар) попадает в g[30+i] слоты -> f.a[slot][fr] -> c.java кадр e.

Вывод: research/analysis/v2/graphics/*.json (этап 15.15)
"""
import json
import sys
from pathlib import Path

OUT = Path("research/analysis/v2/graphics")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    # ---------- 1. sprite-object-creation ----------
    creation = {
        "meta": "Создание sprite-list объектов класса a (загрузчики).",
        "objects": [
            {"object": "g.a[slot]", "creation": "g.g() case 3: a[slot] = g.a(a[slot], n, n3, n4, n5, false)",
             "resource": "a[n] (m0/m1/m2/m7/m11_0/m11_1/m13_2...)", "segment": "n3",
             "slot": "n2 (0..9)", "fields": "a.a(сегмент) + f(a2,n,n2) кол-во + b(a2,n,n2,i) ремаппинг",
             "evidence": "g.java:2518-2540, 2803-2838", "confidence": "CONFIRMED"},
            {"object": "g.b[slot]", "creation": "g.g() case 2: b[slot] = ...; b[slot].b = 4",
             "resource": "a[n]", "segment": "n3", "slot": "n2",
             "evidence": "g.java:2499-2507", "confidence": "CONFIRMED"},
            {"object": "g.a[n][n2] (геймплейные листы)", "creation": "g.java:2501 (a[16+n] -> m6_*); 2524 g.a(byArray)",
             "resource": "m6_0..m6_5", "segment": "все", "slot": "a[16..21]",
             "evidence": "g.java:2501, 2524", "confidence": "CONFIRMED"},
            {"object": "геймплейные маски m7", "creation": "g.java:33601 a(n,n2,byArray): сегменты (n<<1)+1",
             "resource": "m7", "segment": "нечётные", "slot": "d[layer][chunk]",
             "evidence": "g.java:33601-33643", "confidence": "CONFIRMED"},
        ],
        "note": "индекс массива g.a[] НЕ равен resource ID: слоты назначаются сценарием (n2), ресурс задаётся (n)."
    }
    (OUT / "sprite-object-creation.json").write_text(json.dumps(creation, indent=1, ensure_ascii=False))

    # ---------- 2. sprite-slot-map ----------
    slots = {
        "meta": "Карта слотов g.a[]/g.b[] (из статического сценария g.g(), этап 15.11).",
        "slots": [
            {"slot": "a[][0]", "resource": "m0 seg0", "loader": "case 3 {1,0,0,-1,2}", "purpose": "menu/hero", "confidence": "CONFIRMED"},
            {"slot": "a[][1]", "resource": "m0 seg9", "loader": "case 3 {1,1,9,-1,2}", "purpose": "menu", "confidence": "CONFIRMED"},
            {"slot": "b[][1]", "resource": "m1 seg0", "loader": "case 2 {2,1,0,0,10}", "purpose": "menu", "confidence": "CONFIRMED"},
            {"slot": "a[][0]", "resource": "m2 seg1", "loader": "case 3 {3,0,1,0,4}", "purpose": "menu", "confidence": "CONFIRMED"},
            {"slot": "a[][1]", "resource": "m2 seg2", "loader": "case 3 {3,1,2,0,2}", "purpose": "menu", "confidence": "CONFIRMED"},
            {"slot": "a[][2]", "resource": "m2 seg23", "loader": "case 3 {3,2,23,0,2}", "purpose": "menu", "confidence": "CONFIRMED"},
            {"slot": "a[][0]", "resource": "m7 seg3", "loader": "case 3 {22,0,3,-1,9}", "purpose": "menu/фон", "confidence": "CONFIRMED"},
            {"slot": "a[][0..9]", "resource": "m11_0 seg 4,5,7,11,12,13,14,19,20,21", "loader": "case 3 {26,slot,seg,-1,2}", "purpose": "сцены", "confidence": "CONFIRMED"},
            {"slot": "a[][0..6]", "resource": "m11_1 seg 8,10,15,16,17,18,22", "loader": "case 3 {27,slot,seg,-1,2}", "purpose": "сцены", "confidence": "CONFIRMED"},
            {"slot": "a[16..21]", "resource": "m6_0..m6_5", "loader": "геймплей (2501)", "purpose": "ГЕЙМПЛЕЙ (уровни)", "confidence": "CONFIRMED"},
            {"slot": "a[22]", "resource": "m7", "loader": "геймплей (2501)", "purpose": "ГЕЙМПЛЕЙ", "confidence": "CONFIRMED"},
        ],
        "conclusion": "Геймплейные спрайт-листы = m6_0..m6_5 (слоты a[16..21]) и m7 (a[22]); "
                     "тайлы миссий, вероятно, из этих листов (числовая связь tile_id -> лист не доказана)."
    }
    (OUT / "sprite-slot-map-v2.json").write_text(json.dumps(slots, indent=1, ensure_ascii=False))

    # ---------- 3. sprite-loader-script-trace ----------
    loader = {
        "meta": "Трассировка записей сценарного загрузчика g.g() (case 1/2/3/9).",
        "records": [
            {"op": 1, "params": "{1, n8, n9}", "action": "a.a = g.b(n9) (спрайт-лист из сегмента n9 ресурса a[n8])", "evidence": "g.java:2438-2445"},
            {"op": 2, "params": "{2, n, n2, n3, n4, n5}", "action": "g.a(n8,n10,n11,n12,n13,b) (лист в b[]); b[slot].b=4", "evidence": "g.java:2450-2458"},
            {"op": 3, "params": "{3, n, n2, n3, n4, n5}", "action": "a[slot] = g.a(a[slot], n, n3, n4, n5, false) (лист в a[])", "evidence": "g.java:2459-2467"},
            {"op": 9, "params": "{9, n8, n17, n11, n18, n12, n19}", "action": "a[n11].a(n18, g.b(n17)) — загрузка кадра/листа в слот", "evidence": "g.java:2480-2498"},
            {"op": 11, "params": "{11, n21, n22}", "action": "g.a('/'+a[16+n21]) — открытие m6_* (геймплей)", "evidence": "g.java:2499"},
        ]
    }
    (OUT / "sprite-loader-script-trace-v2.json").write_text(json.dumps(loader, indent=1, ensure_ascii=False))

    # ---------- 4. x-index-to-sprite-dataflow ----------
    xfd = {
        "meta": "X-значение -> объект листа (ПОЛНАЯ ЦЕПОЧКА, доказана в a.java).",
        "chain": [
            {"stage": "X-пара", "detail": "g.d(type, anim, fr, 0/1) = X[W10 + fr*2 + 0/1]", "evidence": "g.java:24747"},
            {"stage": "слот анимации", "detail": "g[30+i] = f.b() (новый c-контроллер) с кадрами f.a[slot][fr] = g.d(type, n, fr, 0)", "evidence": "f.java:2719-2721, 2572"},
            {"stage": "кадр c.java", "detail": "c.java: this.d = анимация, this.e = кадр (продвигается по тикам)", "evidence": "c.java:44-130"},
            {"stage": "вызов рендера", "detail": "c.java:117: this.a.a(this.d, this.e, n, n2, this.c)", "evidence": "c.java:117"},
            {"stage": "таблица e/c/d листа", "detail": "a.java:574: n13 = e[n] + i; n6 = c[n13]&0xFF | (n7&0xC0)<<2 (ИНДЕКС ОБЪЕКТА); f/g[n13] = смещения", "evidence": "a.java:574-590"},
            {"stage": "объект листа", "detail": "b(n6, ...) -> декодер a(n6): j-блоки + палитра -> пиксели c[n6]x d[n6]", "evidence": "a.java:666-700, 800"},
            {"stage": "Image + draw", "detail": "createRGBImage -> drawImage/drawRegion(transform)", "evidence": "a.java:763-772"},
        ],
        "conclusion": "X-индекс кадра -> c.java кадр e -> e[n] таблица -> c[n13] = объект листа -> пиксели. МОСТ ДОКАЗАН.",
        "status": "STATICALLY_RESOLVED"
    }
    (OUT / "x-index-to-sprite-dataflow-v2.json").write_text(json.dumps(xfd, indent=1, ensure_ascii=False))

    # ---------- 6. palette-property-trace ----------
    pal = {
        "meta": "prop21 vs prop31.",
        "prop21": {"reads": ["g.java:17669 (n = g.h(f2.g[0], 21))", "g.java:21409 (g.l(n,11) звук?)"],
                   "chain": "g.h(type,21) -> n -> ... (контекст 17669: отрисовка HUD/диалога?)",
                   "status": "UNKNOWN (1 изолированный read; не доказано как palette)"},
        "prop31": {"reads": ["f.java:4107 (g.a(graphics, g.b, null, 9, g.h(type,31), 0, RGBA...))",
                             "f.java:4107 (g.h(type,31) + 1)"],
                   "chain": "g.h(type,31) -> аргумент draw (позиция 5) -> g.a(Graphics, image?, ..., index, ...) — похоже на ИНДЕКС КАДРА/ПАЛИТРЫ при отрисовке",
                   "status": "INFERRED (индекс при отрисовке; точная семантика RENDER_RUNTIME_REQUIRED)"},
        "c_palette": {"detail": "c.java: this.c = палитра актёра (передаётся в a.a(d, e, x, y, this.c)); a.java: кадр с палитрой c — отдельный механизм",
                      "status": "CONFIRMED (передача палитры актёра в рендер)"}
    }
    (OUT / "palette-property-trace-v2.json").write_text(json.dumps(pal, indent=1, ensure_ascii=False))

    # ---------- 7. transform source ----------
    tr = {
        "meta": "Источник n4 & 7 (transform) в drawRegion.",
        "analysis": [
            {"detail": "n4 в a.java a(Graphics) (строка 700+): параметр, приходящий из b(n,n2,n3,n4) (строка 666)",
             "evidence": "a.java:666-772"},
            {"detail": "b(n,n2,n3,n4): n4 используется как n5 (флаги) во внутреннем b(n,n2,n3,n4,n5): смещения f/g (n5&1/2), swap (n5&4), XOR n7&0xF",
             "evidence": "a.java:574-660"},
            {"detail": "c.java:117: this.a.a(this.d, this.e, n, n2, this.c) — n4 = this.c (палитра актёра!)",
             "evidence": "c.java:117"},
            {"detail": "вывод: n4 & 7 в drawRegion использует МЛАДШИЕ БИТЫ палитры актёра this.c как transform-флаг (не отдельный параметр!)",
             "evidence": "a.java:772 (a[n4 & 7]) + c.java:117 (n4 = this.c)"},
            {"detail": "альтернатива: в a(Graphics) (основной вызов) n4 может быть отдельным параметром вызова; оба пути существуют",
             "evidence": "a.java:511/516 (a(Graphics, n, n2, n3, n4, n5))"},
        ],
        "conclusion": "источник n4: (1) палитра актёра this.c из c.java:117; (2) отдельный параметр a(Graphics, ..., n4, n5) из других вызовов. "
                      "Точный источник для конкретного экземпляра — RENDER_RUNTIME_REQUIRED.",
        "status": "PARTIAL"
    }
    (OUT / "sprite-transform-source-v2.json").write_text(json.dumps(tr, indent=1, ensure_ascii=False))

    # ---------- 8. resource-to-sprite-object ----------
    rso = {
        "meta": "resource -> объект листа (структура a.java-листа; конкретные объекты — из данных)",
        "resources": [
            {"resource": "m6_0..m6_5", "slot": "a[16..21]", "objects": "листы a.java (объекты k=0/1/2, кадры c x d, RLE-блоки)", "confidence": "CONFIRMED (структура)"},
            {"resource": "m7", "slot": "a[22]", "objects": "листы + маски (сегменты нечётные)", "confidence": "CONFIRMED (структура)"},
            {"resource": "m0/m1/m2/m11_0/m11_1/m13_2", "slot": "a[][0..9], b[][1]", "objects": "листы сцен/меню", "confidence": "CONFIRMED (структура)"},
        ],
        "note": "привязка конкретного tile_id/X-индекса к объекту конкретного листа: RENDER_RUNTIME_REQUIRED (нет статической таблицы)"
    }
    (OUT / "resource-to-sprite-object-v2.json").write_text(json.dumps(rso, indent=1, ensure_ascii=False))

    # ---------- 9. reference chains (3) ----------
    chains = {
        "meta": "3 эталонные цепочки (архетип 3, враг 107, NPC через g.w). Все шаги CONFIRMED кроме последнего (X->объект листа) — "
                "теперь последний шаг = c[n13] (a.java:574) — доказан структурно!",
        "chains": [
            {"id": "chain-01", "archetype": 3, "instance": "mission_00 type3 record",
             "chain": "props[0] -> g.a(g.m) -> архетип 3 -> prop33 анимаций -> кадр (dir + g.i) -> X-пара -> g[30+i] слот -> c.java кадр e -> e[n] таблица -> c[n13] объект листа -> декодер RLE -> Image -> drawRegion",
             "status": "STATICALLY_RESOLVED (структура); конкретный номер объекта листа из данных листа m6_* — RENDER_RUNTIME_REQUIRED"},
            {"id": "chain-02", "archetype": 107, "instance": "mission_01+ type3 (46 записей)",
             "chain": "та же цепочка; архетип 107 (props: ai=?, анимации prop33)",
             "status": "STATICALLY_RESOLVED (структура)"},
            {"id": "chain-03", "archetype": "NPC (type 9)", "instance": "mission_00 type9 (23 записи)",
             "chain": "props[0] -> g.a(g.w) -> NPC-индекс (m9 seg8) -> NPS props (ag-таблица 15 полей) -> анимации -> ...",
             "status": "STATICALLY_RESOLVED (структура); NPC-анимации через g.k(type,3) инициализация"},
        ]
    }
    for c in chains["chains"]:
        (OUT / "reference-chains").mkdir(parents=True, exist_ok=True)
        (OUT / "reference-chains" / f"{c['id']}.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    (OUT / "reference-chains" / "chains-index.json").write_text(json.dumps(chains, indent=1, ensure_ascii=False))

    # ---------- 10/11. x-to-sprite-map (структурный) ----------
    xmap = {
        "meta": "X-индекс -> sprite: структурный маппинг (полная цепочка доказана; конкретные номера объектов зависят от данных листа).",
        "map": [
            {"x_index": "X[W10 + fr*2 + 0]", "sprite_slot": "g[30+i] (анимационный слот сущности)",
             "resource": "m6_* / m7 (геймплей)", "segment": "по загрузке уровня",
             "object": "c[n13] & 0xFF | (d[n13]&0xC0)<<2 (a.java:574)",
             "evidence": ["g.java:24747 (X)", "f.java:2719 (слоты)", "c.java:117 (кадр)", "a.java:574 (объект листа)"],
             "confidence": "STATICALLY_RESOLVED (структура); RENDER_RUNTIME_REQUIRED (конкретные значения)"}
        ],
        "ranges": {"max_X_entries": 36, "sprite_slots": "10 (сцены) + 6 (m6_*) + 1 (m7)",
                   "objects_per_list": "k=0/1/2 записи (c x d)", "note": "диапазоны НЕ совпадают численно — "
                   "связь через таблицы e/c/d листа, а не через ID"}
    }
    (OUT / "x-to-sprite-map-v2.json").write_text(json.dumps(xmap, indent=1, ensure_ascii=False))

    print("sprite-object-creation, sprite-slot-map, sprite-loader-script-trace, x-index-to-sprite-dataflow,")
    print("palette-property-trace, sprite-transform-source, resource-to-sprite-object, reference-chains, x-to-sprite-map — записаны")
    print("ИТОГ: X-index -> sprite-list bridge = STATICALLY_RESOLVED (a.java:574 c[n13])")


if __name__ == "__main__":
    sys.exit(main())
