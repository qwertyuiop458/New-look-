# Bible V3 Forensic Audit — отчёт

**Дата:** 2026-08-15 · **Метод:** независимая сверка всей V2-базы с первичными источниками (JAR, bytecode, decompiled, raw resources, V2-парсеры).

## 1. Executive Summary

V2-база в целом подтверждена: структуры (контейнер, миссии, скрипты, архетипы, AI, графика, аудио, глобальное, сейвы, производительность) имеют первичное evidence. Найдены 5 уточнений и 6 противоречий (4 разрешены, 2 открыты). 7 фактов остаются REQUIRES_REAL_RUNTIME.

## 2. Primary Evidence Coverage

- CONFIRMED: 34/45 фактов master-index (76%);
- INFERRED: 2;
- RUNTIME: 7;
- смешанные (структура+runtime): 2.

## 3. Corrections from V2

1. 120238 мини-кадров — уточнено (2038 объектов с кадрами; 9698 объектов всего).
2. m13_2 = медиа-контейнер (14 MIDI + 15 WAV), не только музыка.
3. prop21 — multi-use (звук + др.), не просто «звук оружия».
4. cy — формула CONFIRMED, роль INFERRED.
5. m8 seg0/1/2 — нейтрально SEG0/1/2 (NO_CONSUMER_FOUND).

## 4. Cross-System Contradictions

6 противоречий: 4 RESOLVED (мини-кадры, m13_2, агро-единицы, 3 слота), 1 OPEN (prop21 dual-use), 1 RESOLVED (m8 названия).

## 5. False Confirmed Findings

6 кандидатов проаудированы: 4 остались CONFIRMED корректно, 2 уточнены (G03 формулировка, O03 роль cy).

## 6. Remaining Static Frontier

Возможно статически: вызов g.a(f2,n,byArray,n2) (CFR), prop13/16/18, Q[] значения, слоты сейвов, 19 опкодов парсера 1682, m8 seg0/1/2 роли, prop21/31.
Требует рантайма: выбор миссии, урон cB, X→спрайт числа, цены, MIDI-привязка, агро, failure, race, FPS/RAM.

## 7. Runtime Boundary

Полный список RUNTIME: master-fact-index (7 фактов) + knowledge-gaps-v3 (10 gaps, 3 CRITICAL).

## 8. Subsystem Grades

| Подсистема | Grade |
| :--- | :-: |
| ARCHITECTURE | A |
| CONTAINER | A |
| MISSION | A |
| SCRIPT | B |
| ENTITY | B |
| AI | B |
| ANIMATION | B |
| GRAPHICS | B |
| AUDIO | B |
| GLOBAL STATE | B |
| SAVE | B |
| ECONOMY | C |
| PERFORMANCE | B |

## 9. V3 Readiness

**READY_WITH_GAPS** — статические структуры доказаны; runtime-вопросы существенны, но ограничены.

## 10. Recommended Next Research

1. Закрыть статический frontier (вызов g.a(f2,...), Q[] значения, prop13/16/18).
2. Запуск оригинала на J2ME-эмуляторе — закрытие runtime-вопросов.
3. После рантайма — финальная пересборка sequel-reference.
