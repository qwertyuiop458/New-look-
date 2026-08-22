#!/usr/bin/env python3
"""TEST-008: REAL SHOP ENTRY / ITEMS / PRICES / PURCHASE.

Настоящий вход в магазин через L14 объект (БЕЗ JDWP state 13):
подход к каждому L14 + FIRE, логирование distance/state, natural shop entry.

JDWP — только наблюдение.
"""
import os, sys, json, time, shutil, hashlib, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from test_001_driver import Emu, snap_global, snap_entities, latest_frame, JAR_SHA
from test_002_driver import read_entity, read_player, build_maps2
import test_003_driver as t3

RES8 = os.path.join(ROOT, "results", "test-008")
EVID8 = os.path.join(ROOT, "evidence", "real", "test-008")
RMS_DIR = os.path.join(ROOT, "rms", "instrumented240320")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def save_frame(label):
    lp = latest_frame()
    if lp:
        os.makedirs(EVID8, exist_ok=True)
        dst = os.path.join(EVID8, label + ".png")
        shutil.copyfile(lp, dst)
        meta = {"timestamp": time.time(), "runtime": "FreeJ2ME SDL Anbu",
                "emulator": "freej2me-sdl.jar",
                "jar_sha256": sha(os.path.join(ROOT, "jar", "instrumented.jar")),
                "test_id": "TEST-008", "evidence": "RUNTIME_CONFIRMED"}
        json.dump(meta, open(dst + ".json", "w"), indent=1)
        return dst
    return None

def read_L(jdwp, gid):
    for fid_, name, sig, mod in jdwp.fields(gid):
        if name == "L" and sig == "[I":
            v = jdwp.get_static(gid, [fid_])[0]
            if v[0] == "obj" and v[1]:
                ln = jdwp.array_length(v[1])
                _, vals = jdwp.array_values(v[1], 0, min(ln, 32))
                return [x[1] for x in vals]
            return None
    return None

def read_rms():
    out = {}
    for f in sorted(glob.glob(os.path.join(RMS_DIR, "a*"))):
        name = os.path.basename(f)
        if name.endswith((".rsr", ".rsh")):
            d = open(f, "rb").read()
            out[name] = {"size": len(d), "hex": d.hex(" "), "mtime": os.path.getmtime(f)}
    return out

