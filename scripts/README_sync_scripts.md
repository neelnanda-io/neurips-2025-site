# Google Docs Sync Scripts Documentation

## Current Status: Unified Script

As of January 2025, we have consolidated all sync functionality into a single script: `sync_gdocs_unified.py`

### Features of the Unified Script

The unified script combines the best features from all previous versions:

1. **HTML Export with Formatting** (from sync_gdocs_html_fixed.py)
   - Preserves bold, italic, links
   - Converts headers, lists, paragraphs
   - Handles tables (with manual conversion note)

2. **Robust Error Handling** (from sync_gdocs_robust.py)
   - Falls back to plain text if HTML parsing fails
   - Creates debug files for failed HTML parsing
   - Continues processing other documents on failure

3. **Two Document Support**
   - Main content documents → content/*.md
   - Extra content document → data/extra_content.yaml

4. **Content Filtering**
   - Removes duplicate sections handled by template
   - Filters out speakers, schedule, organizers sections

5. **Image Placeholder Processing**
   - Converts {{Image: filename}} to HTML img tags
   - Auto-adds .jpg extension if missing

### Features Gained vs Lost

**Features Gained:**
- ✅ Single script to maintain (no confusion about which to use)
- ✅ Best of all approaches with automatic fallback
- ✅ Support for extra_content document
- ✅ Debug output for troubleshooting
- ✅ More maintainable codebase

**Features Lost:**
- ❌ Enhanced script's Google Docs API features (tables, inline images)
- ❌ Image tracking/IMAGES_NEEDED.md generation
- ❌ Multiple image placeholder pattern support
- ❌ Shortcode processing (now handled separately)

**Trade-offs Accepted:**
- Using HTML export instead of Docs API is simpler and more reliable
- Table support is basic (marked for manual conversion)
- Image tracking can be added back if needed

### Migration Instructions

1. Update `.github/workflows/sync_gdocs.yml`:
```yaml
- name: Pull Google Docs → Markdown
  env:
    GOOGLE_SERVICE_ACCOUNT_KEY: ${{ secrets.GOOGLE_SERVICE_ACCOUNT_KEY }}
    GDOCS_FOLDER_ID: ${{ secrets.GDOCS_FOLDER_ID }}
  run: |
    python scripts/sync_gdocs_unified.py
```

2. Remove old sync scripts:
```bash
rm scripts/sync_gdocs.py
rm scripts/sync_gdocs_enhanced.py
rm scripts/sync_gdocs_html.py
rm scripts/sync_gdocs_html_fixed.py
rm scripts/sync_gdocs_robust.py
```

3. The script handles both regular content and extra_content:
   - Documents with "extra_content" in name → `data/extra_content.yaml`
   - Other documents → appropriate content/*.md files

### Document Naming Convention

The script determines output location based on document names:
- Contains "extra_content" → `data/extra_content.yaml`
- Contains "schedule" → `content/schedule/_index.md`
- Contains "cfp" or "call" → `content/cfp/_index.md`
- Contains "faq" → `content/faq/_index.md`
- Default → `content/_index.md`

### Environment Variables Required

- `GOOGLE_SERVICE_ACCOUNT_KEY`: JSON service account credentials
- `GDOCS_FOLDER_ID`: Google Drive folder containing documents

### How It Works

1. Authenticates with Google using service account
2. Lists all Google Docs in the specified folder
3. For each document:
   - Exports as HTML (preserves formatting)
   - Parses HTML to Markdown
   - If parsing fails, falls back to plain text export
   - Filters out duplicate content (for main pages)
   - Saves to appropriate location
4. Reports success/failure summary

### Debugging

If HTML parsing fails:
- Check `debug_[docname].html` files for the raw HTML
- These files show what Google exported
- Common issues: malformed HTML, unsupported elements

### Future Enhancements

If needed, we could add back:
- Google Docs API for better table support
- Image usage tracking
- More sophisticated HTML parsing
- Support for embedded drawings/charts