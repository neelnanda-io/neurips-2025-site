#!/usr/bin/env python3
import subprocess
import os

# Change to the project directory
os.chdir('/Users/neelnanda/Code/mech-interp-website/neurips-2025-site')

commands = [
    ['git', 'fetch', 'origin'],
    ['git', 'reset', '--hard', 'origin/main'],
    ['git', 'add', 'scripts/sync_gdocs_html_fixed.py'],
    ['git', 'add', '.github/workflows/sync_gdocs.yml'],
    ['git', 'commit', '-m', 'fix: Add improved HTML sync script to handle parsing errors'],
    ['git', 'push']
]

for cmd in commands:
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")
    if result.returncode != 0:
        print(f"Command failed with return code {result.returncode}")
        break
    print("---")

print("Done!")