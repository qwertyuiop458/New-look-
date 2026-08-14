#!/usr/bin/env python3
import os
import json

# Paths
PALETTE_BIN_PATH = "/home/user/New-look-/research/extracted/jar/palettesAmount.bin"
PALETTES_OUT_DIR = "/home/user/New-look-/research/resources/palettes"

def main():
    print("Extracting palettesAmount.bin...")
    if not os.path.exists(PALETTE_BIN_PATH):
        print(f"Error: palettesAmount.bin not found at {PALETTE_BIN_PATH}")
        return

    with open(PALETTE_BIN_PATH, 'rb') as f:
        data = f.read()

    os.makedirs(PALETTES_OUT_DIR, exist_ok=True)

    num_palettes = data[0]
    print(f"Number of palettes: {num_palettes}")

    idx = 1
    palettes_json = {}

    for i in range(num_palettes):
        if idx >= len(data):
            print(f"Warning: Unexpected EOF at index {idx}")
            break
        pal_len = data[idx]
        pal_data = list(data[idx+1 : idx+1+pal_len])
        idx += 1 + pal_len

        palette_name = f"palette_{i:02d}.json"
        pal_path = os.path.join(PALETTES_OUT_DIR, palette_name)
        
        # Save individual JSON
        with open(pal_path, 'w', encoding='utf-8') as out_f:
            json.dump({"palette_id": i, "length_bytes": pal_len, "mapping": pal_data}, out_f, indent=4)

        palettes_json[f"palette_{i:02d}"] = pal_data

    # Also save a combined JSON for easy reading
    with open(os.path.join(PALETTES_OUT_DIR, "all_palettes.json"), 'w', encoding='utf-8') as out_f:
        json.dump(palettes_json, out_f, indent=4)

    print(f"Successfully extracted {num_palettes} palettes to {PALETTES_OUT_DIR}")

if __name__ == "__main__":
    main()
