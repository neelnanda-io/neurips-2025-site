# Google Docs Formatting Guide

## Overview

The new HTML-based sync script (`sync_gdocs_html.py`) preserves formatting from Google Docs. This means you can use normal Google Docs formatting and it will be converted to proper markdown.

## What You Can Use in Google Docs

### Headers
- Use Google Docs heading styles (Format → Paragraph styles → Heading 1, 2, 3, etc.)
- These will be converted to markdown headers (# ## ### etc.)
- No need to write in ALL CAPS anymore

### Bold and Italic Text
- **Bold**: Use Ctrl/Cmd+B or the bold button
- *Italic*: Use Ctrl/Cmd+I or the italic button
- These will be converted to markdown **bold** and *italic*

### Links
- Create links normally in Google Docs (Insert → Link or Ctrl/Cmd+K)
- They will be converted to markdown links: [text](url)

### Lists
- Use normal bullet points or numbered lists in Google Docs
- They will be converted to markdown lists
- Nested lists are supported

### Paragraph Breaks
- Normal paragraph breaks (Enter key) will be preserved
- No need for special formatting

### Images
Use these special tags in your document:
- Single image: `[IMAGE: filename.jpg]`
- Image pair: `[IMAGE-PAIR: image1.jpg | image2.jpg | Caption text]`

### Dynamic Content Shortcodes
Use these tags to insert dynamic sections:
- `[SPEAKERS]` - Inserts the speakers section
- `[ORGANIZERS]` - Inserts the organizers section
- `[SCHEDULE]` - Inserts the schedule table
- `[SIGNUP]` - Inserts the mailing list signup form

Case doesn't matter - `[speakers]`, `[Speakers]`, `[SPEAKERS]` all work.

## Example Google Doc Content

```
Heading 1 (using Google Docs style)

This is a paragraph with **bold text** and *italic text*. Here's a [link to our website](https://mechinterpworkshop.com).

Heading 2 (using Google Docs style)

Here's a list:
• First item
• Second item with **bold**
• Third item

Another paragraph after the list.

[SPEAKERS]

More content here.

[IMAGE-PAIR: conference-pic.jpg | rooftop-pic.jpg | Photos from ICML 2024]
```

## Manual Steps

1. Make your changes in Google Docs using normal formatting
2. The GitHub Action will automatically sync every hour
3. To trigger manual sync:
   - Go to GitHub → Actions → "Sync Google Docs"
   - Click "Run workflow"

## Commit the Changes

To activate the new HTML sync:

```bash
git add scripts/sync_gdocs_html.py
git add .github/workflows/sync_gdocs.yml
git add GOOGLE_DOCS_FORMATTING.md
git commit -m "feat: Add HTML-based Google Docs sync for better formatting preservation"
git push
```

The next sync will use the HTML export and preserve all your formatting!