# TEST-001 — REAL RUNTIME: INPUT + STATE + ENTITY TRACE — ОТЧЁТ

**Дата:** 2026-08-15
**Тест:** TEST-001 (Этап 15.30)
**Runtime:** FreeJ2ME SDL (Anbu) на x86 JRE 17 (Temurin 17.0.19)
**JAR:** original.jar SHA-256 `1111f12bd94e5693bbdd9acab4726e5b543730b9137504af1e8a8ecb09f00d4e`
(использовалась копия `jar/instrumented.jar` — байты идентичны оригиналу, инструментирование внешнее через JDWP)
**Инструментирование:** JVM Debug Interface (JDWP) — классы, поля, массивы и события читаются
извне; оригинальный JAR не изменён (п.9 ТЗ соблюдён).

## 1. Итог

**PASSED** — реальный проход BOOT → MENU → NEW GAME → PROFILE → CHARACTER SELECT → LOADING → GAMEPLAY
выполнен автоматически с сохранёнными evidence, state-trace и entity-trace.

Последовательность экранов (реальные наблюдения state-trace):

```
BOOT (state 1 → 2, загрузка RMS a.1/a.2)
→ CINEMATIC (state 3, x=1, u=4 — «press fire»)
→ MENU (state 3, u=0, v=2, пункт 3)
→ DIFFICULTY/PROFILE (u=7 — экран сложности, пункт 47..50 → bF)
→ CONFIRM/CHARACTER SELECT (u=9 — подтверждение перезаписи сейва, YES=пункт 24)
→ INTRO (state 16, C())
→ LOADING (state 2 → загрузка миссии 0, g.Z(0))
→ GAMEPLAY (state 6, sub 1, bB=0, камера T/U живая)
```

## 2. INPUT BRIDGE (п.1 ТЗ)

- Расширен `research/runtime/sdl_interface`: приём кадров (stdin) + отправка клавиш
  5-байтовыми пакетами в **stderr** (поток `proc.getErrorStream()` — установлено по байткоду
  `Anbu$SDL.start()`).
- Протокол верифицирован по байткоду `Anbu$SDL$SDLKeyTimerTask` (пакет 5 байт:
  `[0]=(type<<4)|pressed`, `[1..4]=u32 BE code`; type 0=KEY, 1=POINTER) и
  `Anbu.getMobileKey` (useFlag=0): SDL-стрелки → '2','8','4','6', ENTER → '5'.
- SOFT_LEFT(-6)/SOFT_RIGHT(-7) **недоставимы** — getMobileKey возвращает 0 для кодов
  вне таблицы (документировано в keymap.json).
- Артефакты: `input/keymap.json`, `input/input-protocol.md`.

## 3. INPUT SMOKE TEST (п.2 ТЗ)

`results/test-001/input-smoke-test.json` — **KEY_RECEIVED**:

| Проверка | Результат |
|---|---|
| control_channel (TCP → stub) | OK (PONG) |
| Брейкпоинт JDWP на `SDLKeyTimerTask.run()` @ putfield code (0x89) | 2 попадания на одно нажатие FIRE (press+release) |
| Вердикт | KEY_RECEIVED |
| Эмулятор жив после теста | true |

Цепочка: key → sdl_interface (5-байтовый пакет в stderr) → Anbu `getErrorStream()`
→ `SDLKeyTimerTask` (разбор пакета) → `getMobileKey` → `MobilePlatform.keyPressed`
→ `g.keyPressed` (бит клавиши).

## 4. STATE TRACE (п.6 ТЗ)

`results/test-001/state-trace.json` — 122 события изменения полей, 146+ снимков:

- поля: state, sub, bB, bC, bF, by, bz, ey, ez, u, v, aF, x, w, dm, dn, T, U;
- ключевые переходы: state 1→2→3 (загрузка/кинематика), 3→16 (новая игра),
  16→2→6 (геймплей); u: 0→7→9 (меню→сложность→подтверждение); T/U ожили
  на геймплее (T=23193642, U=9678953).

## 5. ENTITY TRACE (п.7 ТЗ)

`results/test-001/entity-trace.json` — **1034 реальных сущности** миссии 0:

| L (тип) | Кол-во | Статическая семантика |
|---|---|---|
| 10 | 473 | объекты (10–26 = объекты) |
| 3 | 152 | **враги** (type 3 = враг) |
| 1 | 84 | (объекты/декорации) |
| 20 | 59 | объекты |
| 14 | 51 | объекты |
| 9 | 47 | **NPC** (type 9 = NPC) |
| 18 | 36 | объекты |
| 15, 16, 22, 23, 11, 12, 21, 24, 25, 26 | 131 | объекты |

Структура хранения подтверждена: `f[mission][map] = f[]` (12 сеток a..l);
позиции в fixed-point (>>14); MC (L=0) в сетках отсутствует — хранится отдельно.

## 6. SCREENSHOTS (п.5 ТЗ)

`evidence/real/test-001/` (каждый с метаданными .json):

| Файл | Экран |
|---|---|
| boot.png | кинематика «press fire» |
| menu.png | главное меню |
| profile.png | экран сложности (профиль) |
| character-select.png | подтверждение перезаписи сейва |
| loading.png | загрузка миссии |
| gameplay.png | геймплей (state 6) |
| first-entity.png | геймплей с отмеченными видимыми сущностями (4 шт.) |

## 7. STATIC vs RUNTIME (п.8 ТЗ)

`results/test-001/comparison.json` — 14 пунктов: **MATCH ×11, PARTIAL ×1 (S07 props),
NEW_OBSERVATION ×1 (S09 — «серия +5» в меню), INCONCLUSIVE ×1 (S12 — звук,
AUDIO_RUNTIME_BLOCKED_BY_STUB)**.

## 8. AUDIO (п.9 ТЗ)

libaudio.so — JNI-заглушка (реального звука нет). Аудио-поведение НЕ помечено
RUNTIME_CONFIRMED. Статус: **AUDIO_RUNTIME_BLOCKED_BY_STUB**.

## 9. Ограничения и наблюдения

1. Пункт 45 (новая игра, bB=3) недостижим навигацией меню: первое нажатие после
   активации даёт серию +5 шагов курсора (цикл v: {2,7,8,9,10}) — артефакт
   конвейера кадров эмулятора; использован штатный путь: пункт 3 → сложность → подтверждение.
2. Одно JDWP-чтение GetValues на объекте неверного класса (массив вместо f) может
   вызывать JVM SIGSEGV (InstanceKlass::find_local_field_from_offset) — обходится
   корректной структурой чтения.
3. Эмулятор FreeJ2ME не имеет пути доставки -6/-7 (SOFT_LEFT/SOFT_RIGHT) в этой игре.
