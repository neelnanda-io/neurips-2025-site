# Complete Guide to Images and HTML in Your Workshop Site

## What Appears in Google Docs Next to Images

When you paste an image into Google Docs, here's what happens:

1. **In Google Docs**: You see the image normally
2. **In the exported markdown**: You'll see a placeholder like:
   ```
   [IMAGE: Embedded image - please add manually]
   (Original title: Speaker Photo)
   ```
3. **Why**: Google Docs API cannot export embedded images - they're stored internally

## How to Handle Images

### Method 1: Use Image Placeholders (Recommended)

In your Google Doc, instead of pasting images, write:

```
[IMAGE: chrisolah.jpeg]
```

Or with markdown syntax:
```
![Chris Olah speaking at conference](chrisolah.jpeg)
```

Or with Hugo shortcode style:
```
{{< image src="speaker-photo.jpg" alt="Speaker at podium" >}}
```

The enhanced sync script converts all of these to:
```html
<img src="/img/filename.jpg" alt="description" class="content-image">
```

### Method 2: Direct HTML in Google Docs

You can write HTML directly in Google Docs:
```html
<img src="/img/workshop-banner.png" alt="Workshop Banner" style="width: 100%; max-width: 800px;">
```

This passes through unchanged to your website.

## Finding Exact Image Names and Files

### For Speakers/Organizers (Already Configured)

Look in `data/speakers.yaml` and `data/organizers.yaml`:

```yaml
speakers:
  - name: "Chris Olah"
    image: "chrisolah.jpeg"    # ← This is the exact filename needed
```

To see what images are needed:
1. Run: `grep -r "image:" data/`
2. Or check `IMAGES_NEEDED.md`

### For Content Images

After running the enhanced sync script, it will:
1. List all images referenced in your docs
2. Show ✓ or ✗ for each image (exists or missing)
3. Update `IMAGES_NEEDED.md` with missing images

Example output:
```
📷 Images referenced in documents (5 total):
  ✓ chrisolah.jpeg
  ✗ workshop-banner.png
  ✗ schedule-diagram.png
```

## Editing the HTML Structure

### 1. Layouts Control Structure

The HTML structure is in the `layouts/` folder:

- **Homepage**: `layouts/index.html`
- **Other pages**: `layouts/_default/single.html`
- **Header/Footer**: `layouts/partials/header.html`, `layouts/partials/footer.html`

### 2. Where Speaker/Organizer Images Are Rendered

In `layouts/index.html`:

```html
{{ range .speakers }}
<div class="speaker">
  <img src="/img/{{ .image }}" alt="{{ .name }}" />
  <div>
    <h3><a href="{{ .website }}">{{ .name }}</a></h3>
    <p>{{ .affiliation }}</p>
  </div>
</div>
{{ end }}
```

To change this structure, edit the template directly.

### 3. Adding Custom HTML Sections

You can add raw HTML in several ways:

**In Google Docs** (appears in content):
```html
<div class="custom-section">
  <h2>Special Announcement</h2>
  <img src="/img/announcement.png" alt="Important">
  <p>Custom HTML content here</p>
</div>
```

**In layouts** (appears on every page):
Edit `layouts/index.html` to add sections:
```html
<!-- After the organizers section -->
<section class="sponsors">
  <h2>Sponsors</h2>
  <div class="sponsor-logos">
    <img src="/img/sponsor1.png" alt="Sponsor 1">
    <img src="/img/sponsor2.png" alt="Sponsor 2">
  </div>
</section>
```

### 4. CSS for Images

Edit `assets/css/main.css` to style images:

```css
/* Content images from Google Docs */
.content-image {
  max-width: 100%;
  height: auto;
  margin: 1rem 0;
}

/* Speaker photos */
.speaker img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
}

/* Custom image galleries */
.image-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}
```

## Step-by-Step Image Workflow

1. **In Google Docs**, write:
   ```
   [IMAGE: workshop-poster.png]
   ```

2. **Run sync**:
   ```bash
   python scripts/sync_gdocs_enhanced.py
   ```

3. **Check output** for missing images:
   ```
   ✗ workshop-poster.png
   ```

4. **Add image** to `static/img/`:
   ```bash
   cp ~/Downloads/workshop-poster.png static/img/
   ```

5. **Rebuild site**:
   ```bash
   hugo
   ```

6. **Image appears** on website at `/img/workshop-poster.png`

## Advanced HTML Customization

### Creating a Photo Gallery

In Google Docs:
```html
<div class="photo-gallery">
  <img src="/img/workshop-photo-1.jpg" alt="Workshop session">
  <img src="/img/workshop-photo-2.jpg" alt="Poster session">
  <img src="/img/workshop-photo-3.jpg" alt="Panel discussion">
</div>
```

In CSS:
```css
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}
```

### Custom Speaker Cards

Edit `layouts/index.html`:
```html
{{ range .speakers }}
<div class="speaker-card">
  <div class="speaker-photo">
    <img src="/img/{{ .image }}" alt="{{ .name }}">
  </div>
  <div class="speaker-info">
    <h3>{{ .name }}</h3>
    <p class="affiliation">{{ .affiliation }}</p>
    <a href="{{ .website }}" class="speaker-link">Biography →</a>
  </div>
</div>
{{ end }}
```

## Debugging Images

1. **Check if image exists**:
   ```bash
   ls -la static/img/
   ```

2. **Check references**:
   ```bash
   grep -r "chrisolah" content/ data/ layouts/
   ```

3. **View in browser**: 
   - Go to `http://localhost:1313/img/chrisolah.jpeg`
   - Should see the image directly

4. **Check console** for 404 errors in browser DevTools

## Summary

- **Google Docs images** → Use placeholders like `[IMAGE: filename.jpg]`
- **Image files** → Put in `static/img/` folder
- **HTML structure** → Edit files in `layouts/` folder
- **Styling** → Edit `assets/css/main.css`
- **Test locally** → Run `hugo server -D` and check browser