#!/bin/bash
# Reset to remote state and push only the sync script fixes

echo "=== Resetting to remote state ==="
git fetch origin
git reset --hard origin/main

echo "=== Re-applying only the sync script changes ==="
# The sync script changes are what we actually want to keep
git add scripts/sync_gdocs_html_fixed.py
git add .github/workflows/sync_gdocs.yml

echo "=== Committing sync fixes ==="
git commit -m "fix: Add improved HTML sync script to handle parsing errors

- Add sync_gdocs_html_fixed.py with better error handling
- Update GitHub Actions to prefer the fixed HTML sync script
- This should prevent content truncation during sync"

echo "=== Pushing changes ==="
git push

echo "=== Done! ==="
echo "The content files will be updated by the next GitHub Actions sync"