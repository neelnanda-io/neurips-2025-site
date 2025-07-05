# NeurIPS 2025 Mechanistic Interpretability Workshop

This repository contains the website for the NeurIPS 2025 Mechanistic Interpretability Workshop.

## Architecture

- **Hugo**: Static site generator
- **Netlify**: Hosting and continuous deployment
- **Google Docs**: Content management via Google Drive
- **GitHub Actions**: Automated sync from Google Docs to markdown

## Setup Instructions

See `SETUP_INSTRUCTIONS.md` for detailed setup steps.

## Content Management

Content is managed through Google Docs in a shared folder. The GitHub Action syncs these docs to markdown files hourly.

### Document Mapping

- `main` → Homepage content
- `cfp` → Call for Papers
- `speakers` → Speakers and Panelists (displayed on homepage)
- `schedule` → Workshop Schedule  
- `organizers` → Organizing Committee (displayed on homepage)

### Initial Content Setup

See the `gdocs-content/` folder for markdown files containing all the website content. Copy these into your Google Docs to get started.

## Local Development

```bash
hugo server -D
```

## Deployment

Pushes to `main` branch automatically deploy via Netlify.
