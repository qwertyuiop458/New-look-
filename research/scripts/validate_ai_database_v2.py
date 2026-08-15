#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_ai_database_v2.py — валидация AI базы (этап 15.17)."""
import json, sys
from pathlib import Path
AI = Path("research/analysis/v2/ai")
ERR, WARN = [], []
def err(m): ERR.append(m)
def warn(m): WARN.append(m)
def load(p):
    f = AI / p
    if not f.exists(): err(f"нет {p}"); return None
    return json.loads(f.read_text(encoding="utf-8"))

def main():
    sm = load("ai-state-machine-v2.json")
    tg = load("ai-transition-graph-v2.json")
    master = load("archetype-behavior-master-v2.json")
    ib = load("mission-instance-behavior-v2.json")
    fm = load("ai-formulas-v2.json")
    if sm:
        if "100" not in sm["states"]: err("нет терминального состояния")
        if len(sm["states"]) < 10: err("состояний < 10")
    if tg:
        if len(tg["transitions"]) < 10: err("переходов < 10")
    if master:
        if len(master["archetypes"]) != 56: err("архетипов != 56")
        for a in master["archetypes"]:
            if a.get("ai_class_prop10") is None: err(f"нет AI class: {a['archetype_id']}")
    if ib:
        total = sum(len(m["instances"]) for m in ib["missions"])
        if total != 666: err(f"instances != 666 ({total})")
    if fm:
        if len(fm["formulas"]) < 5: err("формул < 5")
    print("=" * 60)
    print("VALIDATE AI DATABASE V2")
    print("=" * 60)
    if WARN:
        for w in WARN[:10]: print("  !", w)
    if ERR:
        for e in ERR: print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERR)}")
        return 1
    print("РЕЗУЛЬТАТ: PASS — структура согласована (семантика см. документы)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
