#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_game_bible_v2.py — quality gate для Game Bible V2.

Проверки:
  1. schema: обязательные секции game-bible-data-v2.json
  2. source evidence: каждый CONFIRMED обязан иметь evidence
  3. duplicate IDs: оружие/патроны/архетипы
  4. references: v2/weapons.json, v2/entities.json, v2/level-inventory.json согласованы с мастер-базой
  5. contradictions: V2 не содержит ложных V1-утверждений (2/3 оружия, 10 опкодов, 17 состояний, 30 COMPLETE)
  6. unsupported CONFIRMED: CONFIRMED без evidence
  7. missing sources: evidence без source_file
  8. container format: base = 1+4A; последний сегмент недоступен

Запуск: python3 research/scripts/validate_game_bible_v2.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AN = ROOT / "research" / "analysis"
V2 = AN / "v2"
ERRORS = []
WARNINGS = []


def err(m):
    ERRORS.append(m)


def warn(m):
    WARNINGS.append(m)


def load(p, required=True):
    if not p.exists():
        if required:
            err(f"Отсутствует файл: {p.relative_to(ROOT)}")
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def has_evidence(entry):
    ev = entry.get("evidence")
    if ev is None:
        return False
    if isinstance(ev, str):
        return bool(ev.strip())
    if isinstance(ev, dict):
        return bool(ev) and any(v for v in ev.values() if v is not None)
    return False


def check_evidence(entries, where):
    """Каждый CONFIRMED обязан иметь evidence; evidence без source_file -> warning."""
    for e in entries:
        if not isinstance(e, dict):
            continue
        st = e.get("status")
        if st == "CONFIRMED" and not has_evidence(e):
            err(f"{where}: CONFIRMED без evidence: {e.get('claim') or e.get('id')}")
        ev = e.get("evidence")
        if isinstance(ev, dict) and ev and "source_file" not in ev:
            warn(f"{where}: evidence без source_file: {e.get('claim') or e.get('id')}")


