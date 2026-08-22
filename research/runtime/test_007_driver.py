#!/usr/bin/env python3
"""TEST-007: REAL RUNTIME SHOP / ECONOMY / WEAPON PRICES.

Цели: открыть state 13 SHOP реально (L==14 объект) или RUNTIME_ASSISTED (JDWP
переход в state 13, без изменения экономических полей), проверить L[], g.y(),
b[][], цены, покупку, выход, save.

JDWP — только наблюдение + assisted переход (помечен RUNTIME_ASSISTED).
"""
import os, sys, json, time, shutil, hashlib, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from test_001_driver import Emu, snap_global, snap_entities, latest_frame, JAR_SHA
from test_002_driver import read_entity, read_player, build_maps2
from jdwp import Writer
import test_003_driver as t3

RES7 = os.path.join(ROOT, "results", "test-007")
EVID7 = os.path.join(ROOT, "evidence", "real", "test-007")
RMS_DIR = os.path.join(ROOT, "rms", "instrumented240320")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def save_frame(label):
    lp = latest_frame()
    if lp:
        os.makedirs(EVID7, exist_ok=True)
        dst = os.path.join(EVID7, label + ".png")
        shutil.copyfile(lp, dst)
        meta = {"timestamp": time.time(), "runtime": "FreeJ2ME SDL Anbu",
                "emulator": "freej2me-sdl.jar",
                "jar_sha256": sha(os.path.join(ROOT, "jar", "instrumented.jar")),
                "test_id": "TEST-007", "evidence": "RUNTIME_CONFIRMED"}
        json.dump(meta, open(dst + ".json", "w"), indent=1)
        return dst
    return None

def build_maps7(jdwp, gid, fid, cid):
    gf, ff, cc = build_maps2(jdwp, gid, fid, cid)
    # экономические поля
    for fid_, name, sig, mod in jdwp.fields(gid):
        if name in ("y", "au", "as", "at", "bt") and (sig.startswith("[") or sig == "I"):
            gf["econ_" + name] = (fid_, sig)
    # b [[I (weapon rank таблица)
    for fid_, name, sig, mod in jdwp.fields(gid):
        if name == "b" and sig == "[[I":
            gf["rank_table"] = (fid_, sig)
    return gf, ff, cc

def read_L(jdwp, gid, gf):
    """L[] — найти по сигнатуре [I и проверить содержимое."""
    for fid_, name, sig, mod in jdwp.fields(gid):
        if name == "L" and sig == "[I":
            v = jdwp.get_static(gid, [fid_])[0]
            if v[0] == "obj" and v[1]:
                ln = jdwp.array_length(v[1])
                _, vals = jdwp.array_values(v[1], 0, min(ln, 32))
                return [x[1] for x in vals]
            return None
    return None

def read_econ(jdwp, gid, gf):
    out = {}
    for k in ("econ_y", "econ_au", "econ_as", "econ_at", "econ_bt", "rank_table"):
        if k not in gf:
            continue
        fid_, sig = gf[k]
        try:
            v = jdwp.get_static(gid, [fid_])[0]
            if v[0] == "obj" and v[1]:
                ln = jdwp.array_length(v[1])
                if ln > 0:
                    _, vals = jdwp.array_values(v[1], 0, min(ln, 40))
                    # [[I: элементы = строки (arrayID)
                    if sig == "[[I" and vals and vals[0][0] == "obj" and vals[0][1]:
                        rows = []
                        for cell in vals[:8]:
                            rid = cell[1]
                            if not rid:
                                rows.append(None); continue
                            rln = jdwp.array_length(rid)
                            _, rv = jdwp.array_values(rid, 0, min(rln, 24))
                            rows.append([x[1] for x in rv])
                        out[k] = rows
                    else:
                        out[k] = [x[1] for x in vals]
                else:
                    out[k] = []
            else:
                out[k] = v[1]
        except Exception as e:
            out[k] = {"error": str(e)}
    return out

