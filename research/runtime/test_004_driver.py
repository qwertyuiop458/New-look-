#!/usr/bin/env python3
"""TEST-004: REAL RUNTIME AI / AGGRO / ATTACK.

Цель: реально проверить AI на доступном враге (L==3, HP>0) без mission-object.

Правила:
- JDWP только для НАБЛЮДЕНИЯ (state/HP/AI не меняются).
- Исключение: выбор миссии (bB) через JDWP — RUNTIME_ASSISTED (как TEST-003),
  если в mission 0 нет достижимого живого врага. bB — не state/HP/AI.
- Медленный подход реальными клавишами.
"""
import os, sys, json, time, shutil, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from test_001_driver import Emu, snap_global, snap_entities, latest_frame, JAR_SHA, KEYMAP
from test_002_driver import read_entity, read_player, dist2, build_maps2

RES4 = os.path.join(ROOT, "results", "test-004")
EVID4 = os.path.join(ROOT, "evidence", "real", "test-004")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def save_frame(label):
    lp = latest_frame()
    if lp:
        os.makedirs(EVID4, exist_ok=True)
        dst = os.path.join(EVID4, label + ".png")
        shutil.copyfile(lp, dst)
        meta = {"timestamp": time.time(), "runtime": "FreeJ2ME SDL Anbu",
                "emulator": "freej2me-sdl.jar",
                "jar_sha256": sha(os.path.join(ROOT, "jar", "instrumented.jar")),
                "test_id": "TEST-004", "evidence": "RUNTIME_CONFIRMED"}
        json.dump(meta, open(dst + ".json", "w"), indent=1)
        return dst
    return None

def live_enemies(ents):
    """Враги с HP>0 (живые/активные) и state<100 (не мёртвые)."""
    out = []
    for e in ents:
        if e["L"] != 3 or not e["x"]:
            continue
        p = e["props"] or []
        if len(p) <= 16:
            continue
        hp = p[7] or 0
        st = p[12] or 0
        if hp > 0 and st < 100:
            out.append((e, hp, st))
    return out

