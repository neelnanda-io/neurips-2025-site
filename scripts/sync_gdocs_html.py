#!/usr/bin/env python3
"""
Google Docs sync using HTML export to preserve formatting
Converts Google Docs HTML to clean markdown
"""
import os
import json
import re
from html.parser import HTMLParser
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

class GoogleDocsHTMLToMarkdown(HTMLParser):
    """Convert Google Docs HTML to Markdown"""
    
    def __init__(self):
        super().__init__()
        self.output = []
        self.current_text = []
        self.in_link = False
        self.link_href = None
        self.in_list = False
        self.list_type = None
        self.list_depth = 0
        self.in_bold = False
        self.in_italic = False
        self.in_heading = False
        self.heading_level = 1
        self.skip_style = False
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Skip style tags
        if tag == 'style':
            self.skip_style = True
            return
            
        # Headers
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self._flush_text()
            self.in_heading = True
            self.heading_level = int(tag[1])
            
        # Paragraphs
        elif tag == 'p':
            self._flush_text()
            
        # Links
        elif tag == 'a':
            href = attrs_dict.get('href', '')
            if href and not href.startswith('#'):  # Skip internal links
                self.in_link = True
                self.link_href = href
                
        # Lists
        elif tag == 'ul':
            self._flush_text()
            self.in_list = True
            self.list_type = 'ul'
            self.list_depth += 1
            
        elif tag == 'ol':
            self._flush_text()
            self.in_list = True
            self.list_type = 'ol'
            self.list_depth += 1
            
        elif tag == 'li':
            self._flush_text()
            
        # Formatting
        elif tag == 'b' or tag == 'strong':
            self.in_bold = True
            
        elif tag == 'i' or tag == 'em':
            self.in_italic = True
            
        # Line breaks
        elif tag == 'br':
            self.current_text.append('\n')
            
    def handle_endtag(self, tag):
        # Skip style tags
        if tag == 'style':
            self.skip_style = False
            return
            
        # Headers
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self._flush_text()
            self.in_heading = False
            self.output.append('\n')
            
        # Paragraphs
        elif tag == 'p':
            self._flush_text()
            self.output.append('\n')
            
        # Links
        elif tag == 'a':
            if self.in_link and self.link_href:
                text = ''.join(self.current_text).strip()
                if text:
                    self.current_text = [f'[{text}]({self.link_href})']
            self.in_link = False
            self.link_href = None
            
        # Lists
        elif tag in ['ul', 'ol']:
            self._flush_text()
            self.list_depth -= 1
            if self.list_depth == 0:
                self.in_list = False
                self.output.append('\n')
                
        elif tag == 'li':
            self._flush_text()
            
        # Formatting
        elif tag in ['b', 'strong']:
            self.in_bold = False
            
        elif tag in ['i', 'em']:
            self.in_italic = False
            
    def handle_data(self, data):
        if self.skip_style:
            return
            
        # Clean up the data
        text = data
        
        # Apply formatting
        if self.in_bold and not self.in_heading:
            text = f'**{text}**'
        if self.in_italic:
            text = f'*{text}*'
            
        self.current_text.append(text)
        
    def _flush_text(self):
        """Flush accumulated text to output"""
        if not self.current_text:
            return
            
        text = ''.join(self.current_text).strip()
        if not text:
            self.current_text = []
            return
            
        # Handle different contexts
        if self.in_heading:
            prefix = '#' * self.heading_level
            self.output.append(f'{prefix} {text}')
        elif self.in_list:
            indent = '  ' * (self.list_depth - 1)
            if self.list_type == 'ul':
                self.output.append(f'{indent}* {text}')
            else:
                self.output.append(f'{indent}1. {text}')
        else:
            self.output.append(text)
            
        self.current_text = []
        
    def get_markdown(self):
        """Get the final markdown output"""
        self._flush_text()
        
        # Join lines and clean up
        content = '\n'.join(self.output)
        
        # Clean up excessive newlines
        content = re.sub(r'\n\n\n+', '\n\n', content)
        
        # Ensure proper spacing around headers
        content = re.sub(r'(\n#{1,6} [^\n]+)\n([^\n])', r'\1\n\n\2', content)
        
        # Ensure proper spacing around lists
        content = re.sub(r'([^\n])\n(\* |\d+\. )', r'\1\n\n\2', content)
        
        return content.strip()

def get_credentials():
    """Get credentials from service account JSON"""
    service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_KEY'])
    return service_account.Credentials.from_service_account_info(
        service_account_info, 
        scopes=['https://www.googleapis.com/auth/drive.readonly']
    )

def convert_html_to_markdown(html_content, title):
    """Convert Google Docs HTML to markdown"""
    # Parse HTML
    parser = GoogleDocsHTMLToMarkdown()
    parser.feed(html_content)
    markdown_content = parser.get_markdown()
    
    # Format title for frontmatter
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
    
    # Process special syntax (images and shortcodes)
    markdown_content = process_special_syntax(markdown_content)
    
    return frontmatter + markdown_content

def process_special_syntax(text):
    """Process image placeholders and ensure shortcodes are preserved"""
    # Image placeholders
    text = re.sub(
        r'\[IMAGE:\s*([^\]]+)\]',
        r'<img src="/img/\1" alt="Image" class="content-image">',
        text,
        flags=re.IGNORECASE
    )
    
    # Image pairs
    text = re.sub(
        r'\[IMAGE-PAIR:\s*([^|]+)\|\s*([^|]+)\|\s*([^\]]+)\]',
        r'''<div class="image-pair">
<img src="/img/\1" alt="Workshop photo 1">
<img src="/img/\2" alt="Workshop photo 2">
</div>
<p class="image-caption">\3</p>''',
        text,
        flags=re.IGNORECASE
    )
    
    # Ensure shortcodes are on their own line with proper spacing
    shortcode_pattern = r'(\[[A-Za-z]+\])'
    
    # First, check if shortcode is already on its own line
    lines = text.split('\n')
    new_lines = []
    
    for i, line in enumerate(lines):
        # Check if line contains a shortcode
        if re.search(shortcode_pattern, line, re.IGNORECASE):
            # If the line is JUST the shortcode, ensure spacing
            if re.match(r'^\s*\[[A-Za-z]+\]\s*$', line, re.IGNORECASE):
                # Ensure blank line before (unless at start)
                if i > 0 and new_lines and new_lines[-1].strip():
                    new_lines.append('')
                new_lines.append(line.strip())
                # Next line will handle spacing after
            else:
                # Shortcode is mixed with other content, extract it
                parts = re.split(shortcode_pattern, line, flags=re.IGNORECASE)
                for part in parts:
                    if re.match(shortcode_pattern, part, re.IGNORECASE):
                        # Add spacing and the shortcode
                        if new_lines and new_lines[-1].strip():
                            new_lines.append('')
                        new_lines.append(part)
                    elif part.strip():
                        new_lines.append(part.strip())
        else:
            new_lines.append(line)
    
    text = '\n'.join(new_lines)
    
    # Clean up excessive newlines
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
    
    print("Starting Google Docs sync (HTML export)...")
    
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
            # Export as HTML to preserve formatting
            content = drive_service.files().export(
                fileId=file['id'],
                mimeType='text/html'
            ).execute()
            
            html = content.decode('utf-8')
            
            # Convert to markdown
            markdown = convert_html_to_markdown(html, doc_name)
            
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