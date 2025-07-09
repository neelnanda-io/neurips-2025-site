#!/usr/bin/env python3
import os
import sys

# Files to remove
files_to_remove = [
    "/Users/neelnanda/Code/mech-interp-website/neurips-2025-site/scripts/sync_gdocs.py",
    "/Users/neelnanda/Code/mech-interp-website/neurips-2025-site/scripts/sync_gdocs_enhanced.py",
    "/Users/neelnanda/Code/mech-interp-website/neurips-2025-site/scripts/sync_gdocs_html.py",
    "/Users/neelnanda/Code/mech-interp-website/neurips-2025-site/scripts/sync_gdocs_html_fixed.py",
    "/Users/neelnanda/Code/mech-interp-website/neurips-2025-site/scripts/sync_gdocs_robust.py"
]

print("Removing old sync script files...")
for file_path in files_to_remove:
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"✓ Removed: {os.path.basename(file_path)}")
        else:
            print(f"- File not found: {os.path.basename(file_path)}")
    except Exception as e:
        print(f"✗ Error removing {os.path.basename(file_path)}: {e}")

print("\nRemoval complete!")