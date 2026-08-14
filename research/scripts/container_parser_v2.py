#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
container_parser_v2.py — воспроизводимый парсер первичных ресурсов по формату,
подтверждённому кодом (g.java: a(String)/b(int)/eZ()/dr()).

ФОРМАТ КОНТЕЙНЕРА (подтверждён g.java:4055-4075):
  [0]          1 байт  A = число сегментов
  [1 .. 4A]    A x uint32 LE  h[] — СМЕЩЕНИЯ ОТНОСИТЕЛЬНЫЕ (от конца заголовка)
  Реальное абсолютное смещение сегмента n:  abs(n) = 1 + 4*A + h[n] - h[0]
  Чтение последовательное; последний сегмент (n = A-1) НЕ читается кодом
  (g.b(int): n >= A-1 -> null).

ТАБЛИЦА СУЩНОСТЕЙ (m9 seg4, loader g.dr() g.java:24553):
  tag 6  -> entity archetype: [id u16][32 x u16 props] (67 B)
  tag 7  -> animation record: [10 x u16] (21 B, без id)
  tag 8  -> X record: [2 x u16] (5 B)
  tag 9  -> Y record: [2 x u16] (5 B)
  tag 10 -> frame record: [15 x u16] (31 B)

ТАБЛИЦА ОРУЖИЯ (m9 seg5, loader g.eZ() g.java:31831):
  tag 0 -> weapon: [id u16][28 x u16 props] (59 B)
  tag 1 -> ammo:   [id u16][6 x u16 props]  (15 B)

