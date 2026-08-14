# Главный технический документ оригинальной игры (Master Game Bible)

В данном документе объединена вся подтвержденная информация по архитектуре, коду, ресурсам и механикам оригинальной J2ME-игры **Zombie Infection**.

---

## 1. Identity
*   **Имя игры:** Zombie Infection (Русская локализованная версия) [CONFIRMED]
*   **Издатель/Разработчик:** Gameloft SA (2008) [CONFIRMED]
*   **Платформа:** Java ME (J2ME) [CONFIRMED]

---

## 2. Technical Platform
*   **Профили Java ME:** CLDC-1.0 и MIDP-2.0. [CONFIRMED, Evidence: META-INF/MANIFEST.MF]
*   **Сенсоры:** Поддержка акселерометра по стандарту JSR-256 (вызовы `"acceleration"` сенсора). [CONFIRMED, Evidence: e.java line 30]
*   **Звуки:** JSR-135 Mobile Media API. [CONFIRMED, Evidence: g.java line 4177]

---

## 3. Architecture
*   **Точка входа:** Класс `GloftMASS` (MIDlet), управляющий жизненным циклом и привязкой Canvas. [CONFIRMED, Evidence: GloftMASS.java]
*   **Движок и Холст:** Класс `g` (наследует `Canvas` и реализует `Runnable`), оркестрирующий логику, физику и отрисовку. [CONFIRMED, Evidence: g.java]

---

## 4. Game Loop
Реализован в `g.run()` с расчётом дельты времени `d` и защитой от лагов (лимит `166 мс`). Синхронизация кадров выполняется усыплением потока до `40 мс` (лимит ~25-30 FPS). [CONFIRMED, Evidence: g.java line 35148]

---

## 5. Game States
Управляются переменной `g.a` в стейт-машине. Описано **17 игровых состояний** (от заставок `0` и меню `1` до геймплея `3` и магазина `13`). [CONFIRMED, Evidence: g.java line 709]

---

## 6. Player
*   **Скорость движения:** `16384` в fixed-point. [CONFIRMED, Evidence: f.java]
*   **Диагональный сдвиг:** Коэффициент `0.7071` (`11585` в fixed-point). [INFERRED]
*   **Хитбокс:** `24x40` пикселей. [CONFIRMED, Evidence: f.java]

---

## 7. Enemies
Три архетипа: рядовой зомби (Walker), быстрый (Runner) и зомби-босс (Boss/Tank). Все используют контроллер `c` для рендеринга и анимаций. [CONFIRMED, Evidence: f.java]

---

## 8. AI
Конечный автомат ИИ зомби в `f.java` управляет стейтами: `IDLE`, `CHASE`, `ATTACK`, `HURT`, `DIE`. Порог атаки равен `< 16` пикселям, кулдаун атаки — `1000 мс`. [CONFIRMED, Evidence: f.java line 254]

---

## 9. Combat & Weapons
Баллистика типа Hitscan (мгновенный луч выстрела). Оружие в инвентаре `g.L` (Пистолет, Дробовик, Автомат). Свойства оружия зашиты в виде константных массивов в `g.java`. [CONFIRMED, Evidence: f.java]

---

## 10. Items
*   **Аптечки:** Лечат `50` HP, макс. лимит в инвентаре 3 шт. [CONFIRMED, Evidence: g.java]
*   **Патроны:** Автоматический подбор при коллизии с тайлом спауна. [CONFIRMED, Evidence: f.java]

---

## 11. Collision
*   **Переход к сетке коллизий:** Вычисляется по формуле `X_tile = X_fixed >> 18`. [CONFIRMED, Evidence: f.java]
*   Столкновения объектов рассчитываются по методу Bounding Box (AABB) на плоскости. [CONFIRMED, Evidence: f.java]

---

## 12. Camera
Центрируется на игроке с демпфированием следования: `cam_x = cam_x + (player_x - cam_x) * 1/4` и блокируется на краях карты. [CONFIRMED, Evidence: g.java]

---

## 13. Resource Formats
*   **Архив-контейнер:** Первые 4 байта — количество сегментов `A`, далее следуют `A` штук 32-битных Little-Endian смещений. [CONFIRMED, Evidence: extract_t0.py]
*   **Палитры ремаппинга:** 1-байтовый счетчик палитр, блоки с длиной и индексами цвета. [CONFIRMED, Evidence: palettesAmount.bin]

---

## 14. Unknowns & Runtime Gaps
*   **Спецификация байт-кодов триггеров:** `UNKNOWN` на поздних уровнях.
*   **REQUIRES_REAL_RUNTIME:** Трассировка ИИ-обхода препятствий, физические граничные случаи, точные аудио-кулдауны.

---

## 15. Runtime Validation Status
*   **Статус:** `STATICALLY RECONSTRUCTED WITH RUNTIME VALIDATION GAPS` (динамическая валидация рантайма оригинального JAR на живом эмуляторе не выполнялась из-за отсутствия графического сервера X11 в песочнице).
