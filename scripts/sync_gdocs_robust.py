#!/usr/bin/env python3
"""
Robust Google Docs sync that handles bullets and preserves formatting
Falls back gracefully if APIs are not available
"""
import os
import json
import re
import yaml
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configuration
FOLDER_ID = os.environ.get('GDOCS_FOLDER_ID')
DOC_MAPPING = {
    'main': 'content/_index.md',
    'cfp': 'content/cfp/_index.md',
    'speakers': 'content/speakers/_index.md',
    'schedule': 'content/schedule/_index.md',
    'organizers': 'content/organizers/_index.md',
}

def get_credentials():
    """Get credentials from service account JSON"""
    service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_KEY'])
    return service_account.Credentials.from_service_account_info(
        service_account_info, 
        scopes=['https://www.googleapis.com/auth/drive.readonly']
    )

def convert_drive_text_to_markdown(text, title):
    """Convert plain text export to markdown, trying to preserve structure"""
    lines = text.strip().split('\n')
    
    # Format title
    display_title = title
    if title.lower() == 'main':
        display_title = "Mechanistic Interpretability Workshop 2025"
    elif title.lower() == 'cfp':
        display_title = "Call for Papers"
    elif title.lower() == 'schedule':
        display_title = "Schedule"
    
    # Create frontmatter
    frontmatter = f"""---
title: "{display_title}"
---

"""
    
    # Process lines
    markdown_lines = []
    in_list = False
    list_indent = 0
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Skip empty lines unless we're in a list
        if not stripped:
            if in_list:
                in_list = False
                markdown_lines.append("")
            continue
        
        # Detect headers (lines that are ALL CAPS and short)
        if stripped.isupper() and len(stripped) < 60 and not any(char in stripped for char in ['*', '-', '•']):
            in_list = False
            markdown_lines.append(f"\n## {stripped.title()}\n")
            continue
        
        # Detect bullet points
        if stripped.startswith('*') or stripped.startswith('-') or stripped.startswith('•'):
            # Clean up the bullet
            content = stripped.lstrip('*-• ').strip()
            
            # Try to detect indentation by counting leading spaces
            indent_level = (len(line) - len(line.lstrip())) // 2
            indent = '  ' * indent_level
            
            markdown_lines.append(f"{indent}- {content}")
            in_list = True
            continue
        
        # Check if line might be a continued list item (starts with multiple spaces)
        if line.startswith('  ') and in_list:
            # This is likely a wrapped list item
            last_line = markdown_lines[-1] if markdown_lines else ""
            if last_line.strip().startswith('-'):
                # Append to previous list item
                markdown_lines[-1] = last_line + " " + stripped
                continue
        
        # Regular paragraph
        in_list = False
        markdown_lines.append(stripped)
    
    # Join lines and clean up
    content = '\n'.join(markdown_lines)
    
    # Clean up multiple blank lines
    content = re.sub(r'\n\n\n+', '\n\n', content)
    
    # Process any shortcodes or special syntax
    content = process_special_syntax(content)
    
    return frontmatter + content

def process_special_syntax(text):
    """Process image placeholders and ensure shortcodes are preserved"""
    # Image placeholders
    text = re.sub(
        r'\[IMAGE:\s*([^\]]+)\]',
        r'<img src="/img/\1" alt="Image" class="content-image">',
        text
    )
    
    # Image pairs
    text = re.sub(
        r'\[IMAGE-PAIR:\s*([^|]+)\|\s*([^|]+)\|\s*([^\]]+)\]',
        r'''<div class="image-pair">
<img src="/img/\1" alt="Workshop photo 1">
<img src="/img/\2" alt="Workshop photo 2">
</div>
<p class="image-caption">\3</p>''',
        text
    )
    
    # Preserve shortcodes by ensuring they're on their own line
    shortcode_pattern = r'(\[[A-Za-z]+\])'
    text = re.sub(shortcode_pattern, r'\n\n\1\n\n', text)
    
    # Clean up extra newlines
    text = re.sub(r'\n\n\n+', '\n\n', text)
    
    return text

def main():
    """Main sync function"""
    if not FOLDER_ID:
        print("Error: GDOCS_FOLDER_ID environment variable not set")
        return
    
    # Get credentials
    credentials = get_credentials()
    drive_service = build('drive', 'v3', credentials=credentials)
    
    print("Starting Google Docs sync...")
    
    # Get all documents
    all_files = []
    
    # Get documents from main folder
    try:
        results = drive_service.files().list(
            q=f"'{FOLDER_ID}' in parents and mimeType='application/vnd.google-apps.document'",
            fields="files(id, name)"
        ).execute()
        all_files.extend(results.get('files', []))
    except HttpError as e:
        print(f"Error accessing folder: {e}")
        return
    
    # Also check subfolders
    try:
        folder_results = drive_service.files().list(
            q=f"'{FOLDER_ID}' in parents and mimeType='application/vnd.google-apps.folder'",
            fields="files(id, name)"
        ).execute()
        
        for subfolder in folder_results.get('files', []):
            sub_results = drive_service.files().list(
                q=f"'{subfolder['id']}' in parents and mimeType='application/vnd.google-apps.document'",
                fields="files(id, name)"
            ).execute()
            all_files.extend(sub_results.get('files', []))
    except HttpError:
        pass  # Ignore subfolder errors
    
    if not all_files:
        print("No documents found")
        return
    
    # Process each document
    for file in all_files:
        doc_name = file['name'].lower().replace(' ', '_')
        
        if doc_name not in DOC_MAPPING:
            print(f"Skipping unknown document: {file['name']}")
            continue
        
        print(f"Processing {file['name']}...")
        
        try:
            # Export as plain text (most reliable)
            content = drive_service.files().export(
                fileId=file['id'],
                mimeType='text/plain'
            ).execute()
            
            text = content.decode('utf-8')
            
            # Convert to markdown
            markdown = convert_drive_text_to_markdown(text, doc_name)
            
            # Write to file
            output_path = DOC_MAPPING[doc_name]
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, 'w') as f:
                f.write(markdown)
            
            print(f"  → Saved to {output_path}")
            
            # Filter main content if needed
            if output_path == 'content/_index.md':
                import subprocess
                try:
                    subprocess.run(['python', 'scripts/filter_main_content.py'], check=True)
                    print("  → Filtered duplicate sections from main content")
                except:
                    pass  # Ignore filter errors
                    
        except HttpError as e:
            print(f"  → Error processing {file['name']}: {e}")
            continue
    
    print("\nSync complete!")

if __name__ == '__main__':
    # Load .env file if it exists
    if os.path.exists('.env'):
        from dotenv import load_dotenv
        load_dotenv()
    
    # Re-get FOLDER_ID after loading .env
    FOLDER_ID = os.environ.get('GDOCS_FOLDER_ID')
    
    main()