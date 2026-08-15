# Reference Chain — archetype 3 (этап 15.14)

**Дата:** 2026-08-15 · **Статус:** STATICALLY_RESOLVED до кадра; RENDER_RUNTIME_REQUIRED для последнего шага.

## Цепочка (все шаги с evidence)

```
mission record [type 3][id][x][y][len][props]
  → g[0] = g.a(g.m, props[0])                    (f.c(), таблица m из m9 seg4)         CONFIRMED
  → архетип 3: props32 = [...]                    (m9 seg4, tag6)                       CONFIRMED
  → анимации: prop33 = N; слоты g[30+i]          (f.g(), f.java:2572)                   CONFIRMED
  → кадр: n5 = dir + g.i(type, state)            (f.java:4656; V[prop34*15+state])      CONFIRMED
  → X: g.d(type, anim, fr, 0/1) = X[W10+fr*2+0/1] (g.java:24747)                        CONFIRMED
  → пиксели: a(int n) — RLE-блоки j + палитра a[i][256]
      форматы: 25840 (RLE+маска), 10225/22258 (RLE), 5632 (4bpp), 2048 (3bpp),
               1024 (2bpp), 512 (1bpp), 22018 (8bpp)                                     CONFIRMED
  → Image: createRGBImage(pixels, w, h, alpha)   (a.java:763)                           CONFIRMED
  → render: drawImage/drawRegion(..., a[n4&7], ...) (a.java:770-772; трансформы {0,2,1,3,5,7,4,6}) CONFIRMED
  → КАКОЙ X-индекс → КАКОЙ объект листа (c x d):     RENDER_RUNTIME_REQUIRED
```

## Вывод

Мост frame → pixel data → Image **найден и доказан статически** на уровне декодера и рендера.
Единственный оставшийся шаг — сопоставление конкретного X-индекса кадра с конкретным объектом
спрайт-листа (размеры c×d) — требует рантайм-рендера (нет статической таблицы соответствия).
