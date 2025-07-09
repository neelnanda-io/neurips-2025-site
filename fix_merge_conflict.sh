#!/bin/bash
# Script to fix the merge conflict and push only the sync script changes

set -e  # Exit on error

echo "=== Fixing Git Merge Conflict ==="
echo "Working directory: $(pwd)"

# First, let's check the current status
echo ""
echo "=== Current Git Status ==="
git status

# Fetch latest from origin
echo ""
echo "=== Fetching from origin ==="
git fetch origin

# Reset to match remote
echo ""
echo "=== Resetting to origin/main ==="
git reset --hard origin/main

# Now add only the files we want
echo ""
echo "=== Adding sync script files ==="
git add scripts/sync_gdocs_html_fixed.py
git add .github/workflows/sync_gdocs.yml

# Show what we're about to commit
echo ""
echo "=== Files to be committed ==="
git status --short

# Commit the changes
echo ""
echo "=== Committing changes ==="
git commit -m "fix: Add improved HTML sync script to handle parsing errors"

# Push to origin
echo ""
echo "=== Pushing to origin ==="
git push

echo ""
echo "=== ✅ Done! ==="
echo "The sync script changes have been pushed."
echo "Content files will be updated by the next GitHub Actions sync."