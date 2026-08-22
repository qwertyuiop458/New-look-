#!/usr/bin/env python3
"""TEST-005: REAL RUNTIME PLAYER DEATH / FAILURE.

Полный жизненный цикл: HP>0 -> damage -> HP<=0 -> death handling ->
state/substate -> retry/game over -> save/load.

Миссия: mission 03 (RUNTIME_ASSISTED bB=3 — только выбор миссии).
JDWP — только наблюдение.
"""
import os, sys, json, time, shutil, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from test_001_driver import Emu, snap_global, snap_entities, latest_frame, JAR_SHA, KEYMAP
from test_002_driver import read_entity, read_player, build_maps2
import test_003_driver as t3

RES5 = os.path.join(ROOT, "results", "test-005")
EVID5 = os.path.join(ROOT, "evidence", "real", "test-005")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def save_frame(label):
    lp = latest_frame()
    if lp:
        os.makedirs(EVID5, exist_ok=True)
        dst = os.path.join(EVID5, label + ".png")
        shutil.copyfile(lp, dst)
        meta = {"timestamp": time.time(), "runtime": "FreeJ2ME SDL Anbu",
                "emulator": "freej2me-sdl.jar",
                "jar_sha256": sha(os.path.join(ROOT, "jar", "instrumented.jar")),
                "test_id": "TEST-005", "evidence": "RUNTIME_CONFIRMED"}
        json.dump(meta, open(dst + ".json", "w"), indent=1)
        return dst
    return None

