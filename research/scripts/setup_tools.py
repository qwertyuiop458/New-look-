#!/usr/bin/env python3
import sys
import os
import urllib.request
import tarfile
import shutil

# Paths
TOOLS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tools"))
JRE_DIR = os.path.join(TOOLS_DIR, "jre")
CFR_JAR_PATH = os.path.join(TOOLS_DIR, "cfr.jar")

# URLs
JRE_URL = "https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.9%2B9/OpenJDK17U-jre_x64_linux_hotspot_17.0.9_9.tar.gz"
CFR_URL = "https://github.com/leibnitz27/cfr/releases/download/0.152/cfr-0.152.jar"

def download_file(url, dest_path):
    print(f"Downloading {url} to {dest_path}...")
    # Clean old file if exists
    if os.path.exists(dest_path):
        os.remove(dest_path)
    
    # Custom User-Agent to avoid issues
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    
    with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
        length = response.getheader('content-length')
        if length:
            length = int(length)
            blocksize = 1024 * 1024
            downloaded = 0
            while True:
                buffer = response.read(blocksize)
                if not buffer:
                    break
                downloaded += len(buffer)
                out_file.write(buffer)
                percent = (downloaded / length) * 100
                print(f"\rProgress: {percent:.1f}% ({downloaded / (1024*1024):.1f} MB / {length / (1024*1024):.1f} MB)", end='', flush=True)
            print()
        else:
            out_file.write(response.read())
            print("Download completed (unknown size).")

def setup_jre():
    os.makedirs(TOOLS_DIR, exist_ok=True)
    tar_path = os.path.join(TOOLS_DIR, "jre.tar.gz")
    
    # Download JRE if not extracted already
    if not os.path.exists(os.path.join(JRE_DIR, "bin", "java")):
        print("JRE not found. Setting up JRE...")
        download_file(JRE_URL, tar_path)
        
        # Extract tar.gz
        print("Extracting JRE...")
        if os.path.exists(JRE_DIR):
            shutil.rmtree(JRE_DIR)
            
        with tarfile.open(tar_path, "r:gz") as tar:
            # The tar has a root folder like jdk-17.0.9+9-jre, we need to extract and rename/move it
            tar.extractall(path=TOOLS_DIR)
            
            # Find the extracted folder
            extracted_folder = None
            for item in os.listdir(TOOLS_DIR):
                if item.startswith("jdk-17") and os.path.isdir(os.path.join(TOOLS_DIR, item)):
                    extracted_folder = os.path.join(TOOLS_DIR, item)
                    break
            
            if extracted_folder:
                os.rename(extracted_folder, JRE_DIR)
                print(f"JRE extracted successfully and moved to {JRE_DIR}")
            else:
                print("Error: Could not find extracted JDK/JRE folder.")
                sys.exit(1)
                
        # Clean up the tar.gz
        if os.path.exists(tar_path):
            os.remove(tar_path)
    else:
        print("JRE already configured.")

def setup_cfr():
    os.makedirs(TOOLS_DIR, exist_ok=True)
    if not os.path.exists(CFR_JAR_PATH):
        print("CFR Decompiler not found. Setting up CFR...")
        download_file(CFR_URL, CFR_JAR_PATH)
        print(f"CFR Decompiler downloaded to {CFR_JAR_PATH}")
    else:
        print("CFR Decompiler already configured.")

def verify_tools():
    print("\nVerifying tools...")
    java_bin = os.path.join(JRE_DIR, "bin", "java")
    if not os.path.exists(java_bin):
        print(f"Error: Java binary not found at {java_bin}")
        return False
    
    # Check java version
    import subprocess
    try:
        res = subprocess.run([java_bin, "-version"], capture_output=True, text=True, check=True)
        print("Java is working:")
        print(res.stderr.strip() if res.stderr else res.stdout.strip())
    except Exception as e:
        print(f"Error executing java: {e}")
        return False
        
    # Check CFR
    try:
        res = subprocess.run([java_bin, "-jar", CFR_JAR_PATH, "--help"], capture_output=True, text=True)
        if "CFR" in res.stderr or "CFR" in res.stdout:
            print("CFR Decompiler is working.")
        else:
            print("Warning: CFR executed but output did not contain 'CFR'.")
            print(res.stdout or res.stderr)
    except Exception as e:
        print(f"Error executing CFR: {e}")
        return False
        
    return True

if __name__ == "__main__":
    setup_jre()
    setup_cfr()
    if verify_tools():
        print("\nAll tools configured successfully!")
    else:
        print("\nTool verification failed.")
        sys.exit(1)
