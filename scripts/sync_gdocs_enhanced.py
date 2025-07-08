#!/usr/bin/env python3
"""
Enhanced Google Docs to Hugo markdown sync with image support
"""
import os
import json
import re
import yaml
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configuration
SCOPES = ['https://www.googleapis.com/auth/documents.readonly',
          'https://www.googleapis.com/auth/drive.readonly']
FOLDER_ID = os.environ.get('GDOCS_FOLDER_ID')

# Mapping of doc names to content paths
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
        service_account_info, scopes=SCOPES)

def get_document_content(docs_service, document_id):
    """Retrieve the document content using Google Docs API"""
    try:
        document = docs_service.documents().get(documentId=document_id).execute()
        return document
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def extract_text_from_element(element):
    """Extract text from a document element"""
    text = ''
    if 'textRun' in element:
        text = element['textRun']['content']
    return text

def apply_text_formatting(text, text_style):
    """Apply markdown formatting based on text style"""
    if not text.strip():
        return text
        
    # Handle bold
    if text_style.get('bold'):
        text = f"**{text.strip()}**"
    
    # Handle italic
    if text_style.get('italic'):
        text = f"*{text.strip()}*"
    
    # Handle links
    if 'link' in text_style:
        url = text_style['link'].get('url', '')
        text = f"[{text.strip()}]({url})"
    
    return text

def process_image_placeholders(text):
    """Convert various image placeholder formats to HTML"""
    # Pattern 1: [IMAGE: filename.jpg]
    text = re.sub(
        r'\[IMAGE:\s*([^\]]+)\]',
        r'<img src="/img/\1" alt="Image" class="content-image">',
        text
    )
    
    # Pattern 2: ![alt text](filename.jpg) - Markdown style
    text = re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        lambda m: f'<img src="/img/{m.group(2)}" alt="{m.group(1)}" class="content-image">' 
        if not m.group(2).startswith('http') 
        else f'<img src="{m.group(2)}" alt="{m.group(1)}" class="content-image">',
        text
    )
    
    # Pattern 3: {{< image src="filename.jpg" alt="description" >}}
    text = re.sub(
        r'\{\{<\s*image\s+src="([^"]+)"\s*(?:alt="([^"]+)")?\s*>\}\}',
        r'<img src="/img/\1" alt="\2" class="content-image">',
        text
    )
    
    # Pattern 4: <img> tags (pass through but ensure /img/ prefix for local images)
    text = re.sub(
        r'<img\s+src="(?!http)([^"]+)"',
        r'<img src="/img/\1"',
        text
    )
    
    return text

def convert_paragraph_to_markdown(paragraph, inline_objects=None):
    """Convert a paragraph element to markdown"""
    style = paragraph.get('paragraphStyle', {})
    named_style = style.get('namedStyleType', '')
    
    elements = paragraph.get('elements', [])
    text_content = ''
    
    for element in elements:
        if 'textRun' in element:
            text = element['textRun']['content']
            text_style = element['textRun'].get('textStyle', {})
            
            # Apply formatting (don't skip empty text runs as they might be part of lists)
            formatted_text = apply_text_formatting(text, text_style)
            text_content += formatted_text
            
        elif 'inlineObjectElement' in element:
            # This is where embedded images appear in Google Docs
            obj_id = element['inlineObjectElement']['inlineObjectId']
            text_content += f"\n[IMAGE: Embedded image - please add manually]\n"
            if inline_objects and obj_id in inline_objects:
                # We can get some info about the image but not the actual file
                obj = inline_objects[obj_id]
                props = obj.get('inlineObjectProperties', {}).get('embeddedObject', {})
                if 'title' in props:
                    text_content += f"(Original title: {props['title']})\n"
    
    # Check for list items first (before checking if content is empty)
    if 'bullet' in style:
        # Process image placeholders
        text_content = process_image_placeholders(text_content)
        
        # Calculate indent level
        indent_start = style.get('indentStart', {}).get('magnitude', 0)
        indent_level = int(indent_start / 36) if indent_start else 0
        indent = '  ' * indent_level
        
        # Determine bullet type
        nesting_level = style['bullet'].get('nestingLevel', 0)
        if nesting_level % 2 == 0:
            bullet = '-'
        else:
            bullet = '*'
        
        return f"{indent}{bullet} {text_content.strip()}\n"
    
    # Skip empty non-list paragraphs
    if not text_content.strip():
        return ''
    
    # Process image placeholders
    text_content = process_image_placeholders(text_content)
    
    # Apply paragraph-level formatting
    if named_style == 'HEADING_1':
        return f"# {text_content.strip()}\n"
    elif named_style == 'HEADING_2':
        return f"## {text_content.strip()}\n"
    elif named_style == 'HEADING_3':
        return f"### {text_content.strip()}\n"
    elif named_style == 'HEADING_4':
        return f"#### {text_content.strip()}\n"
    elif named_style == 'HEADING_5':
        return f"##### {text_content.strip()}\n"
    elif named_style == 'HEADING_6':
        return f"###### {text_content.strip()}\n"
    else:
        # Regular paragraph
        return f"{text_content.strip()}\n"

