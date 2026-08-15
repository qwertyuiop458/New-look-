#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_entity_animation_db.py — сборка entity/animation/frame базы (этап 15.11).

Источники:
  - m9 seg4 (dr(), g.java:24553): tag6 = архетип [id u16][32 x u16 props] (67 Б),
    tag7 = анимация [10 x u16] (21 Б), tag10 = кадр [15 x u16] (31 Б),
    tag8 = X [2 x u16] (5 Б), tag9 = Y [2 x u16] (5 Б)
  - доступы: g.h(type,prop)=U[T+prop]; g.d(type,anim,f)=W[P32+anim*13+f];
    g.i(type,f)=V[P34*15+f]; g.d(type,anim,fr,0/1)=X[X10+fr*2+0/1]
  - семантика свойств из ВСЕХ чтений g.h/g.i в g.java/f.java (собрано ниже)

Вывод: research/analysis/v2/entities/*.json, graphics/*.json, animation/…
"""
import json
import struct
import sys
from collections import Counter
from pathlib import Path

JAR = Path("research/extracted/jar")
OUT = Path("research/analysis/v2/entities")
GFX = Path("research/analysis/v2/graphics")
ANIM = Path("research/analysis/v2/animation")


def read(p):
    d = (JAR / p).read_bytes()
    A = d[0]
    h = [struct.unpack("<I", d[1 + 4 * i:5 + 4 * i])[0] for i in range(A)]
    return d, A, h, 1 + 4 * A


def seg(d, h, base, n):
    return d[base + h[n] - h[0]:base + h[n + 1] - h[0]]


# ---------------------------------------------------------------- 1. entity table
d9, A9, h9, b9 = read("m9")
seg4 = seg(d9, h9, b9, 4)
types = []
anims = []
frames = []
xs = []
ys = []
i = 0
while i < len(seg4):
    t = seg4[i]
    iid = struct.unpack_from("<H", seg4, i + 1)[0] if t == 6 else None
    if t == 6:
        props = [struct.unpack_from("<H", seg4, i + 3 + 2 * j)[0] for j in range(32)]
        types.append({"id": iid, "offset": i, "props32": props})
        i += 67
    elif t == 7:
        vals = [struct.unpack_from("<H", seg4, i + 1 + 2 * j)[0] for j in range(10)]
        anims.append({"offset": i, "raw10": vals})
        i += 21
    elif t == 10:
        vals = [struct.unpack_from("<H", seg4, i + 1 + 2 * j)[0] for j in range(15)]
        frames.append({"offset": i, "raw15": vals})
        i += 31
    elif t == 8:
        xs.append({"offset": i, "pair": [struct.unpack_from("<H", seg4, i + 1 + 2 * j)[0] for j in range(2)]})
        i += 5
    elif t == 9:
        ys.append({"offset": i, "pair": [struct.unpack_from("<H", seg4, i + 1 + 2 * j)[0] for j in range(2)]})
        i += 5
    else:
        i += 1

OUT.mkdir(parents=True, exist_ok=True)
ANIM.mkdir(parents=True, exist_ok=True)
GFX.mkdir(parents=True, exist_ok=True)

# 35 свойств: 32 из файла + 33(счётчик анимаций), 34(индекс frame), 32(старт анимаций W)
ent_table = {"meta": {"source": "m9 seg4 (dr() g.java:24553)", "parser": "tag6: [id u16][32 x u16 props] (67 Б)",
                      "props35": "32 из файла + кодом: prop32=старт в W, prop33=кол-во анимаций, prop34=индекс frame-записи (V)",
                      "names": "ARCHETYPE_XXX (семантические имена не присвоены без доказательства)"},
             "count": len(types), "archetypes": []}
for idx, t in enumerate(types):
    ent_table["archetypes"].append({
        "entity_id": t["id"], "name": f"ARCHETYPE_{t['id']:03d}",
        "record_offset": t["offset"],
        "props32": t["props32"],
        "prop32_anim_start": None, "prop33_anim_count": None, "prop34_frame_index": None,
        "note": "prop32/33/34 вычисляются кодом dr() и зависят от порядка записей",
    })
(OUT / "entity-table-v2.json").write_text(json.dumps(ent_table, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- 2. property semantics
PROP_SEM = {
    2: ("dir_offset", "INFERRED", "сдвиг направления (f.java:4618/4654 n += g.h(type,2); m(): n += g.h(type,2))"),
    3: ("dir_offset_alt", "INFERRED", "сдвиг для состояния g[12]==1 (f.java:4660 n += g.h(type,3))"),
    6: ("collision_size", "INFERRED", "размер бокса *16 (g.java:21399 k(type,6)*16)"),
    7: ("facing_range_a", "CONFIRMED", "диапазон направлений [n, n+4): f.s/I() (f.java:3667,4604: f2.a.d >= n2 && < n2+4)"),
    8: ("facing_range_b", "CONFIRMED", "второй диапазон направлений [n, n+4) (f.java:3668,4605)"),
    10: ("behavior_class", "CONFIRMED", "класс поведения ИИ: 0/3/5/7 — ветвления направлений/стрельбы; 1,2 — особые (f.java:2380,2637,3662,4603)"),
    12: ("prop12", "UNKNOWN", "5 чтений в f.java (контексты не изолированы)"),
    14: ("prop14", "UNKNOWN", "5 чтений в f.java"),
    15: ("flag15", "INFERRED", "бинарный флаг (f.java:4644 g.h(type,15)==1 ? 1 : 0)"),
    17: ("prop17", "UNKNOWN", "f.java:2 чтения"),
    18: ("prop18", "UNKNOWN", "f.java:1 чтение"),
    19: ("prop19", "UNKNOWN", "f.java:2 чтения"),
    20: ("prop20", "UNKNOWN", "g.java:2 чтения"),
    24: ("sprite_width", "INFERRED", "смещение X при отрисовке (f.java:4107,4720,4728 n5 = n + (g.h(type,24) + g[28]*4))"),
    25: ("prop25", "UNKNOWN", "f.java:1 чтение"),
    29: ("prop29", "UNKNOWN", "f.java:2 чтения"),
    31: ("prop31", "UNKNOWN", "f.java:2 чтения"),
    32: ("anim_start_W", "CONFIRMED", "старт анимаций в W (dr() g.java:24646; g.d(type,anim,f)=W[P32+anim*13+f])"),
    33: ("anim_count", "CONFIRMED", "число анимаций (dr() g.java:24677; циклы по g.h(type,33))"),
    34: ("frame_index_V", "CONFIRMED", "индекс frame-записи в V (dr() g.java:24681; g.i(type,f)=V[P34*15+f]; ==-1 => нет кадров)"),
}
props_out = {"meta": "семантика свойств по всем чтениям g.h(type,prop)/g.i(type,f) в g.java+f.java",
             "properties": []}
for p in range(35):
    if p in PROP_SEM:
        name, conf, desc = PROP_SEM[p]
        props_out["properties"].append({"property_index": p, "possible_semantics": name,
                                        "confidence": conf, "evidence": desc})
    else:
        props_out["properties"].append({"property_index": p, "possible_semantics": f"UNKNOWN_PROPERTY_{p}",
                                        "confidence": "UNKNOWN", "evidence": "нет чтений в исследованном коде"})
(OUT / "entity-properties-v2.json").write_text(json.dumps(props_out, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- 5. animation table
anim_table = {"meta": {"source": "m9 seg4 tag7: [10 x u16] (21 Б)", "count": len(anims),
                       "fields": "raw10 + кодом 3 поля: 10=X-старт (dr: W[++]=var10_12), 11=кол-во X-кадров (+1 при tag8), 12=Y-индекс (tag9)",
                       "accessor": "g.d(type, anim, f) = W[prop32 + anim*13 + f]",
                       "frame_sequence": "g.d(type, anim, fr, 0/1) = X[X10 + fr*2 + 0/1] — пары u16 (кадр, ?)"},
              "animations": []}
for a in anims:
    anim_table["animations"].append({"animation_offset": a["offset"], "raw10": a["raw10"]})
(ANIM / "animation-table-v2.json").write_text(json.dumps(anim_table, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- 6. frame table
frame_table = {"meta": {"source": "m9 seg4 tag10: [15 x u16] (31 Б)", "count": len(frames),
                        "note": "V[15] = смещения кадров по состояниям g[12]: f.a() switch: g.i(type,0..13) для состояний "
                                "0/6/28,1,2,3,4,7,8,9,5,10,11,12,13; g.i(type,14) — отдельное использование (g.java:2935). "
                                "3 записи != 3 визуальных кадра: это НАБОРЫ смещений (вероятно для 3 групп L).",
                        "accessor": "g.i(type, f) = V[prop34*15 + f] (g.java:24765)"},
               "frames": [{"frame_offset": f["offset"], "raw15": f["raw15"]} for f in frames],
               "x_table": {"count": len(xs), "accessor": "g.d(type,anim,fr,0/1)=X[X10+fr*2+0/1]", "records": xs},
               "y_table": {"count": len(ys), "accessor": "g.j(n,n2)=Y[n*2+n2]", "records": ys}}
(ANIM / "frame-table-v2.json").write_text(json.dumps(frame_table, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- 4. behavior
behav = {"meta": "Поведение = L-класс (ветвления f2.L) + состояние g[12] + подсостояние g[10] + флаги g[16] + prop10 (класс ИИ)",
         "L_classes": [
             {"L": [0, 1, 2], "class": "MC (main character)", "evidence": "g.java:7111 (aB)"},
             {"L": 3, "class": "ENEMY", "evidence": "f.java:681,700"},
             {"L": 9, "class": "NPC", "evidence": "g.java:21399, 31810"},
             {"L": 10, "class": "object", "evidence": "f.java:17010"},
             {"L": 11, "class": "item/interactive", "evidence": "g.java:8249"},
             {"L": 14, "class": "scenario object", "evidence": "f.java:17010"},
             {"L": 16, "class": "object", "evidence": "f.java:17010"},
             {"L": 15, "class": "trigger/zone (g.e[] L15)", "evidence": "f.java:2402 (f3.L != 15 continue; AABB-зоны)"},
             {"L": [20, 21, 22, 23, 24, 25], "class": "tile-objects (g.g[layer][x][y])", "evidence": "g.java:16622,18203 j(),18239 k()"},
             {"L": 26, "class": "tile-object", "evidence": "f.java/g.java L==26"},
         ],
         "states_g12": {"values": [0, 1, 4, 7, 8, 9, 14, 17, 18, 19, 23, 100, 101, 103, 104, 106, 107],
                        "note": "17+ значений; 100+ = терминальные (смерть); семантика каждого — REQUIRES_REAL_RUNTIME"},
         "substates_g10": {"values": [0, 3, 4, 5]},
         "flags_g16": {"bits": ["0x20", "0x100", "0x400", "0x800", "0x2000", "0x4000", "0x8000"]},
         "prop10_behavior_classes": {"0": "standard", "1": "special", "2": "special2", "3": "variant", "5": "shooter", "7": "shooter2",
                                     "note": "ветвления f.java (d(), C(), I(), J(), s(), e()): 0/3/5/7 = направленные/стреляющие; 2 = особый (g[12] 7/8)"},
         "ai_entry": "f.b(entity) из g.B() state 6 (g.java:1107)"}
(OUT / "entity-behavior-v2.json").write_text(json.dumps(behav, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- 3. entity-script-links
links = {"meta": "opcode -> свойства/поля сущностей (из opcode-master-v2, этап 15.10)",
         "links": [
             {"opcode": 110, "field": "g[28] (оружие), g[29], позиция a, направление", "target": "сущность по (n,n2,n3,n4)"},
             {"opcode": 113, "field": "g.g[layer][x][y].g[prop]", "target": "tile-object: L25->g[9], L20->g[6], L21->g[4], L22->g[6], L24->g[2]"},
             {"opcode": 114, "field": "g[0] (тип), L-поведение", "target": "tile-object: L23=дверь open/close, L21->f.b, L25->f.a"},
             {"opcode": 115, "field": "g[n4] = n5", "target": "сущность сетки f[layer][x][y]"},
             {"opcode": 116, "field": "g[n4] += n5", "target": "сущность сетки"},
             {"opcode": 118, "field": "позиция a.b(x*16+8, y*16+8), g[9..12] (L14)", "target": "сущность в тайле"},
             {"opcode": 120, "field": "g[n3+14] merge 65280", "target": "сущность g.a(n)"},
             {"opcode": 127, "field": "передача буфера z", "target": "сущность + данные"},
             {"opcode": 128, "field": "g[n] = n2", "target": "игрок g.c"},
             {"opcode": 134, "field": "активный персонаж", "target": "переключение c[]"},
             {"opcode": 141, "field": "c[], bt, L[1], M[0]", "target": "смена персонажа"},
             {"opcode": 142, "field": "g[26], g[27] (слой), a.b(n5,n6)", "target": "персонаж"},
             {"opcode": 147, "field": "выбор по координатам", "target": "сущность"},
             {"opcode": 148, "field": "цель NPC", "target": "MC/NPC"},
             {"opcode": 150, "field": "как 110 + var8_8", "target": "сущность"},
             {"opcode": 151, "field": "СПАВН: g.a(g.b,0,...)", "target": "новая сущность"},
             {"opcode": 152, "field": "f.y", "target": "сущность"},
             {"opcode": 160, "field": "СПАВН вариант", "target": "новая сущность"},
             {"opcode": 162, "field": "как 110 + bool", "target": "сущность"},
         ]}
(OUT / "entity-script-links-v2.json").write_text(json.dumps(links, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- 8. graphics resource map
grm = {"meta": "Маппинг графических ресурсов. Спрайт-листы a.java: сценарий g.g() case 1/2/3 "
               "(g.java:2414-2540) + геймплейные m6_*/m7 (g.java:2501).",
       "sprite_lists_from_script": [
           {"resource": "m0", "segments": [0, 9], "slot": "a[][0..1]"},
           {"resource": "m1", "segments": [0], "slot": "b[][1]"},
           {"resource": "m2", "segments": [1, 2, 23], "slot": "a[][0..2]"},
           {"resource": "m7", "segments": [3, 6], "slot": "a[][0]"},
           {"resource": "m11_0", "segments": [4, 5, 7, 11, 12, 13, 14, 19, 20, 21], "slot": "a[][0..9]"},
           {"resource": "m11_1", "segments": [8, 10, 15, 16, 17, 18, 22], "slot": "a[][0..6]"},
           {"resource": "m13_2", "segments": [0, 1, 2, 3, 6, 23], "slot": "a[][-1]", "note": "СЕГМЕНТ 0 = MIDI (MThd) — m13_2 содержит музыку!"},
       ],
       "gameplay_graphics": [
           {"resource": "m6_0..m6_5", "role": "геймплейные листы (g.java:2501: a[16+n] -> m6_*; 2524: g.a(byArray))", "segments": "все"},
           {"resource": "m7", "role": "геймплейные маски/листы (g.java:33601: a(n,n2,byArray): сегменты (n<<1)+1)", "segments": "нечётные"},
       ],
       "midi_audio": {"resource": "m13_2", "seg0_head": "4d546864 (MThd)", "evidence": "MIDI header, g.java:35186 (audio/midi)"},
       "sprite_format": "a.java a(byte[],int): объекты (w×h / смещения), палитры, b/f/e-записи, "
                       "формат u16: 0x8888=ARGB32, 0x4444=ARGB4444, 0x6505=RGB565(+0xF81F alpha); "
                       "g кадров × h пикселей (h u8, 0->256); magic 0x64F0; блоки данных"}