Вывод: research/analysis/v2/{weapons,entities}.json + печать инвентаря.
Запуск: python3 research/scripts/container_parser_v2.py
"""
import json
import struct
import sys
from pathlib import Path

JAR = Path("research/extracted/jar")
V2 = Path("research/analysis/v2")
FILES = ["t0"] + ["m0", "m1", "m2", "m3_0", "m4_0"] + \
        [f"m5_{i}" for i in range(10)] + [f"m6_{i}" for i in range(6)] + \
        ["m7", "m8", "m9", "m10", "m11_0", "m11_1", "m12", "m13_1", "m13_2"]


def parse_container(data):
    """Возвращает (A, h, base, segs) где segs[n] = (abs_start, abs_end, size)."""
    A = data[0]
    h = [struct.unpack("<I", data[1 + 4 * i:5 + 4 * i])[0] for i in range(A)]
    base = 1 + 4 * A
    segs = []
    for n in range(A):
        if n + 1 >= A:
            segs.append(None)  # unreachable (n >= A-1 -> g.b возвращает null)
        else:
            s = base + h[n] - h[0]
            e = base + h[n + 1] - h[0]
            segs.append((s, e, e - s))
    return A, h, base, segs


def u16(data, off):
    return struct.unpack_from("<H", data, off)[0]


def parse_entity_table(seg):
    """dr() формат. Возвращает dict с записями."""
    strides = {6: 67, 7: 21, 8: 5, 9: 5, 10: 31}
    out = {"types": [], "anims": [], "frames": [], "x": [], "y": []}
    i = 0
    while i < len(seg):
        t = seg[i]
        if t not in strides:
            i += 1
            continue
        if t == 6:
            iid = u16(seg, i + 1)
            props = [u16(seg, i + 3 + 2 * j) for j in range(32)]
            out["types"].append({"id": iid, "props": props})
        elif t == 7:
            vals = [u16(seg, i + 1 + 2 * j) for j in range(10)]
            out["anims"].append(vals)
        elif t == 10:
            vals = [u16(seg, i + 1 + 2 * j) for j in range(15)]
            out["frames"].append(vals)
        else:
            vals = [u16(seg, i + 1 + 2 * j) for j in range(2)]
            out["x" if t == 8 else "y"].append(vals)
        i += strides[t]
    return out


def parse_weapon_table(seg):
    """eZ() формат."""
    out = {"weapons": [], "ammo": []}
    i = 0
    while i < len(seg) - 2:
        t = seg[i]
        iid = u16(seg, i + 1)
        if t == 0 and i + 59 <= len(seg):
            props = [u16(seg, i + 3 + 2 * j) for j in range(28)]
            out["weapons"].append({"id": iid, "props": props})
            i += 59
        elif t == 1 and i + 15 <= len(seg):
            props = [u16(seg, i + 3 + 2 * j) for j in range(6)]
            out["ammo"].append({"id": iid, "props": props})
            i += 15
        else:
            i += 3
    return out


def main():
    V2.mkdir(parents=True, exist_ok=True)
    print("=" * 78)
    print("CONTAINER PARSER V2 — формат из кода (1B count + u32 LE REL offsets)")
    print("=" * 78)
    inventory = {}
    for name in FILES:
        p = JAR / name
        if not p.exists():
            inventory[name] = {"exists": False}
            continue
        data = p.read_bytes()
        A, h, base, segs = parse_container(data)
        seg_info = []
        for n, s in enumerate(segs):
            if s is None:
                seg_info.append({"n": n, "state": "UNREACHABLE"})
            else:
                seg_info.append({"n": n, "start": s[0], "end": s[1], "size": s[2]})
        inventory[name] = {"size": len(data), "segments": A, "base": base,
                           "offsets": h, "segs": seg_info}
        print(f"{name:8s} size={len(data):7d} A={A:2d} base={base:4d} readable={A-1}")
    (V2 / "container-inventory.json").write_text(
        json.dumps(inventory, indent=1, ensure_ascii=False), encoding="utf-8")

    # m9: entity table (seg4) + weapon table (seg5)
    m9 = (JAR / "m9").read_bytes()
    A, h, base, segs = parse_container(m9)
    seg4 = m9[segs[4][0]:segs[4][1]]
    seg5 = m9[segs[5][0]:segs[5][1]]

    ents = parse_entity_table(seg4)
    ent_out = {
        "source": "m9 seg4 (g.dr() loader, g.java:24553)",
        "container_format": "tag 6: [id u16][32 u16 props]",
        "counts": {k: len(v) for k, v in ents.items()},
        "types": ents["types"],
        "anims_count": len(ents["anims"]),
        "frames_count": len(ents["frames"]),
        "x_count": len(ents["x"]),
        "y_count": len(ents["y"]),
        "note": "props: 32 из файла + 3 поля добавляются кодом (35 всего): "
                "U[32]=индекс начала анимаций, U[33]=счётчик анимаций, U[34]=кол-во кадров",
        "anims": ents["anims"],
        "frames": ents["frames"],
        "x": ents["x"],
        "y": ents["y"],
    }
    (V2 / "entities.json").write_text(
        json.dumps(ent_out, indent=1, ensure_ascii=False), encoding="utf-8")

    wpn = parse_weapon_table(seg5)
    wout = {
        "source": "m9 seg5 (g.eZ() loader, g.java:31831); g.E() = an.length/28",
        "weapon_count": len(wpn["weapons"]),
        "weapon_ids": sorted(w["id"] for w in wpn["weapons"]),
        "weapons": wpn["weapons"],
        "ammo_count": len(wpn["ammo"]),
        "ammo_ids": sorted(a["id"] for a in wpn["ammo"]),
        "ammo": wpn["ammo"],
        "known_props_from_code": {
            "prop4": "число лучей/выстрелов за один заход (f.java:3379 g.l(n,4))",
            "prop5": "базовый урон (g.java:21382 l(n)=l(n,5)+rand(l(n,6)))",
            "prop6": "случайный разброс урона 0..prop6-1 (g.java:21382)",
            "prop13": "ёмкость магазина (f.java:6529 сравнение g[13+i] < l(weapon,13))",
            "prop18": "идентификатор/ссылка оружия (g.java:6606 f.a(g.l(n3,18)))",
            "prop21": "идентификатор звука (f.java:441/8272 g.l(weapon,21))",
            "prop25": "используется в стрельбе (f.java:3777 g.l(g.L[1],25))"
        },
        "confidence": "поля 4,5,6,13,18,21,25 — из кода; остальные — сырые значения, семантика REQUIRES_RUNTIME",
    }
    (V2 / "weapons.json").write_text(
        json.dumps(wout, indent=1, ensure_ascii=False), encoding="utf-8")

    print("\nentities.json:",
          {k: len(v) for k, v in ents.items()})
    print("weapons.json: weapons =", len(wpn["weapons"]),
          "ids =", sorted(w["id"] for w in wpn["weapons"]),
          "| ammo =", len(wpn["ammo"]),
          "ids =", sorted(a["id"] for a in wpn["ammo"]))
    print("Written to research/analysis/v2/")


if __name__ == "__main__":
    sys.exit(main())
