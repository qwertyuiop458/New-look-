#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_property_semantics_v2.py — полная семантика 35 свойств архетипов (этап 15.12).

Метод: WRITE -> ALL READS -> CONSUMER -> EFFECT (для каждого property собраны все
чтения g.h(type,prop) в g.java/f.java с контекстом и выведена цепочка).

Вывод:
  entities/property-read-write-index.json
  entities/property-formulas-v2.json
  entities/archetype-profiles-v2.json
  entities/archetype-clusters-v2.json
  entities/opcode-archetype-property-map-v2.json
  entities/property-classification-v2.json
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path("research/analysis/v2/entities")

# ---------------- полный индекс чтений (собран программно ранее, дополнен вручную) ----------------
# (prop, семантика, PRIMARY_ROLE, SEMANTIC_STATUS, формула/цепочка, evidence)
PROPS = {
    0: ("RESOURCE", "INFERRED", "индекс/ссылка (g.java: g.h(n,0) в таблицах m(); n4=(n6-4)*10+... — индексация данных)", "g.java:24695-24700 m(int)"),
    1: ("RESOURCE", "INFERRED", "индекс/ссылка (m(int): n5 = (n4-4)*10 + g.h(n,1); t[n5] — выбор записи)", "g.java:24695-24700"),
    2: ("MOVEMENT", "CONFIRMED", "сдвиг направления для состояния g[12]==0/6/28: кадр n = dir + prop2; и m(): направление += prop2", "f.java:4656, 4618, 3637 m()"),
    3: ("MOVEMENT", "CONFIRMED", "сдвиг направления для состояния g[12]==1: кадр n = dir + prop3", "f.java:4660"),
    4: ("MOVEMENT", "CONFIRMED", "сдвиг направления для состояния g[12]==2 (и аналогичных)", "f.java:4679"),
    5: ("MOVEMENT", "CONFIRMED", "сдвиг направления для состояния g[12]==3 (и аналогичных)", "f.java:4746"),
    6: ("MOVEMENT", "CONFIRMED", "сдвиг направления для состояния g[12]==4 (и аналогичных)", "f.java:4768"),
    7: ("AI", "CONFIRMED", "диапазон направлений A [n, n+4): f.s(): f2.a.d >= n2 && < n2+4 (зона видимости/атаки)", "f.java:3667, 4604, 4599"),
    8: ("AI", "CONFIRMED", "диапазон направлений B [n, n+4): второй диапазон", "f.java:3668, 4605"),
    9: ("STATE", "INFERRED", "поле состояния (g.java: var2_2 = g.h(var0.g[0], 9))", "g.java:31805"),
    10: ("AI", "CONFIRMED", "КЛАСС ИИ: 0/3/5/7 = направленные/стреляющие ветвления (d(), C(), I(), J(), s(), e()); 1/2 = особые", "f.java:2380,2637,2830,3662,4603 (46 чтений)"),
    11: ("STATE", "INFERRED", "вспомогательное поле (var5_6 = g.h(var0.g[0], 11) рядом с 12)", "f.java:2830"),
    12: ("AI", "CONFIRMED", "атака/урон-параметр: f.i() case 7: f.d(f2, n2) (урон цели), f.j() case 12/13: тайминги", "f.java:2830, 2952, 3913"),
    13: ("UNKNOWN", "UNKNOWN", "нет чтений в исследованном коде", "-"),
    14: ("AI", "CONFIRMED", "анимация цели при атаке: f.b(f3, g.h(f2.g[0],14)) (проигрывание анимации жертвы)", "f.java:2830 (f.i case 7)"),
    15: ("STATE", "CONFIRMED", "бинарный флаг: var4_4 = g.h(type,15)==1 (выбор ветки поведения)", "f.java:4644"),
    16: ("UNKNOWN", "UNKNOWN", "var6_7 = g.h(var0.g[0], 16) — контекст не изолирован", "f.java:2830"),
    17: ("AI", "CONFIRMED", "дистанция атаки: f.i() case 7: n <= n3 (сравнение с дистанцией); f.j() case 12", "f.java:2830 (f.i), 2952 (f.j)"),
    18: ("UNKNOWN", "UNKNOWN", "var8_9 = g.h(var0.g[0], 18)", "f.java:2830"),
    19: ("COLLISION", "CONFIRMED", "полуширина коллизионного бокса в тайлах: n4 = 16*prop19/2 - 5 << 14 (px fixed); g.a проверки", "f.java:5360-5366"),
    20: ("COLLISION", "CONFIRMED", "полувысота коллизионного бокса в тайлах: n5 = 16*prop20/2 - 5 << 14; также g.java: g.h(type,20)*16/2", "f.java:5361; g.java:12725"),
    21: ("RENDER", "INFERRED", "палитра/цветовой индекс (g.java: n = g.h(f2.g[0], 21) в отрисовке)", "g.java:17669"),
    22: ("AI", "CONFIRMED", "урон атаки: f.java:2894 (n6 = g.h(f2.g[0],22) в ветке нанесения урона — condition f2.g[10]!=5 && g[12]<100)", "f.java:2894"),
    23: ("MOVEMENT", "CONFIRMED", "сдвиг направления для состояния g[12]==9 (кадр = dir + prop23)", "f.java:4789"),
    24: ("RENDER", "CONFIRMED", "смещение X спрайта: n5 = n + (prop24 + g[28]*4) (оружие-сдвиг); n5 = n + prop24", "f.java:4720, 4728, 4107"),
    25: ("RENDER", "INFERRED", "звук/эффект выстрела: g.a(позиция, prop25, позиция, ...50, 200) (AABB-проверка попадания)", "f.java:4107"),
    26: ("STATE", "CONFIRMED", "графика/эффект телепорта: g.b(n5, x<<14, y<<14) (вызов после перемещения)", "f.java:2658-2680"),
    27: ("MOVEMENT", "CONFIRMED", "сдвиг направления для состояния g[12]==10", "f.java:4801"),
    28: ("MOVEMENT", "CONFIRMED", "сдвиг направления для состояния g[12]==11", "f.java:4814"),
    29: ("STATE", "CONFIRMED", "спец-поле: g.h(type,29)==-1 проверка (ветвление); также сдвиг кадра (n5 = n + prop29)", "f.java:2830, 4834"),
    30: ("MOVEMENT", "CONFIRMED", "сдвиг направления для состояния g[12]==12", "f.java:4841"),
    31: ("RENDER", "CONFIRMED", "палитра при отрисовке: g.a(graphics, g.b, null, 9, g.h(type,31), 0, RGBA...) — индекс палитры", "f.java:4107 (2 чтения)"),
    32: ("ANIMATION", "CONFIRMED", "старт анимаций в W (dr(); g.d(type,anim,f) = W[prop32+anim*13+f])", "g.java:24553 dr(), 24756"),
    33: ("ANIMATION", "CONFIRMED", "число анимаций (циклы: for n4 < g.h(type,33); System.arraycopy g[30..])", "f.java:2637, 2719, 3913 (22 чтения)"),
    34: ("ANIMATION", "CONFIRMED", "индекс frame-записи в V (g.i(type,f)=V[prop34*15+f]; -1 = нет кадров)", "g.java:24765; f.java:2935, 3985"),
}

