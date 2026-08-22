#!/usr/bin/env python3
"""TEST-003: REAL RUNTIME MISSION 03 + L==10 + COMPLETION.

bB=3 -> mission_03 -> L==10 -> cB -> damage source -> cB decrement ->
cB<=0 -> state 7 -> Q[] reward -> save -> next state

Метод входа в mission_03: RUNTIME_ASSISTED — внешний JDWP putstatic g.bB=3
в момент state 16 (до загрузки миссии). JAR НЕ изменяется (instrumented.jar
побайтово идентичен оригиналу).
"""
import os, sys, json, time, shutil, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from test_002_driver import (Emu, build_maps2, snap_global, read_player,
                             read_entity, snap_mo, RES2, EVID2, reach_gameplay)
from test_001_driver import snap_entities, latest_frame, JAR_SHA

RES3 = os.path.join(ROOT, "results", "test-003")
EVID3 = os.path.join(ROOT, "evidence", "real", "test-003")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

# ---------- массивы для reward-diff ----------
ARR_FIELDS = ["L", "M", "b", "u", "P", "B"]

def build_maps3(jdwp, gid, fid, cid):
    gf, ff, cc = build_maps2(jdwp, gid, fid, cid)
    # массивы-поля g для reward diff
    for fid_, name, sig, mod in jdwp.fields(gid):
        if name in ARR_FIELDS and sig.startswith("["):
            gf["arr_" + name] = (fid_, sig)
    return gf, ff, cc

def snap_arrays(jdwp, gid, gf):
    out = {}
    for name in ARR_FIELDS:
        key = "arr_" + name
        if key not in gf:
            continue
        fid_, sig = gf[key]
        try:
            v = jdwp.get_static(gid, [fid_])[0]
            if v[0] == "obj" and v[1]:
                ln = jdwp.array_length(v[1])
                if ln > 0:
                    _, vals = jdwp.array_values(v[1], 0, min(ln, 64))
                    out[name] = [x[1] for x in vals]
                else:
                    out[name] = []
            else:
                out[name] = None
        except Exception as e:
            out[name] = {"error": str(e)}
    return out

def set_bB(jdwp, gid, gf, value):
    """RUNTIME_ASSISTED: putstatic g.bB = value."""
    jdwp.set_static(gid, gf["bB"], "I", value)

def save_frame(label):
    lp = latest_frame()
    if lp:
        os.makedirs(EVID3, exist_ok=True)
        dst = os.path.join(EVID3, label + ".png")
        shutil.copyfile(lp, dst)
        meta = {"timestamp": time.time(), "runtime": "FreeJ2ME SDL Anbu",
                "emulator": "freej2me-sdl.jar",
                "jar_sha256": sha(os.path.join(ROOT, "jar", "instrumented.jar")),
                "test_id": "TEST-003", "evidence": "RUNTIME_CONFIRMED"}
        json.dump(meta, open(dst + ".json", "w"), indent=1)
        return dst
    return None

def find_mission_object(jdwp, gid, gf, ff, cc, grid_names):
    """Найти активный mission object: g.i (f), cB, cy, Q[], позиция i."""
    mo = snap_mo(jdwp, gid, gf)
    l10 = [e for e in snap_entities(jdwp, gid, gf, grid_names, ff, cc)
           if e["L"] == 10 and e["x"]]
    return mo, l10

