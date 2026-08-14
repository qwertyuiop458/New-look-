#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
forensic_parse.py — воспроизводимый парсер первичных ресурсов JAR по формату,
восстановленному НЕПОСРЕДСТВЕННО из байткода (g.java: a(String) / g.a(byte[])):

  container: [count: 1B][offsets: count x uint32 LE]  (g.a(String), строки 4055-4075)
  trigger table (внутри сегментов): 2-байтовый заголовок; опкоды 11-44 с операндами
  (g.a(byte[]), строки 1682-1870)
  weapon table (m9 seg5): [tag:1B][id:2B LE][28 x u16 LE] — tag 0; ammo — tag 1 (6 x u16)

Запуск: python3 research/scripts/forensic_parse.py
Не требует сторонних библиотек.
"""
import struct
import sys
from pathlib import Path

JAR = Path("research/extracted/jar")
LEVELS = ["t0", "m0", "m1", "m2", "m3_0", "m4_0"] + \
         [f"m5_{i}" for i in range(10)] + [f"m6_{i}" for i in range(6)] + \
         ["m7", "m8", "m9", "m10", "m11_0", "m11_1", "m12", "m13_1", "m13_2"]


def read_container(path):
    data = path.read_bytes()
    if len(data) < 5:
        return data, 0, []
    cnt = data[0]
    offs = []
    if 1 + 4 * cnt > len(data):
        return data, cnt, []
    for i in range(cnt):
        offs.append(struct.unpack("<I", data[1 + 4 * i:5 + 4 * i])[0])
    return data, cnt, offs


def utf8_cyrillic_ratio(seg):
    if not seg:
        return 0.0
    try:
        txt = seg.decode("utf-8")
    except Exception:
        return 0.0
    letters = sum(1 for ch in txt if ch.isalpha())
    if not letters:
        return 0.0
    cyr = sum(1 for ch in txt if "а" <= ch.lower() <= "я")
    return cyr / letters


def parse_trigger_table(seg):
    """Повторяет первый проход g.a(byte[]) для таблицы триггеров."""
    opcodes = {}
    records = 0
    i = 0
    n = len(seg)
    # заголовок записи: 2 байта (c[n]) — значение; если 2 или 3 — +2 байта
    while i + 3 < n:
        hdr = seg[i] | (seg[i + 1] << 8)
        i += 2
        if hdr == 2 or hdr == 3:
            i += 2
        if i + 2 > n:
            break
        count = struct.unpack("<H", seg[i:i + 2])[0]
        i += 2
        records += 1
        for _ in range(count):
            if i >= n:
                break
            length = seg[i]
            i += 1
            for _ in range(length):
                if i >= n:
                    break
                op = seg[i]
                i += 1
                opcodes[op] = opcodes.get(op, 0) + 1
                size = {11: 4, 12: 4, 13: 5, 21: 4, 22: 2, 23: 4, 24: 4,
                        31: 4, 32: 2, 34: 4, 35: 6, 36: 8, 37: 2, 38: 4,
                        39: 6, 41: 4, 42: 1, 43: 4, 44: 4}.get(op, 4)
                if size == 0:
                    break
                i += size
        if i >= n:
            break
    return records, opcodes


def main():
    print("=" * 78)
    print("FORENSIC PARSE — первичные ресурсы (формат из байткода: 1B count + uint32 LE offsets)")
    print("=" * 78)
    summary = []
    for name in LEVELS:
        p = JAR / name
        if not p.exists():
            print(f"{name:8s} MISSING")
            continue
        data, cnt, offs = read_container(p)
        print(f"\n== {name}  size={len(data)}  segments={cnt}  offsets={offs[:8]}{'...' if cnt > 8 else ''}")
        texts = 0
        for i in range(cnt):
            start = offs[i]
            end = offs[i + 1] if i + 1 < cnt else len(data)
            seg = data[start:end]
            ratio = utf8_cyrillic_ratio(seg)
            head = seg[:8].hex()
            if ratio > 0.5:
                texts += 1
                kind = "TEXT"
            else:
                kind = "DATA"
            print(f"   seg {i:02d}: {start:7d}..{end:7d} ({end-start:7d} B) {kind:4s} cyr={ratio:.2f} head={head}")
        # попытка найти таблицу триггеров в каждом сегменте
        best = (0, 0, {})
        for i in range(cnt):
            start = offs[i]
            end = offs[i + 1] if i + 1 < cnt else len(data)
            recs, ops = parse_trigger_table(data[start:end])
            if recs > best[0]:
                best = (recs, i, ops)
        recs, segidx, ops = best
        if recs:
            print(f"   -> trigger-таблица: {recs} записей в seg{segidx}; опкоды: {dict(sorted(ops.items()))}")
        summary.append((name, len(data), cnt, texts, recs))
    print("\n" + "=" * 78)
    print("СВОДКА")
    print("=" * 78)
    for name, size, cnt, texts, recs in summary:
        print(f"{name:8s} size={size:7d} segs={cnt:2d} text_segs={texts} trigger_records={recs}")


if __name__ == "__main__":
    sys.exit(main())
