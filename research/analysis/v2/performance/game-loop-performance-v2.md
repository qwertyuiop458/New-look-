# Game Loop Performance V2

```
run() (g.java:35148):
  d = now - c; if (d > 166 || d <= 0) d = 166        // CLAMP (лаг-защита)
  c = now
  c.a((int)d)                                        // обновление (state logic)
  if (!az): repaint(); serviceRepaints()             // РЕНДЕР
  do { l = now - c; Thread.yield(); } while (l < 40) // ОЖИДАНИЕ до 40 мс
while (a != 99)
```

- TARGET_FRAME_INTERVAL: 40 мс (25 FPS номинал).
- UPDATE_TIME: зависит от состояния (геймплей: g.B() — f.b() агро + per-entity).
- RENDER_TIME: state render (g.p()); worst-case: геймплей с N сущностями.
- SLEEP: yield-спин (не sleep) — экономия на sleep-аллокациях.
- **STATIC_MODEL_ONLY**: реальные FPS/RAM — REQUIRES_REAL_RUNTIME.
