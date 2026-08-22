#!/usr/bin/env python3
"""TEST-003: NPC-диалог + широкий обход к северу (тайл 31)."""
import sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_003_driver import (Emu, build_maps3, snap_global, set_bB, snap_mo,
                             RES3, read_player)
from test_001_driver import snap_entities

LOG = os.path.join(RES3, "npc-progress.log")
def log(msg):
    with open(LOG, "a") as f:
        f.write(f"{time.time():.1f} {msg}\n")

def main():
    emu = Emu()
    try:
        emu.start(os.path.join(RES3, "npc.log"))
        gid = emu.classes['Lg;'][1]
        gf, ff, cc = build_maps3(emu.jdwp, gid, emu.classes['Lf;'][1], emu.classes['Lc;'][1])
        grid_names = sorted(k[5:] for k in gf if k.startswith('grid_'))
        time.sleep(6)
        for _ in range(8):
            if snap_global(emu.jdwp, gid, gf)['u'] == 0:
                break
            emu.key('FIRE', hold=0.15); time.sleep(2.5)
        emu.key('FIRE', hold=0.15); time.sleep(2)
        emu.key('FIRE', hold=0.15); time.sleep(3)
        for _ in range(4):
            if snap_global(emu.jdwp, gid, gf)['u'] == 9:
                break
            emu.key('FIRE', hold=0.15); time.sleep(2.5)
        emu.key('FIRE', hold=0.15); time.sleep(3)
        set_bB(emu.jdwp, gid, gf, 3)
        t0 = time.time()
        while time.time() - t0 < 120:
            g = snap_global(emu.jdwp, gid, gf)
            if g['bB'] == 0 and g['state'] in (16, 4, 2):
                set_bB(emu.jdwp, gid, gf, 3)
            if g['state'] == 6:
                break
            if g['state'] == 2 and g['sub'] == 1:
                emu.key('FIRE', hold=0.2); time.sleep(0.5)
            else:
                time.sleep(0.005)
        t1 = time.time()
        while time.time() - t1 < 60:
            g = snap_global(emu.jdwp, gid, gf)
            if g['sub'] == 0:
                break
            emu.key('FIRE', hold=0.25)
            time.sleep(2.5)
        log('mission 3 sub=0')
        def goto(tx, ty, timeout=60, label=''):
            pl = read_player(emu.jdwp, gid, gf, ff, cc)
            log(f'goto {label} ({tx},{ty}) from ({pl["x"]>>14},{pl["y"]>>14})')
            t_end = time.time() + timeout
            last = None
            stuck = 0
            while time.time() < t_end:
                g = snap_global(emu.jdwp, gid, gf)
                mo = snap_mo(emu.jdwp, gid, gf)
                if mo['i'] or mo['cB']:
                    log(f'*** MO: i={mo["i"]} cB={mo["cB"]} Q={mo["Q"]}')
                    return True
                pl = read_player(emu.jdwp, gid, gf, ff, cc)
                if not pl or not pl['x']:
                    break
                pos = (pl['x']>>14, pl['y']>>14)
                if pos != last:
                    log(f'pos={pos} bz={g["bz"]} sub={g["sub"]}')
                    last = pos
                if g['sub'] == 1:
                    emu.key('FIRE', hold=0.25)
                    time.sleep(1.2)
                    continue
                dx = tx*16384 - pl['x']; dy = ty*16384 - pl['y']
                d = (dx*dx + dy*dy) ** 0.5
                if d < 15000:
                    log(f'arrived ({tx},{ty})')
                    return False
                key = None
                if abs(dx) > abs(dy):
                    key = 'RIGHT' if dx > 0 else 'LEFT'
                else:
                    key = 'DOWN' if dy > 0 else 'UP'
                emu.key(key, hold=0.25)
                if last == pos:
                    stuck += 1
                    if stuck >= 6:
                        alt = {'UP':'RIGHT','DOWN':'LEFT','LEFT':'UP','RIGHT':'DOWN'}[key]
                        emu.key(alt, hold=0.8)
                        stuck = 0
                time.sleep(0.12)
            return False
        # ближайший NPC
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        npc = [e for e in ents if e['L'] == 9 and e['x']]
        pl = read_player(emu.jdwp, gid, gf, ff, cc)
        if npc and pl:
            near = min(npc, key=lambda e: abs(e['x']-pl['x'])+abs(e['y']-pl['y']))
            log(f'npc near: ({near["x"]>>14},{near["y"]>>14})')
            goto(near['x']>>14, near['y']>>14, 60, 'npc')
            for i in range(8):
                emu.key('FIRE', hold=0.25)
                time.sleep(1.5)
                g = snap_global(emu.jdwp, gid, gf)
                mo = snap_mo(emu.jdwp, gid, gf)
                log(f'npc FIRE {i}: sub={g["sub"]} i={mo["i"]} cB={mo["cB"]}')
                if mo['i']:
                    break
        # широкий обход: запад -> север -> восток
        goto(30, 509, 60, 'west')
        goto(30, 50, 90, 'north')
        goto(32, 112, 60, 'tile31')
        goto(64, 0, 60, 'tile31b')
        g = snap_global(emu.jdwp, gid, gf)
        mo = snap_mo(emu.jdwp, gid, gf)
        log(f'FINAL: bz={g["bz"]} i={mo["i"]} cB={mo["cB"]}')
    finally:
        emu.stop()

if __name__ == '__main__':
    main()
