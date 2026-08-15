#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_global_state_v2.py — глобальное состояние / прогрессия / сейвы (этап 15.19).

Источники: g.java (ci()/a(bl,bl2) — профиль; ad(int)/запись 2 — прогресс; B(int) — слоты;
c(n)/a(n,byte[]) — RMS), b.java (IGP igp19), state machine 18 состояний.
"""
import json
import sys
from pathlib import Path

OUT = Path("research/analysis/v2/global")
SV = Path("research/analysis/v2/save")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    SV.mkdir(parents=True, exist_ok=True)

    # ---------- 1. global state vector ----------
    gsv = {"meta": "Глобальные поля g, переживающие update (первичные писатели/читатели)",
           "fields": [
               {"field": "g.a", "type": "int", "meaning": "ГЛОБАЛЬНОЕ СОСТОЯНИЕ (0..99)", "writers": "переходы состояний", "readers": "switch(a)", "lifetime": "вся игра", "confidence": "CONFIRMED"},
               {"field": "g.b", "type": "int", "meaning": "подсостояние (загрузка 0/1, геймплей 0/4)", "writers": "g.d(n,m)", "readers": "switch(b)", "confidence": "CONFIRMED"},
               {"field": "g.u", "type": "int", "meaning": "подменю (состояние 8)", "writers": "меню", "readers": "switch(u)", "confidence": "CONFIRMED"},
               {"field": "bB", "type": "int", "meaning": "ТЕКУЩАЯ МИССИЯ (индекс; пишется в D[1], E[1])", "writers": "ci(), ad(), меню", "readers": "g.Z(bB), сохранение", "lifetime": "профиль", "confidence": "CONFIRMED"},
               {"field": "bC", "type": "int", "meaning": "режим (0/1/2/3 — новые данные/продолжение)", "writers": "o(int)", "readers": "ad(), конец миссии", "confidence": "CONFIRMED"},
               {"field": "ce", "type": "int", "meaning": "профиль-флаг (D[0])", "writers": "ci()", "readers": "M()", "confidence": "CONFIRMED"},
               {"field": "i", "type": "boolean", "meaning": "флаг (D[2]==1)", "writers": "ci()", "readers": "-", "confidence": "CONFIRMED"},
               {"field": "bF", "type": "int", "meaning": "сложность/параметр (D[3]; используется в уроне 30%*bF)", "writers": "ci()", "readers": "f.b() урон", "confidence": "CONFIRMED"},
               {"field": "e (byte)", "type": "byte", "meaning": "настройки (D[4]; бит 4 = звук)", "writers": "ci()/a(bl,bl2)", "readers": "e.a()/e.b()", "confidence": "CONFIRMED"},
               {"field": "g.b (массив)", "type": "int[][]", "meaning": "состояние оружия (b[n][16] и др. — D-запись)", "writers": "сохранение/магазин", "readers": "оружие", "confidence": "CONFIRMED"},
               {"field": "g.u[]", "type": "int[]", "meaning": "массив u (сохраняется в D)", "writers": "ci()", "readers": "-", "confidence": "CONFIRMED"},
               {"field": "g.P", "type": "int[]", "meaning": "статистика/прогресс (P[7]=время, P[4], P[14])", "writers": "ad()", "readers": "результаты", "confidence": "CONFIRMED"},
               {"field": "f.z", "type": "int", "meaning": "глобальное время (сохраняется)", "writers": "ad()", "readers": "таймеры", "confidence": "CONFIRMED"},
               {"field": "g.t[]", "type": "byte[20]", "meaning": "массив t (-1 дефолт)", "writers": "Z()", "readers": "-", "confidence": "INFERRED"},
               {"field": "g.c[]", "type": "f[]", "meaning": "активные персонажи (c[0..n])", "writers": "спавн/смена", "readers": "геймплей", "confidence": "CONFIRMED"},
               {"field": "g.L[]", "type": "int[]", "meaning": "инвентарь: L[1]=оружие, L[3], L[4]=деньги/очки (45000 cap)", "writers": "g.ah(), af()", "readers": "магазин/стрельба", "confidence": "CONFIRMED"},
               {"field": "g.M[]", "type": "int[]", "meaning": "патроны по типам (M[0] сброс)", "writers": "d(n,bl)", "readers": "стрельба", "confidence": "CONFIRMED"},
               {"field": "g.by/g.bz", "type": "int", "meaning": "текущий слой/тайл (by,bz)", "writers": "движение", "readers": "коллизии", "confidence": "CONFIRMED"},
               {"field": "g.bP/bO/bQ", "type": "int", "meaning": "скрипт-указатель: bP=скрипт, bO=позиция, bQ=счётчик", "writers": "g.b(int)", "readers": "g.H()/K()", "confidence": "CONFIRMED"},
               {"field": "g.P (диалог)", "type": "boolean", "meaning": "режим паузы диалога (J())", "writers": "J()", "readers": "H()/K()", "confidence": "CONFIRMED"},
               {"field": "g.bM", "type": "int", "meaning": "глобальный флаг (опкод 169)", "writers": "опкод 169", "readers": "J()", "confidence": "CONFIRMED"},
               {"field": "g.bD", "type": "int", "meaning": "глобальная переменная (опкод 131; header миссии)", "writers": "опкод 131", "readers": "header", "confidence": "CONFIRMED"},
               {"field": "g.bi", "type": "int", "meaning": "глобальная переменная (опкод 139)", "writers": "опкод 139", "readers": "-", "confidence": "CONFIRMED"},
               {"field": "g.Q", "type": "boolean", "meaning": "флаг паузы скрипта (опкод 158)", "writers": "опкод 158", "readers": "I()", "confidence": "CONFIRMED"},
               {"field": "g.dE/g.O", "type": "int/boolean", "meaning": "захват состояния диалога (опкод 161)", "writers": "опкод 161", "readers": "K()", "confidence": "CONFIRMED"},
           ]}
    (OUT / "global-state-vector-v2.json").write_text(json.dumps(gsv, indent=1, ensure_ascii=False))

    # ---------- 2. global state machine ----------
    gsm = {"meta": "Глобальная state machine (18 ID, switch(a) g.java:714-793)", "states": [
        {"id": 0, "handler": "g.v()", "label": "SPLASH", "exit": "1", "confidence": "CONFIRMED"},
        {"id": 1, "handler": "g.x()", "label": "MENU", "entry": "0,4,10,16", "exit": "5/8/12/16/17/18/19", "confidence": "CONFIRMED"},
        {"id": 2, "handler": "g.F()", "label": "LOADING", "sub": "b 0/1", "entry": "1,7,10", "exit": "3/6/11", "confidence": "CONFIRMED"},
        {"id": 3, "handler": "g.V()", "label": "CINEMATIC", "entry": "2", "exit": "6", "confidence": "CONFIRMED"},
        {"id": 4, "handler": "g.z()", "label": "PAUSE", "entry": "6", "exit": "6/1", "confidence": "CONFIRMED"},
        {"id": 5, "handler": "g.bK()", "label": "OPTIONS", "entry": "1/4", "exit": "1/4", "confidence": "CONFIRMED"},
        {"id": 6, "handler": "g.B()", "label": "GAMEPLAY", "entry": "2/3/11", "exit": "4/7/10/11", "confidence": "CONFIRMED"},
        {"id": 7, "handler": "g.cd()", "label": "MISSION_COMPLETE", "entry": "6", "exit": "13/2", "confidence": "CONFIRMED"},
        {"id": 8, "handler": "switch(u)", "label": "SUB_MENUS", "entry": "5", "exit": "5", "confidence": "CONFIRMED"},
        {"id": 10, "handler": "g.dH()", "label": "GAME_OVER", "entry": "6", "exit": "2/1", "confidence": "CONFIRMED"},
        {"id": 11, "handler": "g.dA()", "label": "DIALOGUE", "entry": "2/6", "exit": "6", "confidence": "CONFIRMED"},
        {"id": 12, "handler": "g.eh()", "label": "HELP", "entry": "1", "exit": "1", "confidence": "CONFIRMED"},
        {"id": 13, "handler": "g.fE()", "label": "SHOP", "entry": "7", "exit": "2", "confidence": "CONFIRMED"},
        {"id": 16, "handler": "g.C()", "label": "PROFILES", "entry": "1", "exit": "2/1", "confidence": "CONFIRMED"},
        {"id": 17, "handler": "g.aO()", "label": "CHARACTER_SELECT", "entry": "1", "exit": "2", "confidence": "CONFIRMED"},
        {"id": 18, "handler": "g.E()", "label": "CREDITS", "entry": "1", "exit": "1", "confidence": "CONFIRMED"},
        {"id": 19, "handler": "g.G()", "label": "QUIT_CONFIRM", "entry": "1", "exit": "1/99", "confidence": "CONFIRMED"},
        {"id": 99, "handler": "exit", "label": "EXIT", "entry": "19", "confidence": "CONFIRMED"},
    ]}
    (OUT / "global-state-machine-v2.json").write_text(json.dumps(gsm, indent=1, ensure_ascii=False))

    # ---------- 3/4. mission start/end ----------
    (OUT / "mission-start-pipeline-v2.md").write_text("""# Mission Start Pipeline V2