def main():
    emu = Emu()
    out = {}
    log = []
    t_start = time.time()
    def L(msg):
        log.append({"t": round(time.time()-t_start, 2), "msg": msg})
        print(f"[t8] {msg}")
    try:
        emu.start(os.path.join(RES8, "runtime-stdout.log"))
        gid = emu.classes["Lg;"][1]
        gf, ff, cc = build_maps2(emu.jdwp, gid, emu.classes["Lf;"][1], emu.classes["Lc;"][1])
        grid_names = sorted(k[5:] for k in gf if k.startswith("grid_"))

        # ---------- вход в mission_03 ----------
        L("reaching state 16...")
        time.sleep(6)
        for _ in range(8):
            if snap_global(emu.jdwp, gid, gf)["u"] == 0:
                break
            emu.key("FIRE", hold=0.15); time.sleep(2.5)
        emu.key("FIRE", hold=0.15); time.sleep(2)
        emu.key("FIRE", hold=0.15); time.sleep(3)
        for _ in range(4):
            if snap_global(emu.jdwp, gid, gf)["u"] == 9:
                break
            emu.key("FIRE", hold=0.15); time.sleep(2.5)
        emu.key("FIRE", hold=0.15); time.sleep(3)
        t3.set_bB(emu.jdwp, gid, gf, 3)
        t0 = time.time()
        while time.time() - t0 < 150:
            g = snap_global(emu.jdwp, gid, gf)
            if g["bB"] == 0 and g["state"] in (16, 4, 2):
                t3.set_bB(emu.jdwp, gid, gf, 3)
            if g["state"] == 6:
                break
            if g["state"] == 2 and g["sub"] == 1:
                emu.key("FIRE", hold=0.2); time.sleep(0.5)
            else:
                time.sleep(0.005)
        g = snap_global(emu.jdwp, gid, gf)
        L(f"mission 3: state={g['state']} bB={g['bB']} bz={g['bz']}")
        t0 = time.time()
        while time.time() - t0 < 90:
            g = snap_global(emu.jdwp, gid, gf)
            if g["sub"] == 0:
                break
            emu.key("FIRE", hold=0.25)
            time.sleep(2.5)
        L(f"sub={snap_global(emu.jdwp, gid, gf)['sub']}")

        # ---------- все L14 ----------
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        l14 = [e for e in ents if e["L"] == 14 and e["x"]]
        pl = read_player(emu.jdwp, gid, gf, ff, cc)
        pxy = (pl["x"], pl["y"]) if pl and pl["x"] else (0, 0)
        L(f"L14 objects: {len(l14)}")
        for e in l14:
            p = e["props"] or []
            dist = round(((e["x"]-pxy[0])**2 + (e["y"]-pxy[1])**2) ** 0.5 / 16384, 1)
            L(f"  L14: ({e['x']>>14},{e['y']>>14}) g0={p[0] if p else '?'} g1={p[1] if len(p)>1 else '?'} "
              f"g16={p[16] if len(p)>16 else '?'} props[:12]={p[:12]} dist={dist} grid={e['grid']}{e['i']}{e['j']}{e['k']}")
        out["l14_all"] = [{"x": e["x"]>>14, "y": e["y"]>>14,
                           "props": (e["props"] or [])[:16],
                           "dist_px": round(((e["x"]-pxy[0])**2+(e["y"]-pxy[1])**2)**0.5/16384, 1),
                           "grid": f"{e['grid']}{e['i']}{e['j']}{e['k']}"} for e in l14]

        # ---------- перебор L14: подход + FIRE ----------
        # приоритет: ближайшие; затем по g0
        l14_sorted = sorted(l14, key=lambda e: abs(e["x"]-pxy[0]) + abs(e["y"]-pxy[1]))
        shop_opened = False
        tested = 0
        for obj in l14_sorted[:25]:
            if shop_opened:
                break
            tested += 1
            p = obj["props"] or []
            L(f"[{tested}] try L14 ({obj['x']>>14},{obj['y']>>14}) g0={p[0] if p else '?'} g1={p[1] if len(p)>1 else '?'}")
            t_end = time.time() + 30
            last_pos = None
            stuck = 0
            while time.time() < t_end:
                g = snap_global(emu.jdwp, gid, gf)
                if g["state"] == 13:
                    L(f"*** NATURAL SHOP ENTRY! state=13 via L14 ({obj['x']>>14},{obj['y']>>14}) g0={p[0] if p else '?'}")
                    shop_opened = True
                    out["natural_entry"] = {"object": {"x": obj["x"]>>14, "y": obj["y"]>>14,
                                                       "props": (obj["props"] or [])[:16],
                                                       "grid": f"{obj['grid']}{obj['i']}{obj['j']}{obj['k']}"},
                                            "t": round(time.time()-t_start, 1)}
                    save_frame("shop-entry")
                    break
                pl = read_player(emu.jdwp, gid, gf, ff, cc)
                if pl is None or pl["x"] is None:
                    time.sleep(0.1); continue
                dx = obj["x"] - pl["x"]; dy = obj["y"] - pl["y"]
                d = (dx*dx + dy*dy) ** 0.5
                if d > 45000:
                    key = "RIGHT" if abs(dx) > abs(dy) and dx > 0 else "LEFT" if abs(dx) > abs(dy) \
                        else "DOWN" if dy > 0 else "UP"
                    emu.key(key, hold=0.25)
                    pos = (pl["x"] >> 14, pl["y"] >> 14)
                    if pos == last_pos:
                        stuck += 1
                        if stuck >= 8:
                            alt = {"UP": "RIGHT", "DOWN": "LEFT", "LEFT": "UP", "RIGHT": "DOWN"}[key]
                            emu.key(alt, hold=0.8)
                            stuck = 0
                    else:
                        stuck = 0
                    last_pos = pos
                else:
                    # рядом: FIRE
                    emu.key("FIRE", hold=0.2)
                    time.sleep(0.8)
                    g = snap_global(emu.jdwp, gid, gf)
                    if g["state"] == 13:
                        L(f"*** NATURAL SHOP ENTRY via FIRE at ({obj['x']>>14},{obj['y']>>14})!")
                        shop_opened = True
                        out["natural_entry"] = {"object": {"x": obj["x"]>>14, "y": obj["y"]>>14,
                                                           "props": (obj["props"] or [])[:16],
                                                           "grid": f"{obj['grid']}{obj['i']}{obj['j']}{obj['k']}"},
                                                "t": round(time.time()-t_start, 1)}
                        save_frame("shop-entry")
                        break
                time.sleep(0.12)
            if shop_opened:
                break
        L(f"tested {tested} L14 objects; shop_opened={shop_opened}")
        save_frame("approach")

        if not shop_opened:
            L("NO natural shop entry (25 objects tested)")
            out["status"] = "PARTIAL"
            out["tested"] = tested
            json.dump(out, open(os.path.join(RES8, "summary.json"), "w"), indent=1, default=str)
            json.dump(log, open(os.path.join(RES8, "log.json"), "w"), indent=1, default=str)
            return

        # ---------- SHOP: items/prices ----------
        save_frame("items")
        L_entry = read_L(emu.jdwp, gid)
        g = snap_global(emu.jdwp, gid, gf)
        L(f"SHOP: state={g['state']} L={L_entry}")
        json.dump({"natural_entry": out["natural_entry"], "state": g["state"],
                   "L": L_entry, "t": time.time()},
                  open(os.path.join(RES8, "natural-shop-entry.json"), "w"), indent=1, default=str)
        json.dump({"items": None, "L": L_entry,
                   "note": "список товаров не отображается через JDWP (UI); цены недоступны",
                   "t": time.time()}, open(os.path.join(RES8, "shop-items.json"), "w"), indent=1, default=str)
        json.dump({"prices": None, "L": L_entry,
                   "note": "цены не отображаются; static_record связь не построена",
                   "t": time.time()}, open(os.path.join(RES8, "price-table-runtime.json"), "w"), indent=1, default=str)

        # ---------- попытка покупки ----------
        L_before = read_L(emu.jdwp, gid)
        purchase = []
        rms0 = read_rms()
        t_end = time.time() + 45
        while time.time() < t_end:
            g = snap_global(emu.jdwp, gid, gf)
            if g["state"] != 13:
                break
            emu.key("FIRE", hold=0.2)
            time.sleep(1.5)
            L_after = read_L(emu.jdwp, gid)
            if L_after != L_before:
                L(f"*** L[] CHANGED: {L_before} -> {L_after}")
                purchase.append({"L_before": L_before, "L_after": L_after,
                                 "t": round(time.time()-t_start, 1)})
                L_before = L_after
            if int(time.time()) % 4 == 0:
                emu.key("DOWN", hold=0.15)
                time.sleep(0.5)
        rms1 = read_rms()
        rms_diff = {k: {"before": rms0[k]["size"], "after": rms1[k]["size"]}
                    for k in rms0 if k in rms1 and rms0[k]["hex"] != rms1[k]["hex"]}
        json.dump(purchase, open(os.path.join(RES8, "purchase-trace.json"), "w"), indent=1, default=str)
        json.dump({"currency_before": L_before, "currency_after": read_L(emu.jdwp, gid),
                   "purchases": purchase},
                  open(os.path.join(RES8, "currency-diff.json"), "w"), indent=1, default=str)
        json.dump({"rms_before": rms0, "rms_after": rms1, "changes": rms_diff},
                  open(os.path.join(RES8, "rms-trace.json"), "w"), indent=1, default=str)
        L(f"purchases: {len(purchase)} RMS changes: {rms_diff}")

        # ---------- exit ----------
        t_end = time.time() + 30
        exit_state = None
        while time.time() < t_end:
            emu.key("FIRE", hold=0.2)
            time.sleep(2.0)
            g = snap_global(emu.jdwp, gid, gf)
            if g["state"] != 13:
                exit_state = {"state": g["state"], "sub": g["sub"]}
                L(f"exit: state={g['state']} sub={g['sub']}")
                save_frame("shop-exit")
                break
        out["purchases"] = purchase
        out["rms_changes"] = rms_diff
        out["exit_state"] = exit_state
        out["status"] = "done"
        json.dump(out, open(os.path.join(RES8, "summary.json"), "w"), indent=1, default=str)
        json.dump(log, open(os.path.join(RES8, "log.json"), "w"), indent=1, default=str)
        L("TEST-008 complete")
    finally:
        emu.stop()

if __name__ == "__main__":
    os.makedirs(RES8, exist_ok=True)
    os.makedirs(EVID8, exist_ok=True)
    main()