def main():
    db = load(AN / "game-bible-data-v2.json")
    if db is not None:
        # 1. schema
        required = ["meta", "architecture", "states", "entities", "weapons", "items",
                    "ai", "movement", "combat", "collision", "camera", "animation",
                    "graphics", "audio", "save", "levels", "scripts", "resources",
                    "runtime_gaps"]
        for k in required:
            if k not in db:
                err(f"game-bible-data-v2.json: отсутствует секция '{k}'")
        # 2. evidence для CONFIRMED
        check_evidence(list(db.get("architecture", {}).values()), "architecture")
        check_evidence(db.get("states", []), "states")
        check_evidence(db.get("items", []), "items")
        check_evidence(db.get("ai", []), "ai")
        check_evidence(db.get("movement", []), "movement")
        check_evidence(db.get("combat", []), "combat")
        check_evidence(db.get("collision", []), "collision")
        check_evidence(db.get("camera", []), "camera")
        check_evidence(db.get("animation", []), "animation")
        check_evidence(db.get("graphics", []), "graphics")
        check_evidence(db.get("audio", []), "audio")
        check_evidence(db.get("save", []), "save")
        # entities
        for k, v in db.get("entities", {}).items():
            if isinstance(v, list):
                check_evidence(v, f"entities.{k}")
        # 5. contradictions (V1-ложь не должна присутствовать в V2)
        w = db.get("weapons", {})
        if w.get("record_count") != 16:
            err(f"weapons.record_count != 16 ({w.get('record_count')})")
        if sorted(w.get("ids", [])) != sorted([2, 3, 4, 5, 6, 7, 8, 11, 16, 17, 18, 19, 20, 21, 22, 24]):
            err(f"weapons.ids не совпадают с первичными данными: {w.get('ids')}")
        if w.get("ammo_count") != 6:
            err(f"weapons.ammo_count != 6")
        if db.get("entities", {}).get("archetype_count") != 56:
            err("entities.archetype_count != 56")
        if "10 опкодов" in str(db.get("scripts", {}).get("claim", "")):
            err("scripts: V1-ложь '10 опкодов' попала в V2")
        if db.get("states", []) and len([s for s in db["states"] if isinstance(s.get("id"), int)]) != 18:
            err("states: количество ID != 18")
        if "30" in str(db.get("levels", {}).get("claim", "")) and "полных уровней 0" not in str(db.get("levels", {}).get("claim", "")):
            err("levels: утверждение '30 уровней COMPLETE' попало в V2")

    # 3. duplicates в v2-таблицах
    wpn = load(V2 / "weapons.json")
    if wpn is not None:
        ids = [w["id"] for w in wpn["weapons"]]
        if len(ids) != len(set(ids)):
            err("v2/weapons.json: дубликаты weapon id")
        aids = [a["id"] for a in wpn["ammo"]]
        if len(aids) != len(set(aids)):
            err("v2/weapons.json: дубликаты ammo id")
        if len(ids) != 16 or len(aids) != 6:
            err(f"v2/weapons.json: {len(ids)} weapons / {len(aids)} ammo (ожидается 16/6)")
    ent = load(V2 / "entities.json")
    if ent is not None:
        tids = [t["id"] for t in ent["types"]]
        if len(tids) != 56 or len(tids) != len(set(tids)):
            err(f"v2/entities.json: типов {len(tids)}, уникальных {len(set(tids))} (ожидается 56)")
        for t in ent["types"]:
            if len(t["props"]) != 32:
                err(f"v2/entities.json: тип {t['id']} имеет {len(t['props'])} props (ожидается 32)")
    lv = load(V2 / "level-inventory.json")
    if lv is not None:
        classes = [v["class"] for v in lv["levels"].values()]
        if len(classes) != 30:
            err(f"level-inventory: {len(classes)} файлов (ожидается 30)")
        if lv["summary"]["GLOBAL_DATA"] != 1 or lv["summary"]["FULL_LEVEL"] != 0:
            err("level-inventory: неверная сводка классов")
        if "m9" not in lv["levels"] or lv["levels"]["m9"]["class"] != "GLOBAL_DATA":
            err("level-inventory: m9 должен быть GLOBAL_DATA")
        for name in ("m5_0", "m5_3", "m5_4", "m5_7", "m5_8", "m5_9"):
            if lv["levels"].get(name, {}).get("class") != "STUB":
                err(f"level-inventory: {name} должен быть STUB")

    # 4. references между мастер-базой и v2-таблицами
    if db is not None and wpn is not None:
        if sorted(wpn["weapon_ids"]) != sorted(db["weapons"]["ids"]):
            err("weapons.json и game-bible-data-v2.json: ids не согласованы")

    # 8. container format: база/доступность
    inv = load(V2 / "container-inventory.json")
    if inv is not None:
        m0 = inv.get("m0", {})
        if m0.get("base") != 1 + 4 * m0.get("segments", 0):
            err("container-inventory: m0 base != 1+4A")
        m9 = inv.get("m9", {})
        if m9.get("base") != 1 + 4 * m9.get("segments", 0):
            err("container-inventory: m9 base != 1+4A")
        last = m9.get("segs", [])[-1]
        if last.get("state") != "UNREACHABLE":
            err("container-inventory: последний сегмент m9 должен быть UNREACHABLE")

    # 6/7: unsupported CONFIRMED / missing sources — уже покрыто check_evidence

    print("=" * 66)
    print("VALIDATE GAME BIBLE V2 — quality gate")
    print("=" * 66)
    if WARNINGS:
        print(f"WARNING ({len(WARNINGS)}):")
        for w in WARNINGS:
            print(f"  ! {w}")
    if ERRORS:
        print(f"ERROR ({len(ERRORS)}):")
        for e in ERRORS:
            print(f"  x {e}")
        print("=" * 66)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERRORS)} ошибок")
        return 1
    print(f"РЕЗУЛЬТАТ: PASS — ошибок нет{f', предупреждений {len(WARNINGS)}' if WARNINGS else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
