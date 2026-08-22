#!/usr/bin/env python3
"""TEST-003: FIRE-марафон в mission 03 — мониторинг i/cB/bO/bQ."""
import sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_003_driver import (Emu, build_maps3, snap_global, set_bB, snap_mo,
                             RES3, read_player)

def main():
    emu = Emu()
    try:
        emu.start(os.path.join(RES3, "marathon.log"))
        gid = emu.classes['Lg;'][1]
        gf, ff, cc = build_maps3(emu.jdwp, gid, emu.classes['Lf;'][1], emu.classes['Lc;'][1])
        bof = bqf = None
        for fid_, name, sig, mod in emu.jdwp.fields(gid):
            if name == 'bO' and sig == 'I': bof = fid_
            if name == 'bQ' and sig == 'I': bqf = fid_
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
        print('mission 3 loaded')
        # FIRE-марафон 4 минуты
        t1 = time.time()
        last = None
        fired = 0
        while time.time() - t1 < 240:
            g = snap_global(emu.jdwp, gid, gf)
            mo = snap_mo(emu.jdwp, gid, gf)
            bq = emu.jdwp.get_static(gid, [bqf])[0][1] if bqf else None
            bo = emu.jdwp.get_static(gid, [bof])[0][1] if bof else None
            pl = read_player(emu.jdwp, gid, gf, ff, cc)
            sig = (mo['i'], mo['cB'], bo, bq, g['sub'])
            if sig != last:
                print(f"t={time.time()-t1:.0f} i={mo['i']} cB={mo['cB']} cy={mo['cy']} cz={mo['cz']} "
                      f"Q={mo['Q']} bO={bo} bQ={bq} sub={g['sub']} "
                      f"pl={((pl['x']>>14) if pl and pl['x'] else '?', (pl['y']>>14) if pl and pl['y'] else '?')}")
                last = sig
            if mo['i'] or mo['cB']:
                print(f'*** MO ACTIVATED: i={mo["i"]} cB={mo["cB"]} Q={mo["Q"]}')
                break
            emu.key('FIRE', hold=0.2)
            fired += 1
            time.sleep(2.0)
        print(f'fired {fired} times; final i={snap_mo(emu.jdwp, gid, gf)["i"]} '
              f'cB={snap_mo(emu.jdwp, gid, gf)["cB"]}')
    finally:
        emu.stop()

if __name__ == '__main__':
    main()
