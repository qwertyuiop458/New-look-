#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_completion_model_v2.py — трассировка mission script → global → completion (этап 15.20).

ГЛАВНОЕ ОТКРЫТИЕ:
  g.a(f2, n, byArray, n2) (g.java:23300): сущность L==10 = ОБЪЕКТ-МИССИЯ
    i = f2; cB = 200 (HP миссии); cz = n; Q[] = 4 пары наград (id, значение) из данных
  g.cZ() (23598): каждый кадр геймплея:
    cw==0: cB <= 0 -> g.e() -> state 7 (MISSION_COMPLETE)
           g.i.a.a() > cy (время) -> ap(1) -> награды
           иначе cY() (продолжение)
    cw==1/2/3: награды из Q[] (db = M(da) индекс), ap(2..4)
    cw==4: n(0) -> MENU
  cB уменьшается: cB -= f.a(8|16, n9) (урон миссии-объекта)
  state 7 (cd()): анимация завершения (b 0..4), затем SHOP(13) или LOADING(2)
  g.e() (18893): g.d(7,0) — переход в state 7
  bB: пишется только в меню (0), пункт 45 (3), из сейва — ИНКРЕМЕНТА НЕТ:
    следующая миссия выбирается меню/сейвом (REQUIRES_REAL_RUNTIME)
  Сохранение прогресса: g.ad(bC==1?0:2) (14504) + a(2,E) (19938)
