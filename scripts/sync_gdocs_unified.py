#!/usr/bin/env python3
"""
Unified Google Docs sync script for the Mechanistic Interpretability Workshop website.

This script combines the best features from all previous sync scripts:
- HTML export with formatting preservation (from sync_gdocs_html_fixed.py)
- Robust error handling and fallback to plain text (from sync_gdocs_robust.py)
- Support for two documents: main content and extra_content
- Image placeholder processing
- Debug output for troubleshooting

Features:
- Exports Google Docs as HTML to preserve formatting (bold, italic, links)
- Falls back to plain text export if HTML parsing fails
- Handles two documents: main content and extra_content
- Extra content is saved to data/extra_content.yaml for Hugo data access
- Filters out content from other pages to prevent duplication
- Processes image placeholders
- Creates debug files when HTML parsing fails
"""

import json
import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
CONTENT_DIR = "content"
DATA_DIR = "data"
EXTRA_CONTENT_FILE = "extra_content.yaml"

# Content filtering patterns to prevent duplication
FILTER_PATTERNS = [
    r'## Keynote Speakers.*?(?=##|\Z)',
    r'## Organizing Committee.*?(?=##|\Z)',
    r'<section class="embedded-signup">.*?</section>',
    r'<section class="embedded-speakers">.*?</section>',
    r'<section class="embedded-schedule">.*?</section>',
    r'<section class="embedded-organizers">.*?</section>',
    r'<div class="embedded-signup">.*?</div>',
    r'## Schedule \(Provisional\).*?(?=##|\Z)',
    r'## Contact.*?(?=##|\Z)',
    r'Sign up to our mailing list.*?(?=##|\Z)',
    r'Stay Updated.*?</form>\s*</div>',
]

class FormatSegment:
    """Represents a text segment with its formatting."""
    def __init__(self, text, bold=False, italic=False):
        self.text = text
        self.bold = bold
        self.italic = italic
    
    def to_markdown(self):
        """Convert segment to markdown with proper formatting."""
        result = self.text
        if self.bold:
            result = f"**{result}**"
        if self.italic:
            result = f"*{result}*"
        return result

