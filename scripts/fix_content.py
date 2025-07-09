#!/usr/bin/env python3
"""
Fix the main content file by:
1. Adding the missing ORGANIZERS section
2. Cleaning up Google redirect URLs
"""
import re

# Read the current content
with open('content/_index.md', 'r') as f:
    content = f.read()

# Remove the trailing '[' if present
content = content.rstrip()
if content.endswith('['):
    content = content[:-1].rstrip()

# Add the organizers section if it's missing
if '<section class="embedded-organizers">' not in content:
    organizers_html = '''

<section class="embedded-organizers">
<h2>Organizing Committee</h2>
<div class="organizers speakers">
  <div class="speaker">
    <img src="/img/neelnanda.jpeg" alt="Neel Nanda" />
    <div>
      <h3><a href="https://www.neelnanda.io/about">Neel Nanda</a></h3>
      <p>Senior Research Scientist, Google DeepMind</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/martinwattenberg.png" alt="Martin Wattenberg" />
    <div>
      <h3><a href="https://www.bewitched.com">Martin Wattenberg</a></h3>
      <p>Professor, Harvard University & Principal Research Scientist, Google DeepMind</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/sarahwiegreffe.jpeg" alt="Sarah Wiegreffe" />
    <div>
      <h3><a href="https://sarahwie.github.io/">Sarah Wiegreffe</a></h3>
      <p>Postdoc, Allen Institute for AI, incoming Assistant Professor, University of Maryland</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/atticusgeiger.jpeg" alt="Atticus Geiger" />
    <div>
      <h3><a href="https://atticusg.github.io/">Atticus Geiger</a></h3>
      <p>Lead, Pr(Ai)²R Group</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/juliusadebayo.jpeg" alt="Julius Adebayo" />
    <div>
      <h3><a href="https://juliusadebayo.com">Julius Adebayo</a></h3>
      <p>Founder and Researcher, Guide Labs</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/kayoyin.jpeg" alt="Kayo Yin" />
    <div>
      <h3><a href="https://kayoyin.github.io/">Kayo Yin</a></h3>
      <p>3rd year PhD student, UC Berkeley</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/fazlbarez.jpeg" alt="Fazl Barez" />
    <div>
      <h3><a href="https://fbarez.github.io/">Fazl Barez</a></h3>
      <p>Senior Research Fellow, Oxford Martin AI Governance Initiative</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/lawrencechan.jpeg" alt="Lawrence Chan" />
    <div>
      <h3><a href="https://chanlawrence.me/">Lawrence Chan</a></h3>
      <p>Researcher, METR</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/matthewwearden.jpeg" alt="Matthew Wearden" />
    <div>
      <h3>Matthew Wearden</h3>
      <p>London Director, MATS</p>
    </div>
  </div>
</div>
</section>'''
    
    content += organizers_html

# Clean up Google redirect URLs
def clean_google_url(match):
    """Extract the actual URL from Google's redirect wrapper"""
    full_match = match.group(0)
    # Extract the URL from q= parameter
    url_match = re.search(r'q=([^&]+)&', full_match)
    if url_match:
        actual_url = url_match.group(1)
        # Get the link text (everything before the URL in parentheses)
        text_match = re.search(r'\[([^\]]+)\]\(', full_match)
        if text_match:
            link_text = text_match.group(1)
            return f'[{link_text}]({actual_url})'
    return full_match

# Fix Google redirect URLs
content = re.sub(
    r'\[[^\]]+\]\(https://www\.google\.com/url\?[^)]+\)',
    clean_google_url,
    content
)

# Also fix standalone Google URLs that might not be in markdown link format
content = re.sub(
    r'https://www\.google\.com/url\?q=([^&]+)&[^\s\)]+',
    r'\1',
    content
)

# Fix any malformed markdown links
# Fix [text] (url) -> [text](url)
content = re.sub(r'\[([^\]]+)\]\s+\(([^)]+)\)', r'[\1](\2)', content)

# Write the fixed content back
with open('content/_index.md', 'w') as f:
    f.write(content)

print("✓ Added missing organizers section")
print("✓ Cleaned up Google redirect URLs")
print("✓ Fixed markdown link formatting")

# Also create a simple sync script that doesn't truncate
with open('scripts/sync_simple.py', 'w') as f:
    f.write('''#!/usr/bin/env python3
"""
Simple sync that just copies Google Docs content without truncation
"""
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

# Get credentials
service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_KEY'])
credentials = service_account.Credentials.from_service_account_info(
    service_account_info, 
    scopes=['https://www.googleapis.com/auth/drive.readonly']
)

drive_service = build('drive', 'v3', credentials=credentials)
FOLDER_ID = os.environ.get('GDOCS_FOLDER_ID')

# Just export main doc as text
results = drive_service.files().list(
    q=f"'{FOLDER_ID}' in parents and mimeType='application/vnd.google-apps.document' and name='main'",
    fields="files(id, name)"
).execute()

if results.get('files'):
    file = results['files'][0]
    content = drive_service.files().export(
        fileId=file['id'],
        mimeType='text/plain'
    ).execute()
    
    text = content.decode('utf-8')
    
    # Write raw content for debugging
    with open('debug_main.txt', 'w') as f:
        f.write(text)
    
    print(f"Exported {len(text)} characters from Google Docs")
''')