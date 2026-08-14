#!/usr/bin/env python3
import os
import json
import sys

ANALYSIS_DIR = "/home/user/New-look-/research/analysis"
REGISTRY_JSON = os.path.join(ANALYSIS_DIR, "entities", "entity-registry.json")
WEAPONS_JSON = os.path.join(ANALYSIS_DIR, "combat", "weapons.json")

def validate_mechanics():
    print("Starting game mechanics specifications validation check...")
    errors = 0

    # 1. Check entity-registry.json
    if not os.path.exists(REGISTRY_JSON):
        print(f"  [ERROR] Registry file missing: {REGISTRY_JSON}")
        errors += 1
    else:
        with open(REGISTRY_JSON, 'r') as f:
            data = json.load(f)
        for ent in data["entities"]:
            # Check non-empty ID and health
            if not ent["id"] or ent["health"]["initial"] <= 0:
                print(f"  [ERROR] Invalid entity in registry: {ent['id']}")
                errors += 1

    # 2. Check weapons.json
    if not os.path.exists(WEAPONS_JSON):
        print(f"  [ERROR] Weapons file missing: {WEAPONS_JSON}")
        errors += 1
    else:
        with open(WEAPONS_JSON, 'r') as f:
            data = json.load(f)
        for wp in data:
            if wp["damage"] <= 0 or wp["ammo_capacity"] <= 0:
                print(f"  [ERROR] Invalid weapon configuration: {wp['name']}")
                errors += 1

    if errors == 0:
        print("  [SUCCESS] All mechanics specifications validated successfully with 0 errors!")
    else:
        print(f"  [FAILURE] Mechanics validation failed with {errors} errors.")
        sys.exit(1)

if __name__ == "__main__":
    validate_mechanics()
