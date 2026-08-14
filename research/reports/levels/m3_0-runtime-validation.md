# Отчёт по симуляционной валидации уровня `m3_0` (m3_0 Validation Report)

---

### RUNTIME STATUS: NOT EXECUTED
*   **Причина:** `J2ME emulator GUI runtime unavailable because X11/display support is unavailable in this headless sandbox environment.`
*   **Статус валидации рантайма:** `REQUIRES_REAL_RUNTIME` (динамический запуск оригинального мидлета не выполнялся).
*   **Статус симуляции:** `SIMULATED` (все динамические выводы построены на основе точной математической реконструкции оригинальной рантайм-логики).

---

## 1. Сводная таблица верификации (Claim-Observation Map)

| CLAIM (Утверждение) | STATIC (Ожидаемое значение) | RUNTIME (Фактическое наблюдение) | RESULT (Результат) |
| :--- | :--- | :--- | :---: |
| **A. Player Spawn Point** | Координаты `tile=(27, 62)`, `fixed_x=442368` | `REQUIRES_REAL_RUNTIME` | **SIMULATED** |
| **B. Zombie Spawn Points** | Координаты `(56,12)`, `(68,15)`, `(81,18)` | `REQUIRES_REAL_RUNTIME` | **SIMULATED** |
| **C. Keycard Placement** | Координаты `(18, 16)` в офисе шерифа | `REQUIRES_REAL_RUNTIME` | **SIMULATED** |
| **D. Map Dimensions** | Сетка `110x82` тайлов | `REQUIRES_REAL_RUNTIME` | **SIMULATED** |
| **E. Tile Rendering Size** | `16x16` пикселей на тайл | `REQUIRES_REAL_RUNTIME` | **SIMULATED** |
| **F. Collision System** | Маска `1` блокирует ось X/Y (`future_x >> 18`) | `REQUIRES_REAL_RUNTIME` | **SIMULATED** |
| **G. Trigger Behavior** | Дверь `(25, 50)` закрыта до взятия ключа | `REQUIRES_REAL_RUNTIME` | **SIMULATED** |
| **H. Dialogue Texts** | Строка `"Дверь заблокирована..."` в CP1251 | `REQUIRES_REAL_RUNTIME` | **SIMULATED** |

---

## 2. Реалистичная оценка статуса исследования (Confidence Metrics)

*   **Уверенность статического анализа (Static Analysis Confidence):** **HIGH** (100% кода классов `a`, `c`, `f`, `g` полностью декомпилированы, взаимосвязи и бинарные форматы разложены до уровня байт-кода и проверены).
*   **Уверенность симуляционной реконструкции (Simulated Reconstruction Confidence):** **HIGH** (написанные математические тесты `test_t0_decoder.py` и генераторы подтвердили полную корректность структур данных).
*   **Фактический статус рантайм-валидации (Runtime Validation Status):** **NOT EXECUTED** (требует живого выполнения на J2ME-совместимом эмуляторе с поддержкой X11 графического сервера).

---

## 3. Детальные разделы отчета

### 1. Environment & Emulator Limitations
*   Текущая песочница является безголовым сервером Linux (headless), не поддерживающим системные переменные `DISPLAY` или графические библиотеки AWT/Swing, необходимые для запуска JVM-эмуляторов KEmulator/FreeJ2ME. Установка `Xvfb` заблокирована сетевым экраном песочницы.

### 2. Map & Collision (Simulated)
*   Сетка коллизий `110x82` тайлов была полностью проверена математически по первому сегменту `m3_0` и полностью сходится. Проходимость рассчитывается в `f.java` через операцию сдвига координат `fixed_x >> 18`.

### 3. Triggers & Dialogue (Simulated)
*   Успешно восстановлена таблица из 10 опкодов триггеров. Тексты диалогов, извлеченные из CP1251 Segment 09, полностью верифицированы. Все скриншоты, сохраненные в каталоге `research/runtime/simulated-evidence/`, являются **реконструированными (simulated-evidence)** на основе Pillow-генератора и не захватывались с реально работающего эмулятора.
