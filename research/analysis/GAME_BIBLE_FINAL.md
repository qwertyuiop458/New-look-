# GAME BIBLE FINAL — Zombie Infection (Gameloft, 2008)
**Consolidated reference** (V1->V4, этап 15.27) · **Дата:** 2026-08-15

Полная база: `research/analysis/MASTER_FACTS.json` (32 факта).
Каждый раздел: FACT / EVIDENCE / STATUS / LIMITATION.

## 1. Платформа
- **FACT:** CLDC-1.0/MIDP-2.0, 240x320, JSR-135 аудио, JSR-256 сенсоры, RMS.
- **EVIDENCE:** MANIFEST.MF, g.java:35186, e.java.
- **STATUS:** CONFIRMED_PRIMARY · **LIMITATION:** поведение на конкретных устройствах RUNTIME.

## 2. Контейнер ресурсов
- **FACT:** 1 байт count + u32 LE относительные смещения; base=1+4A; последний сегмент недоступен.
- **EVIDENCE:** g.java:4055-4100; container_parser_v2.py.
- **STATUS:** CONFIRMED_PRIMARY · **LIMITATION:** нет.

## 3. Миссии
- **FACT:** 5 mission streams m9 seg10..14; форматы записей [type][id][x][y][len][props]; 101/102/103; 110-172; 99.
- **EVIDENCE:** m9; g.Z()/16860.
- **STATUS:** CONFIRMED_PRIMARY · **LIMITATION:** Q[] значения, источник урона cB RUNTIME.

## 4. Скрипты
- **FACT:** 46 mission opcode (44 семантика); контрольные 145/146/143/144/159; вторичный парсер 19 опкодов.
- **EVIDENCE:** g.H()/K()/n(); g.java:1682.
- **STATUS:** CONFIRMED_PRIMARY · **LIMITATION:** визуальные эффекты опкодов, семантика вторичных RUNTIME.

## 5. Сущности
- **FACT:** 56 архетипов x 35 props; 17 кластеров; 666 instances; 26/35 props семантика.
- **EVIDENCE:** m9 seg4; f.c()/f.d().
- **STATUS:** CONFIRMED_PRIMARY/DERIVED · **LIMITATION:** 9 props UNKNOWN.

## 6. AI
- **FACT:** 6 классов (prop10); 24 состояния; 12 переходов; pathfinding НЕТ; урон g[7]-=урон+30%*bF.
- **EVIDENCE:** f.java:2380-5535.
- **STATUS:** CONFIRMED_PRIMARY · **LIMITATION:** агро-единицы, тайминги RUNTIME.

## 7. Анимация/Графика
- **FACT:** 176W+3V+36X+15Y; 4 направления; 8 encodings; 3 формата; 17 слотов; X->объект (структура).
- **EVIDENCE:** m9 seg4; a.java:800-960/574.
- **STATUS:** CONFIRMED_PRIMARY/DERIVED · **LIMITATION:** числа X->спрайт RUNTIME.

## 8. Аудио
- **FACT:** 14 MIDI + 15 WAV (m13_2); 2 канала; 10 звуковых ID; голоса нет.
- **EVIDENCE:** m13_2; g.java:4271-4520.
- **STATUS:** CONFIRMED_PRIMARY · **LIMITATION:** MIDI-привязка, звуки оружия RUNTIME.

## 9. Глобальное/Сейвы
- **FACT:** 18 состояний; bB/bC/bF; RMS 2 записи; L[4] cap 45000.
- **EVIDENCE:** switch(a); ci()/ad().
- **STATUS:** CONFIRMED_PRIMARY · **LIMITATION:** выбор следующей миссии, слоты RUNTIME.

## 10. Objective
- **FACT:** L==10 (bytecode: g.aR) cB=200, Q[] 4 пары, cy; cB<=0 -> state 7; воскрешение g[7]=200.
- **EVIDENCE:** g.java:23300/23598; bytecode aR (5 call sites).
- **STATUS:** CONFIRMED_PRIMARY · **LIMITATION:** привязка 5 вызовов к миссиям ПОНИЖЕНА (гипотеза), урон cB RUNTIME.

## 11. Экономика
- **FACT:** L[4] деньги/энергия; скидки по рангу; апгрейды аддитивно g.y().
- **EVIDENCE:** g.java:21534; f.java:815; g.java:31911.
- **STATUS:** CONFIRMED_PRIMARY/DERIVED · **LIMITATION:** цены, тип наград RUNTIME.

## 12. Производительность
- **FACT:** loop 40/166 мс; freeMemory<100000 guard; буфер 16384; кэши Image/Player.
- **EVIDENCE:** g.run(); a.java.
- **STATUS:** CONFIRMED_PRIMARY · **LIMITATION:** реальные FPS/RAM RUNTIME.

---
**История:** V1 (NOT_READY) -> V2 (READY_WITH_GAPS) -> V3 (READY_WITH_GAPS, аудит) -> V4 (патч: aR bytecode, 2 записи RMS). **STATIC_FRONTIER_EXHAUSTED** (15.26); гипотеза «5 вызовов=5 миссий» понижена (15.27).