ROLE_COUNT = Counter()
STATUS_COUNT = Counter()
for p, (role, st, desc, ev) in PROPS.items():
    ROLE_COUNT[role] += 1
    STATUS_COUNT[st] += 1

# 1) property-read-write-index
idx = {"meta": "Полный read/write индекс 35 свойств. WRITE: только dr() (загрузка из m9 seg4). "
               "READS: все g.h(type,prop) из g.java/f.java (программно собранные + вручную контексты).",
       "properties": []}
for p in range(35):
    if p in PROPS:
        role, st, desc, ev = PROPS[p]
        idx["properties"].append({"property": p, "writes": ["m9 seg4 (dr())"],
                                  "reads": f"см. desc: {desc}", "methods": [ev.split(":")[0]],
                                  "fields": [], "operations": [], "confidence": st,
                                  "primary_role": role, "chain": desc})
    else:
        idx["properties"].append({"property": p, "writes": ["m9 seg4 (dr())"],
                                  "reads": [], "methods": [], "fields": [],
                                  "operations": [], "confidence": "UNKNOWN",
                                  "primary_role": "UNKNOWN", "chain": "PARTIAL_STATIC"})
(OUT / "property-read-write-index.json").write_text(json.dumps(idx, indent=1, ensure_ascii=False))

# 2) property-formulas
fm = {"meta": "Формулы/преобразования для подтверждённых свойств", "formulas": []}
for p in (2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 17, 19, 20, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34):
    if p in PROPS:
        role, st, desc, ev = PROPS[p]
        if p == 19:
            formula = "n4 = (16 * prop19 / 2 - 5) << 14  [fixed-point px; полуширина бокса]"
        elif p == 20:
            formula = "n5 = (16 * prop20 / 2 - 5) << 14; g.h(type,20)*16/2"
        elif p == 24:
            formula = "n5 = n + prop24 + g[28]*4 (со смещением оружия); n5 = n + prop24"
        elif p in (2, 3, 4, 5, 6, 23, 27, 28, 30):
            formula = f"кадр = dir + prop{p} (сдвиг направления для состояния)"
        elif p in (7, 8):
            formula = f"зона: prop{p} <= направление < prop{p}+4"
        elif p == 17:
            formula = "сравнение: дистанция <= prop17 (порог атаки)"
        elif p == 22:
            formula = "урон: применяется в ветке атаки (f.java:2894)"
        elif p == 31:
            formula = "индекс палитры при отрисовке (2 варианта: prop31 / prop31+1)"
        elif p == 33:
            formula = "циклы: for (i < prop33) — число анимаций; arraycopy g[30..30+prop33]"
        elif p == 34:
            formula = "g.i(type,f) = V[prop34*15 + f]; prop34 == -1 => нет кадров"
        elif p == 32:
            formula = "g.d(type,anim,f) = W[prop32 + anim*13 + f]"
        else:
            formula = desc.split(":")[-1].strip() if ":" in desc else desc
        fm["formulas"].append({"property": p, "formula": formula, "source": ev,
                               "confidence": st})
