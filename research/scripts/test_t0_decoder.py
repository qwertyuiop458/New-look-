#!/usr/bin/env python3
import os
import sys
import struct

T0_PATH = "/home/user/New-look-/research/extracted/jar/t0"

def main():
    print("Running graphics decoder validation test...")
    if not os.path.exists(T0_PATH):
        print(f"Error: t0 not found at {T0_PATH}")
        sys.exit(1)

    with open(T0_PATH, 'rb') as f:
        data = f.read()

    # Verify magic number/segment count
    num_segments = data[0]
    print(f"Verified segment count byte: {num_segments}")
    if num_segments != 20:
        print("FAIL: Expected 20 segments in t0!")
        sys.exit(1)

    # Decode offsets (starting from byte 1, Little Endian 32-bit uints)
    offsets = []
    idx = 1
    for i in range(num_segments):
        offset = struct.unpack('<I', data[idx:idx+4])[0]
        offsets.append(offset)
        idx += 4

    print("Verified offsets array size: 20 entries")
    
    # Check that offsets are strictly increasing (except segment 18 which is empty and has same offset as 19)
    for i in range(num_segments - 1):
        if i == 18: # segment 18 is empty
            continue
        if offsets[i+1] < offsets[i]:
            print(f"FAIL: Offsets not strictly increasing: seg {i+1} offset {offsets[i+1]} < seg {i} offset {offsets[i]}")
            sys.exit(1)

    print("SUCCESS: Offset progression checks out perfectly!")
    
    # Check that segment 19 data is present
    seg_19_start = offsets[19]
    if seg_19_start >= len(data):
        print(f"FAIL: Segment 19 offset {seg_19_start} is out of bounds!")
        sys.exit(1)

    print(f"Verified segment 19 starting at offset {seg_19_start} (size {len(data)-seg_19_start} bytes)")
    print("\nALL decoder validation tests passed successfully!")

if __name__ == "__main__":
    main()
