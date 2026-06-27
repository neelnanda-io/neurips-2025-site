# NeurIPS 2025 Mechanistic Interpretability Workshop

This repository contains the Hugo website for the Mechanistic Interpretability
Workshop. It currently serves the **ICML 2026** edition (`mechinterpworkshop.com`);
the **NeurIPS 2025** site is archived under `/neurips2025/`.

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

## Accepted Posters page

The accepted-papers listing lives at two pages:

- `/posters/` — in-person posters (spotlights showcased at the top, then grouped
  by topic), rendered by `layouts/posters/list.html`.
- `/posters/virtual/` — virtual posters grouped by topic, rendered by
  `layouts/posters-virtual/list.html`.

Both share `layouts/partials/poster-styles.html` (styles) and
`layouts/partials/poster-card.html` (one compact card), and read from a single
committed data file, **`data/icml2026_posters.json`** — one entry per accepted
paper: `number`, `title`, `authors`, `openreview`, `abstract`, `category` (one
of 8 poster topics), `track` (`inperson` / `virtual` / `spotlight`), and
`is_spotlight`.

Unlike the Google-Docs-synced content above, this data file is generated out of
band by `icml_2026/submissions/build_poster_website_data.py` in the
`mech-interp-workshop` data repo: it joins the curated `poster_categorization.json`
(topic + track) with title/authors/abstract fetched fresh from OpenReview (one
snapshot, the definitive source). To refresh, run that script with
`--out` pointed at this file (it overwrites `data/icml2026_posters.json`).

## Local Development

```bash
hugo server -D
```

## Deployment

Pushes to `main` branch automatically deploy via Netlify.
