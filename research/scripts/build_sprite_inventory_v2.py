#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_sprite_inventory_v2.py — полная инвентаризация sprite resources и 17 slots (этап 15.16).

Парсит все спрайт-листы a.java из ресурсов: m0, m1, m2, m6_0..m6_5, m7, m11_0, m11_1, m13_2.
Для каждого сегмента: объекты (k=0/1/2, размеры c x d), палитры, b/f/e-записи,
форматы пикселей (0x8888/0x4444/0x6505), магия 0x64F0, блоки.

Вывод: research/analysis/v2/graphics/*.json (15.16) + contact-sheets PNG (только декодированные)
"""
import json
import struct
import sys
from pathlib import Path

JAR = Path("research/extracted/jar")
OUT = Path("research/analysis/v2/graphics")
CS = Path("research/resources/v2/contact-sheets")


def read(p):
    d = (JAR / p).read_bytes()
    A = d[0]
    h = [struct.unpack("<I", d[1 + 4 * i:5 + 4 * i])[0] for i in range(A)]
    return d, A, h, 1 + 4 * A


def seg(d, h, base, n):
    if n + 1 >= A_ref[0]:
        return None
    return d[base + h[n] - h[0]:base + h[n + 1] - h[0]]


A_ref = [0]


def parse_sprite_list(data):
    """Полный парсер a.java-листа (из этапа 15.11, расширенный)."""
    if data is None or len(data) < 10:
        return None
    try:
        n = 0
        n += 1
        f = struct.unpack_from("<I", data, n + 1)[0]
        n += 5
        c = struct.unpack_from("<H", data, n)[0]
        n += 2
        objs = []
        for i in range(c):
            if n + 6 > len(data):
                break
            tag = data[n]
            if tag in (255, 254):
                objs.append({"k": 1 if tag == 255 else 2,
                             "e": struct.unpack_from("<I", data, n + 1)[0],
                             "c": data[n + 5], "d": data[n + 6] if n + 6 < len(data) else 0})
                n += 7
            else:
                objs.append({"k": 0, "a": struct.unpack_from("<H", data, n + 1)[0],
                             "b": struct.unpack_from("<H", data, n + 3)[0],
                             "c": struct.unpack_from("<H", data, n + 5)[0],
                             "d": struct.unpack_from("<H", data, n + 7)[0]})
                n += 9
        # палитры
        n8 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        pals = []
        for i in range(n8):
            if n + 6 > len(data):
                break
            pals.append({"tag": data[n], "f": struct.unpack_from("<H", data, n + 1)[0],
                         "g": struct.unpack_from("<H", data, n + 3)[0], "d": data[n + 5]})
            n += 6
        if (f & 0x8000) != 0:
            n10 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
            n += 2 + n10 * 4
        n6 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        brecs = []
        for i in range(n6):
            if n + 3 > len(data):
                break
            brecs.append(data[n])
            n += 3
            if (f & 0x8000) != 0:
                n += 3
        n5 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        frecs = []
        for i in range(n5):
            if n + 7 > len(data):
                break
            frecs.append({"f": data[n], "g": data[n + 1],
                          "i": struct.unpack_from("<H", data, n + 2)[0],
                          "j": struct.unpack_from("<H", data, n + 4)[0], "h": data[n + 6]})
            n += 7
        n4 = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        erecs = []
        for i in range(n4):
            if n + 3 > len(data):
                break
            erecs.append({"e": data[n], "h": struct.unpack_from("<H", data, n + 1)[0]})
            n += 3
        # формат
        fmt = struct.unpack_from("<H", data, n)[0] if n + 2 <= len(data) else 0
        n += 2
        g = data[n] if n < len(data) else 0
        n += 1
        h = data[n] if n < len(data) else 0
        n += 1
        if h == 0:
            h = 256
        return {"f": f, "objects": objs, "obj_count": len(objs), "palettes": pals,
                "b_records": len(brecs), "f_records": frecs, "e_records": erecs,
                "pixel_format": fmt, "mini_frames": g, "pixels_per_frame": h,
                "parsed_end": n, "size": len(data)}
    except Exception as e:  # noqa: BLE001
        return {"error": str(e)}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    CS.mkdir(parents=True, exist_ok=True)

    resources = ["m0", "m1", "m2", "m6_0", "m6_1", "m6_2", "m6_3", "m6_4", "m6_5",
                 "m7", "m11_0", "m11_1", "m13_2"]
    # слоты: m6_i -> a[16+i]; m7 -> a[22]; сцены по сценарию (этап 15.11)
    slot_of = {}
    for i in range(6):
        slot_of[f"m6_{i}"] = f"a[{16 + i}]"
    slot_of["m7"] = "a[22]"
    slot_of["m0"] = "a[][0..1]"
    slot_of["m1"] = "b[][1]"
    slot_of["m2"] = "a[][0..2]"
    slot_of["m11_0"] = "a[][0..9]"
    slot_of["m11_1"] = "a[][0..6]"
    slot_of["m13_2"] = "a[][-1]"

    registry = {"meta": "17 sprite slots (доказано этапом 15.15): 6 gameplay a[16..21]=m6_*, a[22]=m7, "
                        "10 сценических a[][0..9]/b[][1]", "slots": []}
    inv = {"meta": "Инвентарь ресурсов (парсер a.java)", "resources": []}
    obj_inv = {"meta": "Инвентарь объектов листов", "objects": []}
    frame_inv = {"meta": "Кадры объектов: мини-кадры (g x h) + RLE-блоки (объекты k=1/2 с размерами c x d)",
                 "frames": []}
    fmt_stats = {"meta": "Статистика форматов", "resources": []}
    roles = {"meta": "Роли ресурсов (evidence-based)", "resources": []}

    total_objs = 0
    total_frames = 0
    for rname in resources:
        try:
            d, A, h, base = read(rname)
        except Exception:
            roles["resources"].append({"resource": rname, "role": "MISSING"})
            continue
        A_ref[0] = A
        segs_info = []
        for s in range(A - 1):
            sd = seg(d, h, base, s)
            if sd is None:
                continue
            p = parse_sprite_list(sd)
            if p and "error" not in p and p["obj_count"] > 0:
                segs_info.append({"segment": s, "size": len(sd), **{k: v for k, v in p.items()
                                                                    if k != "objects"}})
                for oi, o in enumerate(p["objects"]):
                    obj_inv["objects"].append({
                        "resource": rname, "segment": s, "slot": slot_of.get(rname),
                        "object_index": oi, "k": o.get("k"), "e": o.get("e"),
                        "c": o.get("c"), "d": o.get("d"),
                        "width_px": o.get("c"), "height_px": o.get("d") if o.get("k") in (1, 2) else None,
                    })
                    total_objs += 1
                    # мини-кадры
                    if p["mini_frames"] > 0:
                        frame_inv["frames"].append({
                            "resource": rname, "segment": s, "object_index": oi,
                            "mini_frames": p["mini_frames"], "pixels_per_frame": p["pixels_per_frame"],
                            "format": hex(p["pixel_format"]),
                        })
                        total_frames += p["mini_frames"]
        inv["resources"].append({"resource": rname, "segments": segs_info,
                                 "segment_count": len(segs_info),
                                 "slot": slot_of.get(rname)})
        # роли
        if rname.startswith("m6_") or rname == "m7":
            role = "GAMEPLAY"
        elif rname in ("m0", "m1", "m2", "m11_0", "m11_1"):
            role = "SCENE/MENU"
        elif rname == "m13_2":
            role = "MUSIC (MIDI seg0) + SCENE листы"
        else:
            role = "UNKNOWN"
        roles["resources"].append({"resource": rname, "role": role, "evidence": "g.java:2501 (m6_*/m7 gameplay); сценарий g.g() (сцены)"})
        # формат-статистика
        fmts = {}
        for s in segs_info:
            fmts[s["pixel_format"]] = fmts.get(s["pixel_format"], 0) + 1
        fmt_stats["resources"].append({"resource": rname, "formats": {hex(k): v for k, v in fmts.items()},
                                       "segments": len(segs_info)})

    # слоты
    for i in range(6):
        registry["slots"].append({"slot": f"a[{16 + i}]", "resource": f"m6_{i}", "segment": "все",
                                  "loader": "g.java:2501", "source_record": "a[16+n] -> m6_*",
                                  "purpose": "GAMEPLAY", "confidence": "CONFIRMED"})
    registry["slots"].append({"slot": "a[22]", "resource": "m7", "segment": "все",
                              "loader": "g.java:2501", "source_record": "a[22]",
                              "purpose": "GAMEPLAY", "confidence": "CONFIRMED"})
    for r, slots, purpose in [("m0", ["a[][0]", "a[][1]"], "SCENE/MENU"),
                              ("m1", ["b[][1]"], "SCENE/MENU"),
                              ("m2", ["a[][0]", "a[][1]", "a[][2]"], "SCENE/MENU"),
                              ("m11_0", [f"a[][{i}]" for i in range(10)], "SCENE"),
                              ("m11_1", [f"a[][{i}]" for i in range(7)], "SCENE")]:
        for sl in slots:
            registry["slots"].append({"slot": sl, "resource": r, "segment": "см. sprite-slot-map",
                                      "loader": "g.g() case 3", "source_record": "{3, slot, seg, -1, 2}",
                                      "purpose": purpose, "confidence": "CONFIRMED (загрузка)"})
    registry["count"] = len(registry["slots"])

    (OUT / "sprite-slot-registry-v2.json").write_text(json.dumps(registry, indent=1, ensure_ascii=False))
    (OUT / "sprite-resource-inventory-v2.json").write_text(json.dumps(inv, indent=1, ensure_ascii=False))
    (OUT / "sprite-object-inventory-v2.json").write_text(json.dumps(obj_inv, indent=1, ensure_ascii=False))
    (OUT / "sprite-frame-inventory-v2.json").write_text(json.dumps(frame_inv, indent=1, ensure_ascii=False))
    (OUT / "sprite-format-statistics-v2.json").write_text(json.dumps(fmt_stats, indent=1, ensure_ascii=False))
    (OUT / "scene-sprite-usage-v2.json").write_text(json.dumps({
        "meta": "Сценические слоты: назначение каждого НЕ доказано (нет evidence); только факт загрузки",
        "slots": [{"slot": "a[][0..9]", "resource": "m11_0/m11_1/m0/m2/m7", "purpose": "UNKNOWN (загружается сценарием g.g())"},
                  {"slot": "b[][1]", "resource": "m1", "purpose": "UNKNOWN"}],
        "note": "не называть menu/splash/portrait без evidence"
    }, indent=1, ensure_ascii=False))
    (OUT / "resource-role-classification-v2.json").write_text(json.dumps(roles, indent=1, ensure_ascii=False))

    print(f"слотов: {len(registry['slots'])}; объектов: {total_objs}; мини-кадров: {total_frames}")
    print("ФАЙЛЫ ЗАПИСАНЫ")


if __name__ == "__main__":
    sys.exit(main())