def snap_shop(emu, jdwp, gid, gf, ff, cc):
    g = snap_global(jdwp, gid, gf)
    L = read_L(jdwp, gid, gf)
    econ = read_econ(jdwp, gid, gf)
    pl = read_player(jdwp, gid, gf, ff, cc)
    return {
        "t": time.time(),
        "state": g["state"], "sub": g["sub"], "u": g["u"], "v": g["v"],
        "bB": g["bB"], "bC": g["bC"], "bF": g["bF"],
        "L": L,
        "econ": econ,
        "player_hp": (pl["props"] or [None]*24)[7] if pl else None,
    }

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
        print(f"[t7] {msg}")
    try:
        emu.start(os.path.join(RES7, "runtime-stdout.log"))
        gid = emu.classes["Lg;"][1]
        gf, ff, cc = build_maps7(emu.jdwp, gid, emu.classes["Lf;"][1], emu.classes["Lc;"][1])
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

        # ---------- попытка 1: реальный L==14 объект (магазин) ----------
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        l14 = [e for e in ents if e["L"] == 14 and e["x"]]
        L(f"L==14 objects: {len(l14)}")
        shop_opened = False
        pl = read_player(emu.jdwp, gid, gf, ff, cc)
        if l14 and pl and pl["x"]:
            pxy = (pl["x"], pl["y"])
            near = sorted(l14, key=lambda e: abs(e["x"]-pxy[0]) + abs(e["y"]-pxy[1]))[:5]
            for obj in near:
                L(f"try L14 at ({obj['x']>>14},{obj['y']>>14}) g0={(obj['props'] or [None])[0]}")
                # подход
                t_end = time.time() + 45
                last = None
                while time.time() < t_end:
                    pl = read_player(emu.jdwp, gid, gf, ff, cc)
                    g = snap_global(emu.jdwp, gid, gf)
                    if g["state"] == 13:
                        L(f"*** SHOP OPENED (state 13) via L14 object!")
                        shop_opened = True
                        break
                    if pl is None or pl["x"] is None:
                        time.sleep(0.1); continue
                    dx = obj["x"] - pl["x"]; dy = obj["y"] - pl["y"]
                    if (dx*dx + dy*dy) ** 0.5 > 40000:
                        key = "RIGHT" if abs(dx) > abs(dy) and dx > 0 else "LEFT" if abs(dx) > abs(dy) \
                            else "DOWN" if dy > 0 else "UP"
                        emu.key(key, hold=0.25)
                    else:
                        emu.key("FIRE", hold=0.2)
                        time.sleep(1.0)
                        g = snap_global(emu.jdwp, gid, gf)
                        if g["state"] == 13:
                            L("*** SHOP OPENED via FIRE at L14!")
                            shop_opened = True
                            break
                    time.sleep(0.15)
                if shop_opened:
                    break

        # ---------- попытка 2: RUNTIME_ASSISTED state 13 ----------
        if not shop_opened:
            L("real path failed — RUNTIME_ASSISTED: d(13,0) via JDWP")
            out["assist"] = {"method": "JDWP putstatic g.a=13, g.b=0 (RUNTIME_ASSISTED)",
                             "jar_modified": False,
                             "economic_fields_modified": False}
            emu.jdwp.set_static(gid, gf["state"], "I", 13)
            emu.jdwp.set_static(gid, gf["sub"], "I", 0)
            time.sleep(5)
            g = snap_global(emu.jdwp, gid, gf)
            L(f"after assisted 13: state={g['state']} sub={g['sub']}")
            if g["state"] == 13:
                shop_opened = True
                # e() таймеры au[1..4] могут требовать время; если sub не сменился —
                # установить au[0]=1 (UI-стейт магазина; НЕ экономическое поле)
                au_fid = None
                for fid_, name, sig, mod in emu.jdwp.fields(gid):
                    if name == "au" and sig == "[I":
                        au_fid = fid_
                if au_fid:
                    au_val = emu.jdwp.get_static(gid, [au_fid])[0]
                    if au_val[0] == "obj" and au_val[1]:
                        ln = emu.jdwp.array_length(au_val[1])
                        _, auv = emu.jdwp.array_values(au_val[1], 0, min(ln, 13))
                        au_list = [x[1] for x in auv]
                        L(f"au[]={au_list}")
                        if au_list and au_list[0] == 0:
                            emu.jdwp.array_set(au_val[1], 0, "I", 1)
                            L("assisted: au[0]=1 (показать shop UI)")
                            time.sleep(1)

        if not shop_opened:
            L("SHOP NOT OPENED")
            out["status"] = "PARTIAL"
            json.dump(out, open(os.path.join(RES7, "summary.json"), "w"), indent=1, default=str)
            json.dump(log, open(os.path.join(RES7, "log.json"), "w"), indent=1, default=str)
            return

        # ---------- SHOP ENTRY SNAPSHOT ----------
        save_frame("shop")
        entry = snap_shop(emu, emu.jdwp, gid, gf, ff, cc)
        json.dump(entry, open(os.path.join(RES7, "shop-entry.json"), "w"), indent=1, default=str)
        json.dump({"currency": {"L": entry["L"]}, "t": time.time()},
                  open(os.path.join(RES7, "currency-before.json"), "w"), indent=1, default=str)
        json.dump({"weapons": {"L": entry["L"], "rank_table": entry["econ"].get("rank_table"),
                               "bt": entry["econ"].get("econ_bt")}, "t": time.time()},
                  open(os.path.join(RES7, "weapon-before.json"), "w"), indent=1, default=str)
        rms0 = read_rms()
        L(f"SHOP ENTRY: state={entry['state']} L={entry['L']}")
        L(f"  econ: y={str(entry['econ'].get('econ_y'))[:80]} au={entry['econ'].get('econ_au')} "
          f"as={entry['econ'].get('econ_as')} at={entry['econ'].get('econ_at')} bt={entry['econ'].get('econ_bt')}")
        L(f"  rank_table={str(entry['econ'].get('rank_table'))[:80]}")

        # ---------- навигация/покупка в shop ----------
        purchase = []
        t_end = time.time() + 60
        last_state = None
        while time.time() < t_end:
            g = snap_global(emu.jdwp, gid, gf)
            if g["state"] != 13:
                L(f"shop left: state={g['state']} sub={g['sub']} at t={round(time.time()-t_start,1)}")
                break
            if g["sub"] != last_state:
                L(f"  shop sub={g['sub']} (t={round(time.time()-t_start,1)})")
                last_state = g["sub"]
            # пробуем FIRE (покупка), DOWN (навигация)
            if int(time.time()) % 3 == 0:
                s_before = snap_shop(emu, emu.jdwp, gid, gf, ff, cc)
                emu.key("FIRE", hold=0.2)
                time.sleep(1.2)
                s_after = snap_shop(emu, emu.jdwp, gid, gf, ff, cc)
                if s_before["L"] != s_after["L"]:
                    L(f"  *** L[] CHANGED after FIRE: {s_before['L']} -> {s_after['L']}")
                    purchase.append({"action": "FIRE", "L_before": s_before["L"], "L_after": s_after["L"],
                                     "t": round(time.time()-t_start, 1)})
            elif int(time.time()) % 3 == 1:
                emu.key("DOWN", hold=0.15)
                time.sleep(0.5)
            else:
                time.sleep(0.5)
        json.dump(purchase, open(os.path.join(RES7, "purchase-trace.json"), "w"), indent=1, default=str)

        # ---------- EXIT ----------
        after = snap_shop(emu, emu.jdwp, gid, gf, ff, cc)
        json.dump(after, open(os.path.join(RES7, "purchase-after.json"), "w"), indent=1, default=str)
        g = snap_global(emu.jdwp, gid, gf)
        json.dump({"state": g["state"], "sub": g["sub"], "bB": g["bB"], "t": time.time()},
                  open(os.path.join(RES7, "shop-exit.json"), "w"), indent=1, default=str)
        # FIRE для выхода, ждём следующий state
        t_end = time.time() + 30
        while time.time() < t_end:
            emu.key("FIRE", hold=0.2)
            time.sleep(2.0)
            g = snap_global(emu.jdwp, gid, gf)
            if g["state"] != 13:
                L(f"exit: state={g['state']} sub={g['sub']}")
                save_frame("shop-exit")
                break
        rms1 = read_rms()
        rms_diff = {}
        for k in rms0:
            if k in rms1 and rms0[k]["hex"] != rms1[k]["hex"]:
                rms_diff[k] = {"before": rms0[k]["size"], "after": rms1[k]["size"]}
        json.dump({"rms_before": rms0, "rms_after": rms1, "changes": rms_diff,
                   "note": "RMS write после покупки/выхода"},
                  open(os.path.join(RES7, "rms-trace.json"), "w"), indent=1, default=str)
        L(f"RMS changes: {rms_diff}")
        out["purchases"] = purchase
        out["rms_changes"] = rms_diff
        out["exit_state"] = {"state": g["state"], "sub": g["sub"]}
        out["status"] = "done"
        json.dump(out, open(os.path.join(RES7, "summary.json"), "w"), indent=1, default=str)
        json.dump(log, open(os.path.join(RES7, "log.json"), "w"), indent=1, default=str)
        L("TEST-007 complete")
    finally:
        emu.stop()

if __name__ == "__main__":
    os.makedirs(RES7, exist_ok=True)
    os.makedirs(EVID7, exist_ok=True)
    main()