def convert_document_to_markdown(document, title):
    """Convert a Google Docs document to markdown with frontmatter"""
    content = document.get('body', {}).get('content', [])
    inline_objects = document.get('inlineObjects', {})
    
    # Format title properly
    display_title = title
    if title.lower() == 'main':
        display_title = "Mechanistic Interpretability Workshop 2025"
    elif title.lower() == 'cfp':
        display_title = "Call for Papers"
    elif title.lower() == 'schedule':
        display_title = "Schedule"
    
    # Create frontmatter - only include title
    # Navigation menu is handled in config.yaml, not in content files
    frontmatter = {
        'title': display_title
    }
    
    markdown_content = f"---\n{yaml.dump(frontmatter, default_flow_style=False)}---\n\n"
    
    # Convert content
    for element in content:
        if 'paragraph' in element:
            paragraph_md = convert_paragraph_to_markdown(
                element['paragraph'], 
                inline_objects
            )
            if paragraph_md:
                markdown_content += paragraph_md + '\n'
        elif 'table' in element:
            # Basic table support
            markdown_content += "\n| | |\n|---|---|\n"
            table = element['table']
            for row in table.get('tableRows', []):
                row_content = '|'
                for cell in row.get('tableCells', []):
                    cell_text = ''
                    for content_element in cell.get('content', []):
                        if 'paragraph' in content_element:
                            for elem in content_element['paragraph'].get('elements', []):
                                cell_text += extract_text_from_element(elem)
                    row_content += f" {cell_text.strip()} |"
                markdown_content += row_content + '\n'
            markdown_content += '\n'
    
    return markdown_content

def list_images_needed(markdown_content):
    """Extract list of images referenced in the markdown"""
    images = []
    
    # Find <img> tags
    img_pattern = r'<img\s+src="/img/([^"]+)"'
    images.extend(re.findall(img_pattern, markdown_content))
    
    # Find markdown images
    md_pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    for match in re.findall(md_pattern, markdown_content):
        if not match.startswith('http'):
            images.append(match)
    
    return list(set(images))  # Remove duplicates

def main():
    """Main sync function"""
    if not FOLDER_ID:
        print("Error: GDOCS_FOLDER_ID environment variable not set")
        return
        
    # Get credentials and build services
    credentials = get_credentials()
    drive_service = build('drive', 'v3', credentials=credentials)
    docs_service = build('docs', 'v1', credentials=credentials)
    
    # List files in folder and subfolders
    try:
        # First get direct documents
        results = drive_service.files().list(
            q=f"'{FOLDER_ID}' in parents and mimeType='application/vnd.google-apps.document'",
            fields="files(id, name)"
        ).execute()
        
        files = results.get('files', [])
        
        # Then check for subfolders
        folder_results = drive_service.files().list(
            q=f"'{FOLDER_ID}' in parents and mimeType='application/vnd.google-apps.folder'",
            fields="files(id, name)"
        ).execute()
        
        subfolders = folder_results.get('files', [])
        
        # Get documents from subfolders
        for subfolder in subfolders:
            print(f"Checking subfolder: {subfolder['name']}")
            sub_results = drive_service.files().list(
                q=f"'{subfolder['id']}' in parents and mimeType='application/vnd.google-apps.document'",
                fields="files(id, name)"
            ).execute()
            sub_files = sub_results.get('files', [])
            files.extend(sub_files)
            
    except HttpError as error:
        print(f"Error accessing folder: {error}")
        return
    
    if not files:
        print('No documents found in the specified folder or subfolders.')
        return
    
    print(f"Found {len(files)} documents to sync")
    
    all_images = []
    
    # Process each document
    for file in files:
        doc_name = file['name'].lower().strip()
        
        # Find matching content path
        output_path = None
        for key, path in DOC_MAPPING.items():
            if key in doc_name or doc_name in key:
                output_path = path
                break
        
        if not output_path:
            print(f"⚠️  No mapping found for document: {file['name']}")
            continue
            
        print(f"Processing {file['name']}...")
        
        # Get document content
        document = get_document_content(docs_service, file['id'])
        
        if document:
            # Convert to markdown
            markdown = convert_document_to_markdown(document, file['name'])
            
            # Extract images
            images = list_images_needed(markdown)
            if images:
                all_images.extend(images)
                print(f"  📷 Found {len(images)} image references: {', '.join(images)}")
            
            # Write to file
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            print(f"  ✓ Saved to {output_path}")
        else:
            print(f"  ✗ Failed to retrieve document content")
    
    # Report all images needed
    if all_images:
        unique_images = sorted(set(all_images))
        print(f"\n📷 Images referenced in documents ({len(unique_images)} total):")
        for img in unique_images:
            img_path = f"static/img/{img}"
            exists = "✓" if os.path.exists(img_path) else "✗"
            print(f"  {exists} {img}")
        
        # Update IMAGES_NEEDED.md
        missing_images = [img for img in unique_images 
                         if not os.path.exists(f"static/img/{img}")]
        if missing_images:
            with open('IMAGES_NEEDED.md', 'a') as f:
                f.write("\n\n## Images Referenced in Content\n")
                f.write("These images are referenced in your Google Docs:\n\n")
                for img in missing_images:
                    f.write(f"- `{img}` - Referenced in content\n")

    print("\nSync complete!")

if __name__ == '__main__':
    # Load .env file if it exists
    if os.path.exists('.env'):
        from dotenv import load_dotenv
        load_dotenv()
    
    main()