#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_mission_object_model_v2.py — объект миссии L==10 (этап 15.21).

ДОКАЗАННО:
  - создание: g.Z() case 10 (14256): g.a[layer][x][y] = new f(s, 10, x, y, props)
  - объект-миссия: g.a(f2, n, byArray, n2) (23300): f2.L==10 -> i=f2, cB=200, cz=n,
    Q[] = 4 пары u16 (id, значение) из byArray, aU/bw/bx=1
  - поведение: f.java:1388 (AABB бокс g[2]+2 x g[3]+2), f.java:8266 (L==10 && g[7]!=0 статичный),
    g.java:8996 (L==10 соответствует слою g[i]/h[i]/j[i])
  - завершение: cZ(): cB<=0 -> g.e() -> state 7; награды Q[] (k(n,10), ap(3/4))
"""
import json
import sys
from pathlib import Path

OUT = Path("research/analysis/v2/objectives")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    cr = {"meta": "Создание объектов L==10", "sites": [
        {"method": "g.Z() case 10 (14256)", "source_record": "type 10 запись миссии",
         "creation": "new f(s, 10, n44, n45, nArray34) -> g.a[layer][x][y]",
         "initialization": "props (nArray34); L=10; позиция (n44,n45)", "confidence": "CONFIRMED"},
        {"method": "g.a(f2, n, byArray, n2) (23300)", "source_record": "объект L==10 + данные byArray",
         "creation": "i=f2 (объект-миссия); cB=200; cz=n; Q[]=4 пары; aU/bw/bx=1",
         "initialization": "cP() (границы), q(false), r(false)", "confidence": "CONFIRMED"},
        {"method": "f.java:8266", "source_record": "-", "creation": "L==10 && g[7]!=0 — пропуск обновления (статичный)",
         "confidence": "CONFIRMED"},
    ]}
    (OUT / "mission-object-creation-v2.json").write_text(json.dumps(cr, indent=1, ensure_ascii=False))

    sv = {"meta": "Поля объекта-миссии L==10", "fields": [
        {"field": "L", "value": 10, "meaning": "класс объекта-миссии", "confidence": "CONFIRMED"},
        {"field": "g[0]", "meaning": "архетип/тип (для слоя g[i]/h[i])", "confidence": "CONFIRMED"},
        {"field": "g[1]", "meaning": "подтип (для слоя h[i])", "confidence": "INFERRED"},
        {"field": "g[2]/g[3]", "meaning": "размеры бокса (AABB: n3=g[2]+2, n4=g[3]+2)", "confidence": "CONFIRMED"},
        {"field": "g[7]", "meaning": "флаг/HP (==0 -> обновляется; !=0 -> статичный)", "confidence": "CONFIRMED"},
        {"field": "позиция c.a/c.b", "meaning": "мировые координаты", "confidence": "CONFIRMED"},
        {"field": "i (глобальный)", "meaning": "ссылка на активный объект-миссию", "confidence": "CONFIRMED"},
        {"field": "cB (глобальный)", "meaning": "HP/прогресс миссии (init 200)", "confidence": "CONFIRMED"},
        {"field": "cy (глобальный)", "meaning": "лимит ((ab?3:16)*d.length*16)", "confidence": "CONFIRMED"},
        {"field": "Q[] (глобальный)", "meaning": "4 пары наград (id, значение)", "confidence": "CONFIRMED"},
        {"field": "cz", "meaning": "параметр миссии (n при создании)", "confidence": "CONFIRMED"},
        {"field": "cS", "meaning": "первый объект слоя (g[0])", "confidence": "INFERRED"},
        {"field": "aU/bw/bx", "meaning": "флаги активности (=1)", "confidence": "CONFIRMED"},
    ]}
    (OUT / "mission-object-state-v2.json").write_text(json.dumps(sv, indent=1, ensure_ascii=False))

    cp = {"meta": "Параметры создания", "parameters": [
        {"param": "cB", "source": "константа 200", "offset": "-", "decoded": 200, "consumer": "cZ() завершение", "confidence": "CONFIRMED"},
        {"param": "cy", "source": "(ab?3:16) * d.length * 16", "offset": "-", "decoded": "зависит от слоя", "consumer": "cZ() время", "confidence": "CONFIRMED"},
        {"param": "Q[]", "source": "byArray (данные миссии), 4 пары u16", "offset": "n2 + i*4", "decoded": "8 байт", "consumer": "награды k(n,10)", "confidence": "CONFIRMED"},
        {"param": "cz", "source": "n (параметр вызова)", "offset": "-", "decoded": "неизвестно", "consumer": "миссия", "confidence": "CONFIRMED (передача)"},
        {"param": "props записи", "source": "type 10 запись миссии", "offset": "поток", "decoded": "8+ u16", "consumer": "объект", "confidence": "CONFIRMED"},
    ]}
    (OUT / "mission-object-creation-params-v2.json").write_text(json.dumps(cp, indent=1, ensure_ascii=False))

    cb = {"meta": "cB dataflow", "dataflow": [
        {"op": "init", "value": 200, "site": "g.a(f2,...) 23307", "confidence": "CONFIRMED"},
        {"op": "decrement", "formula": "cB = cB >= (n8 += f.a(bl?8:16, n9)) ? cB - n8 : 0", "site": "g.java:23434", "confidence": "CONFIRMED"},
        {"op": "compare", "condition": "cB <= 0 (cw==0)", "site": "cZ() 23605", "effect": "g.e() -> state 7", "confidence": "CONFIRMED"},
        {"op": "compare", "condition": "cB > 0", "site": "cZ()", "effect": "продолжение cY()", "confidence": "CONFIRMED"},
    ], "note": "cB уменьшается через f.a(8|16, n9) — урон от объекта (n9) с коэффициентом 8 или 16"}
    (OUT / "mission-object-cb-dataflow-v2.json").write_text(json.dumps(cb, indent=1, ensure_ascii=False))

    ds = {"meta": "Источники урона cB", "sources": [
        {"source": "f.a(bl?8:16, n9)", "detail": "cB -= урон; n9 из контекста; коэффициент 8/16", "status": "CONFIRMED (формула); источник n9 REQUIRES_REAL_RUNTIME"},
        {"source": "AABB столкновение", "detail": "f.a(f2,f3): L==10 бокс g[2]+2 x g[3]+2", "status": "CONFIRMED (механизм)"},
        {"source": "скрипты", "detail": "опкоды 112/167/172 — действия над объектами-тайлами", "status": "UNKNOWN"},
        {"source": "таймер", "detail": "cy: превышение -> ap(1) (награды, не fail)", "status": "CONFIRMED"},
    ]}
    (OUT / "mission-object-damage-sources-v2.json").write_text(json.dumps(ds, indent=1, ensure_ascii=False))

    cy = {"meta": "cy", "detail": "cy = (ab ? 3 : 16) * d.length * 16 (g.java:23280)",
          "unit": "тайлы*16 = пиксели (не мс!)", "initial": "зависит от слоя d.length",
          "compare": "g.i.a.a() > cy (позиция X объекта-миссии > лимит)", "effect": "ap(1) — награды (не fail)",
          "role": "ПРОСТРАНСТВЕННЫЙ лимит (позиция X), НЕ таймер",
          "confidence": "CONFIRMED (формула); точная семантика REQUIRES_REAL_RUNTIME"}
    (OUT / "mission-object-timer-v2.json").write_text(json.dumps(cy, indent=1, ensure_ascii=False))

    rw = {"meta": "Награды Q[]", "structure": "Q[i*2] = id (u16), Q[i*2+1] = значение (u16); 4 пары; из byArray n2+i*4",
          "reward_flow": "cZ() cw==1: da = cU*1 + cW*-10 + cY*-5 (>0?); db = M(da); "
                         "cw==2/3: n = Q[dc*2+1]; g.k(n, 10); g.ap(3); ap(4) — конец",
          "what": "g.k(n, 10) — выдача (id из Q[]); точный тип REQUIRES_REAL_RUNTIME",
          "confidence": "CONFIRMED (структура/поток); тип наград REQUIRES_REAL_RUNTIME"}
    (OUT / "mission-rewards-v2.json").write_text(json.dumps(rw, indent=1, ensure_ascii=False))

    sl = {"meta": "Объект-миссия <-> скрипты", "links": [
        {"opcode": "151/160", "detail": "спавн сущностей (включая L==10?)", "status": "INFERRED"},
        {"opcode": "112/167/172", "detail": "действия над объектами-тайлами (g.c(2,...) — слой 2 = объекты)", "status": "CONFIRMED (механизм)"},
        {"opcode": "118", "detail": "размещение сущности в тайле (L 9/10/11/16 удаляются при повторном)", "status": "CONFIRMED"},
        {"opcode": "k(n,10)", "detail": "выдача наград (после завершения)", "status": "CONFIRMED"},
    ]}
    (OUT / "mission-object-script-links-v2.json").write_text(json.dumps(sl, indent=1, ensure_ascii=False))

    gl = {"meta": "Объект-миссия -> глобальное", "chain": [
        "L==10 объект (i) -> cB -> cZ() -> g.e() -> state 7 -> cd() -> награды Q[] -> ad() сохранение -> state 13/2",
        "bB: НЕ меняется объектом-миссией (инкремента нет)",
    ], "confidence": "CONFIRMED (цепочка); выбор следующей REQUIRES_REAL_RUNTIME"}
    (OUT / "mission-object-global-link-v2.json").write_text(json.dumps(gl, indent=1, ensure_ascii=False))

    card = {"meta": "Кардинальность L==10",
            "static": "в g.a(f2,...) ОДИН глобальный i (перезаписывается); несколько L==10 объектов возможны в слоях",
            "mission_count": "1 активный объект-миссия (i) на миссию (статические данные)",
            "shared_state": "cB/cy/Q[] глобальные (одни на миссию)",
            "confidence": "CONFIRMED (один i); точное число L==10 в слоях REQUIRES_REAL_RUNTIME"}
    (OUT / "mission-object-cardinality-v2.json").write_text(json.dumps(card, indent=1, ensure_ascii=False))

    cmp = {"meta": "Сравнение type 10 записей по миссиям (кандидаты L==10)", "missions": []}
    for mi in range(5):
        recs = json.load(open(f'research/analysis/v2/missions/mission_{mi:02d}/records.json'))
        t10 = [r for r in recs if r['type'] == 10]
        cmp["missions"].append({"mission": f"mission_{mi:02d}", "type10_count": len(t10),
                                "sample": t10[:3]})
    cmp["note"] = "type 10 в миссиях — объекты слоёв (тысячи); L==10 объект-миссия активируется g.a(f2,...) при старте"
    (OUT / "mission-object-mission-compare-v2.json").write_text(json.dumps(cmp, indent=1, ensure_ascii=False))

    rc = {"meta": "Race conditions",
          "order": "cZ() вызывается из B() (1162) ПОСЛЕ обновлений; cB<=0 проверяется в cw==0",
          "static": "порядок: f.b() (агро) -> ... -> cZ() — завершение после обновлений кадра",
          "races": ["cB=0 и смерть игрока одновременно", "несколько уронов за тик", "таймер cy и cB=0 одновременно"],
          "status": "REQUIRES_REAL_RUNTIME (точный порядок при совпадении)"}
    (OUT / "mission-object-race-conditions-v2.json").write_text(json.dumps(rc, indent=1, ensure_ascii=False))

    cc = {"meta": "Причинная цепочка завершения", "chain": [
        {"step": 1, "event": "cB уменьшается (f.a(8|16, n9))", "status": "CONFIRMED"},
        {"step": 2, "event": "cZ() cw==0: cB <= 0", "status": "CONFIRMED"},
        {"step": 3, "event": "g.e(): g.d(7,0)", "status": "CONFIRMED"},
        {"step": 4, "event": "state 7 cd(): b 0..4 (L() 2000ms, статистика)", "status": "CONFIRMED"},
        {"step": 5, "event": "награды Q[]: da -> db = M(da) -> k(Q[dc*2+1], 10); ap(3/4)", "status": "CONFIRMED"},
        {"step": 6, "event": "ad(bC==1?0:2) сохранение", "status": "CONFIRMED"},
        {"step": 7, "event": "state 13 (shop) или 2 (loading)", "status": "CONFIRMED (переходы)"},
    ]}
    (OUT / "mission-completion-causal-chain-v2.json").write_text(json.dumps(cc, indent=1, ensure_ascii=False))

    (OUT / "player-death-v2.md").write_text("""# Player Death V2

- HP: g[7]; урон: f.b(f2,n) (g[7] -= n + 30%*bF).
- ВОСКРЕШЕНИЕ (g.java:14998): if (g.c.g[7] <= 0) g.c.g[7] = 200 — при 0 HP игрок восстанавливается до 200.
- state 10 (GAME_OVER): существует (g.dH()); триггер REQUIRES_REAL_RUNTIME.
- Retry: state 10 -> LOADING (2) / MENU (1).
- Чекпоинты: НЕ найдены.
""")

    mt = {"meta": "Модель типа миссии",
          "finding": "все 5 миссий используют одинаковую модель L==10 (один i, cB=200, Q[] 4 пары) — единый OBJECTIVE_TYPE",
          "type": "OBJECTIVE_TYPE_A (единый)", "confidence": "CONFIRMED (структура); различия REQUIRES_REAL_RUNTIME"}
    (OUT / "mission-type-model-v2.json").write_text(json.dumps(mt, indent=1, ensure_ascii=False))

    print("записаны 15 файлов objectives/")


if __name__ == "__main__":
    sys.exit(main())
