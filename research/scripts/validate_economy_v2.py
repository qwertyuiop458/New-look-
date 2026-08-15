#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_economy_v2.py — валидация экономики (этап 15.22)."""
import json, sys
from pathlib import Path
ECO = Path("research/analysis/v2/economy")
ERR = []
def err(m): ERR.append(m)
def load(p):
    f = ECO / p
    if not f.exists(): err(f"нет {p}"); return None
    return json.loads(f.read_text(encoding="utf-8"))

def main():
    cur = load("currency-v2.json")
    shop = load("shop-items-v2.json")
    fm = load("shop-formulas-v2.json")
    wa = load("weapon-economy-map-v2.json")
    se = load("economy-save-schema-v2.json")
    if cur:
        if len(cur["L4"]) < 2: err("currency L4 < 2 роли")
        if not any("45000" in str(w) for w in cur["L4"]): err("нет cap 45000")
    if shop:
        if len(shop["items"]) < 3: err("shop items < 3")
    if fm:
        if len(fm["formulas"]) < 5: err("формул < 5")
    if wa:
        if len(wa["records"]) != 16: err("weapon records != 16")
    if se:
        if len(se["records"]) != 2: err("save records != 2")
    print("=" * 60)
    print("VALIDATE ECONOMY V2")
    print("=" * 60)
    if ERR:
        for e in ERR: print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERR)}")
        return 1
    print("РЕЗУЛЬТАТ: PASS — структура согласована")
    return 0

if __name__ == "__main__":
    sys.exit(main())
