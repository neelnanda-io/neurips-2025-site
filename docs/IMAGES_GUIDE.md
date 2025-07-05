# Images in Google Docs Sync

## The Challenge

When you paste images directly into Google Docs, they are stored internally by Google and cannot be easily extracted via the API. The Google Docs export API (which we use) only exports text content, not images.

## How to Handle Images

### Option 1: Reference Images by Filename (Recommended)

1. **In Google Docs**, add a placeholder like:
   ```
   ![Chris Olah](chrisolah.jpeg)
   ```
   or just write:
   ```
   [IMAGE: chrisolah.jpeg]
   ```

2. **Upload the actual image** to `static/img/` in your repository

3. **The sync script** will convert these to proper image tags

### Option 2: Use External Image URLs

In Google Docs, you can reference images hosted elsewhere:
```
![Speaker Name](https://example.com/image.jpg)
```

### Option 3: Manual HTML in Google Docs

You can write HTML directly in Google Docs:
```html
<img src="/img/speaker.jpg" alt="Speaker Name">
```

## Current Image Setup

For your workshop site, images are already referenced in the data files:
- Speaker images in `data/speakers.yaml`
- Organizer images in `data/organizers.yaml`

These are automatically displayed on the homepage. You just need to:
1. Upload the actual image files to `static/img/`
2. Use the exact filenames specified in the data files

## For Content Images

If you want to add images to the content (like in the Call for Papers), you would:

1. In Google Docs, write:
   ```
   [IMAGE: workshop-poster.png]
   ```

2. Upload `workshop-poster.png` to `static/img/`

3. Optionally, update the sync script to convert `[IMAGE: filename]` to `<img>` tags

## Enhanced Sync Script

If you need image support, we can enhance the sync script to:
- Convert `[IMAGE: filename]` to proper `<img>` tags
- Support markdown image syntax `![alt text](filename)`
- Add image captions and styling

Would you like me to create an enhanced version of the sync script with image support?