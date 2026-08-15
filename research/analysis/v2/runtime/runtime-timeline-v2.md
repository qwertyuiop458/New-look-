# Runtime Timeline V2

```
T0 SPAWN     запись миссии -> props -> архетип -> g[12]=0/23, анимация, позиция
T1 UPDATE    g.B() каждый кадр (state 6): eF, Q, bM, bE, f.b() (агро)
T2 AI        f.i()/f.j()/f.o()/f.p() по g[12] (+ подсостояние g[10])
T3 MOVEMENT  velocity g[13]/g[14] -> шаг 819200 -> позиция c.a/c.b
T4 COLLISION 5-точечный зонд + AABB; f.p() смена направления
T5 ATTACK    g[12] 7/8/12: таймеры g[15]/f.w, урон f.b(f3, prop14)
T6 DAMAGE    g[7] -= урон + 30%*bF; смерть g[12]>=100
T7 ANIMATION c.java: аккумулятор 62 -> кадр e -> f.a() по состоянию
T8 RENDER    a.java: декодер -> Image -> drawRegion (трансформ a[n4&7])
```

Зависимости: T2 зависит от T1; T5 зависит от T2/T3; T7 зависит от g[12]; T8 от T7 и камеры.