class MarkdownHTMLParser(HTMLParser):
    """Convert HTML to Markdown with error handling."""
    
    def __init__(self):
        super().__init__()
        self.markdown = []
        self.current_segments = []  # List of FormatSegments for current element
        self.in_heading = False
        self.heading_level = 0
        self.current_bold = False
        self.current_italic = False
        self.in_link = False
        self.link_href = ""
        self.link_text = ""
        self.in_list = False
        self.bold_depth = 0
        self.italic_depth = 0
        self.in_list_item = False
        self.list_type = None
        self.list_depth = 0
        self.in_table = False
        self.in_table_row = False
        self.in_table_cell = False
        self.table_rows = []
        self.current_row = []
        self.ignore_paragraph_bold = False
        self.span_format_stack = []  # Track formatting applied by each span
        
    def handle_starttag(self, tag, attrs):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.flush_current_element()
            self.in_heading = True
            self.heading_level = int(tag[1])
        elif tag == 'p':
            self.flush_current_element()
            # Check if paragraph has bold styling (we want to ignore this)
            style = None
            for attr_name, attr_value in attrs:
                if attr_name == 'style':
                    style = attr_value
                    break
            if style and ('font-weight:700' in style or 'font-weight: 700' in style or 'font-weight:bold' in style):
                self.ignore_paragraph_bold = True
        elif tag == 'a':
            self.in_link = True
            for attr_name, attr_value in attrs:
                if attr_name == 'href':
                    self.link_href = attr_value
        elif tag in ['b', 'strong']:
            self.bold_depth += 1
            self.current_bold = True
        elif tag in ['i', 'em']:
            self.italic_depth += 1
            self.current_italic = True
        elif tag == 'span':
            # Track what formatting this span applies
            applied_formatting = {"bold": False, "italic": False}
            
            # Google Docs sometimes uses spans with font-weight for bold
            style = None
            for attr_name, attr_value in attrs:
                if attr_name == 'style':
                    style = attr_value
                    break
            if style:
                if 'font-weight:700' in style or 'font-weight: 700' in style or 'font-weight:bold' in style:
                    self.bold_depth += 1
                    self.current_bold = True
                    applied_formatting["bold"] = True
                if 'font-style:italic' in style or 'font-style: italic' in style:
                    self.italic_depth += 1
                    self.current_italic = True
                    applied_formatting["italic"] = True
            
            # Push to stack so we know what to undo when we close this span
            self.span_format_stack.append(applied_formatting)
        elif tag in ['ul', 'ol']:
            self.flush_current_element()
            self.in_list = True
            self.list_type = 'ordered' if tag == 'ol' else 'unordered'
            # Check for Google Docs list classes to determine depth
            for attr_name, attr_value in attrs:
                if attr_name == 'class' and 'lst-' in attr_value:
                    # Google Docs uses classes like lst-kix_xxxxx-0, lst-kix_xxxxx-1 for nesting
                    match = re.search(r'-(\d+)(?:\s|$)', attr_value)
                    if match:
                        self.list_depth = int(match.group(1))
                        break
            else:
                # If no class found, increment normally
                self.list_depth += 1
        elif tag == 'li':
            self.flush_current_element()
            self.in_list_item = True
        elif tag == 'br':
            if self.in_list_item:
                # Add a newline within the list item
                self.current_segments.append(FormatSegment('\n', self.current_bold, self.current_italic))
            else:
                self.current_segments.append(FormatSegment('\n', False, False))
        elif tag == 'table':
            self.flush_current_element()
            self.in_table = True
            self.table_rows = []
        elif tag == 'tr':
            if self.in_table:
                self.in_table_row = True
                self.current_row = []
        elif tag in ['td', 'th']:
            if self.in_table:
                self.flush_current_element()
                self.in_table_cell = True
            
    def handle_endtag(self, tag):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.flush_current_element()
            self.in_heading = False
        elif tag == 'p':
            self.flush_current_element()
            self.markdown.append('\n')
            # Reset ignore flag
            self.ignore_paragraph_bold = False
        elif tag == 'a':
            if self.link_text:
                # Add link as a segment
                self.current_segments.append(FormatSegment(f"[{self.link_text}]({self.link_href})", self.current_bold, self.current_italic))
                self.link_text = ""
            self.in_link = False
            self.link_href = ""
        elif tag in ['b', 'strong']:
            self.bold_depth = max(0, self.bold_depth - 1)
            if self.bold_depth == 0:
                self.current_bold = False
        elif tag in ['i', 'em']:
            self.italic_depth = max(0, self.italic_depth - 1)
            if self.italic_depth == 0:
                self.current_italic = False
        elif tag == 'span':
            # Pop formatting that this span applied
            if self.span_format_stack:
                applied = self.span_format_stack.pop()
                if applied.get("bold"):
                    self.bold_depth = max(0, self.bold_depth - 1)
                    if self.bold_depth == 0:
                        self.current_bold = False
                if applied.get("italic"):
                    self.italic_depth = max(0, self.italic_depth - 1)
                    if self.italic_depth == 0:
                        self.current_italic = False
        elif tag in ['ul', 'ol']:
            # Only decrease depth if we're actually in a list
            if self.in_list:
                self.list_depth = max(0, self.list_depth - 1)
                if self.list_depth == 0:
                    self.in_list = False
        elif tag == 'li':
            self.flush_current_element()
            self.in_list_item = False
        elif tag == 'table':
            if self.in_table:
                self.format_table()
                self.in_table = False
        elif tag == 'tr':
            if self.in_table_row:
                self.table_rows.append(self.current_row)
                self.in_table_row = False
        elif tag in ['td', 'th']:
            if self.in_table_cell:
                self.flush_current_element()
                self.in_table_cell = False
            
    def handle_data(self, data):
        if data:
            # Replace non-breaking spaces with regular spaces
            data = data.replace('\xa0', ' ')
            
            if self.in_link:
                self.link_text += data
                return
            
            # Add as a segment with current formatting
            bold = self.current_bold and not self.ignore_paragraph_bold
            self.current_segments.append(FormatSegment(data, bold, self.current_italic))
    
    def flush_current_element(self):
        """Flush accumulated segments to markdown."""
        if not self.current_segments:
            return
            
        # Combine segments into formatted text
        formatted_parts = []
        for segment in self.current_segments:
            formatted_parts.append(segment.to_markdown())
        
        text = ''.join(formatted_parts).strip()
        
        if text:
            if self.in_heading:
                prefix = '#' * self.heading_level
                self.markdown.append(f"{prefix} {text}\n")
            elif self.in_list_item:
                # Use 2 spaces per indent level for better compatibility
                indent = '  ' * max(0, self.list_depth)
                bullet = '* ' if self.list_type == 'unordered' else '1. '
                self.markdown.append(f"{indent}{bullet}{text}\n")
            elif self.in_table_cell:
                self.current_row.append(text)
            else:
                self.markdown.append(text)
                if not self.in_table_cell:
                    self.markdown.append(' ')
        
        self.current_segments = []
    
    def format_table(self):
        """Format table rows as a markdown table."""
        if not self.table_rows:
            return
            
        # Create markdown table
        self.markdown.append('\n')
        
        # First row is header
        if len(self.table_rows) > 0:
            headers = self.table_rows[0]
            self.markdown.append('| ' + ' | '.join(headers) + ' |\n')
            self.markdown.append('|' + '---|' * len(headers) + '\n')
            
            # Remaining rows are data
            for row in self.table_rows[1:]:
                # Ensure row has same number of columns as header
                while len(row) < len(headers):
                    row.append('')
                self.markdown.append('| ' + ' | '.join(row[:len(headers)]) + ' |\n')
        
        self.markdown.append('\n')
            
    def get_markdown(self):
        self.flush_current_element()
        content = ''.join(self.markdown)
        # Clean up excessive newlines
        content = re.sub(r'\n{3,}', '\n\n', content)
        return content.strip()


