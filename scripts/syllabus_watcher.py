#!/usr/bin/env python3
import os
import time
import subprocess
import threading

WORKSPACE_ROOT = "/home/sravan/ktu"
SYLLABUS_DIR = os.path.join(WORKSPACE_ROOT, "syllabus")
SCRAPER_SCRIPT = os.path.join(WORKSPACE_ROOT, "scripts", "pyq_scraper_pipeline.py")
PYTHON_EXEC = os.path.join(WORKSPACE_ROOT, "venv", "bin", "python3")

def get_all_syllabus_files():
    """Returns a set of all .txt files currently in the syllabus directory tree."""
    files = set()
    if not os.path.exists(SYLLABUS_DIR):
        return files
        
    for root, _, filenames in os.walk(SYLLABUS_DIR):
        for filename in filenames:
            if filename.endswith(".txt"):
                files.add(os.path.join(root, filename))
    return files

def run_scraper():
    print("\n[WATCHER] New syllabus file detected! Triggering PYQ Scraper Pipeline...")
    # Run the scraper asynchronously so the watcher isn't completely blocked, 
    # though we wait for it so we don't spam multiple triggers
    try:
        subprocess.run([PYTHON_EXEC, SCRAPER_SCRIPT], cwd=WORKSPACE_ROOT, check=True)
        print("[WATCHER] PYQ Scraper Pipeline completed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"[WATCHER ERROR] Pipeline failed with error code {e.returncode}\n")
    except Exception as e:
        print(f"[WATCHER ERROR] Could not run pipeline: {e}\n")

def main():
    print("===================================================")
    print("  KTU Syllabus Watcher & Auto-Scraper is active!   ")
    print("===================================================")
    print(f"Monitoring: {SYLLABUS_DIR}")
    print("Waiting for new syllabus files to be added...\n")
    
    # Initial state
    known_files = get_all_syllabus_files()
    
    try:
        while True:
            time.sleep(2) # Poll every 2 seconds
            
            current_files = get_all_syllabus_files()
            
            # Find new files
            new_files = current_files - known_files
            
            if new_files:
                for f in new_files:
                    print(f"[WATCHER] Detected new file: {os.path.relpath(f, SYLLABUS_DIR)}")
                    
                # Update known files BEFORE running the scraper to avoid duplicate triggers
                known_files = current_files
                
                # We wait an extra second to ensure the file has finished downloading/copying
                time.sleep(1)
                run_scraper()
                print("[WATCHER] Resuming monitoring...\n")
                
            # We also update known files in case files were deleted (we don't trigger on delete)
            known_files = current_files
            
    except KeyboardInterrupt:
        print("\n[WATCHER] Shutting down gracefully.")

if __name__ == "__main__":
    main()
