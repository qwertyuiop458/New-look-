#!/usr/bin/env python3
"""TEST-008 v2: прицельные попытки на L14 с g0=39/42/41 (кандидаты-магазины)."""
import os, sys, json, time, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_001_driver import Emu, snap_global, snap_entities, latest_frame
from test_002_driver import read_player, build_maps2
import test_003_driver as t3

RES8 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "test-008")

def main():
    emu = Emu()
    log = []
    t_start = time.time()
    def L(msg):
        log.append({"t": round(time.time()-t_start, 2), "msg": msg})
        print(f"[t8v2] {msg}")
    try:
        emu.start(os.path.join(RES8, "runtime-stdout-v2.log"))
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
        t0 = time.time()
        while time.time() - t0 < 90:
            g = snap_global(emu.jdwp, gid, gf)
            if g["sub"] == 0:
                break
            emu.key("FIRE", hold=0.25)
            time.sleep(2.5)
        L(f"mission 3 sub=0")

        # кандидаты: g0=39 (ближний), 41/42 (повторы — возможно магазины/двери)
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        l14 = [e for e in ents if e["L"] == 14 and e["x"]]
        pl = read_player(emu.jdwp, gid, gf, ff, cc)
        pxy = (pl["x"], pl["y"])
        cands = [e for e in l14 if (e["props"] or [None])[0] in (39, 41, 42, 45, 12)]
        cands.sort(key=lambda e: abs(e["x"]-pxy[0]) + abs(e["y"]-pxy[1]))
        L(f"candidates (g0 in 39/41/42/45/12): {len(cands)}")
        for e in cands[:8]:
            L(f"  cand: ({e['x']>>14},{e['y']>>14}) g0={(e['props'] or [None])[0]} g1={(e['props'] or [None]*2)[1]}")

        shop_opened = False
        for obj in cands[:6]:
            if shop_opened:
                break
            L(f"--- try ({obj['x']>>14},{obj['y']>>14}) g0={(obj['props'] or [None])[0]}")
            t_end = time.time() + 50
            last = None
            stuck = 0
            fired = 0
            while time.time() < t_end:
                g = snap_global(emu.jdwp, gid, gf)
                if g["state"] == 13:
                    L(f"*** NATURAL SHOP ENTRY via ({obj['x']>>14},{obj['y']>>14}) g0={(obj['props'] or [None])[0]}!")
                    shop_opened = True
                    break
                if g["sub"] != 0 and g["state"] == 6:
                    # диалог/взаимодействие началось
                    L(f"  interaction: sub={g['sub']}")
                    emu.key("FIRE", hold=0.2)
                    time.sleep(1.0)
                    continue
                pl = read_player(emu.jdwp, gid, gf, ff, cc)
                if pl is None or pl["x"] is None:
                    time.sleep(0.1); continue
                dx = obj["x"] - pl["x"]; dy = obj["y"] - pl["y"]
                d = (dx*dx + dy*dy) ** 0.5
                if d > 50000:
                    key = "RIGHT" if abs(dx) > abs(dy) and dx > 0 else "LEFT" if abs(dx) > abs(dy) \
                        else "DOWN" if dy > 0 else "UP"
                    emu.key(key, hold=0.25)
                    pos = (pl["x"] >> 14, pl["y"] >> 14)
                    if pos == last:
                        stuck += 1
                        if stuck >= 10:
                            alt = {"UP": "RIGHT", "DOWN": "LEFT", "LEFT": "UP", "RIGHT": "DOWN"}[key]
                            emu.key(alt, hold=0.7)
                            stuck = 0
                    else:
                        stuck = 0
                    last = pos
                else:
                    # рядом: FIRE с разных сторон
                    fired += 1
                    emu.key("FIRE", hold=0.25)
                    time.sleep(1.2)
                    if fired % 3 == 0:
                        emu.key("RIGHT", hold=0.5)
                        time.sleep(0.5)
                    if fired % 3 == 1:
                        emu.key("LEFT", hold=0.5)
                        time.sleep(0.5)
                    g = snap_global(emu.jdwp, gid, gf)
                    if g["state"] == 13:
                        L(f"*** NATURAL SHOP ENTRY!")
                        shop_opened = True
                        break
                time.sleep(0.12)
        L(f"shop_opened={shop_opened}")
        json.dump(log, open(os.path.join(RES8, "log-v2.json"), "w"), indent=1, default=str)
        json.dump({"shop_opened": shop_opened}, open(os.path.join(RES8, "summary-v2.json"), "w"), indent=1)
    finally:
        emu.stop()

if __name__ == "__main__":
    main()
