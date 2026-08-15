# Player Death V2

- HP: g[7]; урон: f.b(f2,n) (g[7] -= n + 30%*bF).
- ВОСКРЕШЕНИЕ (g.java:14998): if (g.c.g[7] <= 0) g.c.g[7] = 200 — при 0 HP игрок восстанавливается до 200.
- state 10 (GAME_OVER): существует (g.dH()); триггер REQUIRES_REAL_RUNTIME.
- Retry: state 10 -> LOADING (2) / MENU (1).
- Чекпоинты: НЕ найдены.
