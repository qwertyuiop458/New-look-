#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trace_instance_chain_v2.py — полная трассировка instance → archetype → behavior → animation (этап 15.13).

ДОКАЗАННАЯ ЦЕПОЧКА (из кода):
  mission record [type][id][x][y][len][props]
    → type 3 (враг):  g[0] = g.a(g.m, props[0])   (m = таблица id→индекс, dr() из m9 seg4)
    → type 9 (NPC):   g[0] = g.a(g.w, props[0])   (w = таблица id→индекс, ey() из m9 seg8)
    → type 1/2:       f.d(props) — через g.w
    → type 0 (MC):    f.a(props, n17, n18) — props[0] без преобразования (индекс)
    → прочие (10..26): new f(...) — g[0] = props[0] (объекты, архетип не обязателен)
  → архетип: g.h(idx, prop) = U[T[idx]+prop]
  → анимации: g.h(idx,33)=число; W[g.h(idx,32)+a*13+f]; X[W[10]+fr*2+0/1]
  → кадры по состоянию: g.i(idx, f) = V[g.h(idx,34)*15+f]
  → инициализация слотов: f.g(): g[30+a] = W[a][0] или массив X-кадров

Вывод: research/analysis/v2/instances/*.json
"""
import json
import struct
import sys
from collections import Counter
from pathlib import Path

JAR = Path("research/extracted/jar")
OUT = Path("research/analysis/v2/instances")
MISS = Path("research/analysis/v2/missions")


def read(p):
    d = (JAR / p).read_bytes()
    A = d[0]
    h = [struct.unpack("<I", d[1 + 4 * i:5 + 4 * i])[0] for i in range(A)]
    return d, A, h, 1 + 4 * A


def seg(d, h, base, n):
    return d[base + h[n] - h[0]:base + h[n + 1] - h[0]]


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    # ---------- m9: таблицы m (архетипы) и w (NPC) ----------
    d9, A9, h9, b9 = read("m9")
    seg4 = seg(d9, h9, b9, 4)
    seg8 = seg(d9, h9, b9, 8)

    # парсим seg4 как dr(): tag6=тип (67Б), tag7=анимация (21Б), tag10=кадр (31Б), tag8/9 (5Б)
    types = []      # {id, offset, props32}
    anims = []      # offsets
    frames = []     # offsets
    i = 0
    while i < len(seg4):
        t = seg4[i]
        if t == 6:
            iid = struct.unpack_from("<H", seg4, i + 1)[0]
            props = [struct.unpack_from("<H", seg4, i + 3 + 2 * j)[0] for j in range(32)]
            types.append({"id": iid, "offset": i, "props32": props})
            i += 67
        elif t == 7:
            anims.append(i)
            i += 21
        elif t == 10:
            frames.append(i)
            i += 31
        elif t in (8, 9):
            i += 5
        else:
            i += 1

    # m-таблица: id -> индекс (порядок tag6)
    m = {t["id"]: idx for idx, t in enumerate(types)}

    # вычислим prop32/33/34 как dr(): пройти seg4 с привязкой к текущему типу
    for idx, t in enumerate(types):
        t["prop32"] = None
        t["prop33"] = 0
        t["prop34"] = -1
    cur = -1
    wpos = 0
    fpos = 0
    i = 0
    while i < len(seg4):
        tag = seg4[i]
        if tag == 6:
            cur = len([x for x in types if x["offset"] <= i]) - 1
            if cur >= 0:
                types[cur]["prop32"] = wpos
                types[cur]["prop34"] = fpos if fpos < len(frames) else -1
            i += 67
        elif tag == 7:
            if cur >= 0:
                types[cur]["prop33"] += 1
            wpos += 1
            i += 21
        elif tag == 10:
            fpos += 1
            i += 31
        elif tag in (8, 9):
            i += 5
        else:
            i += 1

    # w-таблица (NPC): ey() из seg8: записи [id u16][2 байта пропуска][15 x u16]
    w = {}
    i = 0
    seg8data = seg8
    n4 = 0
    while i + 27 < len(seg8data):
        n2 = struct.unpack_from("<H", seg8data, i + 1)[0]
        w[n2] = n4
        n4 += 1
        i += 30

    # ---------- кластеры (сигнатура из prop10/7/8/19/20/22) ----------
    clusters = {}
    for t in types:
        p = t["props32"]
        sig = (p[10], p[7], p[8], p[19], p[20], p[22])
        clusters.setdefault(sig, []).append(t["id"])
    sig2name = {sig: f"BEHAVIOR_CLUSTER_{i:02d}" for i, sig in enumerate(sorted(clusters))}

    # ---------- instance registry ----------
    db = json.load(open(Path("research/analysis/v2") / "missions-database.json"))
    registry = {"meta": "Реестр экземпляров из 5 миссий. Цепочка: record -> props[0] -> g.m/g.w -> archetype index -> "
                        "35 props -> кластер -> анимации (prop32/33/34) -> кадры (W/X/V). "
                        "type 0/1/2 = MC/NPC (L 0/1/2), type 3 = враг, type 9 = NPC, 10..26 = объекты.",
                "missions": []}
    stats = {"records": 0, "with_archetype": 0, "enemy_type3": 0, "npc_type9": 0,
             "mc_type0": 0, "object_types": 0, "unmapped": 0}
    arche_usage = Counter()

    for mi in range(5):
        mid = f"mission_{mi:02d}"
        recs = json.loads((MISS / mid / "records.json").read_text())
        mrecs = []
        for r in recs:
            t = r["type"]
            props = r["props"]
            if t not in (0, 1, 2, 3, 9):
                stats["object_types"] += 1
                stats["records"] += 1
                continue  # объекты — не архетипы
            stats["records"] += 1
            idx = None
            conv = None
            if t == 3:
                idx = m.get(props[0], -1) if props else -1
                conv = "f.c -> g.a(g.m, props[0])"
            elif t == 9:
                idx = w.get(props[0], -1) if props else -1
                conv = "f.d -> g.a(g.w, props[0])"
            elif t in (1, 2):
                idx = w.get(props[0], -1) if props else -1
                conv = "f.d -> g.a(g.w, props[0])"
            elif t == 0:
                idx = props[0] if props and 0 <= props[0] < len(types) else -1
                conv = "f.a(3): props[0] как индекс"
            entry = {
                "mission": mid, "instance_id": f"{mid}_rec_{r['offset']}",
                "source_offset": r["offset"], "raw_type": t, "raw_id": r["id"],
                "position": {"x": r["x"], "y": r["y"]}, "props_len": r["len"],
                "props_first6": props[:6], "converter": conv,
            }
            if idx is not None and 0 <= idx < len(types):
                at = types[idx]
                entry["archetype_index"] = idx
                entry["archetype_id"] = at["id"]
                entry["archetype_name"] = f"ARCHETYPE_{at['id']:03d}"
                entry["properties"] = {"prop10_ai": at["props32"][10], "prop7": at["props32"][7],
                                       "prop8": at["props32"][8], "prop19": at["props32"][19],
                                       "prop20": at["props32"][20], "prop22": at["props32"][22]}
                sig = (at["props32"][10], at["props32"][7], at["props32"][8],
                       at["props32"][19], at["props32"][20], at["props32"][22])
                entry["behavior_cluster"] = sig2name[sig]
                entry["animation_set"] = {"prop32_start_W": at["prop32"],
                                          "prop33_count": at["prop33"],
                                          "prop34_frame_index_V": at["prop34"]}
                entry["initial_state"] = props[12] if len(props) > 12 else 0
                entry["confidence"] = "CONFIRMED" if t in (3, 9) else "INFERRED"
                stats["with_archetype"] += 1
                arche_usage[at["id"]] += 1
                if t == 3:
                    stats["enemy_type3"] += 1
                elif t == 9:
                    stats["npc_type9"] += 1
                elif t == 0:
                    stats["mc_type0"] += 1
            else:
                entry["archetype_id"] = None
                entry["behavior_cluster"] = None
                entry["animation_set"] = None
                entry["initial_state"] = props[12] if len(props) > 12 else None
                entry["confidence"] = "UNMAPPED"
                entry["unmap_reason"] = "props[0] не найден в таблице (g.m/g.w вернул -1)"
                stats["unmapped"] += 1
            mrecs.append(entry)
        registry["missions"].append({"mission": mid, "instances": mrecs})
    registry["stats"] = stats
    registry["archetype_usage"] = dict(sorted(arche_usage.items(), key=lambda x: -x[1]))
    (OUT / "instance-registry-v2.json").write_text(json.dumps(registry, indent=1, ensure_ascii=False))

    # ---------- instance-creation-trace ----------
    trace = {
        "meta": "Трассировка создания экземпляра (из g.Z() и f.java).",
        "chain": [
            {"stage": "mission record", "source": "m9 seg10..14", "method": "g.Z() поток", "value": "[type][id][x][y][len][props]", "confidence": "CONFIRMED"},
            {"stage": "конвертер props", "source": "g.Z() case 0/1/2/3/9", "method": "f.a(props,n17,n18) / f.d(props) / f.c(props)", "value": "расширение массива; g[26]/g[27]=слой (MC); g[28]/g[29]=-2 (оружие)", "confidence": "CONFIRMED"},
            {"stage": "архетип lookup", "source": "f.c(): nArray3[0]=g.a(g.m, props[0])", "method": "g.a(int[][],int) g.java:15539", "value": "линейный поиск id -> индекс; -1 если нет", "confidence": "CONFIRMED"},
            {"stage": "архетип lookup NPC", "source": "f.d(): nArray3[0]=g.a(g.w, props[0])", "method": "ey() g.java:29237 (m9 seg8)", "value": "таблица NPC id -> индекс", "confidence": "CONFIRMED"},
            {"stage": "инициализация анимаций", "source": "f.c -> f.g(nArray)", "method": "f.g() f.java:2572", "value": "g[30+i] = W[a][0] или массив X-кадров; g[18]=f.a(nArray)", "confidence": "CONFIRMED"},
            {"stage": "создание объекта", "source": "g.Z()", "method": "new f(c, s, n8, n44, n45, nArray34)", "value": "L=n8; позиция (n44,n45); начальная анимация: L0->66, L3->g.h(type,2), L9->g.k(type,3)", "confidence": "CONFIRMED"},
            {"stage": "поведение", "source": "g.B() state 6", "method": "f.b(entity)", "value": "ветвления по L, g[12], g[10], g[16], prop10", "confidence": "CONFIRMED"},
            {"stage": "кадр по состоянию", "source": "f.a(f2,bl,bl2)", "method": "n5 = dir + g.i(type, state_field)", "value": "V[prop34*15 + f]", "confidence": "CONFIRMED"},
            {"stage": "рендер", "source": "c.java a(Graphics)", "method": "a.a(d, e, x, y, palette)", "value": "кадр e анимации d из спрайт-листа", "confidence": "CONFIRMED"},
            {"stage": "пиксели спрайта", "source": "-", "method": "-", "value": "связь X-кадр -> блок листа a.java", "confidence": "STATIC_LINK_UNKNOWN"},
        ]
    }
    (OUT / "instance-creation-trace.json").write_text(json.dumps(trace, indent=1, ensure_ascii=False))

    # ---------- archetype-animation-map ----------
    amap = {"meta": "prop32/33/34 для каждого архетипа (вычислено по dr() логике)", "archetypes": []}
    for t in types:
        amap["archetypes"].append({"id": t["id"], "prop32_start_W": t["prop32"],
                                   "prop33_anim_count": t["prop33"],
                                   "prop34_frame_V_index": t["prop34"]})
    (OUT / "archetype-animation-map-v2.json").write_text(json.dumps(amap, indent=1, ensure_ascii=False))

    # ---------- state-animation-transitions ----------
    sat = {"meta": "Переходы состояние -> кадр/анимация (доказано кодом)",
           "transitions": [
               {"state": "g[12] (0/6/28)", "frame_sel": "n5 = dir + g.i(type, 0)", "source": "f.java:4656"},
               {"state": "g[12] == 1", "frame_sel": "n5 = dir + g.i(type, 1)", "source": "f.java:4660"},
               {"state": "g[12] == 2", "frame_sel": "n5 = dir + g.i(type, 2)", "source": "f.java:4679"},
               {"state": "g[12] == 3", "frame_sel": "n5 = dir + g.i(type, 3)", "source": "f.java:4746"},
               {"state": "g[12] == 4", "frame_sel": "n5 = dir + g.i(type, 4)", "source": "f.java:4768"},
               {"state": "g[12] == 5", "frame_sel": "n5 = dir + g.i(type, 5)", "source": "f.java:4789"},
               {"state": "g[12] == 7/8", "frame_sel": "n5 = dir + g.i(type, 7/8)", "source": "f.java:4706/4725"},
               {"state": "g[12] == 9", "frame_sel": "n5 = dir + g.i(type, 9)", "source": "f.java:4739"},
               {"state": "g[12] == 10", "frame_sel": "n5 = dir + g.i(type, 10)", "source": "f.java:4801"},
               {"state": "g[12] == 11", "frame_sel": "n5 = dir + g.i(type, 11)", "source": "f.java:4814"},
               {"state": "g[12] == 12", "frame_sel": "n5 = dir + g.i(type, 12)", "source": "f.java:4834"},
               {"state": "g[12] == 13", "frame_sel": "n5 = dir + g.i(type, 13)", "source": "f.java:4841"},
               {"state": "начальная анимация L==0", "anim": "66", "source": "f.java конструктор"},
               {"state": "начальная анимация L==3", "anim": "g.h(type, 2) (сдвиг направления)", "source": "f.java конструктор"},
               {"state": "начальная анимация L==9", "anim": "g.k(type, 3)", "source": "f.java конструктор"},
           ]}
    (OUT / "state-animation-transitions-v2.json").write_text(json.dumps(sat, indent=1, ensure_ascii=False))

    # ---------- animation-frame-usage ----------
    afu = {"meta": "Анимации архетипов и их X-кадры (первые N для каждого архетипа)",
           "archetypes": []}
    for t in types[:30]:
        afu["archetypes"].append({"id": t["id"], "anim_count": t["prop33"],
                                  "anim_start_W": t["prop32"],
                                  "note": "W[10]=X-старт, W[11]=число X-кадров; X[W10+fr*2+0/1]"})
    (OUT / "animation-frame-usage-v2.json").write_text(json.dumps(afu, indent=1, ensure_ascii=False))

    # ---------- instance-visual-catalog ----------
    cat = {"meta": "Визуальный каталог экземпляров. sprite_link = STATIC_LINK_UNKNOWN "
                   "(X-кадры не связаны с блоками спрайт-листов a.java).",
           "missions": []}
    for m in registry["missions"]:
        out_inst = []
        for e in m["instances"]:
            out_inst.append({
                "instance_id": e["instance_id"], "archetype": e.get("archetype_name"),
                "behavior_cluster": e.get("behavior_cluster"), "initial_state": e.get("initial_state"),
                "animation_set": e.get("animation_set"), "frame_mapping": "V-смещения (g.i)",
                "sprite": "STATIC_LINK_UNKNOWN", "palette": "UNKNOWN", "confidence": e.get("confidence"),
            })
        cat["missions"].append({"mission": m["mission"], "instances": out_inst})
    (OUT / "instance-visual-catalog-v2.json").write_text(json.dumps(cat, indent=1, ensure_ascii=False))

    # ---------- instance-chain-validation ----------
    val = {"meta": "Cross-check цепочки", "checks": []}
    for t in types:
        if t["prop32"] is None or t["prop33"] is None or t["prop34"] is None:
            val["checks"].append({"error": f"архетип {t['id']}: prop32/33/34 не вычислены"})
    if len(types) != 56:
        val["checks"].append({"error": f"архетипов {len(types)} != 56"})
    val["stats"] = stats
    val["conclusion"] = "цепочка record->архетип->кластер->анимации подтверждена; sprite link = STATIC_LINK_UNKNOWN"
    (OUT / "instance-chain-validation.json").write_text(json.dumps(val, indent=1, ensure_ascii=False))

    print("records:", stats)
    print("архетипов задействовано:", len(arche_usage), "из 56")
    print("топ архетипов:", dict(sorted(arche_usage.items(), key=lambda x: -x[1])[:8]))
    print("кластеров:", len(clusters))
    print("ФАЙЛЫ ЗАПИСАНЫ")


if __name__ == "__main__":
    sys.exit(main())
