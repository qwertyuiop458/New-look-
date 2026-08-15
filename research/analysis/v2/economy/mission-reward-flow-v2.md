# Mission Reward Flow V2

```
L==10 completion (cB<=0) -> state 7
  -> cZ() cw==1: da = cU*1 + cW*-10 + cY*-5 (счёт)
  -> db = M(da): последний порог Q[i*2] <= da
  -> cw==2/3: n = Q[dc*2+1]; g.k(n, 10) — выдача награды
  -> ap(4) -> конец -> ad() сохранение -> state 13/2
```
- Q[] значения из данных миссии (8 байт) — REQUIRES_REAL_RUNTIME (вызов не найден статически).
- Тип награды k(n,10): REQUIRES_REAL_RUNTIME.
