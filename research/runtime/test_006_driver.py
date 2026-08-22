#!/usr/bin/env python3
"""TEST-006: REAL RUNTIME SAVE / LOAD / RMS PROGRESSION.

GAMEPLAY -> state change/progress -> RMS WRITE -> death/reload -> RMS READ -> restored state

Миссия: mission 03 (RUNTIME_ASSISTED bB=3 — только выбор миссии).
JDWP — только наблюдение. RMS не модифицируется через JDWP (только чтение файлов).
"""
import os, sys, json, time, shutil, hashlib, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from test_001_driver import Emu, snap_global, snap_entities, latest_frame, JAR_SHA, KEYMAP
from test_002_driver import read_entity, read_player, build_maps2
import test_003_driver as t3

RES6 = os.path.join(ROOT, "results", "test-006")
EVID6 = os.path.join(ROOT, "evidence", "real", "test-006")
RMS_DIR = os.path.join(ROOT, "rms", "instrumented240320")

ARR_FIELDS = ["L", "M", "P", "B", "b", "u", "D", "E", "Q"]

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def save_frame(label):
    lp = latest_frame()
    if lp:
        os.makedirs(EVID6, exist_ok=True)
        dst = os.path.join(EVID6, label + ".png")
        shutil.copyfile(lp, dst)
        meta = {"timestamp": time.time(), "runtime": "FreeJ2ME SDL Anbu",
                "emulator": "freej2me-sdl.jar",
                "jar_sha256": sha(os.path.join(ROOT, "jar", "instrumented.jar")),
                "test_id": "TEST-006", "evidence": "RUNTIME_CONFIRMED"}
        json.dump(meta, open(dst + ".json", "w"), indent=1)
        return dst
    return None

def read_rms():
    """Прочитать физические RMS-файлы."""
    out = {}
    for f in sorted(glob.glob(os.path.join(RMS_DIR, "a*"))):
        name = os.path.basename(f)
        d = open(f, "rb").read()
        out[name] = {"size": len(d), "hex": d.hex(" "), "mtime": os.path.getmtime(f)}
    return out

def build_maps6(jdwp, gid, fid, cid):
    gf, ff, cc = build_maps2(jdwp, gid, fid, cid)
    arr = {}
    for fid_, name, sig, mod in jdwp.fields(gid):
        if name in ARR_FIELDS and sig.startswith("["):
            arr[name] = (fid_, sig)
    return gf, ff, cc, arr

def snap_arrays(jdwp, gid, arr, maxlen=96):
    out = {}
    for name, (fid_, sig) in arr.items():
        try:
            v = jdwp.get_static(gid, [fid_])[0]
            if v[0] == "obj" and v[1]:
                ln = jdwp.array_length(v[1])
                if ln > 0:
                    _, vals = jdwp.array_values(v[1], 0, min(ln, maxlen))
                    out[name] = [x[1] for x in vals]
                else:
                    out[name] = []
            else:
                out[name] = None
        except Exception as e:
            out[name] = {"error": str(e)}
    return out

def full_snapshot(emu, jdwp, gid, gf, ff, cc, arr):
    g = snap_global(jdwp, gid, gf)
    pl = read_player(jdwp, gid, gf, ff, cc)
    pr = pl["props"] if pl else None
    snap = {
        "t": time.time(),
        "bB": g["bB"], "bC": g["bC"], "bF": g["bF"], "by": g["by"], "bz": g["bz"],
        "state": g["state"], "sub": g["sub"],
        "player_hp": pr[7] if pr else None,
        "player_state": pr[12] if pr else None,
        "player_pos": (pl["x"], pl["y"]) if pl and pl["x"] else None,
        "arrays": snap_arrays(jdwp, gid, arr),
    }
    return snap

def snap_arrays_raw(jdwp, gid, arr):
    out = {}
    for name, (fid_, sig) in arr.items():
        try:
            v = jdwp.get_static(gid, [fid_])[0]
            out[name] = v
        except Exception as e:
            out[name] = {"error": str(e)}
    return out

