# Images and Dynamic Content in Google Docs

This guide explains how to add images and dynamic content (like the organizers section) to your Google Docs.

## Adding Images

You have several options for adding images to your Google Docs content:

### Option 1: Simple Image Reference (Recommended)
```
[IMAGE: speaker-photo.jpg]
```
This will display an image from `/static/img/speaker-photo.jpg`

### Option 2: Markdown Style
```
![Alt text description](image-filename.jpg)
```
Example: `![Chris Olah speaking](chrisolah-talk.jpg)`

### Option 3: HTML Style
```
<img src="workshop-banner.jpg" alt="Workshop banner">
```

### Option 4: Hugo Shortcode Style
```
{{< image src="diagram.png" alt="Architecture diagram" >}}
```

### Option 5: Side-by-Side Images with Caption
```
[IMAGE-PAIR: conference-pic.jpg | rooftop-pic.jpg | The first Mechanistic Interpretability Workshop (ICML 2024).]
```
This creates two images side by side with a centered caption below

## Important Notes for Images:
1. All images must be uploaded to `/static/img/` in the GitHub repository first
2. Use just the filename in Google Docs (not the full path)
3. Images will be automatically styled with:
   - Responsive sizing (max-width: 100%)
   - Centered alignment
   - Rounded corners
   - Subtle shadow

## Adding Dynamic Sections

You can embed various sections anywhere in your Google Docs:

### To Add Organizers Section:
Simply type one of these in your Google Doc:
```
[ORGANIZERS]
```
or
```
{{< organizers >}}
```

### To Add Speakers Section:
Simply type one of these in your Google Doc:
```
[SPEAKERS]
```
or
```
{{< speakers >}}
```

### To Add Schedule Table:
Simply type one of these in your Google Doc:
```
[SCHEDULE]
```
or
```
{{< schedule >}}
```

### To Add Signup Box:
Simply type one of these in your Google Doc:
```
[SIGNUP]
```
or
```
{{< signup >}}
```

## Example Usage

Here's how you might structure your main page in Google Docs:

```
# The Workshop

This is a 1 day workshop at NeurIPS...

## Why This Workshop?

Mechanistic interpretability is a rapidly-growing...

[IMAGE: workshop-overview.png]

## Key Topics for NeurIPS 2025

### Sparse Autoencoders
- Point about SAEs
- Another point
- Third point

### Rigorous Benchmarking
- First benchmark point
- Second point

[SPEAKERS]

[SCHEDULE]

[ORGANIZERS]

## Get Involved

Stay updated on workshop announcements:

[SIGNUP]

## Additional Information

More content here...
```

## How It Works

1. When you add these placeholders to your Google Doc
2. The sync script downloads your content
3. The shortcode processor replaces `[ORGANIZERS]` and `[SPEAKERS]` with the actual HTML
4. Images are converted to proper HTML tags
5. The site is built and deployed

## Updating Speaker/Organizer Data

The actual speaker and organizer information is stored in:
- `/data/speakers.yaml`
- `/data/organizers.yaml`

These files control what appears when you use the shortcodes. Edit these files directly on GitHub to update the information.

## Limitations

- Google Docs embedded images are not directly supported (the API doesn't provide image data)
- You must upload images to GitHub first, then reference them by filename
- Shortcodes are processed during build, so changes to YAML files require a rebuild

## Tips

1. Test image filenames carefully - they're case-sensitive
2. Keep images reasonably sized (under 1MB recommended)
3. Use descriptive alt text for accessibility
4. The shortcodes can be used multiple times if needed
5. You can mix regular content and dynamic sections freely