#!/usr/bin/env python3
"""
Fix the git merge conflict by resetting to origin/main
and re-adding only the sync script files
"""
import subprocess
import os
import sys

def run_command(cmd, cwd=None):
    """Run a command and print output"""
    print(f"\n=== Running: {' '.join(cmd)} ===")
    try:
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"stderr: {result.stderr}", file=sys.stderr)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        raise

def main():
    # Change to the project directory
    project_dir = "/Users/neelnanda/Code/mech-interp-website/neurips-2025-site"
    os.chdir(project_dir)
    print(f"Working directory: {os.getcwd()}")
    
    try:
        # Check current status
        print("\n=== Current Git Status ===")
        run_command(["git", "status"])
        
        # Fetch from origin
        print("\n=== Fetching from origin ===")
        run_command(["git", "fetch", "origin"])
        
        # Reset to origin/main
        print("\n=== Resetting to origin/main ===")
        run_command(["git", "reset", "--hard", "origin/main"])
        
        # Add only the files we want
        print("\n=== Adding sync script files ===")
        run_command(["git", "add", "scripts/sync_gdocs_html_fixed.py"])
        run_command(["git", "add", ".github/workflows/sync_gdocs.yml"])
        
        # Show what we're about to commit
        print("\n=== Files to be committed ===")
        run_command(["git", "status", "--short"])
        
        # Commit the changes
        print("\n=== Committing changes ===")
        commit_message = "fix: Add improved HTML sync script to handle parsing errors"
        run_command(["git", "commit", "-m", commit_message])
        
        # Push to origin
        print("\n=== Pushing to origin ===")
        run_command(["git", "push"])
        
        print("\n=== ✅ Done! ===")
        print("The sync script changes have been pushed.")
        print("Content files will be updated by the next GitHub Actions sync.")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error occurred: {e}")
        print("Please check the error messages above and fix any issues.")
        sys.exit(1)

if __name__ == "__main__":
    main()