```
MENU(1) -> PROFILES(16): g.C() — выбор слота (RMS 'a', запись 1 = профиль)
  -> ci(): D = g.c(1); читает ce, bB (миссия), i, bF, e, b (оружие), u[]
  -> CHARACTER_SELECT(17): g.aO() — выбор персонажа
  -> LOADING(2): g.F() -> g.g() (сценарий загрузки: t0/m0..m5 листы)
  -> g.Z(bB): загрузка миссии (m9 seg10+bB) + m8
  -> CINEMATIC(3): g.V() — вступление
  -> GAMEPLAY(6): g.B()
```

Условия/переменные: bB = индекс миссии (0..4); bC = режим (0=новая, 1=продолжение, 2/3);
D[1] = сохранённая миссия.
""")
    (OUT / "mission-completion-pipeline-v2.md").write_text("""# Mission Completion Pipeline V2

- Завершение: достижение финального скрипт-события миссии (спец-опкоды; точный триггер REQUIRES_REAL_RUNTIME).
- Обработка конца миссии: g.Z()-регион (g.java:14504):
    if (bC == 1 || bC == 3): g.ad(bC==1 ? 0 : 2)  // СОХРАНЕНИЕ ПРОГРЕССА (запись 2)
                              g.a(0); g.c(c, 0)
