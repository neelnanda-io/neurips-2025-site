#!/bin/bash
# Script to remove old sync scripts after migrating to unified version

echo "=== Removing old sync scripts ==="

# List of old scripts to remove
OLD_SCRIPTS=(
    "sync_gdocs.py"
    "sync_gdocs_enhanced.py"
    "sync_gdocs_html.py"
    "sync_gdocs_html_fixed.py"
    "sync_gdocs_robust.py"
)

# Remove each old script
for script in "${OLD_SCRIPTS[@]}"; do
    if [ -f "scripts/$script" ]; then
        rm "scripts/$script"
        echo "✓ Removed scripts/$script"
    else
        echo "- scripts/$script not found (already removed?)"
    fi
done

echo ""
echo "=== Cleanup complete ==="
echo "The unified script is now at: scripts/sync_gdocs_unified.py"
echo "Documentation is at: scripts/README_sync_scripts.md"