#!/usr/bin/env python3
"""
Sync Google Docs to Hugo markdown files
"""
import os
import json
import yaml
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configuration
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
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

def export_doc_as_markdown(service, file_id):
    """Export a Google Doc as plain text (we'll convert to markdown)"""
    try:
        # Export as plain text
        content = service.files().export(
            fileId=file_id, 
            mimeType='text/plain'
        ).execute()
        return content.decode('utf-8')
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def text_to_markdown(text, title):
    """Convert plain text to markdown with frontmatter"""
    # Basic conversion - you may want to enhance this
    lines = text.strip().split('\n')
    
    # Create frontmatter
    frontmatter = f"""---
title: "{title}"
---

"""
    
    # Basic markdown conversion
    markdown_lines = []
    for line in lines:
        line = line.strip()
        if line:
            # Simple heuristic for headers
            if line.isupper() and len(line) < 50:
                markdown_lines.append(f"## {line.title()}")
            else:
                markdown_lines.append(line)
        else:
            markdown_lines.append("")
    
    return frontmatter + '\n'.join(markdown_lines)

def main():
    """Main sync function"""
    # Get credentials and build service
    credentials = get_credentials()
    service = build('drive', 'v3', credentials=credentials)
    
    # List files in folder and subfolders
    # First get direct documents
    results = service.files().list(
        q=f"'{FOLDER_ID}' in parents and mimeType='application/vnd.google-apps.document'",
        fields="files(id, name)"
    ).execute()
    
    files = results.get('files', [])
    
    # Then check for subfolders
    folder_results = service.files().list(
        q=f"'{FOLDER_ID}' in parents and mimeType='application/vnd.google-apps.folder'",
        fields="files(id, name)"
    ).execute()
    
    subfolders = folder_results.get('files', [])
    
    # Get documents from subfolders
    for subfolder in subfolders:
        sub_results = service.files().list(
            q=f"'{subfolder['id']}' in parents and mimeType='application/vnd.google-apps.document'",
            fields="files(id, name)"
        ).execute()
        sub_files = sub_results.get('files', [])
        files.extend(sub_files)
    
    if not files:
        print('No documents found.')
        return
    
    # Process each document
    for file in files:
        doc_name = file['name'].lower().replace(' ', '_')
        
        if doc_name in DOC_MAPPING:
            print(f"Processing {file['name']}...")
            
            # Export document
            content = export_doc_as_markdown(service, file['id'])
            
            if content:
                # Convert to markdown
                markdown = text_to_markdown(content, file['name'])
                
                # Write to file
                output_path = DOC_MAPPING[doc_name]
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                with open(output_path, 'w') as f:
                    f.write(markdown)
                
                print(f"  → Saved to {output_path}")

if __name__ == '__main__':
    # Load .env file if it exists
    if os.path.exists('.env'):
        from dotenv import load_dotenv
        load_dotenv()
    
    # Re-get FOLDER_ID after loading .env
    FOLDER_ID = os.environ.get('GDOCS_FOLDER_ID')
    if not FOLDER_ID:
        print("Error: GDOCS_FOLDER_ID not found in environment")
        exit(1)
    
    main()
