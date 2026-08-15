#!/usr/bin/env python3
"""Валидатор TEST-001: проверяет evidence, quality gate и целостность JAR."""
import json, os, sys, hashlib

ROOT = "/home/user/New-look-/research/runtime"
JAR_SHA = "1111f12bd94e5693bbdd9acab4726e5b543730b9137504af1e8a8ecb09f00d4e"

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def main():
    ok = True
    def check(cond, msg):
        nonlocal ok
        print(("PASS" if cond else "FAIL"), "-", msg)
        if not cond:
            ok = False

    jar = os.path.join(ROOT, "jar", "original.jar")
    check(os.path.exists(jar) and sha(jar) == JAR_SHA, f"original.jar SHA-256 {JAR_SHA}")
    inst = os.path.join(ROOT, "jar", "instrumented.jar")
    check(os.path.exists(inst) and sha(inst) == JAR_SHA, "instrumented.jar == original.jar (bytes)")

    smoke = json.load(open(os.path.join(ROOT, "results", "test-001", "input-smoke-test.json")))
    check(smoke.get("verdict") == "KEY_RECEIVED", "input-smoke-test: KEY_RECEIVED")

    st = json.load(open(os.path.join(ROOT, "results", "test-001", "state-trace.json")))
    gs = [s["global"] for s in st["snapshots"] if s["global"].get("state") == 6]
    check(len(gs) > 0, "state-trace: gameplay (state 6) достигнут")

    et = json.load(open(os.path.join(ROOT, "results", "test-001", "entity-trace.json")))
    n = max((s["count"] for s in et["snapshots"]), default=0)
    check(n > 0, f"entity-trace: {n} реальных сущностей")

    for f in ["boot.png", "menu.png", "profile.png", "character-select.png",
              "loading.png", "gameplay.png", "first-entity.png"]:
        p = os.path.join(ROOT, "evidence", "real", "test-001", f)
        check(os.path.exists(p) and os.path.exists(p + ".json"), f"evidence {f} + metadata")

    gate = json.load(open("/home/user/New-look-/research/analysis/audit/runtime-test-001-readiness.json"))
    check(gate.get("status") == "PASSED", "quality gate: PASSED")

    cmp = json.load(open(os.path.join(ROOT, "results", "test-001", "comparison.json")))
    mism = [i for i in cmp["items"] if i["result"] == "MISMATCH"]
    check(len(mism) == 0, f"comparison: 0 MISMATCH (всего {len(cmp['items'])})")

    print("\nRESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
