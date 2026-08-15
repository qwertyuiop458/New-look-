#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analyze_m8_v2.py — полное исследование m8 (этап 15.9).

Источники истины:
  - чтения m8: ТОЛЬКО g.Z(int) (g.java:13886) — найдено трассировкой всех ссылок "/m8" и a[23]
  - формат записей: [type u8][id u16 LE][x u16 LE][y u16 LE][len u8][len x u16 LE] (g.Z())
  - под-блоки: [0xC8][len u8][len байт] (g.c(int,byte[]), g.java:13736)
  - g.a[23] в g.java:3492 = СЛОТ 23 массива спрайт-листов, заполняется сценарием g.g()
    из m2 seg2 (запись {3,3,2,23,0,2}: n=3(ресурс m2), n2=23(слот), n3=2(сегмент)) — НЕ m8!

Выводы:
  research/analysis/v2/m8/load-trace.json
  research/analysis/v2/m8/seg0-records.json, seg1-records.json, seg2-records.json
  research/analysis/v2/m8/object-types.json
  research/analysis/v2/m8/mission-object-links.json
  research/analysis/v2/m8/seg345.json
  research/analysis/v2/missions/tile-resource-linkage.json
  research/analysis/v2/script-engine/opcode-context.json

Запуск: python3 research/scripts/analyze_m8_v2.py
"""
import json
import struct
import sys
from collections import Counter, defaultdict
from pathlib import Path

JAR = Path("research/extracted/jar")
OUT = Path("research/analysis/v2/m8")
MISS = Path("research/analysis/v2/missions")
SE = Path("research/analysis/v2/script-engine")


def read(p):
    d = (JAR / p).read_bytes()
    A = d[0]
    h = [struct.unpack("<I", d[1 + 4 * i:5 + 4 * i])[0] for i in range(A)]
    return d, A, h, 1 + 4 * A


def seg(d, h, base, n):
    return d[base + h[n] - h[0]:base + h[n + 1] - h[0]]


def parse_records(flow):
    """Записи [type][id u16][x u16][y u16][len u8][len x u16]; маркеры 0xC8 пропускаются."""
    recs = []
    markers = []
    n = 0
    while n < len(flow):
        t = flow[n]
        if t == 0xC8:
            ln = flow[n + 1] if n + 1 < len(flow) else 0
            markers.append({"offset": n, "len": ln,
                            "flags": list(flow[n + 2:n + 2 + ln])})
            n += 2 + ln
            continue
        if n + 8 > len(flow):
            break
        iid = struct.unpack_from("<H", flow, n + 1)[0]
        x = struct.unpack_from("<H", flow, n + 3)[0]
        y = struct.unpack_from("<H", flow, n + 5)[0]
        ln = flow[n + 7]
        if n + 8 + ln * 2 > len(flow):
            break
        props = [struct.unpack_from("<H", flow, n + 8 + 2 * j)[0] for j in range(ln)]
        recs.append({"offset": n, "type": t, "id": iid, "x": x, "y": y,
                     "len": ln, "props": props})
        n += 8 + ln * 2
    return recs, markers


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    SE.mkdir(parents=True, exist_ok=True)

    d8, A8, h8, b8 = read("m8")
    segs8 = [seg(d8, h8, b8, n) for n in range(A8 - 1)]

    # ---------- 1. load-trace.json ----------
    load_trace = {
        "note": "Все чтения m8 в первичном коде (полный grep по decompiled: '\"/m8\"' и 'a[23]').",
        "readings": [
            {
                "m8_segment": "n17 (0..5)",
                "method": "g.Z(int) (g.java:13796)",
                "line": "g.java:13886 (g.a('/m8')), 13895-13899 (g.a(n17), g.c(n17, ...))",
                "parser": "g.c(int, byte[]) (g.java:13736): построение j[seg][k] = позиции маркеров 0xC8; "
                          "вход в под-блок: n = j[n17][n18] + 2 + len(флагов); поток = [конец флагов .. j[n17][n18+1])",
                "destination": "byArrayArray[6] (временный), j[6][] (границы под-блоков)",
                "consumer": "парсер потока миссии (записи 0..26, 101..103, 110..172) в g.Z()",
                "observed_targets": "во всех 5 реальных миссиях n17 = 3 (под-блоки 0..5)",
                "status": "CONFIRMED"
            },
            {
                "m8_segment": "никакой (a[23] != m8)",
                "method": "g.java:3492: g.a[23].a[0][0]",
                "line": "g.java:3492",
                "parser": "нет — g.a[23] = СЛОТ 23 массива спрайт-листов",
                "destination": "Image (кадр 0,0 спрайт-листа слота 23)",
                "consumer": "отрисовка меню (u == 0 && n == 6)",
                "note": "СЛОТ 23 заполняется сценарием g.g() записью {3,3,2,23,0,2}: "
                       "a(int n=3, n2=23, n3=2, ...) -> ресурс a[3]='m2', сегмент 2. НЕ ресурс 23 (m8).",
                "status": "CONFIRMED (не чтение m8)"
            }
        ],
        "conclusion": "m8 открывается ТОЛЬКО в g.Z() (13886) при маркере 99; "
                      "в реальных миссиях читается только SEG3 (под-блоки 0..5); "
                      "SEG0/SEG1/SEG2 не читаются ни одним статическим путём — UNKNOWN_STATIC.",
        "seg0_1_2_consumer": "UNKNOWN_STATIC (не найден в коде; возможные потребители: "
                             "невидимые пути отсутствуют — grep по '/m8' и a[23] исчерпывающий)"
    }
    (OUT / "load-trace.json").write_text(json.dumps(load_trace, indent=1, ensure_ascii=False))

    # ---------- 2. seg0/1/2 records ----------
    for n in range(3):
        flow = segs8[n]
        recs, markers = parse_records(flow)
        data = {
            "segment": n,
            "name": f"SEG{n}",
            "size": len(flow),
            "markers_0xC8": markers,
            "records_count": len(recs),
            "type_counts": dict(sorted(Counter(r["type"] for r in recs).items())),
            "records": recs,
            "coords": {"min_x": min((r["x"] for r in recs), default=None),
                       "max_x": max((r["x"] for r in recs), default=None),
                       "min_y": min((r["y"] for r in recs), default=None),
                       "max_y": max((r["y"] for r in recs), default=None)},
        }
        (OUT / f"seg{n}-records.json").write_text(json.dumps(data, indent=1, ensure_ascii=False))
        print(f"SEG{n}: {len(recs)} записей, типы {data['type_counts']}, "
              f"coords x[{data['coords']['min_x']}..{data['coords']['max_x']}] "
              f"y[{data['coords']['min_y']}..{data['coords']['max_y']}]")

    # ---------- 3. object-types.json ----------
    type_info = {}
    for n in range(3):
        flow = segs8[n]
        recs, _ = parse_records(flow)
        for r in recs:
            t = r["type"]
            ti = type_info.setdefault(t, {"types": [], "count": 0, "lens": Counter(),
                                          "id_range": [None, None], "coords": [[None, None], [None, None]],
                                          "segments": Counter(), "sample_props": []})
            ti["count"] += 1
            ti["lens"][r["len"]] += 1
            ti["segments"][f"SEG{n}"] += 1
            if r["id"] not in ti["types"]:
                ti["types"].append(r["id"])
            if ti["id_range"][0] is None or r["id"] < ti["id_range"][0]:
                ti["id_range"][0] = r["id"]
            if ti["id_range"][1] is None or r["id"] > ti["id_range"][1]:
                ti["id_range"][1] = r["id"]
            for k, v in ((0, r["x"]), (1, r["y"])):
                if ti["coords"][k][0] is None or v < ti["coords"][k][0]:
                    ti["coords"][k][0] = v
                if ti["coords"][k][1] is None or v > ti["coords"][k][1]:
                    ti["coords"][k][1] = v
            if len(ti["sample_props"]) < 3:
                ti["sample_props"].append({"id": r["id"], "x": r["x"], "y": r["y"],
                                           "len": r["len"], "props": r["props"][:8]})
    types_out = {"note": "Классификация типов записей SEG0/SEG1/SEG2. "
                         "Семантика НЕ назначается без доказательства: "
                         "parser=Z(), consumer=UNKNOWN_STATIC (сегменты не читаются миссиями).",
                 "types": {}}
    for t in sorted(type_info):
        ti = type_info[t]
        types_out["types"][str(t)] = {
            "type": t,
            "count": ti["count"],
            "segments": dict(ti["segments"]),
            "lens": dict(ti["lens"]),
            "distinct_ids": len(ti["types"]),
            "id_range": ti["id_range"],
            "coord_x_range": ti["coords"][0],
            "coord_y_range": ti["coords"][1],
            "sample_records": ti["sample_props"],
            "known_behavior": "UNKNOWN_STATIC (parser g.Z-формат; consumer не найден)",
            "confidence": "UNKNOWN_STATIC"
        }
    (OUT / "object-types.json").write_text(json.dumps(types_out, indent=1, ensure_ascii=False))
    print("object-types.json:", len(type_info), "типов")

    # ---------- 4. seg3/4/5 ----------
    seg345 = {"note": "SEG3/SEG4/SEG5: 7 под-блоков [0xC8][0x0A][10 байт флагов]. "
                      "Миссии переключаются на SEG3 под-блоки 0..5; в Z() флаги пропускаются "
                      "(n12 += n7), записей между флагами нет -> поток под-блока пуст, "
                      "немедленный возврат в миссию. НЕ 'заглушки' — флаги существуют, но их "
                      "семантика в Z() не используется (UNKNOWN_STATIC).",
             "segments": {}}
    for n in range(3, 6):
        flow = segs8[n]
        subs = []
        i = 0
        while i < len(flow):
            if flow[i] == 0xC8:
                ln = flow[i + 1]
                subs.append({"index": len(subs), "offset": i, "len": ln,
                             "flags": list(flow[i + 2:i + 2 + ln])})
                i += 2 + ln
            else:
                i += 1
        seg345["segments"][f"SEG{n}"] = {"size": len(flow), "sub_blocks": subs,
                                         "used_by_missions": "SEG3: да (sub 0..5); SEG4/SEG5: нет"}
    (OUT / "seg345.json").write_text(json.dumps(seg345, indent=1, ensure_ascii=False))
    print("seg345.json:", {f"SEG{n}": len(seg345['segments'][f'SEG{n}']['sub_blocks']) for n in range(3, 6)})

    # ---------- 5. mission-object-links ----------
    db = json.load(open(Path("research/analysis/v2") / "missions-database.json"))
    links = {
        "note": "Связь объектов m8 с миссиями. DIRECT = объект читается в потоке миссии; "
                "NONE = не читается ни одной миссией; UNKNOWN = не установлено.",
        "SEG0": {"reference": "NONE", "detail": "340 записей не читаются ни одной из 5 миссий (все switch -> SEG3)"},
        "SEG1": {"reference": "NONE", "detail": "172 записи"},
        "SEG2": {"reference": "NONE", "detail": "64 записи"},
        "SEG3": {"reference": "DIRECT", "detail": "все 212 switch 5 миссий -> SEG3 sub 0..5; "
                                                  "под-блоки = 10-байтовые флаги, записей нет"},
        "SEG4": {"reference": "NONE"},
        "SEG5": {"reference": "NONE"},
        "shared_objects": "не применимо: SEG0/1/2 не используются миссиями",
    }
    (OUT / "mission-object-links.json").write_text(json.dumps(links, indent=1, ensure_ascii=False))

    # ---------- 6. tile-resource-linkage ----------
    tile_ids = db["totals"]["tile_ids_union"]
    obj_ids = db["totals"]["object_ids_union"]
    ents = json.load(open(Path("research/analysis/v2") / "entities.json"))
    arche = set(t["id"] for t in ents["types"])
    trl = {
        "note": "Связь mission tile_id/obj_id с ресурсами визуализации.",
        "tile_ids_union_count": len(tile_ids),
        "tile_id_range": [min(tile_ids), max(tile_ids)],
        "tile_ids_intersect_archetypes": sorted(set(tile_ids) & arche),
        "obj_ids_intersect_archetypes": sorted(set(obj_ids) & arche),
        "graphics_resource": "UNKNOWN — рендер тайлов миссии не прослежен до спрайт-пакета "
                             "(кандидаты m6_0..m6_5/m7/m3_0..m5_9 через g.g() case 2/3/9)",
        "x_y_definition": "y из data[1] маркера строки; x = порядок в фрагменте (см. tile-format.md)",
        "walkability": "data[3]==1 -> g.d[idx] (CONFIRMED, спец-парсер 16860)",
        "world_link": "тайлы миссии не привязаны к объектам SEG0/1/2 (те не читаются); "
                      "связь с SEG3-флагами: UNKNOWN",
        "status": "UNKNOWN (кроме walkability)"
    }
    (MISS / "tile-resource-linkage.json").write_text(json.dumps(trl, indent=1, ensure_ascii=False))

    # ---------- 7. opcode-context.json ----------
    ctx = {"note": "Контексты спец-опкодов 110..172+200 по всем 5 миссиям: к чему привязаны, "
                   "в каком контексте, типичные слова, соседние записи. Семантика не назначается.",
           "opcodes": {}}
    for mi in range(5):
        sp = json.loads((MISS / f"mission_{mi:02d}" / "special-records.json").read_text())
        recs = json.loads((MISS / f"mission_{mi:02d}" / "records.json").read_text())
        rec_by_off = {r["offset"]: r for r in recs}
        for s in sp:
            op = s["opcode"]
            c = ctx["opcodes"].setdefault(str(op), {"count": 0, "lens": Counter(),
                                                    "attached": Counter(), "contexts": Counter(),
                                                    "word_sample": Counter(), "sample": []})
            c["count"] += 1
            c["lens"][s["len"]] += 1
            att = "tile" if s["attached_to_tile"] else ("object" if s["attached_to_object"] else "none")
            c["attached"][att] += 1
            c["contexts"][s["context"]] += 1
            for w in s["words"][:6]:
                c["word_sample"][w] += 1
            if len(c["sample"]) < 2:
                c["sample"].append({"mission": mi, "offset": s["offset"], "len": s["len"],
                                    "words": s["words"][:8], "attached": att,
                                    "tile_index": s["tile_index"], "object_index": s["object_index"]})
    out_ctx = {"opcodes": {}}
    for op in sorted(ctx["opcodes"], key=int):
        c = ctx["opcodes"][op]
        out_ctx["opcodes"][op] = {
            "count": c["count"],
            "operand_lengths": dict(c["lens"]),
            "attached_to": dict(c["attached"]),
            "contexts": dict(c["contexts"]),
            "top_words": c["word_sample"].most_common(8),
            "samples": c["sample"],
            "status": "REQUIRES_REAL_RUNTIME (структура CONFIRMED)"
        }
    (SE / "opcode-context.json").write_text(json.dumps(out_ctx, indent=1, ensure_ascii=False))
    print("opcode-context.json:", len(out_ctx["opcodes"]), "опкодов")


if __name__ == "__main__":
    sys.exit(main())