"""
import json
import sys
from pathlib import Path

OUT = Path("research/analysis/v2/global")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    # 1. global write index
    gwi = {"meta": "Индекс записей в глобальные поля", "writes": [
        {"field": "bB", "writers": ["меню 'новая игра': bB=0 (3650)", "меню пункт 45: bB=3 (3777)", "ci(): bB=D[1]", "ad(): bB=E[1]"],
         "opcode": "-", "condition": "меню/сейв", "effect": "выбор миссии", "confidence": "CONFIRMED"},
        {"field": "bC", "writers": ["g.o(int) (1086: bC=n)", "g.java:3650 регион"], "effect": "режим 0-3", "confidence": "CONFIRMED"},
        {"field": "bF", "writers": ["ci(): bF=D[3]", "меню"], "effect": "сложность (урон 30%*bF)", "confidence": "CONFIRMED"},
        {"field": "P[]", "writers": ["ad(): P[7]=время, P[4]=0, P[14]=0"], "effect": "статистика", "confidence": "CONFIRMED"},
        {"field": "Q (флаг)", "writers": ["опкод 158: g.Q=(o+4==1)"], "effect": "пауза скрипта", "confidence": "CONFIRMED"},
        {"field": "bM", "writers": ["опкод 169: g.bM=z[o+0]"], "effect": "цикл J()", "confidence": "CONFIRMED"},
        {"field": "bD", "writers": ["опкод 131: g.bD=z[o+0]", "header миссии"], "effect": "глобальная переменная", "confidence": "CONFIRMED"},
        {"field": "bi", "writers": ["опкод 139: g.bi=z[o+0]"], "effect": "глобальная переменная", "confidence": "CONFIRMED"},
        {"field": "dE/O", "writers": ["опкод 161: dE=g.d.g[12], O=true"], "effect": "захват диалога", "confidence": "CONFIRMED"},
        {"field": "g.a (state)", "writers": ["g.d(n,m)", "g.m(n)", "g.n(n)", "опкод 165 (T: n==3 -> g.a(6,-1))"],
         "effect": "переходы состояний", "confidence": "CONFIRMED"},
        {"field": "L[]", "writers": ["g.ah() (L[4] деньги)", "g.af() (L[1] оружие)", "d(n,bl) (L[1]=-1)"], "effect": "инвентарь/деньги", "confidence": "CONFIRMED"},
        {"field": "cB (миссия-HP)", "writers": ["g.a(f2,...): cB=200", "cZ(): cB -= f.a(8|16, n9)"], "effect": "завершение миссии", "confidence": "CONFIRMED"},
        {"field": "Q[] (награды)", "writers": ["g.a(f2,...): Q[i*2]=id, Q[i*2+1]=значение (4 пары)"], "effect": "награды при завершении", "confidence": "CONFIRMED"},
    ]}
    (OUT / "global-write-index-v2.json").write_text(json.dumps(gwi, indent=1, ensure_ascii=False))

    # 2. opcode-global-effect
    oge = {"meta": "Эффекты опкодов на глобальное состояние", "map": [
        {"opcode": 157, "handler": "g.a(0, o+0, o+2, o+4==1, o+6==1); g.u=false; g.v=o+8==1", "global": "g.u, g.v, состояние", "effect": "смена состояния/диалога", "status": "CONFIRMED"},
        {"opcode": 158, "handler": "g.Q=(o+4==1); g.j(o+0, o+2)", "global": "g.Q", "effect": "пауза скрипта", "status": "CONFIRMED"},
        {"opcode": 159, "handler": "g.x() (конец); P=false", "global": "P", "effect": "ТЕРМИНАТОР скрипта", "status": "CONFIRMED"},
        {"opcode": 161, "handler": "g.dE = (d.L==11 ? d.g[12] : -3); O=true", "global": "dE, O", "effect": "захват диалога", "status": "CONFIRMED"},
        {"opcode": 165, "handler": "g.T(n): aX=n; e(0,38,0,38); n==3 -> g.a(6,-1)", "global": "state", "effect": "переход в геймплей (6)", "status": "CONFIRMED"},
        {"opcode": 169, "handler": "g.bM = z[o+0]", "global": "bM", "effect": "управление циклом J()", "status": "CONFIRMED"},
        {"opcode": 131, "handler": "g.bD = z[o+0]", "global": "bD", "effect": "глобальная переменная", "status": "CONFIRMED"},
        {"opcode": 126, "handler": "g.ah(n): L[4] += 45000*n/100 (cap)", "global": "L[4]", "effect": "ДЕНЬГИ/ОЧКИ", "status": "CONFIRMED"},
    ]}
    (OUT / "opcode-global-effect-v2.json").write_text(json.dumps(oge, indent=1, ensure_ascii=False))

    # 3. completion search
    cs = {"meta": "Поиск условий завершения", "findings": [
        {"condition": "cB <= 0 (cw==0)", "result": "g.e() -> state 7", "caller": "cZ() из B() (1162)", "effect": "MISSION_COMPLETE", "status": "CONFIRMED"},
        {"condition": "g.i.a.a() > cy (время)", "result": "ap(1) -> награды Q[]", "caller": "cZ()", "effect": "завершение по времени", "status": "CONFIRMED"},
        {"condition": "g.c.g[7] <= 0", "result": "g.c.g[7] = 200 (воскрешение)", "caller": "14998", "effect": "не game over при 0 HP?", "status": "CONFIRMED (восстановление)"},
        {"condition": "state 10 (d(10,...))", "result": "game over", "caller": "25409 и др.", "effect": "GAME_OVER", "status": "CONFIRMED (существует), trigger REQUIRES_REAL_RUNTIME"},
        {"condition": "state 7", "result": "cd(): анимация b 0..4, затем 13/2", "effect": "не completion сам по себе, а экран", "status": "CONFIRMED"},
    ]}
    (OUT / "mission-completion-search-v2.json").write_text(json.dumps(cs, indent=1, ensure_ascii=False))

    # 4. objective engine
    oe = {"meta": "Objective-движок (доказан): объект-миссия L==10 + счётчик cB + награды Q[]",
          "engine": [
              {"component": "объект-миссия", "detail": "сущность L==10: g.a(f2, n, byArray, n2) (23300): i=f2, cB=200, cz=n, Q[]=4 пары", "status": "CONFIRMED"},
              {"component": "HP миссии", "detail": "cB: уменьшается cB -= f.a(8|16, n9) (23434) — урон по объекту-миссии", "status": "CONFIRMED"},
              {"component": "время", "detail": "cy = (ab?3:16) * d.length * 16 — лимит времени", "status": "CONFIRMED"},
              {"component": "награды", "detail": "Q[]: 4 пары (id, значение) из данных миссии; db = M(da) индекс", "status": "CONFIRMED"},
              {"component": "условия скриптов", "detail": "K()/опкоды 124/125 (сравнения свойств) — дополнительные ветвления", "status": "CONFIRMED (механизм), конкретные условия REQUIRES_REAL_RUNTIME"},
          ]}
    (OUT / "objective-condition-engine-v2.json").write_text(json.dumps(oe, indent=1, ensure_ascii=False))

    # 5. script memory model
    smm = {"meta": "Модель памяти", "categories": {
        "SCRIPT_MEMORY": ["g.z (байтовый массив скриптов)", "bO/bQ/bP (указатели)", "g.H[]/g.A[] (таблицы скриптов-тайлов)"],
        "GLOBAL_GAME_STATE": ["g.a/b/u", "bB/bC/bF", "L[]", "M[]", "P[]", "B[]", "Q (флаг)", "bM/bD/bi/dE/O"],
        "ENTITY_STATE": ["f.g[] (27 полей)", "c-объект (анимация)"],
        "MISSION_DATA": ["cB (HP миссии)", "Q[] (награды)", "cy (время)", "i (объект-миссия)"],
    }}
    (OUT / "script-memory-model-v2.json").write_text(json.dumps(smm, indent=1, ensure_ascii=False))

    # 6. if/else flow
    cflow = {"meta": "Control flow скриптов", "control": [
        {"opcode": 145, "role": "if_open", "behavior": "пропуск до 146 при ложном K()", "status": "CONFIRMED"},
        {"opcode": 146, "role": "if_close", "behavior": "конец блока", "status": "CONFIRMED"},
        {"opcode": 143, "role": "else", "behavior": "граница then/else", "status": "CONFIRMED"},
        {"opcode": 144, "role": "endif", "behavior": "конец if", "status": "CONFIRMED"},
        {"opcode": 159, "role": "terminator", "behavior": "конец скрипта", "status": "CONFIRMED"},
        {"opcode": 123, "role": "subroutine", "behavior": "переключение bO/bQ на субскрипт", "status": "CONFIRMED"},
        {"opcode": 117, "role": "wait", "behavior": "блокирующее ожидание", "status": "CONFIRMED"},
    ]}
    (OUT / "mission-script-control-flow-v2.json").write_text(json.dumps(cflow, indent=1, ensure_ascii=False))

    # 7. termination opcodes
    to = {"meta": "Опкоды завершения", "analysis": [
        {"opcode": 159, "role": "script_end", "effect": "конец исполнения; возврат", "completion": "НЕТ (не завершение миссии)", "status": "CONFIRMED"},
        {"opcode": 165, "role": "state_transition", "effect": "T(n): n==3 -> state 6 (геймплей)", "completion": "нет", "status": "CONFIRMED"},
        {"opcode": 169, "role": "loop_control", "effect": "bM; управляет J()", "completion": "нет", "status": "CONFIRMED"},
        {"opcode": 157, "role": "state_change", "effect": "смена состояния/диалога", "completion": "нет прямого", "status": "CONFIRMED"},
        {"opcode": 161, "role": "dialog_capture", "effect": "dE/O", "completion": "нет", "status": "CONFIRMED"},
        {"note": "Завершение миссии НЕ через опкоды: cB (HP объекта-миссии L==10) -> 0 -> g.e() -> state 7", "status": "CONFIRMED"},
    ]}
    (OUT / "termination-opcode-analysis-v2.json").write_text(json.dumps(to, indent=1, ensure_ascii=False))

    # 8. mission index transition
    mit = {"meta": "Переход индекса миссии",
           "bB_writers": ["меню: bB=0 (новая игра)", "меню пункт 45: bB=3", "ci(): bB=D[1] (сейв)", "ad(): bB=E[1] (сейв)"],
           "increment": "НЕ НАЙДЕН (нет bB++/bB+=1)",
           "chain": "завершение (cB=0) -> state 7 -> cd() (b 0..4) -> state 13 (shop) или 2 (loading); "
                    "выбор следующей миссии: REQUIRES_REAL_RUNTIME (вероятно через меню/сейв после shop)",
           "status": "PARTIAL (CONFIRMED: нет инкремента; REQUIRES_REAL_RUNTIME: механизм выбора следующей)"}
    (OUT / "mission-index-transition-v2.json").write_text(json.dumps(mit, indent=1, ensure_ascii=False))

    # 9. results pipeline
    rp = {"meta": "Результаты (state 7, cd())", "pipeline": [
        {"step": "cB<=0", "detail": "cZ() cw==0 -> g.e()", "status": "CONFIRMED"},
        {"step": "state 7", "detail": "cd(): подсостояния b 0..4 (L() 2000ms, анимация, статистика)", "status": "CONFIRMED"},
        {"step": "награды", "detail": "Q[] 4 пары: Q[i*2]=id, Q[i*2+1]=значение; k(n,10) выдача; ap(3/4)", "status": "CONFIRMED"},
        {"step": "время", "detail": "P[7] = время (ad()); f.z", "status": "CONFIRMED"},
        {"step": "деньги", "detail": "L[4] (g.ah)", "status": "CONFIRMED"},
        {"step": "сохранение", "detail": "g.ad(bC==1?0:2) при bC 1/3 (14504)", "status": "CONFIRMED"},
        {"step": "далее", "detail": "state 13 (shop) или 2 (loading)", "status": "CONFIRMED (переходы); выбор REQUIRES_REAL_RUNTIME"},
    ]}
    (OUT / "mission-results-pipeline-v2.json").write_text(json.dumps(rp, indent=1, ensure_ascii=False))

    # 10. save trigger
    st = {"meta": "Триггеры сохранения", "types": {
        "AUTO_SAVE": "g.ad(bC==1?0:2) при завершении миссии (14504); a(2,E) (19938)",
        "MANUAL_SAVE": "g.a(true,true) (профиль запись 1); меню",
        "PROFILE_SAVE": "a(bl,bl2) -> g.a(1,D) (19267)",
        "PROGRESSION_SAVE": "ad() -> запись 2"},
        "status": "CONFIRMED (вызовы); точный UI REQUIRES_REAL_RUNTIME"}
    (OUT / "save-triggers-v2.json").write_text(json.dumps(st, indent=1, ensure_ascii=False))

    # 11. shop transition
    sht = {"meta": "Переход магазина", "detail": "state 7 -> 13 (shop) -> 2 (loading) — переходы подтверждены state machine; "
                                                 "точный flow покупки/выхода REQUIRES_REAL_RUNTIME",
           "shop_data": "g.fE(); g.l(n,prop)=an[..]+g.y(n,prop); L[4] валюта"}
    (OUT / "shop-transition-v2.json").write_text(json.dumps(sht, indent=1, ensure_ascii=False))

    # 12. failure pipeline
    (OUT / "mission-failure-pipeline-v2.md").write_text("""# Mission Failure Pipeline V2

