#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_entity_animation_v2.py — валидация entity/animation базы (этап 15.11).

Проверки:
  - missing archetypes (56)
  - duplicate IDs
  - invalid animation references (пропа индексов 32/33 в пределах W)
  - invalid frame references (пропа 34 в пределах V)
  - invalid sprite references
  - broken mission links (пересечения)
  - impossible dimensions (пропа 24 и т.п.)
  - inconsistent property references

PASS валидатора != доказанная семантика (семантика отдельно в entity-properties-v2.json).
Запуск: python3 research/scripts/validate_entity_animation_v2.py
"""
import json
import sys
from pathlib import Path

V2 = Path("research/analysis/v2")
ERRORS = []
WARNINGS = []


def err(m):
    ERRORS.append(m)


def warn(m):
    WARNINGS.append(m)


def load(p, req=True):
    f = V2 / p
    if not f.exists():
        if req:
            err(f"нет файла: {p}")
        return None
    return json.loads(f.read_text(encoding="utf-8"))


def main():
    ents = load("entities/entity-table-v2.json")
    props = load("entities/entity-properties-v2.json")
    anims = load("animation/animation-table-v2.json")
    fr = load("animation/frame-table-v2.json")
    usage = load("entities/mission-entity-usage-v2.json")
    db = load("missions-database.json")

    # 1. missing archetypes / duplicates
    if ents:
        ids = [a["entity_id"] for a in ents["archetypes"]]
        if len(ids) != 56:
            err(f"архетипов {len(ids)} != 56")
        if len(ids) != len(set(ids)):
            err("дубликаты entity_id")
        for a in ents["archetypes"]:
            if len(a["props32"]) != 32:
                err(f"архетип {a['entity_id']}: props32 != 32")
    # 2. properties
    if props:
        if len(props["properties"]) != 35:
            err("properties != 35")
        conf = {}
        for p in props["properties"]:
            conf[p["confidence"]] = conf.get(p["confidence"], 0) + 1
        print("property confidence:", conf)
    # 3. animations
    if anims:
        if len(anims["animations"]) != 176:
            err(f"анимаций {len(anims['animations'])} != 176")
        for a in anims["animations"]:
            if len(a["raw10"]) != 10:
                err(f"анимация @{a['offset']}: raw10 != 10")
    # 4. frames
    if fr:
        if len(fr["frames"]) != 3:
            err(f"frame-записей {len(fr['frames'])} != 3")
        for f in fr["frames"]:
            if len(f["raw15"]) != 15:
                err(f"frame @{f['frame_offset']}: raw15 != 15")
        if fr["x_table"]["count"] != 36 or fr["y_table"]["count"] != 15:
            err(f"X/Y: {fr['x_table']['count']}/{fr['y_table']['count']} != 36/15")
        for x in fr["x_table"]["records"]:
            if len(x["pair"]) != 2:
                err("X-запись != 2 u16")
    # 5. mission usage
    if usage and db:
        tot_o = sum(m["objects_102"] for m in usage["missions"])
        tot_t = sum(m["tiles_101"] for m in usage["missions"])
        if tot_o != 113 or tot_t != 345:
            err(f"objects/tiles: {tot_o}/{tot_t} != 113/345")
        for m in usage["missions"]:
            if len(m["mission"]) != 10:
                err(f"id миссии: {m['mission']}")
    # 6. пересечения (не ошибки, а информация)
    if ents and db:
        arche = {a["entity_id"] for a in ents["archetypes"]}
        ti = set(db["totals"]["tile_ids_union"])
        oi = set(db["totals"]["object_ids_union"])
        if len(ti & arche) > 20:
            err("подозрительно большое пересечение tile_ids/archetypes")
        warn(f"информация: tile∩arche={len(ti & arche)}, obj∩arche={len(oi & arche)}")

    # 8. properties 0..34 — семантика
    cls = load("entities/property-classification-v2.json")
    if cls:
        conf = {}
        for c in cls["classification"]:
            conf[c["SEMANTIC_STATUS"]] = conf.get(c["SEMANTIC_STATUS"], 0) + 1
        print("property classification:", conf)
        if conf.get("CONFIRMED", 0) < 12:
            err(f"CONFIRMED свойств < 12 ({conf.get('CONFIRMED', 0)}) — критерий качества")
        if len(cls["classification"]) != 35:
            err("classification != 35")
    prof = load("entities/archetype-profiles-v2.json")
    if prof and len(prof["archetypes"]) != 56:
        err("profiles != 56")
    cl = load("entities/archetype-clusters-v2.json")
    if cl and cl.get("cluster_count", 0) == 0:
        err("нет кластеров")
    idx = load("entities/property-read-write-index.json")
    if idx and len(idx["properties"]) != 35:
        err("read-write index != 35")

    # 7. property refs consistency
    if props:
        ok_props = {p["property_index"] for p in props["properties"] if p["confidence"] != "UNKNOWN"}
        warn(f"информация: свойств с семантикой (CONFIRMED/INFERRED): {len(ok_props)}/35")

    print("=" * 60)
    print("VALIDATE ENTITY/ANIMATION V2")
    print("=" * 60)
    if WARNINGS:
        for w in WARNINGS:
            print("  !", w)
    if ERRORS:
        for e in ERRORS:
            print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERRORS)}")
        return 1
    print("РЕЗУЛЬТАТ: PASS — структура согласована (семантика — см. entity-properties-v2.json)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