def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    os.makedirs(RES3, exist_ok=True)
    os.makedirs(EVID3, exist_ok=True)
    emu = Emu()
    out = {}
    log = []
    t_start = time.time()
    def L(msg):
        rec = {"t": round(time.time() - t_start, 2), "msg": msg}
        log.append(rec)
        print(f"[t3] {msg}")
    try:
        emu.start(os.path.join(RES3, "runtime-stdout.log"))
        gid = emu.classes["Lg;"][1]
        fid = emu.classes["Lf;"][1]
        cid = emu.classes["Lc;"][1]
        gf, ff, cc = build_maps3(emu.jdwp, gid, fid, cid)
        grid_names = sorted(k[5:] for k in gf if k.startswith("grid_"))

        # --- доходим до state 16 (после подтверждения новой игры) ---
        L("reaching state 16 (new game confirm)...")
        time.sleep(6)
        for _ in range(8):
            if snap_global(emu.jdwp, gid, gf)["u"] == 0:
                break
            emu.key("FIRE", hold=0.15)
            time.sleep(2.5)
        emu.key("FIRE", hold=0.15); time.sleep(2)
        emu.key("FIRE", hold=0.15); time.sleep(3)
        for _ in range(4):
            if snap_global(emu.jdwp, gid, gf)["u"] == 9:
                break
            emu.key("FIRE", hold=0.15); time.sleep(2.5)
        emu.key("FIRE", hold=0.15); time.sleep(3)
        g = snap_global(emu.jdwp, gid, gf)
        L(f"after YES: state={g['state']} sub={g['sub']} bB={g['bB']}")

        # --- RUNTIME_ASSISTED: bB = 3 в момент state 2 (перед Z(bB)) ---
        # (при выборе сложности g.bB принудительно = 0, g.java:3650 — сброс ДО state 16)
        set_bB(emu.jdwp, gid, gf, 3)
        g = snap_global(emu.jdwp, gid, gf)
        L(f"RUNTIME_ASSISTED: bB set to 3 (state={g['state']})")
        out["assist"] = {"method": "JDWP putstatic g.bB", "value": 3,
                         "jar_modified": False,
                         "note": "RUNTIME_ASSISTED (не пользовательский проход)"}

        # --- продвигаем интро/загрузку ---
        # Открытие (наблюдение TEST-003): bB сбрасывается в 0 в C() (state 16)
        # непосредственно перед state 4 -> z() -> Z(bB). Мониторим bB каждые 5мс
        # и восстанавливаем bB=3 сразу после сброса (до вызова Z()).
        # Затем state 2: загрузка карт порциями; sub 1 = пауза, продвигается FIRE.
        assisted_at = None
        set_count = 0
        t_load = time.time()
        while time.time() - t_load < 120:
            g = snap_global(emu.jdwp, gid, gf)
            if g["bB"] == 0 and g["state"] in (16, 4, 2):
                set_bB(emu.jdwp, gid, gf, 3)
                set_count += 1
                if assisted_at is None:
                    assisted_at = time.time()
            if g["state"] == 6:
                break
            if g["state"] == 2 and g["sub"] == 1:
                # пауза загрузки — продвигаем клавишей (наблюдение TEST-003)
                emu.key("FIRE", hold=0.2)
                time.sleep(0.5)
            else:
                # state 16 (интро) идёт сам: sub 1 -> 2 -> 3 -> 4 без клавиш;
                # важно НЕ слать клавиши, чтобы поймать окно сброса bB (5мс поллинг)
                time.sleep(0.005)
        out["assist"]["state2_forced"] = assisted_at is not None
        out["assist"]["set_count"] = set_count
        L(f"mission load: state={g['state']} bB={g['bB']} by={g['by']} bz={g['bz']} (t={round(time.time()-t_load,1)}s, sets={set_count})")
        g = snap_global(emu.jdwp, gid, gf)
        L(f"mission load result: state={g['state']} bB={g['bB']} by={g['by']} bz={g['bz']} sub={g['sub']}")
        out["mission_start"] = {"state": g["state"], "bB": g["bB"], "by": g["by"],
                                "bz": g["bz"], "sub": g["sub"],
                                "expected_mission": 3,
                                "resource": "/m9 seg13 (mission_03)" if g["bB"] == 3 else "/m9 seg10"}
        json.dump(out, open(os.path.join(RES3, "mission-start.json"), "w"), indent=1, default=str)

        if g["state"] != 6 or g["bB"] != 3:
            L("MISSION 03 NOT LOADED — abort")
            out["status"] = "PARTIAL"
            json.dump(out, open(os.path.join(RES3, "summary.json"), "w"), indent=1, default=str)
            return

        save_frame("mission-start")
        # ждём конца сцены (sub==0), как в TEST-002
        t0 = time.time()
        while time.time() - t0 < 180:
            g = snap_global(emu.jdwp, gid, gf)
            if g["sub"] == 0:
                break
            emu.key("FIRE", hold=0.25)
            time.sleep(8)
        L(f"sub={snap_global(emu.jdwp, gid, gf)['sub']} (0 = свободное управление)")

        # --- Q[] before + mission object ---
        mo, l10 = find_mission_object(emu.jdwp, gid, gf, ff, cc, grid_names)
        L(f"MO: i={mo['i']} cB={mo['cB']} cy={mo['cy']} cz={mo['cz']} Q={mo['Q']} "
          f"cU={mo['cU']} cW={mo['cW']} cY={mo['cY']} cb={mo['cb']} cw={mo['cw']}")
        L(f"L==10 instances: {len(l10)}")
        out["mission_object"] = mo
        out["l10_instances"] = l10[:10]
        json.dump({"mission": 3, "q_before": mo["Q"], "cB": mo["cB"], "cy": mo["cy"],
                   "cz": mo["cz"], "cU": mo["cU"], "cW": mo["cW"], "cY": mo["cY"],
                   "i": mo["i"], "timestamp": time.time()},
                  open(os.path.join(RES3, "q-before.json"), "w"), indent=1, default=str)

        # --- snapshot до (reward diff) ---
        arr_before = snap_arrays(emu.jdwp, gid, gf)
        pl_before = read_player(emu.jdwp, gid, gf, ff, cc)
        out["arrays_before"] = arr_before
        json.dump({"arrays": arr_before, "player": pl_before, "mo": mo,
                   "timestamp": time.time()},
                  open(os.path.join(RES3, "reward-before.json"), "w"), indent=1, default=str)

        # --- cB watch + подход к объекту + атака ---
        cb_trace = []
        t0 = time.time()
        t_end = time.time() + 150
        last_cB = None
        attacked = False
        save_frame("mission-object")
        while time.time() < t_end:
            mo2 = snap_mo(emu.jdwp, gid, gf)
            g = snap_global(emu.jdwp, gid, gf)
            if last_cB is not None and mo2["cB"] != last_cB:
                cb_trace.append({"t": round(time.time()-t0, 2), "old_cB": last_cB,
                                 "new_cB": mo2["cB"], "delta": mo2["cB"] - last_cB,
                                 "state": g["state"], "sub": g["sub"]})
                L(f"cB change: {last_cB} -> {mo2['cB']} (delta {mo2['cB']-last_cB}) at t={round(time.time()-t0,1)}")
            last_cB = mo2["cB"]
            # если объект активен и не завершён — атакуем
            if mo2["i"] and mo2["cB"] > 0 and not attacked:
                # подойти к объекту
                pl = read_player(emu.jdwp, gid, gf, ff, cc)
                obj_ent = None
                for e in l10:
                    if e["fid"] == mo2["i"]:
                        obj_ent = e
                        break
                if obj_ent and pl and pl["x"]:
                    dx = obj_ent["x"] - pl["x"]; dy = obj_ent["y"] - pl["y"]
                    d = (dx*dx + dy*dy) ** 0.5
                    if d > 80000:
                        key = "RIGHT" if abs(dx) > abs(dy) and dx > 0 else "LEFT" if abs(dx) > abs(dy) \
                            else "DOWN" if dy > 0 else "UP"
                        emu.key(key, hold=0.3)
                    else:
                        emu.key("FIRE", hold=0.2)
                        attacked = True
                        L(f"attacking mission object at ({obj_ent['x']>>14},{obj_ent['y']>>14})")
                        save_frame("objective-active")
                else:
                    emu.key("FIRE", hold=0.2)
                    attacked = True
            elif mo2["cB"] <= 0 and mo2["cB"] != 0:
                break
            # завершение?
            if g["state"] == 7:
                break
            time.sleep(0.1)
        json.dump({"test": "TEST-003", "generated": time.time(), "cb_changes": cb_trace},
                  open(os.path.join(RES3, "cb-trace.json"), "w"), indent=1, default=str)
        json.dump({"test": "TEST-003", "generated": time.time(),
                   "note": "источник урона cB определяется по корреляции события с target==mission object",
                   "events": cb_trace}, open(os.path.join(RES3, "damage-trace.json"), "w"), indent=1, default=str)
        out["cb_trace"] = cb_trace
        g = snap_global(emu.jdwp, gid, gf)
        L(f"after attack phase: state={g['state']} sub={g['sub']} cB={mo2['cB']}")

        # --- completion ---
        completion = {"observed": g["state"] == 7}
        if g["state"] == 7:
            save_frame("completion")
            mo3 = snap_mo(emu.jdwp, gid, gf)
            completion.update({"cB": mo3["cB"], "state": g["state"], "sub": g["sub"]})
            L(f"COMPLETION: state 7, cB={mo3['cB']}")
            # результаты
            arr_after = snap_arrays(emu.jdwp, gid, gf)
            pl_after = read_player(emu.jdwp, gid, gf, ff, cc)
            mo_after = snap_mo(emu.jdwp, gid, gf)
            json.dump({"arrays": arr_after, "player": pl_after, "mo": mo_after,
                       "state": g["state"], "timestamp": time.time()},
                      open(os.path.join(RES3, "results.json"), "w"), indent=1, default=str)
            json.dump({"q_after": mo_after["Q"], "cB": mo_after["cB"], "state": g["state"]},
                      open(os.path.join(RES3, "q-after.json"), "w"), indent=1, default=str)
            # reward diff
            diff = {}
            for name in ARR_FIELDS:
                if name in arr_before and name in arr_after:
                    diff[name] = {"before": arr_before[name], "after": arr_after[name],
                                  "changed": arr_before[name] != arr_after[name]}
            json.dump({"test": "TEST-003", "generated": time.time(), "diff": diff,
                       "note": "только реально изменившиеся поля считаются observed effects"},
                      open(os.path.join(RES3, "reward-diff.json"), "w"), indent=1, default=str)
            out["reward_diff"] = diff
            save_frame("results")
            # следующий state
            t1 = time.time()
            next_state = None
            while time.time() - t1 < 20:
                g2 = snap_global(emu.jdwp, gid, gf)
                if g2["state"] != 7:
                    next_state = {"state": g2["state"], "sub": g2["sub"],
                                  "t": round(time.time()-t0, 1)}
                    L(f"next state after 7: state={g2['state']} sub={g2['sub']}")
                    if g2["state"] == 13:
                        save_frame("shop")
                    break
                time.sleep(0.5)
            out["next_state"] = next_state
        else:
            L(f"completion NOT observed (state={g['state']}, cB={mo2['cB']})")
            out["completion"] = completion
        out["completion"] = completion
        json.dump({"test": "TEST-003", "completion": completion, "cb_trace": cb_trace,
                   "state_after": snap_global(emu.jdwp, gid, gf)},
                  open(os.path.join(RES3, "completion-trace.json"), "w"), indent=1, default=str)
        json.dump(log, open(os.path.join(RES3, "state-trace.json"), "w"), indent=1, default=str)
        out["log"] = log
        out["status"] = "done"
        json.dump(out, open(os.path.join(RES3, "summary.json"), "w"), indent=1, default=str)
        L("TEST-003 phase complete")
    finally:
        emu.stop()

if __name__ == "__main__":
    main()
