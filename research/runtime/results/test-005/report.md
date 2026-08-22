# TEST-005 — REAL RUNTIME PLAYER DEATH / FAILURE — ОТЧЁТ

**Дата:** 2026-08-22
**Тест:** TEST-005 (Этап 15.34)
**Runtime:** FreeJ2ME SDL (Anbu) x86 JRE 17; JAR SHA-256 `1111f12b...` (не изменён; instrumented.jar побайтово идентичен)
**Миссия:** mission 03 (RUNTIME_ASSISTED bB=3 — только выбор миссии; JDWP для state/HP не использовался)

## 1. Итог

**PASSED** — полный жизненный цикл смерти прослежен в реальном runtime:
HP 200 → damage ×7 → HP≤0 → death state 7 → reload → HP=200 (retry). **State 10 НЕ наблюдён** — GAME_OVER не объявляется (по ТЗ п.8).

## 2. Damage events (7 попаданий, враг g0=34 state=1)

| t | HP_before → HP_after | dmg | dist_px |
|---|---|---|---|
| 50.1 | 200→170 | 30 | 322 |
| 51.7 | 170→140 | 30 | 325 |
| 54.2 | 140→110 | 30 | 329 |
| 56.7 | 110→80 | 30 | 335 |
| 59.8 | 80→50 | 30 | 340 |
| 60.7 | 50→20 | 30 | 345 |
| 63.1 | 20→**−10** | 30 | 945 |

Период 1.6–3.1с; player_state=8 (боевое) на всём протяжении.

## 3. Death flow (частое логирование после HP≤0)

```
t=63.1  HP<=0 (20->-10), player_state=8
t=63.1  g_state=7 g_sub=0  bB=0  bC=0  u=9  pos=(108,198)   <- DEATH STATE
t=65.4  g_state=7 g_sub=0
t=67.6  g_state=7 g_sub=2  (player=None — экран смерти)
t=69.8  g_state=7 g_sub=3
t=72.0  g_state=7 g_sub=4
t=74.2  g_state=2 g_sub=0  HP=200  pos=(2858,843)  <- RELOAD + RESURRECTION
```

- **Death state = state 7** (не 10!); sub-переходы 0→2→3→4.
- **bB: 3 → 0** (сброс миссии при смерти).
- **Reload**: state 2 (загрузка) → HP=200, стартовая позиция mission 0 (2858,843).
- **Save**: Record a.1 set (профиль) — из лога эмулятора.

## 4. Проверка статической ветки g[7]≤0 → g[7]=200

**observed = YES** (t=74.2, g_state=2 g_sub=0, HP 200 после reload). Контекст: перезагрузка после смерти, не мгновенный reset в том же кадре (B() ветка g.java:14998).

## 5. Retry

**YES**: death → reload (state 2) → HP=200 на старте mission 0 (bB=0). Retry = загрузка сейва (bB=0), НЕ рестарт mission 3.

## 6. Game Over (state 10)

**НЕ наблюдён** (state10_seen=false). После смерти идёт state 7 → reload, без state 10. Семантика state 10 не меняется (по ТЗ п.17).

## 7. Скриншоты (evidence/real/test-005/, с метаданными)

before-death.png, death.png (момент HP≤0), post-death.png (state 7), retry.png (reload). game-over.png НЕ создан (state 10 не показывался — по ТЗ fake не создаём).

## 8. Сравнение со статикой (comparison.json, 10 пунктов)

MATCH ×5 (damage; death trigger; resurrection g[7]=200; reload; player state 8), NEW_OBSERVATION ×3 (state 7 = death state; bB сброс 3→0; death position), PARTIAL ×1 (save — только a.1), INCONCLUSIVE ×1 (state 10). MISMATCH ×0.

## 9. Аудио

**AUDIO_RUNTIME_BLOCKED_BY_STUB** — в PASS/FAIL не входит.

## 10. Ограничения

- Экран «Game Over» (state 10) не показан игрой в этом сценарии — смерть ведёт сразу к reload.
- RMS запись 2 (прогресс) в этом прогоне не подтверждена (только a.1 set).
- Неясно, почему reload в mission 0 (bB=0) вместо mission 3 — вероятно, загрузка сохранённого профиля (bB=0 из сейва).

## 11. Knowledge updates

MASTER_FACTS.json: F056–F058 (death state 7, resurrection observed, bB reset). runtime-frontier-v4.json: test005.
