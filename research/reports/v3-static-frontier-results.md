# V3 Static Frontier Results

**Дата:** 2026-08-15

## Resolved (static)

1. **g.aR (L==10 создание)** — RESOLVED: bytecode показывает 5 invokestatic вызовов aR(f,int,byte[],int) (по одному на миссию); CFR скрыл имя (aR -> a). Цепочка подтверждена.
2. **Save slots** — PARTIALLY: 2 записи RMS подтверждены кодом (B(2), c(1)/c(2), a(1,D)/a(2,E)); >2 не доказано.

## Partially resolved

3. **Вторичный парсер (19 опкодов 1682)** — структура CONFIRMED, семантика RUNTIME.
4. **Q[] значения** — кандидаты есть, точные неоднозначны (RUNTIME).

## Impossible statically

5. **m8 seg0/1/2 consumer** — NO_STATIC_CONSUMER_FOUND (исчерпывающий поиск).
6. **prop13/16/18** — контексты не изолируются.
7. **prop21/31** — multi-use, роль не определяется.

## Runtime-only (не решаемо статикой)

выбор следующей миссии · урон cB (n9) · числа X→спрайт · цены магазина · тип наград k(n,10) · MIDI-привязка · агро-единицы · failure trigger · race conditions · FPS/RAM · семантика 19 вторичных опкодов.

## Newly discovered

- g.aR — настоящее имя метода объекта-миссии в bytecode (CFR-коллизия).
- 5 вызовов aR = 5 миссий.