- g.ad(int n): читает E = g.c(2) (запись 2 = прогресс), n = режим сохранения:
    n==0: полная запись (персонажи, позиции, HP, оружие, патроны, флаги B[])
    n==1: частичная (без позиций)
    n==2: без данных персонажей
- Сохранение записи 2: g.a(2, E) (g.java:19938) — сериализация состояния.
- GAME OVER(10): HP<=0; g.dH() -> рестарт с чекпоинта (2) или меню (1).
- MISSION_COMPLETE(7): g.cd() -> статистика; затем SHOP(13) или LOADING(2) (следующая миссия).
- Следующая миссия: bB инкремент/назначение (точный механизм REQUIRES_REAL_RUNTIME).
""")

    # ---------- 5. objectives ----------
    obj = {"meta": "Objective-система. Прямых objective-полей НЕ найдено в статическом коде: цели задаются "
                   "скриптами миссий (спец-опкоды 110-172) и проверяются K() (условия).",
           "evidence": ["g.H()/g.K() — исполнение условий", "опкоды 124/125 — сравнения свойств",
                        "t0 — тексты целей (HUD)", "completion — REQUIRES_REAL_RUNTIME"],
           "objective_state": "UNKNOWN (нет выделенного поля/массива objectives)",
           "completion": "REQUIRES_REAL_RUNTIME"}
    (OUT / "objective-system-v2.json").write_text(json.dumps(obj, indent=1, ensure_ascii=False))

    # ---------- 6/7. progression / shop ----------
    prog = {"meta": "Прогрессия между миссиями (запись 2 RMS)",
            "persisted": ["персонажи c[] (позиции g[26]/g[27], оружие g[28]/g[29], HP g[7], поле g[11])",
                          "патроны (массивы)", "P[] (статистика/время)", "f.z (время)", "b[][] (оружие-флаги)",
                          "B[] (глобальные флаги)", "q[]/p[]"],
            "money": "g.L[4] (g.ah(): += 45000*n/100, cap 45000) — очки/деньги",
            "weapons": "g.L[1] текущее; g.b[n][16] слоты; upgrades g.y(n,prop) аддитивно",
            "unlocks": "bB (миссия) + флаги B[]",
            "status": "CONFIRMED (структура записи); точные эффекты REQUIRES_REAL_RUNTIME"}
    (OUT / "progression-system-v2.json").write_text(json.dumps(prog, indent=1, ensure_ascii=False))

    shop = {"meta": "Магазин (состояние 13, g.fE()).", "evidence": [
        "g.java:21333 'NEXT WEAPON' — переключение оружия",
        "g.l(n,prop) = an[n*28+prop] + g.y(n,prop) — апгрейды аддитивно (g.java:31911)",
        "g.y(n,prop) — таблица апгрейдов (урон/магазин/перезарядка)",
        "L[4] = валюта (g.ah())"],
        "items": "weapon records m9 seg5 = БАЗОВЫЕ значения; магазин = g.y() поверх",
        "prices": "UNKNOWN (нет статической таблицы цен)",
        "persistence": "через запись 2 (b[][] + g.y-значения)"}
    (OUT / "shop-system-v2.json").write_text(json.dumps(shop, indent=1, ensure_ascii=False))

    # ---------- 8/9. RMS format + slots ----------
    (SV / "rms-format-v2.md").write_text("""# RMS Format V2