def main():
    emu = Emu()
    out = {}
    log = []
    t_start = time.time()
    def L(msg):
        rec = {"t": round(time.time() - t_start, 2), "msg": msg}
        log.append(rec)
        print(f"[t4] {msg}")
    try:
        emu.start(os.path.join(RES4, "runtime-stdout.log"))
        gid = emu.classes["Lg;"][1]
        fid = emu.classes["Lf;"][1]
        cid = emu.classes["Lc;"][1]
        gf, ff, cc = build_maps2(emu.jdwp, gid, fid, cid)
        grid_names = sorted(k[5:] for k in gf if k.startswith("grid_"))

        # ---------- фаза 1: до state 6 (mission 0, стандартный путь) ----------
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
        # state 16 -> ... -> 6 (интро идёт сам; sub 1 пауза -> FIRE)
        t0 = time.time()
        while time.time() - t0 < 150:
            g = snap_global(emu.jdwp, gid, gf)
            if g["state"] == 6:
                break
            if g["state"] == 2 and g["sub"] == 1:
                emu.key("FIRE", hold=0.2); time.sleep(0.5)
            elif g["state"] == 16 and g["sub"] in (3,):
                emu.key("FIRE", hold=0.2); time.sleep(0.5)
            else:
                time.sleep(0.3)
        g = snap_global(emu.jdwp, gid, gf)
        L(f"gameplay: state={g['state']} bB={g['bB']} by={g['by']} bz={g['bz']} sub={g['sub']}")
        # ждём sub=0 (конец сцены)
        t0 = time.time()
        while time.time() - t0 < 60:
            g = snap_global(emu.jdwp, gid, gf)
            if g["sub"] == 0:
                break
            emu.key("FIRE", hold=0.25)
            time.sleep(2.5)
        L(f"sub={snap_global(emu.jdwp, gid, gf)['sub']}")

        # ---------- фаза 2: разведка живых врагов ----------
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        live = live_enemies(ents)
        pl = read_player(emu.jdwp, gid, gf, ff, cc)
        L(f"enemies total={len([e for e in ents if e['L']==3])} live(HP>0)={len(live)} player=({pl['x']>>14 if pl else '?'},{pl['y']>>14 if pl else '?'})")
        for e, hp, st in live[:10]:
            L(f"  live enemy: ({e['x']>>14},{e['y']>>14}) hp={hp} state={st} g0={(e['props'] or [None])[0]} grid={e['grid']}{e['i']}{e['j']}{e['k']}")

        # ---------- фаза 3: выбор врага и подход ----------
        mission = g["bB"]
        target = None
        if live:
            pxy = (pl["x"], pl["y"]) if pl and pl["x"] else (0, 0)
            # ближайший живой по манхэттену
            target = min(live, key=lambda t: abs(t[0]["x"]-pxy[0]) + abs(t[0]["y"]-pxy[1]))
            L(f"target enemy: ({target[0]['x']>>14},{target[0]['y']>>14}) hp={target[1]} state={target[2]}")
        else:
            L("no live enemies in mission 0 — RUNTIME_ASSISTED switch to mission 3")
            # RUNTIME_ASSISTED: bB=3 (как TEST-003)
            # сначала вернуться в меню? нет — проще перезапустить с bB=3 с самого начала.
            # Здесь: выходим, помечаем, что нужен mission 3 прогон.
            out["note"] = "mission 0: no reachable live enemy — use mission 3 pass"
            emu.stop()
            return main_mission3()

        # ---------- фаза 4: медленный подход + трассировка ----------
        trace = []
        t0 = time.time()
        def sel():
            ents2 = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
            for e in ents2:
                if e["L"] == 3 and e["grid"] == target[0]["grid"] and e["i"] == target[0]["i"] \
                        and e["j"] == target[0]["j"] and e["k"] == target[0]["k"] and e["x"]:
                    return read_entity(emu.jdwp, ff, cc, e["fid"])
            return None

        L("approach phase (slow keys)...")
        save_frame("enemy-before")
        t_end = time.time() + 240
        prev_state = None
        prev_hp = None
        player_hp0 = 200
        last_pos = None
        stuck = 0
        while time.time() < t_end:
            e = sel()
            pl = read_player(emu.jdwp, gid, gf, ff, cc)
            g = snap_global(emu.jdwp, gid, gf)
            if e is None or pl is None or pl["x"] is None:
                time.sleep(0.2)
                continue
            pr = pl["props"] or [None]*24
            er = e["props"] or [None]*24
            dx = e["x"] - pl["x"]; dy = e["y"] - pl["y"]
            d_px = round((dx*dx + dy*dy) ** 0.5 / 16384, 1)
            rec = {"t": round(time.time()-t0, 2),
                   "dist_px": d_px,
                   "estate": er[12], "esub": er[10], "ehp": er[7],
                   "ev13": er[13], "ev14": er[14], "etimer": er[15], "eflags": er[16],
                   "ex": e["x"], "ey": e["y"],
                   "px": pl["x"], "py": pl["y"],
                   "php": pr[7], "pstate": pr[12],
                   "bz": g["bz"], "sub": g["sub"]}
            trace.append(rec)
            # события
            if prev_state is not None and er[12] != prev_state:
                L(f"  STATE {prev_state}->{er[12]} dist={d_px} t={rec['t']}")
                save_frame(f"state-{er[12]}")
            if prev_hp is not None and er[7] != prev_hp:
                L(f"  ENEMY HP {prev_hp}->{er[7]} dist={d_px} t={rec['t']}")
            if pr[7] is not None and pr[7] < player_hp0:
                L(f"  *** PLAYER DAMAGED: hp {player_hp0}->{pr[7]} dist={d_px} estate={er[12]} t={rec['t']}")
                save_frame("damage")
                player_hp0 = pr[7]
            prev_state = er[12]; prev_hp = er[7]
            # движение (медленное): если dist > 25000 px*fixed
            if d_px * 16384 > 30000:
                key = None
                if abs(dx) > abs(dy):
                    key = "RIGHT" if dx > 0 else "LEFT"
                else:
                    key = "DOWN" if dy > 0 else "UP"
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
                # рядом: стоим, ждём реакции врага
                pass
            # выход по атаке/смерти
            if er[12] is not None and er[12] >= 100:
                L(f"  enemy dead (state {er[12]})")
                break
            if pr[7] is not None and pr[7] <= 0:
                L("  player dead")
                break
            time.sleep(0.15)
        save_frame("enemy-approach")
        out["trace"] = trace
        json.dump({"test": "TEST-004", "generated": time.time(), "mission": mission,
                   "target": {k: target[0][k] for k in ("grid","i","j","k")},
                   "trace": trace}, open(os.path.join(RES4, "ai-trace.json"), "w"), indent=1, default=str)
        # distance-trace
        json.dump({"test": "TEST-004", "generated": time.time(),
                   "distances": [{"t": r["t"], "dist_px": r["dist_px"], "estate": r["estate"],
                                  "ehp": r["ehp"], "php": r["php"]} for r in trace]},
                  open(os.path.join(RES4, "distance-trace.json"), "w"), indent=1, default=str)
        # attack/damage traces
        attacks = [r for r in trace if r["estate"] in (7, 8, 12)]
        damages = [r for r in trace if r["php"] is not None and r["php"] < 200]
        json.dump({"test": "TEST-004", "generated": time.time(),
                   "attack_states_seen": [r["t"] for r in attacks],
                   "note": "attack cycle = state 7/8/12" if attacks else "attack cycle NOT observed"},
                  open(os.path.join(RES4, "attack-trace.json"), "w"), indent=1, default=str)
        json.dump({"test": "TEST-004", "generated": time.time(),
                   "player_damage_events": [{"t": r["t"], "php": r["php"], "estate": r["estate"],
                                             "dist_px": r["dist_px"]} for r in damages],
                   "note": "damage = player HP < 200" if damages else "no damage observed"},
                  open(os.path.join(RES4, "damage-trace.json"), "w"), indent=1, default=str)
        out["attacks"] = len(attacks)
        out["damages"] = len(damages)
        out["status"] = "done"
        json.dump(out, open(os.path.join(RES4, "summary.json"), "w"), indent=1, default=str)
        json.dump(log, open(os.path.join(RES4, "state-trace.json"), "w"), indent=1, default=str)
        L("TEST-004 phase complete")
    finally:
        emu.stop()

