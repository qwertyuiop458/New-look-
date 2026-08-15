#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parse_reference_level_v2.py — восстановление формата НАСТОЯЩЕГО level package.

ПОДТВЕРЖДЕНО кодом (g.java):
  - g.Z(int n) (строка 13796) = загрузчик миссии:
      a("/m9") -> C(n) по seg0 (таблица длин) -> миссия = m9 seg(10+C(n))
      -> маркеры 99 переключают поток на m8 seg n17 (под-блок n18, границы j[][] из g.c())
  - g.c(int,byte[]) (13736) = парсер m8-сегмента: маркеры 0xC8 делят на под-блоки
  - g.a(byte[],int,int[],int,boolean,int) (16742) / (...,int[][][],int) (16860) =
      спец-парсер записей типов >=101 (101=тайловая ячейка, 102=объект, 103=данные, >=110=спец)
  - Формат обычной записи: [type u8][id u16 LE][x u16 LE][y u16 LE][len u8][len x u16 LE]

Выводы:
  research/analysis/v2/levels/reference-level/segments.json
  research/analysis/v2/levels/reference-level/mission-0.json
  research/analysis/v2/levels/reference-level/entity-links-v2.json
  research/analysis/v2/levels/reference-level/opcode-table-v2.json
  research/analysis/v2/levels/reference-level/level-spec-v2.json

Запуск: python3 research/scripts/parse_reference_level_v2.py
"""
import hashlib
import json
import struct
import sys
from collections import Counter
from pathlib import Path

JAR = Path("research/extracted/jar")
OUT = Path("research/analysis/v2/levels/reference-level")


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


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def parse_flow(data, n, end, out, cur, cnt):
    """Поток записей миссии (по Z() + спец-парсеру)."""
    while n < end:
        t = data[n]
        if t == 99:
            if n + 4 >= end:
                break
            n17, n18 = data[n + 1], data[n + 2]
            n += 4
            gi = struct.unpack_from("<H", data, n)[0] if n + 2 <= end else 0
            n += 2
            out.append({"kind": "switch", "m8_segment": n17, "sub_block": n18,
                        "value": gi, "offset": n - 6, "context": cur})
            return n, (n17, n18)
        if t >= 101:
            n = parse_special(data, n, out, cur, cnt)
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
        out.append({"kind": "record", "type": t, "id": iid, "x": x, "y": y,
                    "len": ln, "props": props, "offset": n, "context": cur})
        n += 8 + ln * 2
    return n, None


def parse_special(data, n, out, cur, cnt):
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
        y = blob[1] if len(blob) > 1 else -1
        val = blob[2] if len(blob) > 2 else -1
        out.append({"kind": "tile_cell", "tile_id": var11, "y": y, "value": val,
                    "flags": list(blob), "offset": n - 4, "context": cur})
        cnt["t101"] += 1
        n += ln
    elif t == 102:
        out.append({"kind": "object", "obj_id": var11, "len": ln,
                    "offset": n - 4, "context": cur})
        cnt["t102"] += 1
    elif t == 103:
        out.append({"kind": "data_bytes", "len": ln, "bytes": list(data[n:n + ln]),
                    "offset": n - 3, "context": cur})
        cnt["t103"] += 1
        n += ln
    elif t >= 110:
        out.append({"kind": "special", "opcode": t, "len": ln,
                    "words": [struct.unpack_from("<H", data, n + 2 * j)[0]
                              for j in range(ln)] if n + ln * 2 <= len(data) else [],
                    "offset": n - 2, "context": cur})
        cnt["spec"] += 1
        n += ln * 2
    else:  # 104..109 — терминатор/стоп
        out.append({"kind": "special_term", "opcode": t, "offset": n - 2, "context": cur})
    return n


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    # ---------- m8: сегменты + sha256 ----------
    d8, A8, h8, b8 = read("m8")
    m8_segs = []
    for n in range(A8 - 1):
        s = seg(d8, h8, b8, n)
        m8_segs.append({"segment": n, "start": b8 + h8[n] - h8[0],
                        "end": b8 + h8[n + 1] - h8[0], "size": len(s),
                        "sha256": sha256(s),
                        "sub_blocks": len(chunk_positions(s))})
    # ---------- m9: миссии ----------
    d9, A9, h9, b9 = read("m9")
    table = seg(d9, h9, b9, 0)
    cum = 0
    missions = []
    for i, ln in enumerate(table):
        missions.append(10 + cum)
        cum += ln
    m9_segs = []
    for n in range(A9 - 1):
        s = seg(d9, h9, b9, n)
        role = "mission" if n in missions else \
            ("global_data" if n in (1, 2, 4, 5, 7, 8, 9) else "binary_block")
        m9_segs.append({"segment": n, "start": b9 + h9[n] - h9[0],
                        "end": b9 + h9[n + 1] - h9[0], "size": len(s),
                        "sha256": sha256(s), "role": role})

    segments_out = {
        "reference_level": "m8 (объектные слои мира) + m9 seg10-14 (миссии)",
        "m8": {"file": "research/extracted/jar/m8", "segments": m8_segs},
        "m9": {"file": "research/extracted/jar/m9", "segments": m9_segs,
               "mission_segments": missions},
        "container_format": "1B count + A x u32 LE rel offsets; abs(n) = 1+4A+h[n]-h[0]",
    }
    (OUT / "segments.json").write_text(
        json.dumps(segments_out, indent=1, ensure_ascii=False), encoding="utf-8")

    # ---------- миссия 0 (seg10) ----------
    mission = seg(d9, h9, b9, missions[0])
    J = {n: chunk_positions(seg(d8, h8, b8, n)) for n in range(6)}
    segs8 = [seg(d8, h8, b8, n) for n in range(6)]
    out = []
    cnt = {"t101": 0, "t102": 0, "t103": 0, "spec": 0}
    header = {"n16": mission[0], "F0": mission[1], "bz": mission[2],
              "cb": mission[3], "bD": mission[4], "bt": mission[5]}
    stack = []
    flow = mission
    n = 6
    cur = "mission"
    while True:
        n2, sw = parse_flow(flow, n, len(flow), out, cur, cnt)
        if sw is not None and sw[0] < 6 and sw[1] < len(J[sw[0]]):
            stack.append((flow, n2, len(flow)))
            flow = segs8[sw[0]]
            n = J[sw[0]][sw[1]] + 2 + segs8[sw[0]][J[sw[0]][sw[1]] + 1]
            cur = f"m8.s{sw[0]}.b{sw[1]}"
            continue
        if stack:
            flow, n, _ = stack.pop()
            cur = "mission"
            continue
        break

    types = Counter(r["type"] for r in out if r["kind"] == "record")
    spec = Counter(r["opcode"] for r in out if r["kind"] == "special")
    mission_out = {
        "mission": 0,
        "source": "m9 seg10",
        "header": header,
        "counts": {"records": sum(types.values()), "tile_cells": cnt["t101"],
                   "objects": cnt["t102"], "data_bytes": cnt["t103"],
                   "special": cnt["spec"], "switches": sum(1 for r in out if r["kind"] == "switch")},
        "record_types": dict(sorted(types.items())),
        "special_opcodes": dict(sorted(spec.items())),
        "records": out,
    }
    (OUT / "mission-0.json").write_text(
        json.dumps(mission_out, indent=1, ensure_ascii=False), encoding="utf-8")

    print("segments.json, mission-0.json записаны")
    print("миссии (m9 seg):", missions)
    print("mission-0 counts:", mission_out["counts"])


if __name__ == "__main__":
    sys.exit(main())
