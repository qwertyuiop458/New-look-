#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_sprite_database_v2.py — cross-check инвентаризации спрайтов (этап 15.16)."""
import json
import sys
from pathlib import Path

V2 = Path("research/analysis/v2/graphics")
ERRORS = []
WARNINGS = []


def err(m):
    ERRORS.append(m)


def warn(m):
    WARNINGS.append(m)


def load(p):
    f = V2 / p
    if not f.exists():
        err(f"нет файла: {p}")
        return None
    return json.loads(f.read_text(encoding="utf-8"))


def main():
    reg = load("sprite-slot-registry-v2.json")
    inv = load("sprite-resource-inventory-v2.json")
    oinv = load("sprite-object-inventory-v2.json")
    finv = load("sprite-frame-inventory-v2.json")
    amap = load("archetype-sprite-map-v2.json")

    if reg:
        slots = {s["slot"] for s in reg["slots"]}
        if len(slots) < 17:
            err(f"уникальных слотов < 17 ({len(slots)})")
        for must in [f"a[{16 + i}]" for i in range(6)] + ["a[22]"]:
            if must not in slots:
                err(f"нет слота {must}")
    if inv:
        res = {r["resource"] for r in inv["resources"]}
        for must in ["m0", "m1", "m2", "m6_0", "m6_5", "m7", "m11_0", "m11_1", "m13_2"]:
            if must not in res:
                err(f"нет ресурса {must}")
    if oinv:
        objs = oinv["objects"]
        if len(objs) < 100:
            err(f"объектов < 100 ({len(objs)})")
        for o in objs[:500]:
            if "c" in o and o["c"] is not None and o["c"] > 512:
                warn(f"подозрительная ширина: {o['resource']} obj {o['object_index']} c={o['c']}")
    if finv:
        if len(finv["frames"]) < 10:
            err(f"кадровых записей < 10")
    if amap:
        if len(amap["archetypes"]) != 56:
            err(f"архетипов в карте != 56")

    print("=" * 60)
    print("VALIDATE SPRITE DATABASE V2")
    print("=" * 60)
    if WARNINGS:
        for w in WARNINGS[:10]:
            print("  !", w)
    if ERRORS:
        for e in ERRORS:
            print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERRORS)}")
        return 1
    print("РЕЗУЛЬТАТ: PASS — инвентаризация согласована")
    return 0


if __name__ == "__main__":
    sys.exit(main())