for p in range(35):
    if p not in PROPS:
        fm["formulas"].append({"property": p, "formula": "UNKNOWN", "source": "-",
                               "confidence": "UNKNOWN"})
(OUT / "property-formulas-v2.json").write_text(json.dumps(fm, indent=1, ensure_ascii=False))

# 3) archetype-profiles
ents = json.load(open(OUT / "entity-table-v2.json"))
profiles = {"meta": "Профили 56 архетипов. Семантика свойств — из property-read-write-index; "
                    "значения — сырые u16 из m9 seg4.", "archetypes": []}
for a in ents["archetypes"]:
    props = {}
    for p in range(32):
        role, st, desc, ev = PROPS.get(p, ("UNKNOWN", "UNKNOWN", "", ""))
        props[f"prop{p}"] = {"value": a["props32"][p], "role": role, "status": st}
    profiles["archetypes"].append({"id": a["entity_id"], "name": a["name"], "properties": props})
(OUT / "archetype-profiles-v2.json").write_text(json.dumps(profiles, indent=1, ensure_ascii=False))

# 4) clusters (структурная кластеризация по signature из подтверждённых свойств)
sig = {}
for a in ents["archetypes"]:
    # сигнатура: prop10 (ИИ), prop7/8 (зоны), prop19/20 (бокс), prop33 (анимации), prop34 (кадры), prop22 (урон)
    s = (a["props32"][10], a["props32"][7], a["props32"][8], a["props32"][19], a["props32"][20],
         a["props32"][33] if 33 < 32 else -1, a["props32"][22])
    sig.setdefault(s, []).append(a["entity_id"])
clusters = {"meta": "Структурная кластеризация по сигнатуре (prop10, prop7, prop8, prop19, prop20, prop22) — "
                    "без субъективных имён. prop33/34 вычисляются кодом и здесь недоступны.",
            "cluster_count": len(sig), "clusters": []}
for s, ids in sorted(sig.items(), key=lambda x: -len(x[1])):
    clusters["clusters"].append({"signature": {"ai_class": s[0], "facing_a": s[1], "facing_b": s[2],
                                               "box_w_tiles": s[3], "box_h_tiles": s[4], "attack_damage": s[5]},
                                 "archetype_ids": sorted(ids), "size": len(ids)})
(OUT / "archetype-clusters-v2.json").write_text(json.dumps(clusters, indent=1, ensure_ascii=False))

# 5) opcode-archetype-property-map
opmap = {"meta": "opcode -> archetype property (из opcode-master-v2 + property index)",
         "map": [
             {"opcode": 110, "property": [28, 29], "effect": "команда: g[28] (оружие), g[29], позиция, направление"},
             {"opcode": 113, "property": [], "effect": "запись g[prop] объекта-тайла (L-зависимо)"},
             {"opcode": 115, "property": [], "effect": "запись g[n4]=n5 сущности сетки"},
             {"opcode": 116, "property": [], "effect": "инкремент g[n4]+=n5"},
             {"opcode": 120, "property": [14], "effect": "запись байта в g[n3+14] (merge 65280)"},
             {"opcode": 128, "property": [], "effect": "g.c.g[n] = n2 (игрок)"},
             {"opcode": 151, "property": [10, 7, 8, 19, 20], "effect": "СПАВН: архетип в props; поведение/бокс из свойств"},
             {"opcode": 160, "property": [10, 7, 8], "effect": "СПАВН вариант"},
             {"opcode": 141, "property": [], "effect": "смена персонажа (c[], bt, L[1])"},
         ]}
(OUT / "opcode-archetype-property-map-v2.json").write_text(json.dumps(opmap, indent=1, ensure_ascii=False))

# 6) classification
cls = {"meta": "Классификация 35 свойств", "classification": []}
for p in range(35):
    if p in PROPS:
        role, st, desc, ev = PROPS[p]
        cls["classification"].append({"property": p, "PRIMARY_ROLE": role, "SEMANTIC_STATUS": st,
                                      "chain": desc, "evidence": ev})
    else:
        cls["classification"].append({"property": p, "PRIMARY_ROLE": "UNKNOWN",
                                      "SEMANTIC_STATUS": "UNKNOWN", "chain": "PARTIAL_STATIC", "evidence": "-"})
(OUT / "property-classification-v2.json").write_text(json.dumps(cls, indent=1, ensure_ascii=False))

print("свойства: CONFIRMED =", STATUS_COUNT.get("CONFIRMED", 0),
      ", INFERRED =", STATUS_COUNT.get("INFERRED", 0),
      ", UNKNOWN =", STATUS_COUNT.get("UNKNOWN", 0))
print("роли:", dict(ROLE_COUNT))
print("кластеров:", clusters["cluster_count"])
print("ФАЙЛЫ ЗАПИСАНЫ")
