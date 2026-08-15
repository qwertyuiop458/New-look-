#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_bible_v3.py — валидация V3 аудита (этап 15.25)."""
import json, sys
from pathlib import Path
V3 = Path("research/analysis/audit/v3")
ERR = []
def err(m): ERR.append(m)
def load(p):
    f = V3 / p
    if not f.exists(): err(f"нет {p}"); return None
    return json.loads(f.read_text(encoding="utf-8"))
def main():
    idx = load("master-fact-index.json")
    fc = load("false-confirmed-candidates.json")
    cm = load("contradiction-matrix.json")
    kg = load("knowledge-gaps-v3.json")
    gr = load("v2-quality-scores.json")
    st = load("bible-v3-readiness.json")
    if idx:
        if len(idx["facts"]) < 40: err(f"фактов < 40 ({len(idx['facts'])})")
        if not any(f["status"] == "CONFIRMED" for f in idx["facts"]): err("нет CONFIRMED")
        if not any("REQUIRES_REAL_RUNTIME" in f["status"] for f in idx["facts"]): err("нет RUNTIME")
    if fc and len(fc["candidates"]) < 5: err("кандидатов < 5")
    if cm and len(cm["contradictions"]) < 5: err("противоречий < 5")
    if kg:
        if not any(g["priority"] == "CRITICAL" for g in kg["gaps"]): err("нет CRITICAL")
    if gr and len(gr["grades"]) != 13: err("оценок != 13")
    if st and st["status"] not in ("NOT_READY", "READY_WITH_GAPS", "STATICALLY_COMPLETE"): err("статус невалиден")
    print("=" * 60); print("VALIDATE BIBLE V3"); print("=" * 60)
    if ERR:
        for e in ERR: print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERR)}"); return 1
    print("РЕЗУЛЬТАТ: PASS — V3 согласован"); return 0
if __name__ == "__main__":
    sys.exit(main())