def main():
    emu = Emu()
    out = {}
    log = []
    t_start = time.time()
    def L(msg):
        rec = {"t": round(time.time() - t_start, 2), "msg": msg}
        log.append(rec)
        print(f"[t5] {msg}")
    try:
        emu.start(os.path.join(RES5, "runtime-stdout.log"))
        gid = emu.classes["Lg;"][1]
        gf, ff, cc = build_maps2(emu.jdwp, gid, emu.classes["Lf;"][1], emu.classes["Lc;"][1])
        grid_names = sorted(k[5:] for k in gf if k.startswith("grid_"))
        # поля для death-логирования
        extra = {}
        for fid_, name, sig, mod in emu.jdwp.fields(gid):
            if sig == "I" and name in ("bC", "u", "v", "aF"):
                extra[name] = fid_

        # ---------- вход в mission_03 (RUNTIME_ASSISTED) ----------
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
        L("RUNTIME_ASSISTED: bB=3")
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

        # ---------- выбор active enemy (state!=0, HP>0) ----------
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        live = []
        for e in ents:
            if e["L"] != 3 or not e["x"]:
                continue
            p = e["props"] or []
            if len(p) <= 16:
                continue
            if (p[7] or 0) > 0 and (p[12] or 0) < 100:
                live.append(e)
        pl = read_player(emu.jdwp, gid, gf, ff, cc)
        pxy = (pl["x"], pl["y"]) if pl and pl["x"] else (0, 0)
        L(f"live enemies: {len(live)} player=({pxy[0]>>14},{pxy[1]>>14})")
        # приоритет: активные (state!=0) затем близкие
        def score(e):
            p = e["props"] or [None]*20
            st = p[12] or 0
            return (0 if st != 0 else 100000) + abs(e["x"]-pxy[0])/16384 + abs(e["y"]-pxy[1])/16384*4
        target = min(live, key=score)
        L(f"target: ({target['x']>>14},{target['y']>>14}) state={(target['props'] or [None]*20)[12]} "
          f"hp={(target['props'] or [None]*20)[7]} g0={(target['props'] or [None])[0]}")

        # ---------- подход + смерть + пост-смерть ----------
        trace = []
        t0 = time.time()
        def sel():
            ents2 = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
            for e in ents2:
                if e["L"] == 3 and e["grid"] == target["grid"] and e["i"] == target["i"] \
                        and e["j"] == target["j"] and e["k"] == target["k"] and e["x"]:
                    return read_entity(emu.jdwp, ff, cc, e["fid"])
            return None

        death_at = None
        death_hp = None
        prev_php = None
        first_dmg = None
        last_pos = None
        stuck = 0
        post_death = []
        save_frame("before-death")
        t_end = time.time() + 240
        while time.time() < t_end:
            e = sel()
            pl = read_player(emu.jdwp, gid, gf, ff, cc)
            g = snap_global(emu.jdwp, gid, gf)
            if pl is None or pl["x"] is None:
                time.sleep(0.1)
                continue
            pr = pl["props"] or [None]*30
            er = e["props"] or [None]*30 if e else [None]*30
            php = pr[7]
            # событие урона
            if prev_php is not None and php is not None and php < prev_php:
                dmg = prev_php - php
                rec_dmg = {"t": round(time.time()-t0, 2), "hp_before": prev_php,
                           "dmg": dmg, "hp_after": php, "player_state": pr[12],
                           "enemy_state": er[12], "dist_px": round((((e["x"]-pl["x"])**2+(e["y"]-pl["y"])**2)**0.5)/16384, 1) if e else None}
                trace.append(rec_dmg)
                if first_dmg is None:
                    first_dmg = rec_dmg
                    L(f"FIRST DAMAGE: {prev_php}->{php} (dmg {dmg}) at t={rec_dmg['t']}")
                if death_at is None and php <= 0:
                    death_at = rec_dmg["t"]
                    death_hp = php
                    L(f"*** HP<=0: {prev_php}->{php} at t={rec_dmg['t']} player_state={pr[12]}")
                    save_frame("death")
            prev_php = php

            if death_at is not None:
                # ПОСТ-СМЕРТЬ: частое логирование всех полей
                bC = emu.jdwp.get_static(gid, [extra["bC"]])[0][1] if "bC" in extra else None
                u_ = emu.jdwp.get_static(gid, [extra["u"]])[0][1] if "u" in extra else None
                post = {"t": round(time.time()-t0, 2), "php": php,
                        "pstate": pr[12], "psub": pr[10], "ptimer": pr[15],
                        "px": pl["x"], "py": pl["y"],
                        "g_state": g["state"], "g_sub": g["sub"],
                        "bB": g["bB"], "bC": bC, "u": u_, "by": g["by"], "bz": g["bz"]}
                post_death.append(post)
                if len(post_death) % 25 == 0 or len(post_death) <= 3:
                    L(f"post-death[{len(post_death)}]: php={php} pstate={pr[12]} psub={pr[10]} "
                      f"g_state={g['state']} g_sub={g['sub']} bB={g['bB']} bC={bC} u={u_} "
                      f"pos=({pl['x']>>14},{pl['y']>>14})")
                # воскрешение?
                if php is not None and php > 0 and len(post_death) > 2:
                    L(f"*** HP RESET to {php} at t={round(time.time()-t0,2)} "
                      f"(g_state={g['state']} g_sub={g['sub']} pstate={pr[12]})")
                    save_frame("post-death")
                    break
                # смена состояния?
                if g["state"] != 6 and len(post_death) > 3:
                    L(f"*** STATE CHANGE after death: g_state={g['state']} g_sub={g['sub']} at t={round(time.time()-t0,2)}")
                    save_frame("game-over" if g["state"] == 10 else "post-death")
                    # дальше: наблюдаем 90с, пробуем FIRE — ждём retry/menu/load
                    t2 = time.time()
                    while time.time() - t2 < 90:
                        g2 = snap_global(emu.jdwp, gid, gf)
                        pl2 = None
                        try:
                            pl2 = read_player(emu.jdwp, gid, gf, ff, cc)
                        except Exception:
                            pass
                        pr2 = (pl2["props"] or [None]*30) if pl2 else [None]*30
                        bC = emu.jdwp.get_static(gid, [extra["bC"]])[0][1] if "bC" in extra else None
                        u_ = emu.jdwp.get_static(gid, [extra["u"]])[0][1] if "u" in extra else None
                        post = {"t": round(time.time()-t0, 2), "php": pr2[7], "pstate": pr2[12],
                                "psub": pr2[10], "px": (pl2["x"] if pl2 else None),
                                "py": (pl2["y"] if pl2 else None),
                                "g_state": g2["state"], "g_sub": g2["sub"], "bB": g2["bB"],
                                "bC": bC, "u": u_, "by": g2["by"], "bz": g2["bz"]}
                        post_death.append(post)
                        if len(post_death) % 15 == 0 or len(post_death) <= 6:
                            L(f"post[{len(post_death)}]: php={pr2[7]} pstate={pr2[12]} "
                              f"g_state={g2['state']} g_sub={g2['sub']} bB={g2['bB']} bC={bC} u={u_} "
                              f"pos={(pl2['x']>>14 if pl2 and pl2['x'] else '?')},{(pl2['y']>>14 if pl2 and pl2['y'] else '?')}")
                        # ретрай: HP>0 снова
                        if pr2[7] is not None and pr2[7] > 0 and len(post_death) > 5:
                            L(f"*** HP RESET to {pr2[7]} (g_state={g2['state']} g_sub={g2['sub']})")
                            save_frame("retry")
                            break
                        # возврат в геймплей
                        if g2["state"] == 6 and len(post_death) > 5:
                            L(f"*** BACK TO GAMEPLAY state 6 (bB={g2['bB']})")
                            save_frame("retry")
                            break
                        # FIRE продвигает death screen
                        emu.key("FIRE", hold=0.2)
                        time.sleep(2.0)
                    break
                time.sleep(0.05)
                continue

            # движение к врагу
            if e is None:
                time.sleep(0.2)
                continue
            dx = e["x"] - pl["x"]; dy = e["y"] - pl["y"]
            d_px = (dx*dx + dy*dy) ** 0.5 / 16384
            if d_px > 2.5:
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
            else:
                if int(time.time()) % 4 == 0:
                    emu.key("FIRE", hold=0.2)
                    time.sleep(0.3)
            time.sleep(0.15)

        # ---------- пост-смерть: наблюдение 30с (если не вышли выше) ----------
        if death_at is not None and not post_death:
            L("extended post-death observation (30s)...")
            t1 = time.time()
            while time.time() - t1 < 30:
                pl = read_player(emu.jdwp, gid, gf, ff, cc)
                g = snap_global(emu.jdwp, gid, gf)
                if pl is None:
                    time.sleep(0.1); continue
                pr = pl["props"] or [None]*30
                bC = emu.jdwp.get_static(gid, [extra["bC"]])[0][1] if "bC" in extra else None
                u_ = emu.jdwp.get_static(gid, [extra["u"]])[0][1] if "u" in extra else None
                post = {"t": round(time.time()-t0, 2), "php": pr[7], "pstate": pr[12],
                        "psub": pr[10], "px": pl["x"], "py": pl["y"],
                        "g_state": g["state"], "g_sub": g["sub"], "bB": g["bB"], "bC": bC,
                        "u": u_, "by": g["by"], "bz": g["bz"]}
                post_death.append(post)
                if pr[7] is not None and pr[7] > 0 and len(post_death) > 2:
                    L(f"*** HP RESET to {pr[7]} (g_state={g['state']} g_sub={g['sub']})")
                    save_frame("post-death")
                    break
                if g["state"] != 6:
                    L(f"*** STATE CHANGE: g_state={g['state']} g_sub={g['sub']}")
                    save_frame("game-over" if g["state"] == 10 else "post-death")
                    break
                time.sleep(0.2)

        # ---------- результаты ----------
        out["death_at"] = death_at
        out["death_hp"] = death_hp
        out["first_damage"] = first_dmg
        out["damage_events"] = trace
        out["post_death"] = post_death
        # анализ пост-смерти
        if post_death:
            states = set(p["g_state"] for p in post_death)
            subs = set(p["g_sub"] for p in post_death)
            hps = [p["php"] for p in post_death if p["php"] is not None]
            out["post_death_analysis"] = {
                "g_states_seen": sorted(states, key=lambda x: str(x)),
                "g_subs_seen": sorted(subs, key=lambda x: str(x)),
                "hp_reset": max(hps) if hps else None,
                "bB_values": sorted(set(p["bB"] for p in post_death)),
                "bC_values": sorted(set(p["bC"] for p in post_death)),
                "state10_seen": 10 in states,
                "resurrection_seen": any(p["php"] is not None and p["php"] > 0 for p in post_death[2:]) if len(post_death) > 2 else False,
            }
            L(f"analysis: states={out['post_death_analysis']['g_states_seen']} "
              f"subs={out['post_death_analysis']['g_subs_seen']} "
              f"state10={out['post_death_analysis']['state10_seen']} "
              f"resurrect={out['post_death_analysis']['resurrection_seen']}")

        # ---------- save-trace из stdout ----------
        save_events = []
        try:
            with open(os.path.join(RES5, "runtime-stdout.log"), "rb") as f:
                data = f.read().decode("utf-8", "replace")
            for line in data.splitlines():
                if "RecordStore" in line or "Record" in line:
                    save_events.append(line.strip())
        except Exception:
            pass
        out["save_events"] = save_events[-15:]

        json.dump(out, open(os.path.join(RES5, "death-trace.json"), "w"), indent=1, default=str)
        json.dump({"test": "TEST-005", "generated": time.time(),
                   "damage_events": trace,
                   "note": "каждый damage event: HP_before -> HP_after"},
                  open(os.path.join(RES5, "damage-trace.json"), "w"), indent=1, default=str)
        json.dump({"test": "TEST-005", "generated": time.time(),
                   "post_death": post_death,
                   "death_at": death_at,
                   "note": "частый лог g.a/g.b/g.u/player после HP<=0"},
                  open(os.path.join(RES5, "state-trace.json"), "w"), indent=1, default=str)
        json.dump({"test": "TEST-005", "generated": time.time(),
                   "retry_observed": out.get("post_death_analysis", {}).get("resurrection_seen", False),
                   "state_after_death": out.get("post_death_analysis", {}),
                   "note": "retry = воскрешение/перезагрузка после смерти"},
                  open(os.path.join(RES5, "retry-trace.json"), "w"), indent=1, default=str)
        json.dump({"test": "TEST-005", "generated": time.time(),
                   "save_events": out.get("save_events", []),
                   "note": "RMS события из лога эмулятора"},
                  open(os.path.join(RES5, "save-trace.json"), "w"), indent=1, default=str)
        json.dump(log, open(os.path.join(RES5, "log.json"), "w"), indent=1, default=str)
        L("TEST-005 complete")
    finally:
        emu.stop()

if __name__ == "__main__":
    os.makedirs(RES5, exist_ok=True)
    os.makedirs(EVID5, exist_ok=True)
    main()
