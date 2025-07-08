#!/usr/bin/env python3
"""
Test script to debug bullet point syncing
"""
import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from sync_gdocs_enhanced import convert_document_to_markdown, get_document_content

# Load credentials
service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_KEY'])
credentials = service_account.Credentials.from_service_account_info(
    service_account_info, 
    scopes=['https://www.googleapis.com/auth/documents.readonly']
)

# Build service
docs_service = build('docs', 'v1', credentials=credentials)

# Get the main document
doc_id = os.environ.get('MAIN_DOC_ID', '')  # You'll need to set this
if not doc_id:
    print("Please set MAIN_DOC_ID environment variable")
    exit(1)

# Get document
document = get_document_content(docs_service, doc_id)
if document:
    # Look for paragraphs with bullets
    content = document.get('body', {}).get('content', [])
    
    print("=== BULLET ANALYSIS ===")
    for i, element in enumerate(content):
        if 'paragraph' in element:
            paragraph = element['paragraph']
            style = paragraph.get('paragraphStyle', {})
            
            if 'bullet' in style:
                elements = paragraph.get('elements', [])
                text = ''
                for elem in elements:
                    if 'textRun' in elem:
                        text += elem['textRun']['content']
                
                bullet_info = style['bullet']
                indent_start = style.get('indentStart', {}).get('magnitude', 0)
                
                print(f"\nBullet {i}:")
                print(f"  Text: {text.strip()}")
                print(f"  Nesting Level: {bullet_info.get('nestingLevel', 0)}")
                print(f"  List ID: {bullet_info.get('listId', 'none')}")
                print(f"  Indent: {indent_start}")
                print(f"  Full bullet info: {bullet_info}")
    
    # Now convert and show result
    print("\n=== CONVERTED MARKDOWN ===")
    markdown = convert_document_to_markdown(document, 'main')
    print(markdown)