## RecordStore "a" (главное сохранение, g.java:4129-4230)

| Запись | Содержимое | Чтение | Запись |
| :-: | :--- | :--- | :--- |
| 1 | ПРОФИЛЬ: [ce u8][bB u8][i u8][bF u8][e u8][b-массив][u[]][хвост g.k] | ci() (19217) | a(bl,bl2) (19267) |
| 2 | ПРОГРЕСС: [n9 u8][bB][t][...][персонажи: g[26..29],g[11],позиция,g[7]][патроны][b[][]][B[]][...] | ad() (19300) | ad()-обратный (19938) |

- Инициализация: B(n) (4130): если записей 0 — addRecord n раз (по 1 байту).
- Доступ: c(n) = getRecord; a(n, byte[]) = setRecord.
- Формат: байтовые поля + u16 LE (g.a(E, off)), секции массивов.

## RecordStore "igp19" (b.java:2270-2299) — IGP-данные (не сейв).

## Save slots
- B(int n) вызывается с n=2 (19219: при отсутствии D) — минимум 2 записи.
- g.C() (профили, состояние 16) работает со слотами; ТОЧНОЕ число слотов: статически
  не подтверждено (старое "3 slots" НЕ переносится без доказательства).
- Auto/checkpoint: g.ad() при завершении миссии (bC 1/3) — авто-сохранение; чекпоинты НЕ найдены.
""")
    rms = {"meta": "RMS record schema", "records": [
        {"id": 1, "name": "PROFILE", "fields": ["ce", "bB (миссия)", "i (флаг)", "bF (сложность)", "e (настройки)", "b[][] (оружие)", "u[]"], "size": "10 + x() + D()", "version": "нет версии", "checksum": "нет", "purpose": "профиль+миссия", "confidence": "CONFIRMED"},
        {"id": 2, "name": "PROGRESS", "fields": ["n9", "bB", "t", "персонажи (позиции/HP/оружие)", "патроны", "b[][]", "P[]", "B[]", "q[]/p[]"], "size": "переменный", "version": "нет", "checksum": "нет", "purpose": "состояние кампании", "confidence": "CONFIRMED"},
        {"id": "igp19", "name": "IGP", "fields": ["не сейв"], "purpose": "онлайн-данные", "confidence": "CONFIRMED"},
    ]}
    (SV / "rms-record-schema-v2.json").write_text(json.dumps(rms, indent=1, ensure_ascii=False))

    # ---------- 12. versioning ----------
    ver = {"meta": "Версионирование сейвов",
           "version_byte": "НЕ НАЙДЕН", "migration": "NOT_IMPLEMENTED (нет кода миграции)",
           "corruption": "частично: c(n) возвращает null при ошибке; B(n) инициализирует пустой стор",
           "validation": "нет чексумм", "status": "UNKNOWN/NOT_IMPLEMENTED"}
    (SV / "save-versioning-v2.json").write_text(json.dumps(ver, indent=1, ensure_ascii=False))

    # ---------- 13. profile ----------
    prof = {"meta": "Профиль", "profile_state": "запись 1: ce, bB, i, bF, e, оружие, u[]",
            "player_state": "персонажи c[] (в записи 2)", "campaign": "bB + B[] флаги",
            "RMS": "RecordStore 'a'" , "slots": "UNKNOWN (см. rms-format)"}
    (OUT / "profile-system-v2.json").write_text(json.dumps(prof, indent=1, ensure_ascii=False))

    # ---------- 14. mission index ----------
    mi = {"meta": "Индекс миссий (m9 seg0 = [1,1,1,1,1])", "missions": [
        {"index": 0, "stream": "m9 seg10", "prereq": "-", "order": "bB=0"},
        {"index": 1, "stream": "m9 seg11", "prereq": "прохождение 0", "order": "bB=1"},
        {"index": 2, "stream": "m9 seg12", "prereq": "прохождение 1", "order": "bB=2"},
        {"index": 3, "stream": "m9 seg13", "prereq": "прохождение 2", "order": "bB=3"},
        {"index": 4, "stream": "m9 seg14", "prereq": "прохождение 3", "order": "bB=4"},
    ], "note": "5 mission streams (не '5 уровней' без проверки); переход между ними — bB + сохранение (ad); "
              "точный инкремент REQUIRES_REAL_RUNTIME"}
    (OUT / "mission-index-v2.json").write_text(json.dumps(mi, indent=1, ensure_ascii=False))

    # ---------- 15. opcode-global ----------
    ogm = {"meta": "Опкоды, меняющие глобальное состояние", "map": [
        {"opcode": 131, "global": "g.bD", "status": "CONFIRMED"},
        {"opcode": 132, "global": "g.d.g[9] (диалог)", "status": "CONFIRMED"},
        {"opcode": 139, "global": "g.bi", "status": "CONFIRMED"},
        {"opcode": 157, "global": "g.u, g.v, состояние", "status": "CONFIRMED"},
        {"opcode": 158, "global": "g.Q (пауза скрипта)", "status": "CONFIRMED"},
        {"opcode": 159, "global": "P (диалог-режим)", "status": "CONFIRMED"},
        {"opcode": 161, "global": "g.dE, g.O", "status": "CONFIRMED"},
        {"opcode": 165, "global": "aX, переход состояния", "status": "CONFIRMED"},
        {"opcode": 169, "global": "g.bM", "status": "CONFIRMED"},
        {"opcode": 126, "global": "L[4] (деньги)", "status": "CONFIRMED"},
    ]}
    (OUT / "opcode-global-state-map-v2.json").write_text(json.dumps(ogm, indent=1, ensure_ascii=False))

    # ---------- 16/17. game over / results ----------
    (OUT / "game-over-pipeline-v2.md").write_text("""# Game Over Pipeline V2