def setup_google_auth():
    """Set up Google API authentication."""
    creds = None
    
    # Try service account first (for GitHub Actions)
    service_account_key = os.getenv('GOOGLE_SERVICE_ACCOUNT_KEY')
    if service_account_key:
        try:
            service_account_info = json.loads(service_account_key)
            creds = service_account.Credentials.from_service_account_info(
                service_account_info,
                scopes=['https://www.googleapis.com/auth/drive.readonly']
            )
            print("✓ Authenticated with service account")
        except Exception as e:
            print(f"✗ Service account auth failed: {e}")
            
    if not creds:
        print("✗ No authentication credentials found")
        sys.exit(1)
        
    return creds

def export_doc_as_html(service, file_id, title):
    """Export a Google Doc as HTML."""
    try:
        # Export as HTML
        response = service.files().export(
            fileId=file_id,
            mimeType='text/html'
        ).execute()
        
        print(f"  ✓ Exported as HTML: {title}")
        return response.decode('utf-8')
    except HttpError as e:
        print(f"  ✗ Failed to export {title}: {e}")
        return None

def export_doc_as_text(service, file_id, title):
    """Export a Google Doc as plain text (fallback)."""
    try:
        response = service.files().export(
            fileId=file_id,
            mimeType='text/plain'
        ).execute()
        
        print(f"  ✓ Exported as plain text: {title}")
        return response.decode('utf-8')
    except HttpError as e:
        print(f"  ✗ Failed to export {title}: {e}")
        return None

def remove_css_styles(html_content):
    """Remove CSS styles and style tags from HTML content."""
    # Remove style tags and their contents
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove @import statements that might be outside style tags
    html_content = re.sub(r'@import\s+url\([^)]+\);[^<]*', '', html_content, flags=re.IGNORECASE)
    
    # Remove the specific CSS pattern you're seeing (ul.lst-kix_... etc)
    html_content = re.sub(r'ul\.lst-[a-zA-Z0-9_-]+\{[^}]+\}', '', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'\.lst-[a-zA-Z0-9_-]+\s*>\s*li:before\{[^}]+\}', '', html_content, flags=re.MULTILINE)
    
    # Remove any remaining CSS rules
    html_content = re.sub(r'[a-zA-Z0-9\-_\.#]+\s*\{[^}]+\}', '', html_content)
    
    return html_content

def html_to_markdown(html_content, title):
    """Convert HTML to Markdown with error handling."""
    try:
        # Remove CSS styles first
        html_content = remove_css_styles(html_content)
        
        parser = MarkdownHTMLParser()
        parser.feed(html_content)
        markdown = parser.get_markdown()
        
        # Process image placeholders
        markdown = process_image_placeholders(markdown)
        
        return markdown
    except Exception as e:
        print(f"  ⚠ HTML parsing failed for {title}: {e}")
        # Save debug file
        debug_file = f"debug_{title.replace('/', '_')}.html"
        with open(debug_file, 'w') as f:
            f.write(html_content)
        print(f"  → Saved debug HTML to {debug_file}")
        return None

