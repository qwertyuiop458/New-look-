#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
process_all_missions_v2.py — полная реконструкция всех реальных миссий (этап 15.8).

Источники истины (только V2):
  - container header: g.java a(String)/b(int) (см. container-header-final.md)
  - loader миссий: g.Z(int) (g.java:13796), парсеры 16742/16860
  - m9: seg0 = таблица миссий [1,1,1,1,1]; seg1/2 = startup; seg4 = сущности; seg5 = оружие;
        seg10..14 = миссии 0..4
  - m8: seg0..2 = объектные слои мира; seg3..5 = слои-заглушки (7 под-блоков флагов по 10 Б)

Формат записи: [type u8][id u16 LE][x u16 LE][y u16 LE][len u8][len x u16 LE]
Маркер 99: [99][seg u8][sub u8][1 байт][u16] — переключение потока на m8 seg.sub
Спец-записи: 101 = тайловая ячейка, 102 = объект, 103 = данные, 110..172 = скрипты,
             104..109 = терминатор спец-парсера

Вывод: research/analysis/v2/missions/mission_0X/{segments,records,tiles,objects,data,
       special-records,mission-spec}.json + analysis.md,
       research/analysis/v2/missions/world-objects.json,
       research/analysis/v2/missions/mission-world-map.json,
       research/analysis/v2/script-engine/opcode-table-complete.json,
       research/analysis/v2/missions-database.json
