#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_performance_model_v2.py — валидация модели производительности (этап 15.24)."""
import json, sys
from pathlib import Path
PERF = Path("research/analysis/v2/performance")
ERR = []
def err(m): ERR.append(m)
def load(p):
    f = PERF / p
    if not f.exists(): err(f"нет {p}"); return None
    return json.loads(f.read_text(encoding="utf-8"))
def main():
    rlg = load("resource-load-graph-v2.json")
    mg = load("memory-guards-v2.json")
    tl = load("technical-limits-v2.json")
    hs = load("performance-hotspots-v2.json")
    if rlg and len(rlg["loaders"]) < 5: err("лоадеров < 5")
    if mg and len(mg["guards"]) < 3: err("guards < 3")
    if tl and len(tl["limits"]) < 10: err("лимитов < 10")
    if hs and len(hs["hotspots"]) < 5: err("hotspots < 5")
    print("=" * 60); print("VALIDATE PERFORMANCE V2"); print("=" * 60)
    if ERR:
        for e in ERR: print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERR)}"); return 1
    print("РЕЗУЛЬТАТ: PASS — модель согласована"); return 0
if __name__ == "__main__":
    sys.exit(main())