def text_to_markdown(text_content):
    """Convert plain text to Markdown (fallback)."""
    lines = text_content.split('\n')
    markdown_lines = []
    list_indent_stack = []  # Track indentation levels for lists
    
    for line in lines:
        original_line = line
        line = line.rstrip()
        
        # Skip empty lines
        if not line:
            markdown_lines.append('')
            continue
            
        # Convert headers (uppercase lines < 50 chars)
        if line.isupper() and len(line) < 50 and line.strip():
            markdown_lines.append(f"## {line.title()}")
            continue
            
        # Handle bullet points
        stripped = line.lstrip()
        if stripped and stripped[0] in ['*', '-', '•', '○', '■', '▪', '▫', '◦']:
            # Calculate indent level
            indent = len(original_line) - len(stripped)
            
            # Determine list depth based on indentation
            depth = 0
            if list_indent_stack:
                for i, prev_indent in enumerate(list_indent_stack):
                    if indent > prev_indent:
                        depth = i + 1
                    elif indent == prev_indent:
                        depth = i
                        break
                
                # Update stack
                if depth == len(list_indent_stack):
                    list_indent_stack.append(indent)
                elif depth < len(list_indent_stack):
                    list_indent_stack = list_indent_stack[:depth+1]
            else:
                list_indent_stack = [indent]
            
            # Extract content after bullet
            content = stripped[1:].strip() if len(stripped) > 1 else ''
            
            # Apply proper markdown indentation (2 spaces per level)
            md_indent = '  ' * depth
            markdown_lines.append(f"{md_indent}* {content}")
            continue
        else:
            # Not a list item, reset stack
            list_indent_stack = []
            
        # Regular text
        markdown_lines.append(line)
        
    markdown = '\n'.join(markdown_lines)
    
    # Process image placeholders
    markdown = process_image_placeholders(markdown)
    
    return markdown

def process_image_placeholders(content):
    """Process image placeholders in content."""
    # Pattern for {{Image: filename}} placeholders
    pattern = r'\{\{Image:\s*([^\}]+)\}\}'
    
    def replace_image(match):
        filename = match.group(1).strip()
        # Ensure .jpg extension
        if not filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            filename += '.jpg'
        return f'<img src="/img/{filename}" alt="{filename}" />'
    
    return re.sub(pattern, replace_image, content, flags=re.IGNORECASE)

