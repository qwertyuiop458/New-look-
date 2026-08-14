#!/usr/bin/env python3
import os
import struct

EXTRACTED_DIR = "/home/user/New-look-/research/extracted/jar"
OUT_LEVELS_DIR = "/home/user/New-look-/research/resources/levels"

def extract_pack(filepath, out_dir):
    with open(filepath, 'rb') as f:
        data = f.read()

    if not data:
        return

    # First byte is the number of segments
    num_segments = data[0]
    
    # Read offsets
    offsets = []
    idx = 1
    for _ in range(num_segments):
        if idx + 4 > len(data):
            break
        offset = struct.unpack('<I', data[idx:idx+4])[0]
        offsets.append(offset)
        idx += 4

    os.makedirs(out_dir, exist_ok=True)

    # Save meta
    meta = {
        "filename": os.path.basename(filepath),
        "num_segments": num_segments,
        "offsets": offsets
    }
    with open(os.path.join(out_dir, "meta.json"), 'w', encoding='utf-8') as out_f:
        import json
        json.dump(meta, out_f, indent=4)

    # Extract segments
    for i in range(num_segments):
        start = offsets[i]
        end = offsets[i+1] if i + 1 < num_segments else len(data)
        
        # Guard boundaries
        if start >= len(data) or end > len(data) or start > end:
            print(f"  Warning: Invalid segment boundaries for seg {i:02d} in {os.path.basename(filepath)}")
            continue

        seg_data = data[start:end]
        seg_path = os.path.join(out_dir, f"segment_{i:02d}.bin")
        with open(seg_path, 'wb') as out_f:
            out_f.write(seg_data)

def main():
    print("Starting extraction of all 'm' map pack resources...")
    if not os.path.exists(EXTRACTED_DIR):
        print(f"Error: Extracted JRE directory not found at {EXTRACTED_DIR}")
        return

    m_files = sorted([f for f in os.listdir(EXTRACTED_DIR) if f.startswith("m") and not f.endswith(".class") and f != "meta-inf" and f != "META-INF"])
    
    for m_file in m_files:
        filepath = os.path.join(EXTRACTED_DIR, m_file)
        dest_dir = os.path.join(OUT_LEVELS_DIR, m_file)
        print(f"Unpacking {m_file} ({os.path.getsize(filepath)} bytes)...")
        extract_pack(filepath, dest_dir)

    print("\nExtraction of all map packs completed successfully!")

if __name__ == "__main__":
    main()
