#!/usr/bin/env python3
import os
import struct

T0_PATH = "/home/user/New-look-/research/extracted/jar/t0"
T0_OUT_DIR = "/home/user/New-look-/research/resources/t0"

def main():
    print("Running experimental t0 extractor...")
    if not os.path.exists(T0_PATH):
        print(f"Error: t0 not found at {T0_PATH}")
        return

    with open(T0_PATH, 'rb') as f:
        data = f.read()

    os.makedirs(T0_OUT_DIR, exist_ok=True)

    # First 4 bytes: number of segments
    num_segments = struct.unpack('<I', data[:4])[0]
    print(f"Detected {num_segments} segments in t0 package.")

    # The offset list starts at index 5, each is a 32-bit little-endian int
    offsets = []
    idx = 5
    for i in range(num_segments):
        offset = struct.unpack('<I', data[idx:idx+4])[0]
        offsets.append(offset)
        idx += 4

    print("Segment offsets:")
    for i, offset in enumerate(offsets):
        print(f"  Segment {i:02d}: offset={offset}")

    # Extract each segment
    for i in range(num_segments):
        start = offsets[i]
        # End is the start of the next segment, or EOF for the last one
        end = offsets[i+1] if i + 1 < num_segments else len(data)
        
        segment_data = data[start:end]
        segment_name = f"segment_{i:02d}.bin"
        segment_path = os.path.join(T0_OUT_DIR, segment_name)
        
        with open(segment_path, 'wb') as out_f:
            out_f.write(segment_data)
        print(f"  Extracted segment {i:02d} ({len(segment_data)} bytes) to {segment_path}")

    print("t0 segment extraction completed successfully!")

if __name__ == "__main__":
    main()
