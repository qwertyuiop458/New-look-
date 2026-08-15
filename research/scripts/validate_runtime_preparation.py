#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_runtime_preparation.py — валидация runtime-подготовки (этап 15.28)."""
import json, sys
from pathlib import Path
RT = Path("research/runtime")
ERR = []
def err(m): ERR.append(m)
def load(p):
    f = RT / p
    if not f.exists(): err(f"нет {p}"); return None
    return json.loads(f.read_text(encoding="utf-8"))
def main():
    req = load("runtime-requirements-v1.json")
    em = load("emulator-options.json")
    env = load("environment-audit.json")
    intg = load("original-jar-integrity.json")
    ev = load("runtime-event-schema.json")
    ex = load("experiment-design.json")
    pts = load("instrumentation/instrumentation-points.json")
    if req and len(req["requirements"]) != 12: err(f"requirements != 12 ({len(req['requirements'])})")
    if em and len(em["options"]) < 3: err("эмуляторов < 3")
    if env:
        if not any(i["tool"] == "java/javac/javap" and i["status"] == "MISSING" for i in env["items"]): err("java не зафиксирован")
    if intg and len(intg.get("sha256","")) != 64: err("sha256 невалиден")
    if ev and len(ev["events"]) < 18: err(f"событий < 18 ({len(ev['events'])})")
    if ex:
        ids = [t["id"] for t in ex["tests"]]
        if len(ids) != len(set(ids)): err("дубликаты TEST-IDs")
        if len(ids) < 9: err("тестов < 9")
    if pts and len(pts["points"]) < 10: err("точек < 10")
    # evidence policy
    if not (RT / "evidence-policy.md").exists(): err("нет evidence-policy.md")
    # safety
    if not (RT / "safety.md").exists(): err("нет safety.md")
    print("=" * 60); print("VALIDATE RUNTIME PREPARATION"); print("=" * 60)
    if ERR:
        for e in ERR: print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERR)}"); return 1
    print("РЕЗУЛЬТАТ: PASS — подготовка полна"); return 0
if __name__ == "__main__":
    sys.exit(main())