def filter_main_content(content):
    """Filter out sections that are handled by the template."""
    for pattern in FILTER_PATTERNS:
        content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Fix malformed links that have triple brackets [[[text](url)
    content = re.sub(r'\[\[\[([^\]]+)\]\(([^)]+)\)', r'[\1](\2)', content)
    
    # Fix broken list formatting
    content = re.sub(r'\n\*\s+\n+([A-Z\[])', r'\n* \1', content)
    
    # Fix overly aggressive bolding - remove bold from entire paragraphs
    # Look for paragraphs that start and end with ** but contain multiple sentences
    content = re.sub(r'\*\*([^*]+\. [^*]+)\*\*', r'\1', content, flags=re.MULTILINE)
    
    # Remove bold from headers (they're already styled)
    content = re.sub(r'^(#{1,6})\s*\*\*(.+?)\*\*\s*$', r'\1 \2', content, flags=re.MULTILINE)
    
    return content.strip()

def get_gdocs_in_folder(service, folder_id):
    """Get all Google Docs in a folder."""
    try:
        results = service.files().list(
            q=f"'{folder_id}' in parents and mimeType='application/vnd.google-apps.document'",
            fields="files(id, name)"
        ).execute()
        
        files = results.get('files', [])
        print(f"\n✓ Found {len(files)} Google Docs in folder")
        return files
    except HttpError as e:
        print(f"✗ Error accessing folder: {e}")
        return []

def post_process_bold(content):
    """Fix common bold formatting issues from Google Docs."""
    # Fix schedule formatting where bold splits across lines
    # Pattern: "Talk:**\n**Speaker Name" should be "Talk: **Speaker Name**"
    content = re.sub(
        r'Talk:\*\*\s*\n\s*\*\*([^\n]+)',
        r'Talk: **\1**',
        content,
        flags=re.MULTILINE
    )
    
    # Fix "Build understanding **between" -> "**Build understanding** between"
    content = re.sub(
        r'\*\*Build understanding \*\*between',
        '**Build understanding** between',
        content
    )
    
    # Fix "Mechanistic interpretability** addresses" -> "**Mechanistic interpretability** addresses"
    content = re.sub(
        r'^(Mechanistic interpretability)\*\* addresses',
        r'**\1** addresses',
        content,
        flags=re.MULTILINE
    )
    
    # Fix "due** August" -> "due **August**"
    content = re.sub(
        r'due\*\* (August \d+, \d+)',
        r'due **\1**',
        content
    )
    
    # Fix "We request** (but do not require)" -> "We request (but do not require)"
    content = re.sub(
        r'We request\*\* \(but',
        r'We request (but',
        content
    )
    
    # Fix "submitted papers **volunteer as reviewers**" -> "submitted papers volunteer as reviewers"
    content = re.sub(
        r'submitted papers \*\*volunteer as reviewers\*\*',
        r'submitted papers volunteer as reviewers',
        content
    )
    
    # Fix "We welcome any submissions..." pattern
    content = re.sub(
        r'\*\*We welcome any submissions that seek to further our ability to use the internals of models to achieve understanding, regardless of how unconventional the approach may be\. \*\*Please',
        '**We welcome any submissions that seek to further our ability to use the internals of models to achieve understanding, regardless of how unconventional the approach may be.** Please',
        content
    )
    
    # Fix any remaining orphaned ** at the start or end of lines
    content = re.sub(r'^\*\*\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'\s*\*\*$', '', content, flags=re.MULTILINE)
    
    # Fix cases where ** appear at start/end of lines due to line breaks
    content = re.sub(r'\*\*\s*\n\s*\*\*', ' ', content)
    
    # Special handling for the intro paragraphs
    # Only "Mechanistic interpretability" should be bold in the second paragraph
    if content.startswith('As neural networks grow'):
        # Fix the specific case of the first 3 paragraphs
        content = re.sub(
            r'\*\*Mechanistic interpretability\*\*\*\* addresses',
            '**Mechanistic interpretability** addresses',
            content
        )
        # Remove bold from the rest of paragraph 2
        content = re.sub(
            r'addresses this challenge by developing principled methods to analyze and understand a model\'s internals–weights and activations–and to use this understanding to gain greater \*\*\*\*insight into its behavior, and the computation underlying it\. \*\*',
            'addresses this challenge by developing principled methods to analyze and understand a model\'s internals–weights and activations–and to use this understanding to gain greater insight into its behavior, and the computation underlying it.',
            content
        )
        # Remove bold from paragraph 3
        content = re.sub(
            r'\*\*The field has grown rapidly.*?chart future directions\.\*\*',
            lambda m: m.group(0).replace('**', ''),
            content,
            flags=re.DOTALL
        )
    
    # Split into lines for processing
    lines = content.split('\n')
    processed_lines = []
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            processed_lines.append(line)
            continue
            
        # Remove bold from headers (they have their own styling)
        if line.strip().startswith('#'):
            line = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
        
        # Check if entire line/paragraph is bold
        stripped = line.strip()
        if stripped.startswith('**') and stripped.endswith('**'):
            inner_content = stripped[2:-2]
            
            # If it's a long paragraph or contains multiple sentences, remove bold
            if len(inner_content) > 100 or inner_content.count('. ') >= 2:
                line = line.replace(stripped, inner_content)
            # If it contains a link, likely shouldn't be all bold
            elif '](' in inner_content:
                line = line.replace(stripped, inner_content)
        
        # Fix list items that are entirely bold
        if re.match(r'^(\s*\*\s+)\*\*(.+)\*\*\s*$', line):
            line = re.sub(r'^(\s*\*\s+)\*\*(.+)\*\*\s*$', r'\1\2', line)
        
        processed_lines.append(line)
    
    content = '\n'.join(processed_lines)
    
    # Fix bold that spans multiple paragraphs
    content = re.sub(r'\*\*\n\n', '\n\n', content)
    content = re.sub(r'\n\n\*\*', '\n\n', content)
    
    # Fix call for papers formatting issues
    # Pattern: "of**\n**short" should be "of **short**"
    content = re.sub(
        r'of\*\*\s*\n\s*\*\*short',
        'of **short**',
        content,
        flags=re.MULTILINE
    )
    # Pattern: "and**\n**long" should be "and **long**"
    content = re.sub(
        r'and\*\*\s*\n\s*\*\*long',
        'and **long**',
        content,
        flags=re.MULTILINE
    )
    
    return content

def transform_open_problems_link(content):
    """Transform the 'Open Problems in Mechanistic Interpretability' link to only link 'Open'."""
    # Pattern to find the specific link
    content = re.sub(
        r'\[Open Problems in Mechanistic Interpretability\]\(([^)]+)\)',
        r'<span class="open-problems-text">[Open](\1) Problems in Mechanistic Interpretability</span>',
        content
    )
    
    return content

def sync_document(service, doc, output_path, is_extra_content=False):
    """Sync a single document."""
    doc_id = doc['id']
    doc_name = doc['name']
    
    print(f"\n→ Processing: {doc_name}")
    
    # Try HTML export first
    html_content = export_doc_as_html(service, doc_id, doc_name)
    
    if html_content:
        # Try to parse HTML to Markdown
        markdown_content = html_to_markdown(html_content, doc_name)
        
        if not markdown_content:
            # Fall back to plain text
            print(f"  → Falling back to plain text export")
            text_content = export_doc_as_text(service, doc_id, doc_name)
            if text_content:
                markdown_content = text_to_markdown(text_content)
            else:
                print(f"  ✗ Failed to export document")
                return False
    else:
        # Try plain text export
        text_content = export_doc_as_text(service, doc_id, doc_name)
        if text_content:
            markdown_content = text_to_markdown(text_content)
        else:
            print(f"  ✗ Failed to export document")
            return False
    
    # Post-process to fix bold formatting issues
    markdown_content = post_process_bold(markdown_content)
    
    # Transform the Open Problems link if this is extra content
    if is_extra_content:
        markdown_content = transform_open_problems_link(markdown_content)
    
    # Filter main content if needed
    if not is_extra_content:
        markdown_content = filter_main_content(markdown_content)
    
    # Save the content
    if is_extra_content:
        # Save to data directory as YAML
        data_path = Path(DATA_DIR) / EXTRA_CONTENT_FILE
        data_path.parent.mkdir(exist_ok=True)
        
        with open(data_path, 'w') as f:
            yaml.dump({'content': markdown_content}, f, default_flow_style=False)
        
        print(f"  ✓ Saved to: {data_path}")
    else:
        # Save to content directory as Markdown
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            # Preserve frontmatter if it exists
            if output_path.exists():
                existing_content = output_path.read_text()
                if existing_content.startswith('---'):
                    frontmatter_end = existing_content.find('---', 3)
                    if frontmatter_end != -1:
                        frontmatter = existing_content[:frontmatter_end + 3]
                        f.write(frontmatter + '\n\n')
            
            f.write(markdown_content)
        
        print(f"  ✓ Saved to: {output_path}")
    
    return True

def main():
    """Main sync function."""
    print("=== Google Docs Sync (Unified) ===")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Set up authentication
    creds = setup_google_auth()
    service = build('drive', 'v3', credentials=creds)
    
    # Get folder ID
    folder_id = os.getenv('GDOCS_FOLDER_ID')
    if not folder_id:
        print("✗ GDOCS_FOLDER_ID not set")
        sys.exit(1)
    
    # Get all docs in folder
    docs = get_gdocs_in_folder(service, folder_id)
    
    if not docs:
        print("✗ No documents found")
        sys.exit(1)
    
    # Track results
    success_count = 0
    
    # Process each document
    for doc in docs:
        doc_name = doc['name'].lower()
        
        # Determine output path and type
        if 'extra_content' in doc_name:
            # Handle extra content document
            success = sync_document(service, doc, None, is_extra_content=True)
        else:
            # Handle regular content documents
            # Map document names to content paths
            if 'schedule' in doc_name:
                output_path = Path(CONTENT_DIR) / 'schedule' / '_index.md'
            elif 'cfp' in doc_name or 'call' in doc_name:
                output_path = Path(CONTENT_DIR) / 'cfp' / '_index.md'
            elif 'faq' in doc_name:
                output_path = Path(CONTENT_DIR) / 'faq' / '_index.md'
            else:
                # Default to main page
                output_path = Path(CONTENT_DIR) / '_index.md'
            
            success = sync_document(service, doc, output_path, is_extra_content=False)
        
        if success:
            success_count += 1
    
    # Summary
    print(f"\n=== Sync Complete ===")
    print(f"✓ Successfully synced: {success_count}/{len(docs)} documents")
    
    if success_count < len(docs):
        sys.exit(1)

if __name__ == "__main__":
    main()