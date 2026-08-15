#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_ai_database_v2.py — AI и поведение 56 архетипов (этап 15.17).

Источники: f.java (f.b/f.i/f.j/f.o/f.p/f.e/f.s/f.m/f.a), g.java, m9 seg4, instance registry.

AI-классы: prop10 (0/1/2/3/5/7...). Состояния: g[12] (0,1,4,7,8,9,12,13,14,17,18,19,23,24,26,27,28,100+).
Вывод: research/analysis/v2/ai/*.json
"""
import json
import sys
from collections import Counter
from pathlib import Path

OUT = Path("research/analysis/v2/ai")
ENTS = Path("research/analysis/v2/entities")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    ents = json.load(open(ENTS / "entity-table-v2.json"))
    clusters = json.load(open(ENTS / "archetype-clusters-v2.json"))
    reg = json.load(open(Path("research/analysis/v2/instances") / "instance-registry-v2.json"))

    # ---------- 1. AI dispatch map ----------
    dispatch = {
        "meta": "AI диспетчер: prop10 (класс ИИ) -> ветвления в f.java.",
        "classes": {
            "0": {"branches": ["f.d(): n==0 стреляющий класс", "f.C()/I()/J()/s(): n==0|3|5|7 направленные",
                                "f.e(): n==0|5|3|7 (s-зоны)", "f.o(): n2!=0 -> g[10]=0 (простой)",
                                "f.p(): n2==0 -> g[10] ветвления"],
                  "evidence": "f.java:2380,2830,3662,4599,4603,5422"},
            "1": {"branches": ["f.a(): n3==1 && (g[16]&0x100) — особый кадр-режим",
                               "f.e(): n==2 && g[12]==7/8 — спец-состояния"],
                  "evidence": "f.java:4645, 4607"},
            "2": {"branches": ["f.e(): n==2 && (g[12]==7||g[12]==8) — уникальное условие",
                               "f.i(): g.N||n5==2 — не-снарядный класс"],
                  "evidence": "f.java:4607, 2830"},
            "3": {"branches": ["как 0/5/7 (направленные)"], "evidence": "f.java:3662,4599"},
            "5": {"branches": ["f.d(): n==5||7 && (g[16]&0x20) — стрелок с флагом 0x20",
                               "f.C(): n==5||7 && g[12]!=-1 — поведение стрелка"],
                  "evidence": "f.java:2380, 2412"},
            "7": {"branches": ["как 5"], "evidence": "f.java:2380,2412"},
        },
        "property_usage": {
            "prop7": "зона направлений A [n, n+4) — f.s() (видимость/атака)",
            "prop8": "зона направлений B [n, n+4)",
            "prop10": "КЛАСС ИИ (главный диспетчер)",
            "prop12": "урон/параметр атаки (f.i() case 7: f.d(f2, n2))",
            "prop14": "анимация жертвы при атаке",
            "prop15": "флаг выбора ветки (f.a(): prop15==1)",
            "prop17": "порог дистанции атаки (f.i() case 7: n <= n3)",
            "prop22": "урон атаки (f.java:2894)",
            "prop29": "спец-поле (==-1 проверка)",
        }
    }
    (OUT / "ai-dispatch-map-v2.json").write_text(json.dumps(dispatch, indent=1, ensure_ascii=False))

    # ---------- 2. state machine ----------
    sm = {
        "meta": "Состояния сущностей g[12] (по ветвлениям f.java). 100+ = терминальные.",
        "states": {
            "0": {"desc": "idle-подобное (f.o(): n2==0 -> g[13]=0,g[14]=-16384; f.a(): кадр dir+prop2)", "evidence": "f.java:5422, 4645"},
            "1": {"desc": "состояние 1 (f.a(): кадр dir+prop3)", "evidence": "f.java:4660"},
            "4": {"desc": "состояние 4 (f.i() переходы)", "evidence": "f.java:5422"},
            "7": {"desc": "АТАКА: f.i() case 7: если цель в дистанции prop17 -> урон f.b(f3, prop14), переход 8; иначе 4/0", "evidence": "f.java:5422-5456"},
            "8": {"desc": "АТАКА-2: таймер g[15] < 1000 -> звук 21, урон; иначе переход", "evidence": "f.java:5457-5490"},
            "9": {"desc": "состояние 9 (f.i() case 8: f.c(f2,9) при f.m<555)", "evidence": "f.java:5483"},
            "12": {"desc": "АТАКА-3: урон f.b(f3, prop14<<1); f.a(g[13],g[14]) — направленный удар", "evidence": "f.java:5491-5510"},
            "13": {"desc": "завершение атаки -> 4", "evidence": "f.java:5511"},
            "14": {"desc": "состояние 14 (f.o(): переход к 100)", "evidence": "f.java:5422"},
            "17": {"desc": "состояние 17", "evidence": "f.java (ветвления)"},
            "18": {"desc": "состояние 18", "evidence": "f.java"},
            "19": {"desc": "состояние 19", "evidence": "f.java"},
            "23": {"desc": "дефолт спавна (f.java:2799)", "evidence": "f.java:2799"},
            "24": {"desc": "состояние 24: установка флага 0x100 -> 4", "evidence": "f.java:5518"},
            "26": {"desc": "f.p(f2) ветвление (g[10]==0/6)", "evidence": "f.java:5535"},
            "27": {"desc": "f.p(f2)", "evidence": "f.java:5535"},
            "28": {"desc": "f.p(f2); кадр dir+prop2 (f.a() case 0/6/28)", "evidence": "f.java:5535, 4656"},
            "100": {"desc": "ТЕРМИНАЛЬНОЕ (смерть/уничтожение); f.o(): n=100", "evidence": "f.java:5434"},
            "101": {"desc": "ТЕРМИНАЛЬНОЕ (смерть/уничтожение)", "evidence": "f.java:5485"},
            "103..107": {"desc": "терминальные варианты", "evidence": "f.java:3242-3255"},
            "108": {"desc": "f.p(f2) ветвление: g[12]==108 -> 100", "evidence": "f.java:5545"},
        },
        "g10_substates": {"0": "обычное", "3": "подсостояние 3", "4": "подсостояние 4", "5": "не-атакуемое (f.b(): g[10]==5 continue)", "6": "f.p() ветвление"},
        "g16_flags": {"0x20": "стрелок-флаг (f.d)", "0x100": "особый кадр-режим (f.a)", "0x400": "телепорт-флаг", "0x800": "анимации инициализированы", "0x2000/0x4000/0x8000": "прочие"},
        "ai_timers": {"g[15]": "таймер атаки (case 8: < 1000 мс)", "f.w": "таймер 800 мс", "g[22]": "таймеры", "g[24]": "таймер 0x800-флаг", "g[27]": "время последнего действия", "f.g": "глобальное время"}
    }
    (OUT / "ai-state-machine-v2.json").write_text(json.dumps(sm, indent=1, ensure_ascii=False))

    # ---------- 3. transition graph ----------
    tg = {
        "meta": "Граф переходов (из f.i()/f.o()/f.p()/f.j(), доказанные ветки)",
        "transitions": [
            {"from": "23 (спавн)", "to": "0/4", "condition": "инициализация", "evidence": "f.java:2799,2823", "confidence": "CONFIRMED"},
            {"from": "7 (атака)", "to": "8", "condition": "цель в дистанции prop17, анимация завершена", "evidence": "f.java:5448 (f.c(f2,8))", "confidence": "CONFIRMED"},
            {"from": "7", "to": "4", "condition": "цель вне зоны/нет цели", "evidence": "f.java:5452", "confidence": "CONFIRMED"},
            {"from": "7", "to": "0", "condition": "цель = null", "evidence": "f.java:5454", "confidence": "CONFIRMED"},
            {"from": "8", "to": "4", "condition": "после таймера/урона", "evidence": "f.java:5470-5487", "confidence": "CONFIRMED"},
            {"from": "8", "to": "9", "condition": "жертва f.m<555 -> f.d(f3,101)", "evidence": "f.java:5483", "confidence": "CONFIRMED"},
            {"from": "12", "to": "13", "condition": "анимация завершена", "evidence": "f.java:5493", "confidence": "CONFIRMED"},
            {"from": "13", "to": "4", "condition": "завершение", "evidence": "f.java:5511", "confidence": "CONFIRMED"},
            {"from": "24", "to": "4", "condition": "установка флага 0x100", "evidence": "f.java:5518", "confidence": "CONFIRMED"},
            {"from": "14", "to": "100", "condition": "f.o(): переход к терминальному", "evidence": "f.java:5434", "confidence": "CONFIRMED"},
            {"from": "108", "to": "100", "condition": "f.p() g[12]==108", "evidence": "f.java:5545", "confidence": "CONFIRMED"},
            {"from": "0/4/9/14/17/18/19", "to": "100+", "condition": "g[12] >= 100 (смерть)", "evidence": "f.java:3242-3255", "confidence": "CONFIRMED"},
        ]
    }
    (OUT / "ai-transition-graph-v2.json").write_text(json.dumps(tg, indent=1, ensure_ascii=False))

    # ---------- 5/7/8. movement / attacks / damage ----------
    mov = {"meta": "Движение: velocities из g[13]/g[14] (fixed-point); направление f.b(); скорости-константы 50-110 px/s; "
                   "prop2 = сдвиг направления для кадра.",
           "chase": "прямое преследование: f.i()/f.j() наведение g.a(позиция, скорость-таблица n17/n18) — "
                    "velocity к цели (НЕ pathfinding: нет обхода препятствий, только AABB-столкновения)",
           "pathfinding": "НАСТОЯЩЕГО PATHFINDING НЕТ: движение — прямое преследование цели с velocity; "
                          "столкновения — AABB/5-точечный зонд; f.p() проверяет проходимость (g.d(x/16,y/16)) "
                          "и меняет направление",
           "evidence": "f.java:2830 (g.a velocity), 4572 (f.b dir), 2402 (p проверка)"}
    (OUT / "ai-movement-v2.json").write_text(json.dumps(mov, indent=1, ensure_ascii=False))

    att = {"meta": "Модели атак (по состояниям 7/8/12 и prop12/14/17/22)",
           "models": [
               {"id": "ATTACK_7", "condition": "g[12]==7, цель в prop17, анимация", "damage": "f.b(f3, prop14) (урон жертве)", "cooldown": "таймер g[15] (case 8)", "animation": "prop14 = анимация жертвы", "state": "7->8"},
               {"id": "ATTACK_8", "condition": "g[12]==8, цель рядом, g[15]>=1000", "damage": "f.b(g.c, prop14) / f.o(f3, prop14)", "sound": "g.b(21)", "state": "8->4/9"},
               {"id": "ATTACK_12", "condition": "g[12]==12, анимация, цель в зоне", "damage": "f.b(f3, prop14<<1)", "state": "12->13"},
               {"id": "RANGED", "condition": "prop10 ∈ {0,3,5,7}: наведение g.a() со снарядной скоростью (n14=819200 px/s)", "damage": "по prop22/снаряд", "evidence": "f.java:2830"},
           ],
           "ranged_formula": "n15 = |dx|*1000/819200; n17 = dx/(n15+1) — скорость снаряда к цели (fixed-point)"}
    (OUT / "ai-attacks-v2.json").write_text(json.dumps(att, indent=1, ensure_ascii=False))

    dmg = {"meta": "Реакция на урон/смерть",
           "damage": "f.b(f2, n) (f.java:767): g[7] -= урон + 30%*bF; звук 22/23; g.i(n)",
           "hurt": "состояния <100; g[16] флаги",
           "death": "g[12] >= 100 (терминальные 100/101/103..107); f.d(f3,101) жертва",
           "knockback": "НЕ найдено отдельного (движение velocity)",
           "health_source": "g[7] (не prop!) — HP хранится в поле экземпляра, не в архетипе",
           "evidence": "f.java:767-780, 3242-3255"}
    (OUT / "ai-damage-response-v2.json").write_text(json.dumps(dmg, indent=1, ensure_ascii=False))

    # ---------- 10/11. archetype behavior master + cluster profiles ----------
    master = {"meta": "56 архетипов -> кластеры/поведение", "archetypes": []}
    cluster_map = {}
    for c in clusters["clusters"]:
        sig = c["signature"]
        key = (sig["ai_class"], sig["facing_a"], sig["facing_b"], sig["box_w_tiles"], sig["box_h_tiles"], sig["attack_damage"])
        for aid in c["archetype_ids"]:
            cluster_map[aid] = c
    cluster_profiles = {}
    for c in clusters["clusters"]:
        sig = c["signature"]
        cluster_profiles.setdefault(tuple(sorted(c["archetype_ids"])), c)
    for a in ents["archetypes"]:
        aid = a["entity_id"]
        c = cluster_map.get(aid, {})
        master["archetypes"].append({
            "archetype_id": aid, "name": a["name"],
            "behavior_cluster": f"BEHAVIOR_CLUSTER_{list(cluster_map).index(aid) if aid in cluster_map else '?'}",
            "ai_class_prop10": c.get("signature", {}).get("ai_class"),
            "facing_zones": [c.get("signature", {}).get("facing_a"), c.get("signature", {}).get("facing_b")],
            "collision_box_tiles": [c.get("signature", {}).get("box_w_tiles"), c.get("signature", {}).get("box_h_tiles")],
            "attack_damage_prop22": c.get("signature", {}).get("attack_damage"),
            "state_machine": "g[12] общая (см. ai-state-machine-v2)",
            "animation": "prop32/33/34 (см. archetype-animation-map)",
            "sprite": "m6_*/m7 (структурно)",
            "mission_usage": "см. mission-entity-usage",
            "confidence": "CONFIRMED (структура)"
        })
    (OUT / "archetype-behavior-master-v2.json").write_text(json.dumps(master, indent=1, ensure_ascii=False))

    # ---------- 12. instance behavior ----------
    ib = {"meta": "666 экземпляров -> поведение", "missions": []}
    for m in reg["missions"]:
        insts = []
        for e in m["instances"]:
            if e.get("archetype_id") is None:
                continue
            insts.append({"instance_id": e["instance_id"], "archetype": e.get("archetype_name"),
                          "cluster": e.get("behavior_cluster"), "ai_class_prop10": e.get("properties", {}).get("prop10_ai"),
                          "initial_state": e.get("initial_state"), "animation": e.get("animation_set"),
                          "sprite": "m6_*/m7", "confidence": e.get("confidence")})
        ib["missions"].append({"mission": m["mission"], "instances": insts})
    (OUT / "mission-instance-behavior-v2.json").write_text(json.dumps(ib, indent=1, ensure_ascii=False))

    # ---------- 17. NPC ----------
    npc = {"meta": "NPC: таблица g.w (m9 seg8, ey()), 15 полей; L=9; анимации g.k(type,3);"
                   "цели SetNPCTarget (opcode 148); состояния как у сущностей",
           "source": "g.java:29237 ey(); g.java:31810 m() case 9",
           "states": "g[12] общие; L=9 не участвует в enemy-агро (f.b(): L!=3 continue)",
           "note": "NPC отделены от enemy: f.b() фильтрует L==3"}
    (OUT / "npc-v2.json").write_text(json.dumps(npc, indent=1, ensure_ascii=False))

    # ---------- 19. ai-visual-map ----------
    vm = {"meta": "cluster -> sprite", "clusters": []}
    for aid, c in cluster_map.items():
        vm["clusters"].append({"archetype": aid, "cluster": "BEHAVIOR_CLUSTER",
                               "sprite_resources": "m6_*/m7", "visual_dimensions": "UNKNOWN (RENDER_RUNTIME_REQUIRED)"})
    (OUT / "ai-visual-map-v2.json").write_text(json.dumps(vm, indent=1, ensure_ascii=False))

    print("ai-dispatch-map, ai-state-machine, ai-transition-graph, ai-movement, ai-attacks,")
    print("ai-damage-response, archetype-behavior-master, mission-instance-behavior, npc, ai-visual-map — записаны")


if __name__ == "__main__":
    sys.exit(main())