(GFX / "graphics-resource-map-v2.json").write_text(json.dumps(grm, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- 12. mission usage
db = json.load(open(Path("research/analysis/v2") / "missions-database.json"))
usage = {"meta": "Использование объектов миссий (102) и тайлов (101). obj_id/tile_id НЕ совпадают с "
                 "архетипами m9 (пересечения: 1/111 и 9/325) — числового маппинга НЕТ; "
                 "связь запись -> архетип идёт через props (f.a/f.c/f.d) — REQUIRES_REAL_RUNTIME.",
         "missions": []}
for m in db["missions"]:
    mid = m["id"]
    objs = json.load(open(Path("research/analysis/v2/missions") / mid / "objects.json"))
    tiles = json.load(open(Path("research/analysis/v2/missions") / mid / "tiles.json"))
    usage["missions"].append({"mission": mid, "objects_102": len(objs),
                              "object_ids": sorted({o["obj_id"] for o in objs}),
                              "tiles_101": len(tiles),
                              "tile_ids_sample": sorted({t["tile_id"] for t in tiles})[:50]})
(OUT / "mission-entity-usage-v2.json").write_text(json.dumps(usage, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- 11. visual catalog + 13. unused
arche_ids = [t["id"] for t in types]
tile_ids = set(db["totals"]["tile_ids_union"])
obj_ids = set(db["totals"]["object_ids_union"])
used_ids = (tile_ids | obj_ids) & set(arche_ids)
catalog = {"meta": "Визуальный каталог архетипов. Визуальная привязка архетип->спрайт UNKNOWN: "
                   "связь не доказана (V-смещения + X-кадры + спрайт-листы a.java не связаны численно).",
           "archetypes": []}
for t in types:
    catalog["archetypes"].append({"entity_id": t["id"],
                                  "animation_ids": "UNKNOWN (prop33 счётчик; конкретные id требуют рантайма)",
                                  "frame_ids": "UNKNOWN",
                                  "sprite_resources": "UNKNOWN",
                                  "visual_confidence": "UNKNOWN"})
(GFX / "entity-visual-catalog.json").write_text(json.dumps(catalog, indent=1, ensure_ascii=False))

unused = {"meta": "Использование архетипов. UNUSED_STATIC: нет ссылок в статически известных структурах; "
                  "проверка по tile_ids/obj_ids миссий (пересечения) + L-классы.",
          "archetypes_total": len(arche_ids),
          "intersect_mission_tiles": sorted(tile_ids & set(arche_ids)),
          "intersect_mission_objects": sorted(obj_ids & set(arche_ids)),
          "conclusion": "Прямых числовых ссылок миссий на архетипы мало (9+1) — архетипы выбираются через props "
                        "записей (REQUIRES_REAL_RUNTIME); UNUSED статически НЕ доказуем для остальных 46."}
(GFX / "archetype-usage-v2.json").write_text(json.dumps(unused, indent=1, ensure_ascii=False))

print(f"архетипов: {len(types)}, анимаций: {len(anims)}, кадров(V): {len(frames)}, X: {len(xs)}, Y: {len(ys)}")
print("пересечение tile_ids∩archetypes:", len(tile_ids & set(arche_ids)))
print("пересечение obj_ids∩archetypes:", len(obj_ids & set(arche_ids)))
print("ФАЙЛЫ ЗАПИСАНЫ")
