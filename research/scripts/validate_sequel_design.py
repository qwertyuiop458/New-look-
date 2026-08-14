#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_sequel_design.py — валидатор дизайн-библии сиквела «МЁРТВАЯ ЧАСТОТА».

Проверки (Этап 15, раздел 16):
  1. duplicate IDs (внутри и между файлами)
  2. broken references (миссии->механики/враги/оружие/предметы, оружие->механики, боеприпасы->оружие)
  3. missing mission fields (11 обязательных полей)
  4. invalid enemy references
  5. invalid weapon references
  6. contradictions (границы значений, калибры, тайминги, порядок актов)
  7. missing originality boundaries (reference only / independently created)

Python 3, без внешних зависимостей. Запуск из корня репозитория:
    python3 research/scripts/validate_sequel_design.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEQ = ROOT / "research" / "sequel"
ANALYSIS = ROOT / "research" / "analysis"

ERRORS = []
WARNINGS = []
COUNTS = {}


def err(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNINGS.append(msg)


def load_json(path, required=True):
    if not path.exists():
        if required:
            err(f"Файл отсутствует: {path.relative_to(ROOT)}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        err(f"Файл {path.relative_to(ROOT)} не парсится как JSON: {e}")
        return None


# ---------------------------------------------------------------- helpers
def check_unique_ids(entries, kind, id_key="ID"):
    seen = {}
    for e in entries:
        i = e.get(id_key)
        if not i:
            err(f"{kind}: элемент без {id_key}")
            continue
        if i in seen:
            err(f"Дубликат {id_key} в {kind}: {i} (повтор в записи {seen[i]})")
        seen[i] = True
    return [e.get(id_key) for e in entries]


def check_required_fields(obj, fields, where):
    for f in fields:
        v = obj.get(f)
        if v is None or (isinstance(v, str) and not v.strip()):
            err(f"{where}: отсутствует/пусто обязательное поле '{f}'")


def check_ints_between(obj, field, lo, hi, where):
    v = obj.get(field)
    if not isinstance(v, int) or isinstance(v, bool):
        err(f"{where}: поле '{field}' должно быть целым числом")
        return False
    if not (lo <= v <= hi):
        err(f"{where}: поле '{field}' = {v} вне диапазона [{lo}..{hi}]")
        return False
    return True


# ---------------------------------------------------------------- 1. enemies
def validate_enemies(enemies):
    ids = check_unique_ids(enemies, "enemies")
    COUNTS["enemies"] = len(ids)
    if len(ids) < 6:
        err(f"Врагов {len(ids)}, требуется минимум 6")
    required = ["ID", "NAME", "ROLE", "HEALTH", "SPEED", "DAMAGE", "ATTACK",
                "AI_STATES", "WEAKNESS", "ANIMATIONS", "VISUAL_SILHOUETTE", "SPAWN_RULES"]
    for e in enemies:
        where = f"enemy[{e.get('ID')}]"
        check_required_fields(e, required, where)
        check_ints_between(e, "HEALTH", 1, 1000, where)
        check_ints_between(e, "SPEED", 0, 49152, where)
        if e.get("DAMAGE") == 0 and "support" not in str(e.get("ROLE", "")).lower() \
                and "поддержк" not in str(e.get("ROLE", "")).lower():
            err(f"{where}: DAMAGE=0 допустим только для поддержки (нет 'support'/'поддержк' в ROLE)")
        check_ints_between(e, "DAMAGE", 0, 100, where)
        if not isinstance(e.get("AI_STATES"), list) or not e["AI_STATES"]:
            err(f"{where}: AI_STATES должен быть непустым списком")
        if not isinstance(e.get("WEAKNESS"), list) or not e["WEAKNESS"]:
            err(f"{where}: WEAKNESS должен быть непустым списком")
        anim = e.get("ANIMATIONS")
        if not isinstance(anim, dict):
            err(f"{where}: ANIMATIONS должен быть объектом")
        else:
            for need in ("walk", "attack", "die"):
                a = anim.get(need)
                if not isinstance(a, dict) or not isinstance(a.get("frames"), int) \
                        or a["frames"] < 1 or not isinstance(a.get("duration_ms"), int) \
                        or not (50 <= a["duration_ms"] <= 500):
                    err(f"{where}: анимация '{need}' должна иметь frames>=1 и duration_ms в [50..500]")
        att = e.get("ATTACK")
        if not isinstance(att, dict) or not att.get("type"):
            err(f"{where}: ATTACK должен быть объектом с type")
        else:
            check_ints_between(att, "range_tiles", 1, 16, f"{where}.ATTACK")
            if att.get("cooldown_ms") is not None:
                check_ints_between(att, "cooldown_ms", 0, 10000, f"{where}.ATTACK")
    return ids


# ---------------------------------------------------------------- 2. weapons
def validate_weapons(weapons, mech_ids, mission_ids):
    ids = check_unique_ids(weapons, "weapons")
    COUNTS["weapons"] = len(ids)
    if len(ids) < 6:
        err(f"Оружия {len(ids)}, требуется минимум 6")
    required = ["ID", "NAME", "CALIBER", "damage", "fire_rate", "ammo", "reload",
                "range", "spread", "special_behavior", "animation", "sound_concept",
                "platform_notes"]
    for w in weapons:
        where = f"weapon[{w.get('ID')}]"
        check_required_fields(w, required, where)
        check_ints_between(w, "damage", 1, 200, where)
        check_ints_between(w, "fire_rate", 80, 3000, where)
        cat = w.get("category", "")
        if cat == "melee":
            if w.get("ammo") != 999:
                err(f"{where}: melee должно иметь ammo=999 (бесконечность)")
        else:
            check_ints_between(w, "ammo", 1, 250, where)
            check_ints_between(w, "reload", 500, 5000, where)
        check_ints_between(w, "range", 1, 32, where)
        check_ints_between(w, "spread", 0, 100, where)
        if w.get("reload") == 0 and cat != "melee":
            err(f"{where}: reload=0 допустим только для melee")
        if w.get("ammo", 0) >= 100 and cat != "melee":
            err(f"{where}: ammo>=100 допустим только для melee (бесконечные)")
        anim = w.get("animation")
        if not isinstance(anim, dict) or not isinstance(anim.get("shoot"), dict):
            err(f"{where}: animation.shoot обязателен")
        else:
            sh = anim["shoot"]
            frames = sh.get("frames", 0)
            dur = sh.get("duration_ms", 0)
            if not (1 <= frames <= 6 and 40 <= dur <= 300):
                err(f"{where}: animation.shoot: frames 1..6, duration_ms 40..300")
            if cat != "melee" and w.get("fire_rate", 0) < frames * dur:
                err(f"{where}: противоречие: fire_rate ({w.get('fire_rate')}мс) короче "
                    f"анимации выстрела ({frames}*{dur}={frames*dur}мс)")
        # ссылки
        for m in w.get("mechanics_used", []):
            if m not in mech_ids:
                err(f"{where}: mechanics_used ссылается на несуществующую механику '{m}'")
        if mission_ids is not None:
            um = w.get("unlock_mission")
            if not um:
                err(f"{where}: нет unlock_mission (оружие нигде не выдаётся)")
            elif um not in mission_ids:
                err(f"{where}: unlock_mission '{um}' не существует в миссиях")
    return ids


# ---------------------------------------------------------------- 3. items
def validate_items(items, weapon_ids):
    ids = check_unique_ids(items, "items")
    COUNTS["items"] = len(ids)
    cats = {}
    required = ["ID", "NAME", "CATEGORY", "EFFECT", "QUANTITY_MAX", "USE_TRIGGER", "AVAILABILITY"]
    valid_cats = {"healing", "ammo", "quest", "utility", "special"}
    for it in items:
        where = f"item[{it.get('ID')}]"
        check_required_fields(it, required, where)
        cat = it.get("CATEGORY")
        if cat not in valid_cats:
            err(f"{where}: невалидная CATEGORY '{cat}'")
        else:
            cats[cat] = cats.get(cat, 0) + 1
        check_ints_between(it, "QUANTITY_MAX", 1, 999, where)
        av = it.get("AVAILABILITY")
        if av not in {"start", "shop", "drop", "mission"}:
            err(f"{where}: невалидная AVAILABILITY '{av}'")
        for wid in it.get("AMMO_FOR", []):
            if wid not in weapon_ids:
                err(f"{where}: AMMO_FOR ссылается на несуществующее оружие '{wid}'")
            elif cat != "ammo":
                err(f"{where}: AMMO_FOR допустим только для категории ammo")
    for c in valid_cats:
        if c not in cats:
            err(f"Нет ни одного предмета категории '{c}' (требуются все 5 категорий)")
    return ids


# ---------------------------------------------------------------- 4. mechanics
def validate_mechanics(mechanics):
    ids = check_unique_ids(mechanics, "mechanics")
    COUNTS["mechanics"] = len(ids)
    if len(ids) < 5:
        err(f"Механик {len(ids)}, требуется минимум 5")
    classes = set()
    required = ["ID", "NAME", "CLASS", "DESCRIPTION", "TECHNICAL_IMPLEMENTATION"]
    for m in mechanics:
        where = f"mechanic[{m.get('ID')}]"
        check_required_fields(m, required, where)
        cls = m.get("CLASS")
        if cls not in {"CORE", "OPTIONAL", "EXPERIMENTAL"}:
            err(f"{where}: CLASS '{cls}' не в {['CORE','OPTIONAL','EXPERIMENTAL']}")
        else:
            classes.add(cls)
    for c in ("CORE", "OPTIONAL", "EXPERIMENTAL"):
        if c not in classes:
            err(f"Нет ни одной механики класса {c}")
    return ids


# ---------------------------------------------------------------- 5. missions
def validate_missions(missions, enemy_ids, mech_ids, weapon_ids, item_ids, original_level_ids):
    ids = check_unique_ids(missions, "missions")
    COUNTS["missions"] = len(ids)
    if len(ids) < 20:
        err(f"Миссий {len(ids)}, требуется минимум 20")
    required = ["ID", "TITLE", "LOCATION", "PRIMARY_OBJECTIVE", "SECONDARY_OBJECTIVE",
                "NEW_MECHANIC", "ENEMY_TYPES", "KEY_EVENT", "CLIMAX", "REWARD", "VISUAL_THEME"]
    titles = {}
    acts = set()
    mission_act = {}
    for m in missions:
        mid = m.get("ID")
        where = f"mission[{mid}]"
        check_required_fields(m, required, where)
        act = m.get("ACT")
        if act not in {"I", "II", "III"}:
            err(f"{where}: ACT '{act}' не в {{I, II, III}}")
        else:
            acts.add(act)
            mission_act[mid] = act
        if mid and re.match(r"^m\d", str(mid)):
            err(f"{where}: ID '{mid}' похож на оригинальный уровень (m0-m13_2)")
        if mid and mid in original_level_ids:
            err(f"{where}: ID '{mid}' совпадает с оригинальным уровнем")
        title = m.get("TITLE")
        if title:
            if title in titles:
                err(f"{where}: дубликат TITLE '{title}' (также у {titles[title]})")
            titles[title] = mid
        nm = m.get("NEW_MECHANIC")
        if not isinstance(nm, list) or not nm:
            err(f"{where}: NEW_MECHANIC должен быть непустым списком")
        else:
            for x in nm:
                if x not in mech_ids:
                    err(f"{where}: NEW_MECHANIC ссылается на несуществующую механику '{x}'")
        et = m.get("ENEMY_TYPES")
        if not isinstance(et, list) or not et:
            err(f"{where}: ENEMY_TYPES должен быть непустым списком")
        else:
            for x in et:
                if x not in enemy_ids:
                    err(f"{where}: ENEMY_TYPES ссылается на несуществующего врага '{x}'")
        # REWARD-токены: weapon:ID / item:ID / scrap:N / unlock:NAME
        for token in str(m.get("REWARD", "")).split(","):
            token = token.strip()
            if not token:
                err(f"{where}: пустой REWARD-токен")
                continue
            if token.startswith("weapon:"):
                wid = token.split(":", 1)[1]
                if wid not in weapon_ids:
                    err(f"{where}: REWARD ссылается на несуществующее оружие '{wid}'")
            elif token.startswith("item:"):
                iid = token.split(":", 1)[1]
                if iid not in item_ids:
                    err(f"{where}: REWARD ссылается на несуществующий предмет '{iid}'")
            elif token.startswith("scrap:"):
                n = token.split(":", 1)[1]
                if not n.isdigit() or int(n) <= 0:
                    err(f"{where}: REWARD-токен '{token}' должен быть scrap:положительное_число")
            elif not token.startswith("unlock:"):
                err(f"{where}: невалидный REWARD-токен '{token}' "
                    f"(ожидается weapon:/item:/scrap:/unlock:)")
    for a in ("I", "II", "III"):
        if a not in acts:
            err(f"Нет миссий акта {a}")
    return ids, mission_act


# ---------------------------------------------------------------- 6. cross-checks
def cross_checks(enemy_ids, weapon_ids, item_ids, mech_ids, missions, weapons,
                 items, mechanics, mission_act):
    # каждый враг используется хотя бы в одной миссии
    used_enemies = {e for m in missions for e in m.get("ENEMY_TYPES", [])}
    for eid in enemy_ids:
        if eid not in used_enemies:
            err(f"Враг '{eid}' не используется ни в одной миссии")
    # каждая механика используется хотя бы в одной миссии
    used_mech = {x for m in missions for x in m.get("NEW_MECHANIC", [])}
    for mid in mech_ids:
        if mid not in used_mech:
            err(f"Механика '{mid}' не используется ни в одной миссии")
    # оружие: unlock_mission существует и акт выдачи >= акта появления в REWARD
    for w in weapons:
        um = w.get("unlock_mission")
        if um and um in mission_act:
            for m in missions:
                if m["ID"] == um:
                    reward_weapons = [t.split(":", 1)[1] for t in str(m.get("REWARD", "")).split(",")
                                      if t.startswith("weapon:")]
                    if w["ID"] in reward_weapons:
                        continue  # выдано в той же миссии, что и unlock
            # проверить, что оружие вообще где-то выдано
            given_in = [m["ID"] for m in missions
                        if any(t.startswith(f"weapon:{w['ID']}") for t in str(m.get("REWARD", "")).split(","))]
            if not given_in:
                err(f"Оружие '{w['ID']}' нигде не выдаётся в REWARD миссий")
    # предметы: AVAILABILITY=mission -> должен быть в REWARD какой-то миссии
    reward_items = {t.split(":", 1)[1] for m in missions for t in str(m.get("REWARD", "")).split(",")
                    if t.startswith("item:")}
    for it in items:
        if it.get("AVAILABILITY") == "mission" and it["ID"] not in reward_items:
            err(f"Предмет '{it['ID']}' помечен AVAILABILITY=mission, но не выдан ни в одной миссии")
        elif it["ID"] not in reward_items and it.get("AVAILABILITY") in {"start", "shop", "drop"}:
            warn(f"Предмет '{it['ID']}' ({it.get('AVAILABILITY')}) не выдан в миссиях — ожидаемо")
    # боеприпасы: все оружия в AMMO_FOR должны иметь один калибр
    weapons_by_id = {w["ID"]: w for w in weapons}
    for it in items:
        af = it.get("AMMO_FOR", [])
        if af:
            calibers = {weapons_by_id[w].get("CALIBER") for w in af if w in weapons_by_id}
            if len(calibers) > 1:
                err(f"item[{it['ID']}]: AMMO_FOR ссылается на разные калибры {calibers}")
    # глобальная уникальность ID между файлами
    all_ids = {}
    for kind, ids in (("enemies", enemy_ids), ("weapons", weapon_ids),
                      ("items", item_ids), ("mechanics", mech_ids)):
        for i in ids:
            if i in all_ids:
                err(f"ID '{i}' встречается и в {all_ids[i]}, и в {kind}")
            all_ids[i] = kind


# ---------------------------------------------------------------- 7. text files
MARKER_RE = re.compile(r"<!-- marker: (\w+) -->")


def check_markers(path, required_markers, what):
    if not path.exists():
        err(f"Файл отсутствует: {path.relative_to(ROOT)}")
        return
    text = path.read_text(encoding="utf-8")
    found = set(MARKER_RE.findall(text))
    for m in required_markers:
        if m not in found:
            err(f"{what}: отсутствует маркер '{m}' в {path.relative_to(ROOT)}")


def validate_bible():
    p = SEQ / "SEQUEL_DESIGN_BIBLE.md"
    if not p.exists():
        err("Файл отсутствует: SEQUEL_DESIGN_BIBLE.md")
        return
    text = p.read_text(encoding="utf-8")
    for n in range(1, 17):
        if f"## {n}." not in text:
            err(f"SEQUEL_DESIGN_BIBLE.md: отсутствует раздел '## {n}.'")
    if "МЁРТВАЯ ЧАСТОТА" not in text:
        err("SEQUEL_DESIGN_BIBLE.md: нет названия игры «МЁРТВАЯ ЧАСТОТА»")


# ---------------------------------------------------------------- 8. json docs
def validate_level_standard():
    d = load_json(SEQ / "level-design-standard.json")
    if d is None:
        return
    scr = d.get("screen") or {}
    if scr.get("width_px") != 240 or scr.get("height_px") != 320:
        err("level-design-standard: screen должен быть 240x320")
    tile = d.get("tile") or {}
    if tile.get("size_px") != 16:
        err("level-design-standard: tile.size_px должен быть 16")
    grid = d.get("grid") or {}
    if grid.get("width_tiles") != 64 or grid.get("height_tiles") != 64:
        err("level-design-standard: grid должен быть 64x64")
    col = d.get("collision") or {}
    if col.get("representation") != "compact_bitmask":
        err("level-design-standard: collision.representation должен быть compact_bitmask")
    ops = d.get("opcodes")
    if not isinstance(ops, list) or len(ops) < 10:
        err(f"level-design-standard: опкодов {len(ops) if isinstance(ops, list) else 0}, нужно >= 10")
    else:
        seen = set()
        for op in ops:
            oid = op.get("id")
            if oid in seen:
                err(f"level-design-standard: дубликат опкода {oid}")
            seen.add(oid)
            if not op.get("name") or not op.get("description"):
                err(f"level-design-standard: опкод {oid} без name/description")
    if not isinstance(d.get("budgets"), dict):
        err("level-design-standard: отсутствует budgets")


def validate_architecture():
    d = load_json(SEQ / "sequel-architecture.json")
    if d is None:
        return
    plat = d.get("platform") or {}
    if "CLDC-1.0" not in str(plat.get("profile", "")):
        err("sequel-architecture: profile должен содержать CLDC-1.0")
    modules = d.get("modules") or {}
    need = ["game_loop", "state_machine", "entities", "ai", "collision", "camera",
            "animation", "resources", "levels", "script_system", "save_system", "audio"]
    for m in need:
        mod = modules.get(m)
        if not isinstance(mod, dict) or not mod.get("description"):
            err(f"sequel-architecture: модуль '{m}' отсутствует или без description")
        elif not mod.get("budget"):
            warn(f"sequel-architecture: модуль '{m}' без budget")
    imp = d.get("improvements_vs_original")
    if not isinstance(imp, list) or len(imp) < 5:
        err("sequel-architecture: improvements_vs_original должен содержать >= 5 пунктов")


def validate_matrix():
    d = load_json(SEQ / "original-to-sequel-matrix.json")
    if d is None:
        return
    rows = d.get("matrix")
    if not isinstance(rows, list) or len(rows) < 15:
        err(f"original-to-sequel-matrix: строк {len(rows) if isinstance(rows, list) else 0}, нужно >= 15")
        return
    statuses = set()
    for r in rows:
        if not r.get("ORIGINAL") or not r.get("SEQUEL") or not r.get("RATIONALE"):
            err(f"matrix: строка без ORIGINAL/SEQUEL/RATIONALE: {r}")
        st = r.get("STATUS")
        if st not in {"PRESERVED", "EVOLVED", "NEW"}:
            err(f"matrix: невалидный STATUS '{st}'")
        else:
            statuses.add(st)
    for s in ("PRESERVED", "EVOLVED", "NEW"):
        if s not in statuses:
            err(f"matrix: не используется статус {s}")


def validate_design_review():
    check_markers(SEQ / "design-review.md",
                  ["recognizability", "novelty", "technical_realism",
                   "mechanic_coherence", "no_direct_remake"],
                  "design-review.md")


def validate_visual_bible():
    check_markers(SEQ / "SEQUEL_VISUAL_BIBLE.md",
                  ["target_resolution", "tile_size", "sprite_scale", "palette_strategy",
                   "outlines", "shading", "lighting", "animation_cadence",
                   "ui_composition", "typography", "effects", "environmental_density"],
                  "SEQUEL_VISUAL_BIBLE.md")


def validate_originality_boundary():
    p = SEQ / "originality-boundary.md"
    if not p.exists():
        err("Файл отсутствует: originality-boundary.md")
        return
    text = p.read_text(encoding="utf-8")
    found = dict(MARKER_RE.findall(text))
    ref_only = ["original_code", "original_binary_resources", "original_sprites", "original_dialogue"]
    indep = ["new_code", "new_assets", "new_dialogue", "new_levels"]
    lines = [ln.strip() for ln in text.splitlines()]
    for cat in ref_only + indep:
        hit = [ln for ln in lines if ln.startswith(f"- [x] {cat}:")]
        if not hit:
            err(f"originality-boundary: отсутствует строка чек-листа для '{cat}'")
            continue
        if cat in ref_only and "reference only" not in hit[0]:
            err(f"originality-boundary: '{cat}' должен быть помечен 'reference only'")
        if cat in indep and "independently created" not in hit[0]:
            err(f"originality-boundary: '{cat}' должен быть помечен 'independently created'")
    if "reference only" not in text.lower():
        err("originality-boundary: отсутствует общая формулировка 'reference only'")
    if "independently created" not in text.lower():
        err("originality-boundary: отсутствует общая формулировка 'independently created'")


# ---------------------------------------------------------------- main
def main():
    # оригинальные ID уровней — из исследовательской базы (read-only)
    orig = load_json(ANALYSIS / "all-levels-index.json", required=False) or {}
    original_level_ids = set(orig.keys())

    enemies = load_json(SEQ / "enemies-master.json")
    weapons = load_json(SEQ / "weapons-master.json")
    items = load_json(SEQ / "items-master.json")
    mechanics = load_json(SEQ / "mechanics-master.json")
    missions = load_json(SEQ / "missions-master.json")

    enemy_ids = validate_enemies((enemies or {}).get("enemies", [])) if enemies else []
    mech_ids = validate_mechanics((mechanics or {}).get("mechanics", [])) if mechanics else []
    weapon_ids = validate_weapons((weapons or {}).get("weapons", []), mech_ids, None) if weapons else []
    item_ids = validate_items((items or {}).get("items", []), weapon_ids) if items else []
    mission_ids, mission_act = validate_missions(
        (missions or {}).get("missions", []), enemy_ids, mech_ids,
        weapon_ids, item_ids, original_level_ids) if missions else ([], {})

    if weapons:
        # вторая фаза: проверка unlock_mission после валидации миссий
        validate_weapons((weapons or {}).get("weapons", []), mech_ids, mission_ids)

    if missions and enemy_ids and weapon_ids and item_ids and mech_ids:
        cross_checks(enemy_ids, weapon_ids, item_ids, mech_ids,
                     missions.get("missions", []), weapons.get("weapons", []),
                     items.get("items", []), mechanics.get("mechanics", []), mission_act)

    validate_bible()
    validate_visual_bible()
    validate_originality_boundary()
    validate_design_review()
    validate_level_standard()
    validate_architecture()
    validate_matrix()

    # ------------------------------------------------------------- report
    print("=" * 62)
    print("VALIDATE SEQUEL DESIGN — «МЁРТВАЯ ЧАСТОТА» (DEAD FREQUENCY)")
    print("=" * 62)
    print(f"Врагов (enemy archetypes): {COUNTS.get('enemies', 0)}")
    print(f"Оружия (weapons):          {COUNTS.get('weapons', 0)}")
    print(f"Предметы (items):          {COUNTS.get('items', 0)}")
    print(f"Механики (mechanics):      {COUNTS.get('mechanics', 0)}")
    print(f"Миссии (missions):         {COUNTS.get('missions', 0)}")
    print("-" * 62)
    if WARNINGS:
        print(f"WARNING ({len(WARNINGS)}):")
        for w in WARNINGS:
            print(f"  ! {w}")
    if ERRORS:
        print(f"ERROR ({len(ERRORS)}):")
        for e in ERRORS:
            print(f"  x {e}")
        print("=" * 62)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERRORS)} ошибок")
        return 1
    print(f"РЕЗУЛЬТАТ: PASS — ошибок нет"
          f"{f', предупреждений {len(WARNINGS)}' if WARNINGS else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
