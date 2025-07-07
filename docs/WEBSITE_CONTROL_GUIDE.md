# NeurIPS 2025 Website Control Guide

This guide explains all the files you need to manage your workshop website and how to edit them properly.

## Content Management Overview

Your website has **two sources of truth**:
1. **Google Docs** - For all main content (synced hourly)
2. **GitHub Repository** - For configuration, styling, and data files

## Files You Control

### 1. Google Docs Content (Edit in Google Drive)

These documents in your Google Drive folder control the main content:
- **main** → Homepage content
- **cfp** → Call for Papers page
- **schedule** → Draft Schedule page
- **speakers** → Speakers page (if you create one)
- **organizers** → Organizers page (if you create one)

**How to edit**: 
- Edit directly in Google Docs
- Changes sync automatically every hour
- Manual sync: Go to GitHub Actions → "Sync Google Docs" → "Run workflow"

**Important**: Never edit the markdown files in `content/` directory - they're auto-generated!

### 2. Speaker & Organizer Data Files (Edit in GitHub)

#### `/data/speakers.yaml`
Controls the speaker grid on the homepage.

```yaml
speakers:
  - name: "Chris Olah"
    affiliation: "Interpretability Lead and Co-founder, Anthropic"
    website: "https://colah.github.io/about.html"
    image: "chrisolah.jpeg"  # Image must be in /static/img/
```

#### `/data/organizers.yaml`
Controls the organizers grid on the homepage.

```yaml
organizers:
  - name: "Neel Nanda"
    affiliation: "Senior Research Scientist, Google DeepMind"
    website: "https://www.neelnanda.io/about"
    image: "neelnanda.jpeg"  # Image must be in /static/img/
```

**How to edit**: 
- Edit directly on GitHub (web interface) OR
- Clone locally, edit, commit, and push

### 3. Configuration Files

#### `/config.yaml`
Main site configuration and navigation menu.

```yaml
baseURL: "https://neurips-2025-site.netlify.app/"  # Your actual URL
title: "NeurIPS 2025 Mechanistic Interpretability Workshop"

menu:
  main:
    - name: "Home"
      url: "/"
      weight: 1
    - name: "Call for Papers"
      url: "/cfp/"
      weight: 2
```

**What you can change**:
- Site title
- Base URL (when you get custom domain)
- Navigation menu items
- Site description in params

### 4. Styling Files

#### `/assets/css/main.css`
Controls all visual styling.

Key sections you might want to edit:
- `.speaker img` - Speaker image size (currently 120px)
- `.organizers .speaker div` - Organizer text box width
- Color scheme (search for `#667eea` to find purple accent color)
- `.mailing-list-form` - Mailing list form styling

### 5. Layout Templates

#### `/layouts/index.html`
Homepage template - controls structure of homepage.

Key sections:
- Mailing list form (Buttondown integration)
- Speaker grid display
- Organizer grid display

Only edit if you need to:
- Change homepage structure
- Add new sections
- Modify how speakers/organizers display

### 6. Images

#### `/static/img/`
All speaker and organizer photos go here.

Requirements:
- Use JPEG format for photos
- Recommended: Square images, at least 240x240px
- Filename must match what's in YAML files
- Will be displayed as circles (border-radius: 50%)

### 7. Environment Variables

#### `/.env` (Local only, not in GitHub)
```
GOOGLE_SERVICE_ACCOUNT_KEY={"type":"service_account",...}
GDOCS_FOLDER_ID=your-folder-id-here
```

**Never commit this file!** It contains secrets.

### 8. GitHub Secrets (Set in GitHub Settings)

Go to Settings → Secrets and variables → Actions:
- `GOOGLE_SERVICE_ACCOUNT_KEY` - Same JSON as in .env
- `GDOCS_FOLDER_ID` - Your Google Drive folder ID

## Workflow for Common Tasks

### Adding a New Speaker
1. Add their photo to `/static/img/`
2. Edit `/data/speakers.yaml` to add their entry
3. Commit and push (or edit directly on GitHub)

### Changing Site Colors
1. Edit `/assets/css/main.css`
2. Search for color codes (e.g., `#667eea` for purple)
3. Replace with your preferred colors
4. Commit and push

### Adding a New Page
1. Create new document in Google Docs
2. Name it appropriately (e.g., "sponsors")
3. Add to `/scripts/sync_gdocs.py` in DOC_MAPPING
4. Add to navigation in `/config.yaml`
5. Create folder in `/content/` if needed

### Updating Workshop Details
1. Edit the relevant Google Doc
2. Wait for hourly sync OR
3. Trigger manual sync in GitHub Actions

### Custom Domain Setup
1. Update `baseURL` in `/config.yaml`
2. Configure domain in Netlify dashboard
3. Update DNS settings with your domain provider

## Important Notes

1. **Content Hierarchy**:
   - Google Docs content always wins for `/content/` files
   - Local changes to `/content/` will be overwritten
   - Data files (`/data/`) are never overwritten by sync

2. **Testing Changes**:
   - Run `hugo server` locally to preview
   - Check Netlify preview deploys for PRs
   - Use GitHub Actions logs to debug sync issues

3. **Debugging Sync Issues**:
   - Check GitHub Actions logs
   - Verify Google Docs are in correct folder
   - Ensure document names match DOC_MAPPING
   - Check service account has access to docs

4. **Performance Tips**:
   - Optimize images before uploading (< 500KB recommended)
   - Keep speaker photos consistent in size
   - Use web-friendly formats (JPEG for photos)

## Quick Reference

| What to Change | Where to Edit | How to Edit |
|----------------|---------------|-------------|
| Page content | Google Docs | Direct editing |
| Speakers list | `/data/speakers.yaml` | GitHub or local |
| Organizers list | `/data/organizers.yaml` | GitHub or local |
| Navigation menu | `/config.yaml` | GitHub or local |
| Colors & styling | `/assets/css/main.css` | GitHub or local |
| Speaker photos | `/static/img/` | Upload to GitHub |
| Site structure | `/layouts/` | Local editing only |

## Getting Help

- Hugo documentation: https://gohugo.io/documentation/
- Netlify documentation: https://docs.netlify.com/
- GitHub Actions: Check the "Actions" tab for sync logs
- Build errors: Check Netlify dashboard for deploy logs