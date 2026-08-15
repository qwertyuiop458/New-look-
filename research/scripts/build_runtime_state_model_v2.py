#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_runtime_state_model_v2.py — state/timing модель экземпляра (этап 15.18).

Источники: g.B() (update order), f.c (смена состояния), f.g[12]/g[13..29] поля,
c.java (анимация), таймеры f.w/g[15]/g[22]/g[24]/g[27], главный цикл g.run().

Вывод: research/analysis/v2/runtime/*.json + *.md
"""
import json
import sys
from pathlib import Path

OUT = Path("research/analysis/v2/runtime")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    # ---------- 1. state vector ----------
    sv = {"meta": "Вектор состояния экземпляра (поля f.g[], c-объект). Писатели/читатели из f.java/g.java.",
          "fields": [
              {"field": "g[0]", "type": "int", "initial": "props[0] (архетип-индекс)", "writers": ["конвертеры f.c/f.d", "opcode 114 (g[0]=n4)"],
               "readers": ["g.h(type,...) везде"], "meaning": "ИНДЕКС АРХЕТИПА", "confidence": "CONFIRMED"},
              {"field": "g[1]", "type": "int", "initial": "props", "readers": ["f.e(graphics): f2.a.a.e = g[1]", "f.java:2830 (n19=g[1])"],
               "meaning": "поле анимации/типа (передаётся в c-контроллер)", "confidence": "INFERRED"},
              {"field": "g[2]", "type": "int", "initial": "props", "readers": ["f.java:2830 (n20=g[2]); конструктор L9: a.b(g.k(type,3))"],
               "meaning": "поле анимации/состояния", "confidence": "INFERRED"},
              {"field": "g[7]", "type": "int", "initial": "0 (HP)", "writers": ["f.b(f2,n): g[7] -= n + 30%*bF"], "readers": ["урон"],
               "meaning": "HP экземпляра (НЕ в архетипе)", "confidence": "CONFIRMED"},
              {"field": "g[9]", "type": "int", "initial": "-1 (дефолт)", "writers": ["f.c()/инициализация", "opcode 132: g.d.g[9]=0"],
               "readers": ["f.java:2380-2474 (сравнения)"], "meaning": "поле состояния/цели (d.g[9] сброс)", "confidence": "INFERRED"},
              {"field": "g[10]", "type": "int", "initial": "0", "writers": ["f.o(): g[10]=0", "ветвления"], "readers": ["f.b(): g[10]==5 continue", "f.java:2894"],
               "meaning": "ПОДСОСТОЯНИЕ (0/3/4/5/6)", "confidence": "CONFIRMED"},
              {"field": "g[12]", "type": "int", "initial": "23 (спавн) / 4", "writers": ["f.c(f2,n)", "инициализация", "опкоды"],
               "readers": ["все AI-ветки"], "meaning": "СОСТОЯНИЕ (24 значения)", "confidence": "CONFIRMED"},
              {"field": "g[13]", "type": "int", "initial": "0", "writers": ["движение (velocity X)", "f.o(): g[13]=0"], "readers": ["f.b() направление"],
               "meaning": "СКОРОСТЬ X (fixed-point)", "confidence": "CONFIRMED"},
              {"field": "g[14]", "type": "int", "initial": "16384 (дефолт)", "writers": ["движение (velocity Y)", "f.o(): g[14]=-16384"], "readers": ["f.b()"],
               "meaning": "СКОРОСТЬ Y (fixed-point)", "confidence": "CONFIRMED"},
              {"field": "g[15]", "type": "int", "initial": "0", "writers": ["f.i() case 8: g[15] += d"], "readers": ["case 8: g[15] < 1000"],
               "meaning": "ТАЙМЕР АТАКИ (мс)", "confidence": "CONFIRMED"},
              {"field": "g[16]", "type": "int", "initial": "0", "writers": ["флаги: 0x20/0x100/0x400/0x800/0x2000/0x4000/0x8000"],
               "readers": ["все ветки"], "meaning": "БИТОВЫЕ ФЛАГИ", "confidence": "CONFIRMED"},
              {"field": "g[17]", "type": "int", "initial": "-", "writers": ["f.m(f2,n): g[17]=n"], "readers": ["f.e(f2): g[17]"],
               "meaning": "поле (f.e/f.m пара)", "confidence": "INFERRED"},
              {"field": "g[18]", "type": "int", "initial": "f.a(nArray) (инициализация)", "readers": ["f.m(): g[18]==1"], "meaning": "флаг/маска", "confidence": "INFERRED"},
              {"field": "g[19]/g[20]", "type": "int", "initial": "-120/-120 (bounds)", "readers": ["рендер"], "meaning": "границы (установка при спавне)", "confidence": "INFERRED"},
              {"field": "g[21]", "type": "int", "initial": "маска 4 байта", "writers": ["f.c(): merge 255<<n*8"], "readers": ["рендер-палитра"], "meaning": "ЦВЕТОВАЯ МАСКА (4 канала)", "confidence": "CONFIRMED"},
              {"field": "g[22]", "type": "int", "initial": "-1", "writers": ["f.c(): g[22]=-1", "таймеры"], "readers": ["f.java:2353 (g[22]<0)"], "meaning": "ТАЙМЕР/СЧЁТЧИК", "confidence": "INFERRED"},
              {"field": "g[23]", "type": "int", "initial": "prop10==5/7 -> -1", "writers": ["f.c()"], "readers": ["f.java:2422"], "meaning": "поле (стрелки)", "confidence": "INFERRED"},
              {"field": "g[24]", "type": "int", "initial": "0", "writers": ["f.java:4050 (g[24] -= d)"], "readers": ["f.java:4050-4053"], "meaning": "ТАЙМЕР (0x800-флаг)", "confidence": "CONFIRMED"},
              {"field": "g[26]/g[27]", "type": "int", "initial": "слой (f.a(3): n/n2)", "writers": ["опкоды 142 (телепорт)"], "readers": ["телепорт/слой"], "meaning": "КООРДИНАТЫ СЛОЯ (x/y тайловые)", "confidence": "CONFIRMED"},
              {"field": "g[28]", "type": "int", "initial": "-2", "writers": ["f.a(3)", "опкод 110", "смена оружия"], "readers": ["оружие: g.l(..., g[28])"], "meaning": "СЛОТ ОРУЖИЯ", "confidence": "CONFIRMED"},
              {"field": "g[29]", "type": "int", "initial": "-2", "writers": ["опкод 110", "f.a(3)"], "readers": ["оружие/апгрейд"], "meaning": "ПАРАМЕТР ОРУЖИЯ/АПГРЕЙД", "confidence": "INFERRED"},
              {"field": "g[30+i]", "type": "int", "initial": "f.g(): W[i][0] или X-кадры", "writers": ["f.g()", "опкоды"], "readers": ["f.java:2541 (кадры)"], "meaning": "АНИМАЦИОННЫЕ СЛОТЫ (0..prop33)", "confidence": "CONFIRMED"},
              {"field": "c.a/c.b", "type": "fixed-point", "initial": "спавн-позиция", "writers": ["движение", "опкоды 111/142"], "readers": ["рендер", "камера"],
               "meaning": "ПОЗИЦИЯ X/Y (fixed 14)", "confidence": "CONFIRMED"},
              {"field": "c.d", "type": "int", "initial": "анимация при спавне", "writers": ["f.m(): c.b(n)", "смена состояния"], "readers": ["c.java тики"], "meaning": "ТЕКУЩАЯ АНИМАЦИЯ (id)", "confidence": "CONFIRMED"},
              {"field": "c.e", "type": "int", "initial": "0", "writers": ["c.java: тиковый аккумулятор"], "readers": ["рендер a.a(d,e,...)"], "meaning": "ТЕКУЩИЙ КАДР", "confidence": "CONFIRMED"},
              {"field": "c.f", "type": "int", "initial": "0", "writers": ["c.java"], "readers": ["c.java"], "meaning": "суб-кадр", "confidence": "INFERRED"},
              {"field": "c.g", "type": "int", "initial": "-1 (бесконечно)", "writers": ["c.java повторы"], "readers": ["c.java"], "meaning": "ПОВТОРЫ АНИМАЦИИ", "confidence": "CONFIRMED"},
              {"field": "c.h", "type": "int", "initial": "1 (loop)", "writers": ["c.java a(n,n2,n3)"], "readers": ["c.java"], "meaning": "LOOP/ONCE", "confidence": "CONFIRMED"},
              {"field": "f.w", "type": "int", "initial": "0", "writers": ["case 16: f.w += d"], "readers": ["case 16: < 800"], "meaning": "ТАЙМЕР 800 мс", "confidence": "CONFIRMED"},
          ]}
    (OUT / "entity-state-vector-v2.json").write_text(json.dumps(sv, indent=1, ensure_ascii=False))

    # ---------- 2. initial state ----------
    init = {"meta": "Инициализация экземпляра (из g.Z(), f.c(), f.g(), конструктора)",
            "steps": [
                {"step": "спавн", "detail": "запись миссии -> props; конвертер (f.c/f.d/f.a(3))", "evidence": "g.Z()"},
                {"step": "g[0]", "detail": "архетип-индекс (g.a(g.m/g.w, props[0]))", "evidence": "f.c():2599"},
                {"step": "g[12]", "detail": "0 (дефолт) или 23 (спавн); opcode-задаваемое", "evidence": "f.java:2799,2823"},
                {"step": "g[13]/g[14]", "detail": "0/0 или 0/-16384 (f.o)", "evidence": "f.java:5422"},
                {"step": "анимация", "detail": "L0->66, L3->g.h(type,2), L9->g.k(type,3)", "evidence": "конструктор f.java:8026"},
                {"step": "анимационные слоты", "detail": "f.g(): g[30+i] = W[i][0] или X-кадры", "evidence": "f.java:2572"},
                {"step": "HP", "detail": "g[7] = 0 (урон-счётчик); HP-лимит НЕ в архетипе (требуется рантайм)", "evidence": "f.b():767"},
                {"step": "позиция", "detail": "c.a/c.b = x<<14, y<<14 (мировые px)", "evidence": "c.java:34"},
                {"step": "оружие", "detail": "g[28]/g[29] = -2 (или из opcode 151/160)", "evidence": "f.a(3):6300"},
            ]}
    (OUT / "entity-initial-state-v2.json").write_text(json.dumps(init, indent=1, ensure_ascii=False))

    # ---------- 3. update order ----------
    (OUT / "entity-update-order-v2.md").write_text("""# Entity Update Order V2 (доказанный порядок)

Из g.B() (state 6) + f-методов:

```
g.B() (каждый кадр, state 6)
  1. g.eF()            — эффекты/обновление полей
  2. g.Q()             — (глобальные обновления)
  3. g.bM()            — (менеджер)
  4. g.bE()            — (менеджер)
  5. f.b()             — ГЛОБАЛЬНОЕ АГРО: для всех L==3 врагов:
                         дистанция < 1600 && видимость 133 -> f.i(f3) [переход в 9] 
  6. switch (b): b==0 (геймплей):
     - f.e(c) -> g.c(c), f.a(c) (2 раза) — игрок
     - (перемещение/взаимодействие игрока)
  для каждого экземпляра:
     - f.a(f2, bl, bl2)  — кадр по состоянию g[12] и направлению
     - f.i()/f.j()/f.o()/f.p() — AI-обновление по g[12]
     - движение: velocity g[13]/g[14], шаг 819200, AABB-проверки
     - f.c(f2, n)        — смена состояния (пересчёт анимации)
  рендер: g.l(Graphics) — слои, сущности (c.java a(Graphics)), HUD
```

Порядок доказан последовательностью вызовов g.B() (g.java:1107-1140) и структурами f-методов.
""")

    # ---------- 4/5. timers + time units ----------
    timers = {"meta": "Таймеры экземпляра", "timers": [
        {"field": "g[15]", "unit": "мс", "init": 0, "decrement": "НЕТ (аккумуляция: g[15] += d)", "reset": "g[15]=0 (case 8)", "consumer": "атака 8: >= 1000", "confidence": "CONFIRMED"},
        {"field": "f.w", "unit": "мс", "init": 0, "decrement": "нет (аккумуляция)", "reset": "f.w=0", "consumer": "case 16: >= 800", "confidence": "CONFIRMED"},
        {"field": "g[24]", "unit": "мс", "init": 0, "decrement": "g[24] -= d", "reset": "0", "consumer": "<=0 (0x800 флаг)", "confidence": "CONFIRMED"},
        {"field": "g[22]", "unit": "мс", "init": -1, "decrement": "g[22] -= d (f.java:4050 паттерн)", "reset": "-1", "consumer": "< 0", "confidence": "INFERRED"},
        {"field": "g[27]", "unit": "мс (время)", "init": "спавн-время", "decrement": "нет", "reset": "действие", "consumer": "f.j(): f.g - g[27] <= 1500", "confidence": "CONFIRMED"},
        {"field": "c.java аккумулятор", "unit": "тики (62)", "init": 0, "decrement": "нет (j += n; j >= 62)", "reset": "j -= 62", "consumer": "смена кадра", "confidence": "CONFIRMED"},
        {"field": "g[22+i] (случайный)", "unit": "мс", "init": "1000 + rand(500)", "decrement": "да", "reset": "по срабатыванию", "consumer": "таймеры поведения", "confidence": "CONFIRMED"},
    ]}
    (OUT / "entity-timers-v2.json").write_text(json.dumps(timers, indent=1, ensure_ascii=False))

    units = {"meta": "Единицы времени",
             "GAME_LOOP_TIME": "delta d = now-c, clamp 166 мс; кадр 40 мс (g.run())",
             "ENTITY_TIME": "мс (аккумуляция g[15] += d; f.w += d)",
             "ANIMATION_TIME": "62-тиковый аккумулятор c.java (j += n; j >= 62 -> кадр). НЕ равен AI-тику",
             "SCRIPT_TIME": "опкоды 117/153 (таймер bV); bO/bQ продвижение по кадрам",
             "note": "40 мс НЕ = AI tick: AI обновляется каждый кадр геймплея (state 6)"}
    (OUT / "time-units-v2.json").write_text(json.dumps(units, indent=1, ensure_ascii=False))

    # ---------- 6/7. attack/damage timing ----------
    att = {"meta": "Тайминги атак", "attacks": [
        {"model": "ATTACK_7", "trigger": "g[12]==7, цель в prop17, анимация завершена", "timer": "g[15] (после перехода в 8)", "damage": "моментально f.b(f3, prop14)", "transition": "7->8", "confidence": "CONFIRMED"},
        {"model": "ATTACK_8", "trigger": "g[12]==8, g[15] >= 1000", "timer": "g[15] (аккумуляция += d)", "damage": "f.b(g.c, prop14) / f.o(f3, prop14)", "sound": "g.b(21)", "transition": "8->4/9", "confidence": "CONFIRMED"},
        {"model": "ATTACK_12", "trigger": "g[12]==12, анимация, цель в зоне", "damage": "f.b(f3, prop14<<1)", "transition": "12->13->4", "confidence": "CONFIRMED"},
        {"model": "RANGED", "trigger": "prop10 ∈ {0,3,5,7}", "timer": "скорость снаряда n14=819200", "damage": "по попаданию", "transition": "-", "confidence": "CONFIRMED (наведение)"},
    ]}
    (OUT / "attack-timing-v2.json").write_text(json.dumps(att, indent=1, ensure_ascii=False))

    (OUT / "damage-timing-v2.md").write_text("""# Damage Timing V2

- Нанесение: f.b(f2, n) (f.java:767): g[7] -= n + n*30%*bF/100; звук 22/23.
- Множественные удары за тик: НЕ обнаружено ограничения (f.b может вызываться несколько раз — REQUIRES_REAL_RUNTIME).
- Invulnerability: НЕ найдена (нет отдельного таймера неуязвимости; REQUIRES_REAL_RUNTIME).
- Knockback: НЕ найдена отдельная механика (velocity-движение).
- Смерть: g[12] >= 100; f.d(f3, 101) жертва; f.c(f2, 100) в f.i case 12 (f.java:5592) и др.
- Накопление: g[7] аккумулирует урон (HP-счётчик от 0 вниз).
""")

    # ---------- 8. randomness ----------
    rnd = {"meta": "Случайность рантайма", "sources": [
        {"source": "g.a()", "range": "g.a() % 100 (0..99)", "consumer": "смещение цели снаряда 20 + (%100 - 50)", "confidence": "CONFIRMED"},
        {"source": "g.a()", "range": "g.a() % n11", "consumer": "выбор кадра/варианта (f.java:3208)", "confidence": "CONFIRMED"},
        {"source": "g.a()", "range": "1000 + g.a() % 500", "consumer": "случайный таймер поведения", "confidence": "CONFIRMED"},
        {"source": "g.a()", "range": "g.a() % 2", "consumer": "чёт/нечет ветки", "confidence": "CONFIRMED"},
        {"source": "g.a()", "range": "g.a() % 100 < 25", "consumer": "вероятность 25% (f.java:4223)", "confidence": "CONFIRMED"},
        {"seed": "не найден", "note": "платформенный Random (Java ME)"},
    ]}
    (OUT / "runtime-randomness-v2.json").write_text(json.dumps(rnd, indent=1, ensure_ascii=False))

    # ---------- 9. complete transitions ----------
    tr = {"meta": "Полные переходы 24 состояний", "states": {}}
    transitions = {
        "0": ["4 (f.c(f2,4))", "7 (атака)"], "1": ["4"], "4": ["7 (атака)", "8", "12", "100+"],
        "7": ["8 (попадание)", "4 (вне зоны)", "0 (нет цели)"],
        "8": ["4", "9 (жертва m<555)"], "9": ["0/4"], "12": ["13"], "13": ["4"],
        "14": ["100"], "17": ["4"], "18": ["4"], "19": ["4"], "23": ["0/4 (инициализация)"],
        "24": ["4 (после флага 0x100)"], "26": ["100 (f.p)"], "27": ["100"], "28": ["100"],
        "100+": ["терминальные (без перехода)"], "108": ["100"],
    }
    for s, nxt in transitions.items():
        tr["states"][s] = {"next": nxt, "conditions": "см. ai-transition-graph-v2", "source": "f.java"}
    (OUT / "complete-state-transition-v2.json").write_text(json.dumps(tr, indent=1, ensure_ascii=False))

    # ---------- 10. script/AI interaction ----------
    sa = {"meta": "Может ли скрипт переопределять...", "overrides": [
        {"target": "movement", "opcodes": ["111 (телепорт)", "142 (телепорт персонажа)"], "status": "CONFIRMED"},
        {"target": "state", "opcodes": ["157 (смена состояния/диалога)", "132 (g.d.g[9]=0)"], "status": "CONFIRMED"},
        {"target": "position", "opcodes": ["111/142", "118 (размещение в тайле)"], "status": "CONFIRMED"},
        {"target": "target", "opcodes": ["148 (SetNPCTarget)"], "status": "CONFIRMED"},
        {"target": "animation", "opcodes": ["121 (стек анимаций)", "110/150/162 (команды)"], "status": "CONFIRMED"},
        {"target": "attack", "opcodes": ["110/150/162 (команды с направлением)", "128 (g.c.g[n]=n2)"], "status": "CONFIRMED"},
        {"target": "death", "opcodes": ["151/160 (спавн)", "132"], "status": "INFERRED (прямого 'убить' опкода не найдено)"},
        {"target": "visibility", "opcodes": ["нет прямого"], "status": "UNKNOWN"},
    ]}
    (OUT / "script-ai-state-interaction-v2.json").write_text(json.dumps(sa, indent=1, ensure_ascii=False))

    # ---------- 11. animation timing ----------
    at = {"meta": "Тайминг анимации (c.java)", "details": [
        {"field": "аккумулятор j", "unit": "тики (вызовы a(int))", "advance": "j += n; пока j >= 62: j -= 62, кадр++", "evidence": "c.java:44-58"},
        {"field": "кадр e", "unit": "кадры", "advance": "loop: e = (e+1) % count; once: до конца", "evidence": "c.java:60-130"},
        {"field": "повторы g", "unit": "циклы", "advance": "--g при завершении цикла", "evidence": "c.java"},
        {"field": "смена состояния", "unit": "пересчёт", "advance": "f.c(f2,n): f.a(f2,false,true) -> a2.b(n3, n6) — сброс фазы кадра", "evidence": "f.java:4020-4035"},
        {"note": "62 тика НЕ универсальны: это аккумулятор c.java; скорость вызова a(int) зависит от контекста (не доказано, что 62 = 1 кадр за 62 AI-тика)"},
    ]}
    (OUT / "animation-timing-v2.json").write_text(json.dumps(at, indent=1, ensure_ascii=False))

    # ---------- 12/13. movement/collision ----------
    (OUT / "movement-update-v2.md").write_text("""# Movement Update V2

- Позиция: c.a/c.b (fixed 14); velocity: g[13]/g[14].
- Шаг: 819200 (50 px) за тик; скорости-константы 983040 (60), 1048576 (65), 1474560 (90), 1802240 (110) px/s.
- Наведение на цель: n15 = |dx|*1000/819200; n17 = dx/(n15+1) — velocity к цели (f.java:2830).
- Коллизии: 5-точечный зонд (±5/±4) + g.d(x/16, y/16); при блокировке f.p() меняет направление.
- Диагональ: нормализация НЕ найдена (11585 отсутствует) — оси независимы.
""")
    (OUT / "collision-response-v2.json").write_text(json.dumps({
        "meta": "Коллизионные ответы", "types": {
            "WORLD": "g.d(x/16, y/16) + 5-точечный зонд; блокировка движения",
            "ENTITY": "AABB g.a(...197); враги-враги f.b() фильтр L==3",
            "PROJECTILE": "hitscan-луч g.a(n4,n5,...) (стрельба)",
            "SCRIPTED": "опкоды 112/167/172 (активация объектов)"
        }, "confidence": "CONFIRMED"
    }, indent=1, ensure_ascii=False))

    # ---------- 14. camera ----------
    cam = {"meta": "Камера", "detail": "T = player_x - 0x1E0000; U = player_y - 0x280000; клампы [0, map-240/320]; "
                                        "экран = world - (T>>14, U>>14)", "confidence": "CONFIRMED"}
    (OUT / "camera-interaction-v2.json").write_text(json.dumps(cam, indent=1, ensure_ascii=False))

    # ---------- 15/16. timeline + trace schema ----------
    (OUT / "runtime-timeline-v2.md").write_text("""# Runtime Timeline V2

```
T0 SPAWN     запись миссии -> props -> архетип -> g[12]=0/23, анимация, позиция
T1 UPDATE    g.B() каждый кадр (state 6): eF, Q, bM, bE, f.b() (агро)
T2 AI        f.i()/f.j()/f.o()/f.p() по g[12] (+ подсостояние g[10])
T3 MOVEMENT  velocity g[13]/g[14] -> шаг 819200 -> позиция c.a/c.b
T4 COLLISION 5-точечный зонд + AABB; f.p() смена направления
T5 ATTACK    g[12] 7/8/12: таймеры g[15]/f.w, урон f.b(f3, prop14)
T6 DAMAGE    g[7] -= урон + 30%*bF; смерть g[12]>=100
T7 ANIMATION c.java: аккумулятор 62 -> кадр e -> f.a() по состоянию
T8 RENDER    a.java: декодер -> Image -> drawRegion (трансформ a[n4&7])
```

Зависимости: T2 зависит от T1; T5 зависит от T2/T3; T7 зависит от g[12]; T8 от T7 и камеры.
""")
    schema = {"meta": "Формат трассировки экземпляра (для будущего рантайма)",
              "schema": {"timestamp": "int (мс)", "instance_id": "str", "state": "int (g[12])",
                         "substate": "int (g[10])", "x": "int (fixed)", "y": "int (fixed)",
                         "velocity_x": "int (fixed)", "velocity_y": "int (fixed)",
                         "target": "instance_id|null", "hp": "int (g[7])", "flags": "int (g[16])",
                         "timer_g15": "int", "timer_fw": "int", "animation": "int (c.d)",
                         "frame": "int (c.e)", "archetype": "int (g[0])", "cluster": "str"}}
    (OUT / "entity-trace-schema.json").write_text(json.dumps(schema, indent=1, ensure_ascii=False))

    print("state-vector, initial-state, update-order, timers, time-units, attack-timing, damage-timing,")
    print("randomness, complete-transitions, script-ai, animation-timing, movement, collision, camera,")
    print("timeline, trace-schema — записаны")


if __name__ == "__main__":
    sys.exit(main())