def main_mission3():
    """RUNTIME_ASSISTED прогон mission 3 (bB=3): поиск живого врага и aggro."""
    import test_003_driver as t3
    emu = Emu()
    out = {}
    log = []
    t_start = time.time()
    def L(msg):
        log.append({"t": round(time.time()-t_start, 2), "msg": msg})
        print(f"[t4m3] {msg}")
    try:
        emu.start(os.path.join(RES4, "runtime-stdout-m3.log"))
        gid = emu.classes["Lg;"][1]
        gf, ff, cc = build_maps2(emu.jdwp, gid, emu.classes["Lf;"][1], emu.classes["Lc;"][1])
        grid_names = sorted(k[5:] for k in gf if k.startswith("grid_"))
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
        # RUNTIME_ASSISTED: bB=3 (только выбор миссии, не AI)
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
        out["assist"] = {"method": "JDWP putstatic g.bB=3 (RUNTIME_ASSISTED, выбор миссии)",
                         "jar_modified": False}
        # живые враги
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        live = live_enemies(ents)
        pl = read_player(emu.jdwp, gid, gf, ff, cc)
        L(f"enemies={len([e for e in ents if e['L']==3])} live(HP>0)={len(live)} player=({pl['x']>>14 if pl and pl['x'] else '?'},{pl['y']>>14 if pl and pl['y'] else '?'})")
        for e, hp, st in live[:12]:
            L(f"  live: ({e['x']>>14},{e['y']>>14}) hp={hp} state={st} g0={(e['props'] or [None])[0]}")
        if not live:
            L("no live enemies in mission 3 either")
            json.dump({"status": "no-live-enemies", "log": log}, open(os.path.join(RES4, "summary.json"), "w"), indent=1)
            return
        # выбор цели: приоритет малому |dy| (та же горизонталь — путь по прямой)
        pxy = (pl["x"], pl["y"]) if pl and pl["x"] else (0, 0)
        def score(t):
            e = t[0]
            st = (e["props"] or [None]*20)[12] or 0
            # приоритет: активные (state!=0), затем малый |dy|
            return (0 if st != 0 else 100000) + abs(e["x"]-pxy[0])/16384 + abs(e["y"]-pxy[1])/16384 * 4
        target = min(live, key=score)
        L(f"target: ({target[0]['x']>>14},{target[0]['y']>>14}) hp={target[1]} state={target[2]} dist_px={round((((target[0]['x']-pxy[0])**2+(target[0]['y']-pxy[1])**2)**0.5)/16384,1)}")
        save_frame("enemy-before")
        # подход + трассировка
        trace = []
        t0 = time.time()
        def sel():
            ents2 = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
            for e in ents2:
                if e["L"] == 3 and e["grid"] == target[0]["grid"] and e["i"] == target[0]["i"] \
                        and e["j"] == target[0]["j"] and e["k"] == target[0]["k"] and e["x"]:
                    return read_entity(emu.jdwp, ff, cc, e["fid"])
            return None
        t_end = time.time() + 300
        prev_state = None
        prev_hp = None
        player_hp0 = 200
        last_pos = None
        stuck = 0
        aggro_at = None
        while time.time() < t_end:
            e = sel()
            pl = read_player(emu.jdwp, gid, gf, ff, cc)
            g = snap_global(emu.jdwp, gid, gf)
            if e is None or pl is None or pl["x"] is None:
                time.sleep(0.2)
                continue
            pr = pl["props"] or [None]*24
            er = e["props"] or [None]*24
            dx = e["x"] - pl["x"]; dy = e["y"] - pl["y"]
            d_px = round((dx*dx + dy*dy) ** 0.5 / 16384, 1)
            rec = {"t": round(time.time()-t0, 2), "dist_px": d_px,
                   "estate": er[12], "esub": er[10], "ehp": er[7],
                   "ev13": er[13], "ev14": er[14], "etimer": er[15],
                   "ex": e["x"], "ey": e["y"], "px": pl["x"], "py": pl["y"],
                   "php": pr[7], "pstate": pr[12], "sub": g["sub"], "bz": g["bz"],
                   "eprops": (e["props"] or [])[:24]}
            trace.append(rec)
            if prev_state is not None and er[12] != prev_state:
                L(f"  STATE {prev_state}->{er[12]} dist={d_px} t={rec['t']}")
                if aggro_at is None and er[12] != 0 and er[12] is not None:
                    aggro_at = rec["t"]
                    L(f"  *** AGGRO at t={rec['t']} dist={d_px} state={er[12]}")
                    save_frame("enemy-aggro")
            if prev_hp is not None and er[7] != prev_hp:
                L(f"  ENEMY HP {prev_hp}->{er[7]} dist={d_px} t={rec['t']}")
                if aggro_at is None and (er[7] or 0) > (prev_hp or 0):
                    aggro_at = rec["t"]
                    L(f"  *** ENEMY ACTIVATED (hp {prev_hp}->{er[7]}) at t={rec['t']} dist={d_px}")
                    save_frame("enemy-aggro")
            if pr[7] is not None and pr[7] < player_hp0:
                L(f"  *** PLAYER DAMAGED: {player_hp0}->{pr[7]} dist={d_px} estate={er[12]} t={rec['t']}")
                save_frame("damage")
                player_hp0 = pr[7]
            prev_state = er[12]; prev_hp = er[7]
            if d_px * 16384 > 40000:
                key = None
                if abs(dx) > abs(dy):
                    key = "RIGHT" if dx > 0 else "LEFT"
                else:
                    key = "DOWN" if dy > 0 else "UP"
                emu.key(key, hold=0.2)
                pos = (pl["x"] >> 14, pl["y"] >> 14)
                if pos == last_pos:
                    stuck += 1
                    if stuck >= 10:
                        alt = {"UP": "RIGHT", "DOWN": "LEFT", "LEFT": "UP", "RIGHT": "DOWN"}[key]
                        emu.key(alt, hold=0.6)
                        stuck = 0
                else:
                    stuck = 0
                last_pos = pos
            elif d_px <= 40:
                # рядом: FIRE + качели (шаг назад) для провокации атаки врага
                if int(time.time()) % 4 == 0:
                    emu.key("FIRE", hold=0.2)
                    time.sleep(0.3)
                if int(time.time()) % 8 == 3:
                    emu.key("LEFT", hold=0.6)
                    time.sleep(0.3)
                if int(time.time()) % 8 == 6:
                    emu.key("RIGHT", hold=0.6)
                    time.sleep(0.3)
            if er[12] is not None and er[12] >= 100:
                L(f"  enemy dead (state {er[12]})"); break
            if pr[7] is not None and pr[7] <= 0:
                L("  player dead"); break
            time.sleep(0.12)
        save_frame("enemy-approach")
        json.dump({"test": "TEST-004", "generated": time.time(), "mission": 3,
                   "target": {k: target[0][k] for k in ("grid","i","j","k")},
                   "aggro_at": aggro_at, "trace": trace},
                  open(os.path.join(RES4, "ai-trace.json"), "w"), indent=1, default=str)
        json.dump({"test": "TEST-004", "generated": time.time(),
                   "distances": [{"t": r["t"], "dist_px": r["dist_px"], "estate": r["estate"],
                                  "ehp": r["ehp"], "php": r["php"]} for r in trace]},
                  open(os.path.join(RES4, "distance-trace.json"), "w"), indent=1, default=str)
        attacks = [r for r in trace if r["estate"] in (7, 8, 12)]
        damages = [r for r in trace if r["php"] is not None and r["php"] < 200]
        json.dump({"test": "TEST-004", "generated": time.time(),
                   "attack_states_seen": [{"t": r["t"], "estate": r["estate"], "etimer": r["etimer"],
                                           "dist_px": r["dist_px"]} for r in attacks],
                   "note": "attack cycle = state 7/8/12" if attacks else "attack cycle NOT observed"},
                  open(os.path.join(RES4, "attack-trace.json"), "w"), indent=1, default=str)
        json.dump({"test": "TEST-004", "generated": time.time(),
                   "player_damage_events": [{"t": r["t"], "php": r["php"], "estate": r["estate"],
                                             "dist_px": r["dist_px"]} for r in damages],
                   "note": "damage = player HP < 200" if damages else "no damage observed"},
                  open(os.path.join(RES4, "damage-trace.json"), "w"), indent=1, default=str)
        out.update({"aggro_at": aggro_at, "attacks": len(attacks), "damages": len(damages),
                    "assist": out.get("assist"), "status": "done"})
        json.dump(out, open(os.path.join(RES4, "summary.json"), "w"), indent=1, default=str)
        json.dump(log, open(os.path.join(RES4, "state-trace.json"), "w"), indent=1, default=str)
        L("TEST-004 (mission 3) phase complete")
    finally:
        emu.stop()

if __name__ == "__main__":
    os.makedirs(RES4, exist_ok=True)
    os.makedirs(EVID4, exist_ok=True)
    if len(sys.argv) > 1 and sys.argv[1] == "m3":
        main_mission3()
    else:
        main()
