#!/usr/bin/env python3
import sys
import os
import zipfile
import argparse

def main():
    parser = argparse.ArgumentParser(description="Extract a JAR file completely to a directory.")
    parser.add_argument("jar_path", help="Path to the JAR file to extract")
    parser.add_argument("output_dir", help="Directory where files should be extracted")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.jar_path):
        print(f"Error: JAR file '{args.jar_path}' does not exist.")
        sys.exit(1)
        
    os.makedirs(args.output_dir, exist_ok=True)
    
    print(f"Extracting '{args.jar_path}' to '{args.output_dir}'...")
    with zipfile.ZipFile(args.jar_path, 'r') as jar:
        jar.extractall(args.output_dir)
    print("Extraction completed successfully.")

if __name__ == "__main__":
    main()