def main():
    emu = Emu()
    out = {}
    log = []
    t_start = time.time()
    def L(msg):
        rec = {"t": round(time.time() - t_start, 2), "msg": msg}
        log.append(rec)
        print(f"[t6] {msg}")
    try:
        emu.start(os.path.join(RES6, "runtime-stdout.log"))
        gid = emu.classes["Lg;"][1]
        gf, ff, cc, arr = build_maps6(emu.jdwp, gid, emu.classes["Lf;"][1], emu.classes["Lc;"][1])
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

        # ---------- SNAPSHOT PRE (state + rms) ----------
        pre = full_snapshot(emu, emu.jdwp, gid, gf, ff, cc, arr)
        rms_pre = read_rms()
        json.dump({"snapshot": pre, "rms": rms_pre, "t": time.time()},
                  open(os.path.join(RES6, "rms-before.json"), "w"), indent=1, default=str)
        json.dump(pre, open(os.path.join(RES6, "state-before.json"), "w"), indent=1, default=str)
        L(f"PRE: bB={pre['bB']} bC={pre['bC']} bF={pre['bF']} HP={pre['player_hp']} "
          f"L={pre['arrays'].get('L')} M={pre['arrays'].get('M')} P={pre['arrays'].get('P')}")
        L(f"PRE arrays: L[1]={pre['arrays'].get('L', [None]*2)[1] if isinstance(pre['arrays'].get('L'), list) and len(pre['arrays'].get('L', []))>1 else '?'} "
          f"L[2]={pre['arrays'].get('L', [None]*3)[2] if isinstance(pre['arrays'].get('L'), list) and len(pre['arrays'].get('L', []))>2 else '?'} "
          f"L[4]={pre['arrays'].get('L', [None]*5)[4] if isinstance(pre['arrays'].get('L'), list) and len(pre['arrays'].get('L', []))>4 else '?'}")
        L(f"PRE D={pre['arrays'].get('D')} E={pre['arrays'].get('E')}")
        raw = snap_arrays_raw(emu.jdwp, gid, arr)
        L(f"RAW arrays: L={raw.get('L')} P={raw.get('P')} B={raw.get('B')} b={raw.get('b')} E={raw.get('E')}")
        save_frame("before")

        # ---------- ДЕЙСТВИЯ: патроны (FIRE), HP (урон), оружие (*/#) ----------
        L("actions: FIRE x6 (ammo), * and # (weapon switch), take damage...")
        for i in range(6):
            emu.key("FIRE", hold=0.15)
            time.sleep(0.8)
        emu.key("STAR", hold=0.15); time.sleep(1.5)
        emu.key("POUND", hold=0.15); time.sleep(1.5)
        # урон: подойти к ближайшему активному врагу и постоять
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        live = [e for e in ents if e["L"] == 3 and e["x"] and (e["props"] or [None]*20)[7] and
                (e["props"] or [None]*20)[12] == 1]
        pl = read_player(emu.jdwp, gid, gf, ff, cc)
        if live and pl:
            pxy = (pl["x"], pl["y"])
            target = min(live, key=lambda e: abs(e["x"]-pxy[0]) + abs(e["y"]-pxy[1]))
            L(f"approach enemy ({target['x']>>14},{target['y']>>14}) for damage")
            t_end = time.time() + 40
            last = None
            while time.time() < t_end:
                pl = read_player(emu.jdwp, gid, gf, ff, cc)
                g = snap_global(emu.jdwp, gid, gf)
                if pl is None or pl["x"] is None:
                    time.sleep(0.1); continue
                if (pl["props"] or [None]*24)[7] is not None and (pl["props"])[7] < 200:
                    L(f"damage taken: HP={(pl['props'])[7]} at t={round(time.time()-t_start,1)}")
                    break
                dx = target["x"] - pl["x"]; dy = target["y"] - pl["y"]
                if (dx*dx + dy*dy) ** 0.5 > 50000:
                    key = "RIGHT" if abs(dx) > abs(dy) and dx > 0 else "LEFT" if abs(dx) > abs(dy) \
                        else "DOWN" if dy > 0 else "UP"
                    emu.key(key, hold=0.2)
                else:
                    emu.key("FIRE", hold=0.15)
                    time.sleep(0.3)
                time.sleep(0.15)
        time.sleep(2)

        # ---------- SNAPSHOT MID (после действий) ----------
        mid = full_snapshot(emu, emu.jdwp, gid, gf, ff, cc, arr)
        rms_mid = read_rms()
        writes = {}
        for name in rms_mid:
            if name in rms_pre and rms_mid[name]["hex"] != rms_pre[name]["hex"]:
                writes[name] = {"before_size": rms_pre[name]["size"],
                                "after_size": rms_mid[name]["size"],
                                "changed": True}
            elif name not in rms_pre:
                writes[name] = {"created": True, "size": rms_mid[name]["size"]}
        json.dump({"writes": writes, "rms_before": rms_pre, "rms_after": rms_mid,
                   "mid_snapshot": mid},
                  open(os.path.join(RES6, "rms-writes.json"), "w"), indent=1, default=str)
        L(f"RMS writes: {writes}")
        L(f"MID: HP={mid['player_hp']} L={mid['arrays'].get('L')} "
          f"weapon(L1)={mid['arrays'].get('L', [None]*2)[1] if isinstance(mid['arrays'].get('L'), list) and len(mid['arrays'].get('L', []))>1 else '?'} "
          f"ammo(L2)={mid['arrays'].get('L', [None]*3)[2] if isinstance(mid['arrays'].get('L'), list) and len(mid['arrays'].get('L', []))>2 else '?'}")
        save_frame("save-event")

        # ---------- СМЕРТЬ ----------
        L("waiting for death (standing near enemy)...")
        t_end = time.time() + 120
        death_at = None
        while time.time() < t_end:
            pl = read_player(emu.jdwp, gid, gf, ff, cc)
            if pl is None:
                time.sleep(0.1); continue
            if (pl["props"] or [None]*24)[7] is not None and pl["props"][7] <= 0:
                death_at = time.time() - t_start
                L(f"*** DEATH at t={round(death_at,1)}")
                save_frame("death")
                break
            emu.key("FIRE", hold=0.15)
            time.sleep(2.0)
        if death_at is None:
            L("no death — force by waiting more")
            t_end = time.time() + 60
            while time.time() < t_end:
                pl = read_player(emu.jdwp, gid, gf, ff, cc)
                if pl is None:
                    time.sleep(0.1); continue
                if (pl["props"] or [None]*24)[7] is not None and pl["props"][7] <= 0:
                    death_at = time.time() - t_start
                    L(f"*** DEATH at t={round(death_at,1)}")
                    save_frame("death")
                    break
                time.sleep(2.0)

        # ---------- RELOAD + POST ----------
        L("waiting for reload (FIRE to advance death screen)...")
        t_end = time.time() + 150
        reload_done = False
        while time.time() < t_end:
            pl = read_player(emu.jdwp, gid, gf, ff, cc)
            g = snap_global(emu.jdwp, gid, gf)
            if pl and pl["x"] and (pl["props"] or [None]*24)[7] is not None and pl["props"][7] > 0 and g["state"] == 6:
                L(f"reload done: HP={(pl['props'])[7]} state={g['state']} bB={g['bB']} "
                  f"pos=({pl['x']>>14},{pl['y']>>14}) sub={g['sub']}")
                reload_done = True
                break
            # state 7 (экран смерти) или 2 (загрузка) — FIRE продвигает
            if g["state"] in (7, 2, 16):
                emu.key("FIRE", hold=0.2)
            time.sleep(2.0)
        if not reload_done:
            L("reload NOT completed in time — snapshot as-is")
        time.sleep(3)
        post = full_snapshot(emu, emu.jdwp, gid, gf, ff, cc, arr)
        rms_post = read_rms()
        json.dump({"snapshot": post, "rms": rms_post, "t": time.time()},
                  open(os.path.join(RES6, "rms-after.json"), "w"), indent=1, default=str)
        json.dump(post, open(os.path.join(RES6, "state-after.json"), "w"), indent=1, default=str)
        L(f"POST: HP={post['player_hp']} bB={post['bB']} L={post['arrays'].get('L')} "
          f"P={post['arrays'].get('P')} B={post['arrays'].get('B')}")
        save_frame("reload")

        # ---------- DIFF: persisted fields ----------
        diff = {}
        for key in ("bB", "bC", "bF", "player_hp", "player_state"):
            diff[key] = {"pre": pre[key], "mid": mid[key], "post": post[key],
                         "persisted": pre[key] == post[key]}
        for aname in ("L", "M", "P", "B", "b", "u", "D", "E"):
            a_pre = pre["arrays"].get(aname)
            a_post = post["arrays"].get(aname)
            a_mid = mid["arrays"].get(aname)
            diff[aname] = {"pre": a_pre, "mid": a_mid, "post": a_post,
                           "persisted": a_pre == a_post}
        json.dump({"test": "TEST-006", "generated": time.time(), "diff": diff,
                   "note": "persisted = pre == post (значение пережило death/reload); "
                           "изменения mid (патроны/HP) показывают реальные writes"},
                  open(os.path.join(RES6, "save-load-diff.json"), "w"), indent=1, default=str)
        L("DIFF summary:")
        for k, v in diff.items():
            if isinstance(v, dict):
                L(f"  {k}: persisted={v.get('persisted')} pre={str(v.get('pre'))[:60]} post={str(v.get('post'))[:60]}")
        out["diff"] = diff
        out["writes"] = writes
        json.dump(out, open(os.path.join(RES6, "summary.json"), "w"), indent=1, default=str)
        json.dump(log, open(os.path.join(RES6, "log.json"), "w"), indent=1, default=str)
        L("TEST-006 complete")
    finally:
        emu.stop()

if __name__ == "__main__":
    os.makedirs(RES6, exist_ok=True)
    os.makedirs(EVID6, exist_ok=True)
    main()