- GAME_OVER (state 10): существует (g.dH(), d(10,...) 25409).
- Триггер: HP игрока (g[7]) — НО найдено ВОСКРЕШЕНИЕ: после скрипта
  `if (g.c.g[7] <= 0) g.c.g[7] = 200` (g.java:14998) — при 0 HP игрок
  восстанавливается до 200 (вероятно, сюжетный/скриптовый механизм).
- Retry: state 10 -> LOADING (2) или MENU (1) — g.dH().
- Restore: из RMS (запись 1 профиль + запись 2 прогресс).
- Чекпоинты: НЕ найдены.
- Точные условия перехода в state 10: REQUIRES_REAL_RUNTIME.
""")

    # 13. difficulty
    df = {"meta": "bF (сложность): все read sites", "reads": ["f.b(): урон += 30%*bF (f.java:767)", "ci(): bF=D[3]"],
          "effect": "модификатор урона", "status": "CONFIRMED (влияет на урон); полный эффект REQUIRES_REAL_RUNTIME"}
    (OUT / "difficulty-effect-v2.json").write_text(json.dumps(df, indent=1, ensure_ascii=False))

    # 14. mission timeline
    tl = {"meta": "Таймлайн 5 миссий (доказанные переходы)", "missions": []}
    for i in range(5):
        tl["missions"].append({"mission": i, "stream": f"m9 seg{10+i}",
                               "timeline": {
                                   "START": "загрузка g.Z(bB) (CONFIRMED)",
                                   "INITIALIZE": "header + объект-миссия L==10 (CONFIRMED)",
                                   "SCRIPT": "спец-опкоды 110-172 (CONFIRMED структура)",
                                   "GAMEPLAY": "state 6 g.B() (CONFIRMED)",
                                   "CONDITIONS": "K()/124/125 (CONFIRMED механизм)",
                                   "COMPLETION": "cB<=0 -> g.e() -> state 7 (CONFIRMED)",
                                   "RESULTS": "cd() + Q[] награды (CONFIRMED)",
                                   "SAVE": "ad() запись 2 (CONFIRMED)",
                                   "NEXT": "REQUIRES_REAL_RUNTIME"}})
    (OUT / "mission-timeline-v2.json").write_text(json.dumps(tl, indent=1, ensure_ascii=False))

    # 15. confidence matrix
    cm = {"meta": "Матрица уверенности", "matrix": [
        {"stage": "mission index (bB)", "STRUCTURE": "CONFIRMED", "SEMANTIC": "CONFIRMED", "RUNTIME": "инкремент"},
        {"stage": "mission object L==10", "STRUCTURE": "CONFIRMED", "SEMANTIC": "CONFIRMED", "RUNTIME": "-"},
        {"stage": "completion condition (cB<=0)", "STRUCTURE": "CONFIRMED", "SEMANTIC": "CONFIRMED", "RUNTIME": "что уменьшает cB (источники урона)"},
        {"stage": "save call", "STRUCTURE": "CONFIRMED", "SEMANTIC": "CONFIRMED", "RUNTIME": "-"},
        {"stage": "next mission", "STRUCTURE": "CONFIRMED (нет инкремента)", "SEMANTIC": "UNKNOWN", "RUNTIME": "REQUIRED"},
        {"stage": "failure", "STRUCTURE": "CONFIRMED (state 10)", "SEMANTIC": "UNKNOWN", "RUNTIME": "REQUIRED"},
    ]}
    (OUT / "static-confidence-matrix-v2.json").write_text(json.dumps(cm, indent=1, ensure_ascii=False))

    print("global-write-index, opcode-global-effect, mission-completion-search, objective-engine,")
    print("script-memory, control-flow, termination-opcodes, mission-index-transition, results,")
    print("save-triggers, shop-transition, failure, difficulty, timeline, confidence-matrix — записаны")


if __name__ == "__main__":
    sys.exit(main())
