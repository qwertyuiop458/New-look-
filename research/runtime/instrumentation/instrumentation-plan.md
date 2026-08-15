# Instrumentation Plan

**Принцип:** НЕ изменять оригинальный JAR. Инструментирование — через:
1. **Сторонний отладчик** (FreeJ2ME logging hooks — если поддерживает);
2. **Обёртку классов** (instrumentation-версия классов в отдельном classpath, подменяющая только точки наблюдения);
3. **Эмуляторные логи** (freej2me-web console).

Точки инструментирования (по runtime-requirements):
- STATE_CHANGE: g.d(n,m) — глобальные переходы;
- ENTITY_SPAWN: g.Z() case 3/9/10 — создание сущностей;
- AI_STATE: f.c(f2,n) — смена состояния сущности;
- TIMERS: g[15]/f.w — таймеры атак;
- MISSION_OBJECT: g.aR(f,n,byArray,n2) — создание объекта-миссии (cB/Q[]/cy);
- COMPLETION: cZ() — cB<=0;
- REWARD: k(n,10) — награды;
- SHOP: fE() — открытие/покупка;
- SAVE/LOAD: ci()/ad() — RMS;
- AUDIO: a(n,1) — playback (ID, сегмент);
- RENDER: c.java a.a(d,e) — кадры (X->sprite числа).

**Совместимость:** инструментирование через подмену классов требует проверки совместимости с J2ME bytecode (major 45). Альтернатива: эмуляторные hooks.
