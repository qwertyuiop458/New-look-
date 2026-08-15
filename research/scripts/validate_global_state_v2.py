#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_global_state_v2.py — валидация глобальной системы (этап 15.19)."""
import json, sys
from pathlib import Path
G = Path("research/analysis/v2/global")
SV = Path("research/analysis/v2/save")
ERR, WARN = [], []
def err(m): ERR.append(m)
def warn(m): WARN.append(m)
def load(p, base=G):
    f = base / p
    if not f.exists(): err(f"нет {p}"); return None
    return json.loads(f.read_text(encoding="utf-8"))

def main():
    gsm = load("global-state-machine-v2.json")
    sv = load("global-state-vector-v2.json")
    rms = load("rms-record-schema-v2.json", SV)
    mi = load("mission-index-v2.json")
    ogm = load("opcode-global-state-map-v2.json")
    if gsm:
        ids = [s["id"] for s in gsm["states"]]
        if len(ids) != 18: err(f"состояний != 18 ({len(ids)})")
        if 99 not in ids or 6 not in ids: err("нет ключевых состояний")
    if sv:
        if len(sv["fields"]) < 20: err("полей < 20")
    if rms:
        if len(rms["records"]) < 2: err("RMS записей < 2")
    if mi:
        if len(mi["missions"]) != 5: err("миссий != 5")
    if ogm:
        if len(ogm["map"]) < 9: err("опкодов < 9")
    print("=" * 60)
    print("VALIDATE GLOBAL STATE V2")
    print("=" * 60)
    if ERR:
        for e in ERR: print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERR)}")
        return 1
    print("РЕЗУЛЬТАТ: PASS — структура согласована")
    return 0

if __name__ == "__main__":
    sys.exit(main())