Запуск: python3 research/scripts/process_all_missions_v2.py
"""
import hashlib
import json
import struct
import sys
from collections import Counter, defaultdict
from pathlib import Path

JAR = Path("research/extracted/jar")
OUT = Path("research/analysis/v2/missions")
SE = Path("research/analysis/v2/script-engine")


def read(p):
    d = (JAR / p).read_bytes()
    A = d[0]
    h = [struct.unpack("<I", d[1 + 4 * i:5 + 4 * i])[0] for i in range(A)]
    return d, A, h, 1 + 4 * A


def seg(d, h, base, n):
    return d[base + h[n] - h[0]:base + h[n + 1] - h[0]]


def chunk_positions(s):
    pos = []
    i = 0
    while i < len(s):
        if s[i] == 0xC8:
            pos.append(i)
            ln = s[i + 1] if i + 1 < len(s) else 0
            i += 2 + ln
        else:
            i += 1
    return pos


def sha(b):
    return hashlib.sha256(b).hexdigest()


class MissionParser:
    """Парсер потока миссии по g.Z() + спец-парсерам (16742/16860)."""

    def __init__(self, mission_bytes, segs8, J):
        self.mission = mission_bytes
        self.segs8 = segs8
        self.J = J
        self.records = []
        self.tiles = []
        self.objects = []
        self.datas = []
        self.specials = []
        self.switches = []
        self.header = None
        self.row_start = {}   # y -> глобальный индекс первой ячейки строки
        self.cur_y = None
        self.last_tile_idx = None
        self.last_obj_idx = None
        self.attach_tile = False
        self.attach_obj = False

    def parse(self):
        m = self.mission
        self.header = {"n16": m[0], "F0": m[1], "bz": m[2], "cb": m[3], "bD": m[4], "bt": m[5]}
        stack = []
        flow = m
        n = 6
        cur = "mission"
        while True:
            n = self.parse_flow(flow, n, len(flow), cur)
            # переход в m8-под-блок
            if self._pending_switch is not None:
                n17, n18 = self._pending_switch
                self._pending_switch = None
                if n17 < len(self.segs8) and n18 < len(self.J[n17]):
                    stack.append((flow, n, len(flow)))
                    s8 = self.segs8[n17]
                    flow = s8
                    n = self.J[n17][n18] + 2 + s8[self.J[n17][n18] + 1]
                    cur = f"m8.s{n17}.b{n18}"
                    continue
            if stack:
                flow, n, _ = stack.pop()
                cur = "mission"
                continue
            break
        return self

    def parse_flow(self, data, n, end, cur):
        while n < end:
            t = data[n]
            if t == 99:
                if n + 4 >= end:
                    break
                n17, n18 = data[n + 1], data[n + 2]
                n += 4
                gi = struct.unpack_from("<H", data, n)[0] if n + 2 <= end else 0
                n += 2
                self.switches.append({"m8_segment": n17, "sub_block": n18,
                                      "value": gi, "offset": n - 6, "context": cur})
                self._pending_switch = (n17, n18)
                return n
            if t >= 101:
                n = self.parse_special(data, n, cur)
                continue
            if n + 8 > end:
                break
            iid = struct.unpack_from("<H", data, n + 1)[0]
            x = struct.unpack_from("<H", data, n + 3)[0]
            y = struct.unpack_from("<H", data, n + 5)[0]
            ln = data[n + 7]
            if n + 8 + ln * 2 > end:
                break
            props = [struct.unpack_from("<H", data, n + 8 + 2 * j)[0] for j in range(ln)]
            self.records.append({"offset": n, "type": t, "id": iid, "x": x, "y": y,
                                 "len": ln, "props": props, "context": cur})
            n += 8 + ln * 2
        return n

    def parse_special(self, data, n, cur):
        t = data[n]
        n += 1
        var11 = 0
        if t in (101, 102):
            var11 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
            n += 2
        if n >= len(data):
            return n
        ln = data[n]
        n += 1
        if t == 101:
            blob = data[n:n + ln]
            idx = len(self.tiles)
            y = blob[1] if len(blob) > 1 else None
            if len(blob) > 0 and blob[0] == 1 and y is not None:
                self.row_start[y] = idx
                self.cur_y = y
            x = None
            if self.cur_y is not None and self.cur_y in self.row_start:
                x = idx - self.row_start[self.cur_y]
            walk = len(blob) > 3 and blob[3] == 1
            self.tiles.append({"index": idx, "tile_id": var11, "y": self.cur_y,
                               "x_in_row": x, "value": blob[2] if len(blob) > 2 else None,
                               "walkable": walk, "flags": list(blob),
                               "offset": n - 4, "context": cur,
                               "special_start": len(self.specials)})
            self.last_tile_idx = idx
            self.attach_tile = True
            self.attach_obj = False
            n += ln
        elif t == 102:
            idx = len(self.objects)
            self.objects.append({"index": idx, "obj_id": var11, "len": ln,
                                 "offset": n - 4, "context": cur,
                                 "special_start": len(self.specials)})
            self.last_obj_idx = idx
            self.attach_obj = True
            self.attach_tile = False
            # len байт НЕ читаются кодом (case 102: continue без сдвига)
        elif t == 103:
            self.datas.append({"index": len(self.datas), "len": ln,
                               "bytes": list(data[n:n + ln]), "offset": n - 3,
                               "context": cur})
            n += ln
        elif t >= 110:
            words = [struct.unpack_from("<H", data, n + 2 * j)[0] for j in range(ln)] \
                if n + ln * 2 <= len(data) else []
            self.specials.append({"index": len(self.specials), "opcode": t, "len": ln,
                                  "words": words, "offset": n - 2, "context": cur,
                                  "attached_to_tile": self.attach_tile,
                                  "attached_to_object": self.attach_obj,
                                  "tile_index": self.last_tile_idx,
                                  "object_index": self.last_obj_idx})
            n += ln * 2
        else:  # 104..109: терминатор
            self.specials.append({"index": len(self.specials), "opcode": t, "len": 0,
                                  "words": [], "offset": n - 2, "context": cur,
                                  "attached_to_tile": False, "attached_to_object": False,
                                  "tile_index": None, "object_index": None})
        return n


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    SE.mkdir(parents=True, exist_ok=True)

    d8, A8, h8, b8 = read("m8")
    d9, A9, h9, b9 = read("m9")

    segs8 = [seg(d8, h8, b8, n) for n in range(A8 - 1)]
    J = {n: chunk_positions(segs8[n]) for n in range(len(segs8))}

    table = seg(d9, h9, b9, 0)
    cum = 0
    mission_segs = []
    for i, ln in enumerate(table):
        mission_segs.append(10 + cum)
        cum += ln
    assert mission_segs == [10, 11, 12, 13, 14]

    db = {"missions": []}
    all_specials = Counter()
    all_types = Counter()
    all_tiles = Counter()
    all_objects = Counter()
    all_switches = Counter()

    for mi, mseg in enumerate(mission_segs):
        mid = f"mission_{mi:02d}"
        mdir = OUT / mid
        mdir.mkdir(parents=True, exist_ok=True)
        mbytes = seg(d9, h9, b9, mseg)
        parser = MissionParser(mbytes, segs8, J).parse()

        # segments.json
        segs_json = {
            "mission": mid,
            "source": f"m9 seg{mseg}",
            "container": {"file": "m9", "segment": mseg,
                          "start": b9 + h9[mseg] - h9[0],
                          "end": b9 + h9[mseg + 1] - h9[0],
                          "size": len(mbytes), "sha256": sha(mbytes)},
            "m8_used_segments": sorted({sw["m8_segment"] for sw in parser.switches}),
        }
        (mdir / "segments.json").write_text(json.dumps(segs_json, indent=1, ensure_ascii=False))

        # records / tiles / objects / data / specials
        (mdir / "records.json").write_text(json.dumps(parser.records, indent=1, ensure_ascii=False))
        (mdir / "tiles.json").write_text(json.dumps(parser.tiles, indent=1, ensure_ascii=False))
        (mdir / "objects.json").write_text(json.dumps(parser.objects, indent=1, ensure_ascii=False))
        (mdir / "data.json").write_text(json.dumps(parser.datas, indent=1, ensure_ascii=False))
        (mdir / "special-records.json").write_text(json.dumps(parser.specials, indent=1, ensure_ascii=False))

        # mission-spec.json
        rtypes = Counter(r["type"] for r in parser.records)
        spec = {
            "id": mid,
            "source": f"m9 seg{mseg}",
            "header": parser.header,
            "counts": {
                "records": len(parser.records),
                "tile_cells_101": len(parser.tiles),
                "objects_102": len(parser.objects),
                "data_103": len(parser.datas),
                "special_110_172": len([s for s in parser.specials if s["opcode"] >= 110]),
                "switches_99": len(parser.switches),
            },
            "record_types": dict(sorted(rtypes.items())),
            "special_opcodes": dict(sorted(Counter(s["opcode"] for s in parser.specials).items())),
            "m8_segments_used": sorted({sw["m8_segment"] for sw in parser.switches}),
            "sub_blocks_used": sorted({(sw["m8_segment"], sw["sub_block"]) for sw in parser.switches}),
            "rows": {str(k): v for k, v in sorted(parser.row_start.items())},
        }
        (mdir / "mission-spec.json").write_text(json.dumps(spec, indent=1, ensure_ascii=False))

        # analysis.md (авто)
        rows_info = []
        for y, start in sorted(parser.row_start.items()):
            count = sum(1 for t in parser.tiles if t["y"] == y)
            rows_info.append(f"y={y}: start_idx={start}, cells={count}")
        lines = [
            f"# {mid} — analysis (авто-генерация, этап 15.8)",
            "",
            f"**Источник:** m9 seg{mseg} ({len(mbytes)} Б, sha256 {sha(mbytes)[:16]}…)",
            f"**Header:** {json.dumps(parser.header, ensure_ascii=False)}",
            "",
            "## Счётчики",
            f"- records: {len(parser.records)}",
            f"- tile cells (101): {len(parser.tiles)}",
            f"- objects (102): {len(parser.objects)}",
            f"- data (103): {len(parser.datas)}",
            f"- special (110–172): {len([s for s in parser.specials if s['opcode'] >= 110])}",
            f"- switches (99 → m8): {len(parser.switches)}",
            "",
            "## Типы записей",
            "| type | count |",
            "| :-: | :-: |",
        ] + [f"| {t} | {c} |" for t, c in sorted(rtypes.items())] + [
            "",
            "## Спец-опкоды",
            "| opcode | count |",
            "| :-: | :-: |",
        ] + [f"| {t} | {c} |" for t, c in sorted(Counter(s['opcode'] for s in parser.specials).items())] + [
            "",
            "## Строки тайлов (y → start, cells)",
        ] + [f"- {r}" for r in rows_info] + [
            "",
            "## Переключения на m8",
        ] + [f"- seg {sw['m8_segment']} sub {sw['sub_block']} (value={sw['value']})" for sw in parser.switches[:40]] + [
            "",
            "## UNKNOWN",
            "- семантика спец-записей 110–172 — REQUIRES_REAL_RUNTIME",
            "- точная полная сетка x/y тайлов (строки восстановлены, полный мир — runtime)",
            "- назначение data (103) — UNKNOWN",
            "- completion condition — REQUIRES_REAL_RUNTIME",
        ]
        (mdir / "analysis.md").write_text("\n".join(lines), encoding="utf-8")

        all_specials.update(s["opcode"] for s in parser.specials)
        all_types.update(r["type"] for r in parser.records)
        all_tiles.update(t["tile_id"] for t in parser.tiles)
        all_objects.update(o["obj_id"] for o in parser.objects)
        all_switches.update((sw["m8_segment"], sw["sub_block"]) for sw in parser.switches)

        db["missions"].append({
            "id": mid,
            "source_segment": mseg,
            "counts": spec["counts"],
            "rows": spec["rows"],
            "m8_used": spec["m8_segments_used"],
            "sub_blocks": spec["sub_blocks_used"],
        })
        print(f"{mid}: seg{mseg} records={len(parser.records)} tiles={len(parser.tiles)} "
              f"objects={len(parser.objects)} data={len(parser.datas)} "
              f"special={spec['counts']['special_110_172']} switches={len(parser.switches)}")

    # ---------- world-objects.json (m8 seg0..2) ----------
    world = {"segments": {}}
    for n in range(3):
        recs = []
        p = MissionParser.__new__(MissionParser)  # лёгкий разбор без миссии
        flow = segs8[n]
        pos = 0
        i = 0
        while i < len(flow):
            t = flow[i]
            if t == 0xC8:
                ln = flow[i + 1] if i + 1 < len(flow) else 0
                i += 2 + ln
                continue
            if i + 8 > len(flow):
                break
            iid = struct.unpack_from("<H", flow, i + 1)[0]
            x = struct.unpack_from("<H", flow, i + 3)[0]
            y = struct.unpack_from("<H", flow, i + 5)[0]
            ln = flow[i + 7]
            if i + 8 + ln * 2 > len(flow):
                break
            props = [struct.unpack_from("<H", flow, i + 8 + 2 * j)[0] for j in range(ln)]
            recs.append({"offset": i, "type": t, "id": iid, "x": x, "y": y,
                         "len": ln, "props": props})
            i += 8 + ln * 2
        world["segments"][f"seg{n}"] = {
            "size": len(flow), "records": recs,
            "type_counts": dict(sorted(Counter(r["type"] for r in recs).items()))
        }
    (OUT / "world-objects.json").write_text(json.dumps(world, indent=1, ensure_ascii=False))

    # ---------- mission-world-map.json ----------
    mwm = {"missions": {}}
    for mi, mseg in enumerate(mission_segs):
        mid = f"mission_{mi:02d}"
        mdir = OUT / mid
        spec = json.loads((mdir / "mission-spec.json").read_text())
        sws = json.loads((mdir / "segments.json").read_text())
        switches = [s for s in json.loads((mdir / "special-records.json").read_text()) if False] or \
                   json.loads((mdir / "records.json").read_text())
        mwm["missions"][mid] = {
            "source": f"m9 seg{mseg}",
            "m8_segments_used": spec["m8_segments_used"],
            "sub_blocks": spec["sub_blocks_used"],
            "note": "каждый switch [99][seg][sub] = вход в объектный слой m8 seg.sub; "
                    "после исчерпания под-блока поток возвращается в миссию",
        }
    (OUT / "mission-world-map.json").write_text(json.dumps(mwm, indent=1, ensure_ascii=False))

    # ---------- opcode-table-complete.json ----------
    spec_op = defaultdict(lambda: {"count": 0, "lens": Counter(), "attached_to_tile": 0,
                                   "attached_to_object": 0, "contexts": Counter(),
                                   "word_stats": defaultdict(Counter)})
    for mi, mseg in enumerate(mission_segs):
        mdir = OUT / f"mission_{mi:02d}"
        for s in json.loads((mdir / "special-records.json").read_text()):
            op = s["opcode"]
            spec_op[op]["count"] += 1
            spec_op[op]["lens"][s["len"]] += 1
            if s["attached_to_tile"]:
                spec_op[op]["attached_to_tile"] += 1
            if s["attached_to_object"]:
                spec_op[op]["attached_to_object"] += 1
            spec_op[op]["contexts"][s["context"]] += 1
            for w in s["words"][:8]:
                spec_op[op]["word_stats"][s["len"]][w] += 1
    table = {"note": "Полная таблица спец-опкодов 110..172 по всем 5 миссиям. "
                     "Семантика: REQUIRES_REAL_RUNTIME (структура привязки CONFIRMED).",
             "parser": "g.java:16860 (case >=110): [op u8][len u8][len x u16] -> g.z[]; "
                       "привязка к последнему тайлу (101, g.A++) или объекту (102, g.y-секция)",
             "opcodes": []}
    for op in sorted(spec_op):
        st = spec_op[op]
        table["opcodes"].append({
            "opcode": op,
            "count": st["count"],
            "operand_lengths": dict(st["lens"]),
            "attached_to_tile": st["attached_to_tile"],
            "attached_to_object": st["attached_to_object"],
            "contexts": dict(st["contexts"]),
            "sample_words": {str(k): v.most_common(5) for k, v in st["word_stats"].items()},
            "status": "REQUIRES_REAL_RUNTIME",
        })
    (SE / "opcode-table-complete.json").write_text(json.dumps(table, indent=1, ensure_ascii=False))

    # ---------- missions-database.json ----------
    dbase = {
        "note": "Reference database всех 5 реальных миссий (этап 15.8). "
                "Старые '30 уровней' и 'm3_0 level' — опровергнуты (см. reference-level-v1-v2-diff.md).",
        "container_header": "1B count + A x u32 LE rel offsets; abs(n)=1+4A+h[n]-h[0] (CONFIRMED, container-header-final.md)",
        "missions": db["missions"],
        "totals": {
            "special_by_opcode": dict(sorted(all_specials.items())),
            "record_types": dict(sorted(all_types.items())),
            "tile_ids_union": sorted(all_tiles),
            "object_ids_union": sorted(all_objects),
            "switch_targets": {f"{k[0]}.{k[1]}": v for k, v in sorted(all_switches.items())},
        }
    }
    (Path("research/analysis/v2") / "missions-database.json").write_text(
        json.dumps(dbase, indent=1, ensure_ascii=False))

    print("\nИтог:")
    print("  спец-опкоды (union):", len(all_specials), sorted(all_specials))
    print("  tile_ids union:", len(all_tiles))
    print("  obj_ids union:", len(all_objects))
    print("  switch targets:", dict(all_switches))


if __name__ == "__main__":
    sys.exit(main())
