#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_mission_object_v2.py — валидация объекта миссии (этап 15.21)."""
import json, sys
from pathlib import Path
OBJ = Path("research/analysis/v2/objectives")
ERR, WARN = [], []
def err(m): ERR.append(m)
def load(p):
    f = OBJ / p
    if not f.exists(): err(f"нет {p}"); return None
    return json.loads(f.read_text(encoding="utf-8"))

def main():
    cb = load("mission-object-cb-dataflow-v2.json")
    rw = load("mission-rewards-v2.json")
    cc = load("mission-completion-causal-chain-v2.json")
    sv = load("mission-object-state-v2.json")
    if cb:
        if not any(d["op"] == "init" and d["value"] == 200 for d in cb["dataflow"]): err("cB init != 200")
        if not any(d["op"] == "compare" and "cB <= 0" in d["condition"] for d in cb["dataflow"]): err("нет cB<=0")
    if rw:
        if "k(n, 10)" not in rw["reward_flow"]: err("нет k(n,10)")
    if cc:
        if len(cc["chain"]) < 6: err("цепочка < 6 шагов")
        if cc["chain"][-1]["event"] != "state 13 (shop) или 2 (loading)": err("последний шаг неверен")
    if sv:
        if len(sv["fields"]) < 10: err("полей < 10")
    print("=" * 60)
    print("VALIDATE MISSION OBJECT V2")
    print("=" * 60)
    if ERR:
        for e in ERR: print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERR)}")
        return 1
    print("РЕЗУЛЬТАТ: PASS — структура согласована")
    return 0

if __name__ == "__main__":
    sys.exit(main())