- Причина: HP (g[7]) урон до терминального состояния g[12]>=100 (f.b()).
- Переход: GAME_OVER (10): g.dH() -> LOADING (2) [рестарт] или MENU (1).
- Restore: загрузка из RMS (запись 1 профиль + запись 2 прогресс); чекпоинты НЕ найдены
  (рестарт = перезагрузка миссии bB с сохранённым прогрессом).
- Save interaction: ad() вызывается при завершении миссии, не при смерти (REQUIRES_REAL_RUNTIME уточнение).
""")
    res = {"meta": "Результаты миссии", "fields": {
        "kills": "счётчики g.e[] (агро-обработка) — точное поле UNKNOWN",
        "accuracy": "UNKNOWN (нет статического поля)", "time": "f.z / P[7] (сохраняется)",
        "score": "L[4] (деньги/очки)", "rewards": "магазин после завершения (state 13)",
        "statistics": "P[] массив (ad() пишет/читает)"},
        "screen": "MISSION_COMPLETE (7) g.cd()", "status": "PARTIAL"}
    (OUT / "mission-results-v2.json").write_text(json.dumps(res, indent=1, ensure_ascii=False))

    # ---------- 18. difficulty ----------
    diff = {"meta": "Сложность", "bF": "D[3] — параметр профиля; используется в уроне (30%*bF)",
            "status": "INFERRED (bF влияет на урон); отдельных difficulty-настроек не найдено"}
    (OUT / "difficulty-v2.json").write_text(json.dumps(diff, indent=1, ensure_ascii=False))

    # ---------- 19/20. global resources + graph ----------
    grm = {"meta": "Глобальные источники данных", "sources": [
        {"resource": "m9 seg0", "provides": "таблица длин миссий"}, {"resource": "m9 seg1/2", "provides": "стартовые данные"},
        {"resource": "m9 seg4", "provides": "архетипы/анимации"}, {"resource": "m9 seg5", "provides": "оружие/патроны"},
        {"resource": "m9 seg10-14", "provides": "5 mission streams"}, {"resource": "m8", "provides": "мировые объекты/флаги"},
        {"resource": "t0", "provides": "тексты (диалоги, цели, названия)"}, {"resource": "RMS 'a'", "provides": "профиль+прогресс"},
        {"resource": "dataIGP", "provides": "IGP-данные"}, {"resource": "m13_2", "provides": "MIDI-музыка"}]}
    (OUT / "global-resource-map-v2.json").write_text(json.dumps(grm, indent=1, ensure_ascii=False))

    graph = {"meta": "Кросс-системный граф", "nodes": [
        "MENU(1) -> PROFILES(16) -> LOADING(2) -> CINEMATIC(3) -> GAMEPLAY(6)",
        "GAMEPLAY(6) -> MISSION_COMPLETE(7) -> SHOP(13) -> LOADING(2) [след. миссия]",
        "GAMEPLAY(6) -> GAME_OVER(10) -> LOADING(2)/MENU(1)",
        "GAMEPLAY(6) -> DIALOGUE(11) -> GAMEPLAY(6)",
        "SCRIPTS: bP/bO/bQ (глобальный указатель) -> g.H()/K() -> состояния/поля",
        "SAVE: ad() (завершение миссии) -> RMS 'a' запись 2; профиль -> запись 1",
        "PROGRESSION: L[4] деньги, bB миссия, B[] флаги, b[][] оружие" ]}
    (OUT / "global-system-graph-v2.json").write_text(json.dumps(graph, indent=1, ensure_ascii=False))

    print("global-state-vector, global-state-machine, mission-start/end, objective, progression, shop,")
    print("rms-format, rms-schema, versioning, profile, mission-index, opcode-global, game-over, results,")
    print("difficulty, global-resources, global-graph — записаны")


if __name__ == "__main__":
    sys.exit(main())
