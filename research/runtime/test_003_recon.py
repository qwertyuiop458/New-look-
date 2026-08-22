#!/usr/bin/env python3
"""Разведка TEST-003: mission 03 — L==10, MO (i/cB), сцена."""
import sys, time, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_003_driver import (Emu, build_maps3, snap_global, set_bB, snap_mo,
                             RES3, read_player)
from test_001_driver import snap_entities
from collections import Counter

def main():
    emu = Emu()
    try:
        emu.start(os.path.join(RES3, "recon.log"))
        gid = emu.classes['Lg;'][1]
        gf, ff, cc = build_maps3(emu.jdwp, gid, emu.classes['Lf;'][1], emu.classes['Lc;'][1])
        grid_names = sorted(k[5:] for k in gf if k.startswith('grid_'))
        # до state 16
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
        # загрузка mission 3 (мониторинг bB + FIRE на sub 1)
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
        print('mission 3 loaded: state', g['state'], 'bB', g['bB'], 'by', g['by'], 'bz', g['bz'])
        # мониторинг MO + сцена
        t1 = time.time()
        last_mo = None
        while time.time() - t1 < 60:
            g = snap_global(emu.jdwp, gid, gf)
            mo = snap_mo(emu.jdwp, gid, gf)
            sig = (g['sub'], mo['i'], mo['cB'], mo['cy'], mo['cz'])
            if sig != last_mo:
                print(f"t={time.time()-t1:.1f} sub={g['sub']} i={mo['i']} cB={mo['cB']} "
                      f"cy={mo['cy']} cz={mo['cz']} Q={mo['Q']}")
                last_mo = sig
            if g['sub'] == 0 and mo['i'] == 0 and time.time() - t1 > 10:
                break
            time.sleep(0.5)
        # разведка L10
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        l10 = [e for e in ents if e['L'] == 10 and e['x']]
        print('L10 total:', len(l10))
        g0dist = Counter((e['props'] or [None])[0] for e in l10)
        print('L10 g[0] dist:', dict(sorted(g0dist.items(), key=lambda x: str(x[0]))))
        pl = read_player(emu.jdwp, gid, gf, ff, cc)
        print('player:', (pl['x']>>14, pl['y']>>14) if pl and pl['x'] else None)
        # 15 ближайших L10 к игроку
        if pl and pl['x']:
            near = sorted(l10, key=lambda e: abs(e['x']-pl['x'])+abs(e['y']-pl['y']))[:15]
            for e in near:
                print(f"  L10 g0={(e['props'] or [None])[0]} pos=({e['x']>>14},{e['y']>>14}) "
                      f"grid={e['grid']}{e['i']}{e['j']}{e['k']} props={(e['props'] or [])[:10]}")
        # враги/NPC
        en = [e for e in ents if e['L'] == 3]
        npc = [e for e in ents if e['L'] == 9]
        print('enemies:', len(en), 'states:', dict(sorted(Counter((e['props'] or [None]*20)[12] for e in en).items(), key=lambda x: str(x[0]))))
        print('NPC:', len(npc))
        mo = snap_mo(emu.jdwp, gid, gf)
        print('MO final:', {k: mo[k] for k in ('i','cB','cy','cz','Q','cU','cW','cY','cb','cw','cS')})
    finally:
        emu.stop()

if __name__ == '__main__':
    main()
