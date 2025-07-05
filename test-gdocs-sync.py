#!/usr/bin/env python3
"""
Test Google Docs sync configuration
"""
import os
import json
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def test_sync():
    """Test the Google Docs sync configuration"""
    print("🔍 Testing Google Docs sync configuration...\n")
    
    # Check environment variables
    print("1. Checking environment variables...")
    
    if not os.environ.get('GOOGLE_SERVICE_ACCOUNT_KEY'):
        print("❌ GOOGLE_SERVICE_ACCOUNT_KEY not found in environment")
        print("   Make sure you've set it as a GitHub secret or in .env file")
        return False
    else:
        print("✅ GOOGLE_SERVICE_ACCOUNT_KEY found")
    
    if not os.environ.get('GDOCS_FOLDER_ID'):
        print("❌ GDOCS_FOLDER_ID not found in environment")
        print("   Make sure you've set it as a GitHub secret or in .env file")
        return False
    else:
        print("✅ GDOCS_FOLDER_ID found:", os.environ['GDOCS_FOLDER_ID'])
    
    # Test credentials
    print("\n2. Testing Google API credentials...")
    try:
        service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_KEY'])
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info, 
            scopes=['https://www.googleapis.com/auth/drive.readonly']
        )
        print("✅ Credentials parsed successfully")
    except Exception as e:
        print(f"❌ Failed to parse credentials: {e}")
        return False
    
    # Test API connection
    print("\n3. Testing Google Drive API connection...")
    try:
        service = build('drive', 'v3', credentials=credentials)
        print("✅ Connected to Google Drive API")
    except Exception as e:
        print(f"❌ Failed to connect to API: {e}")
        return False
    
    # List files in folder and subfolders
    print("\n4. Checking folder access and contents...")
    try:
        # First, list direct contents
        results = service.files().list(
            q=f"'{os.environ['GDOCS_FOLDER_ID']}' in parents",
            fields="files(id, name, mimeType)"
        ).execute()
        
        files = results.get('files', [])
        
        if not files:
            print("❌ No files found in folder - is the folder empty or not shared?")
            return False
        
        print(f"✅ Found {len(files)} items in main folder:")
        all_docs = []
        subfolders = []
        
        for file in files:
            print(f"   - {file['name']} ({file['mimeType']})")
            if file['mimeType'] == 'application/vnd.google-apps.folder':
                subfolders.append(file)
            elif file['mimeType'] == 'application/vnd.google-apps.document':
                all_docs.append(file)
        
        # Check subfolders for documents
        for subfolder in subfolders:
            print(f"\n   Checking subfolder '{subfolder['name']}'...")
            sub_results = service.files().list(
                q=f"'{subfolder['id']}' in parents and mimeType='application/vnd.google-apps.document'",
                fields="files(id, name, mimeType)"
            ).execute()
            
            sub_files = sub_results.get('files', [])
            if sub_files:
                print(f"   Found {len(sub_files)} documents in subfolder:")
                for file in sub_files:
                    print(f"     - {file['name']}")
                    all_docs.append(file)
        
        print(f"\n5. Checking for expected documents...")
        expected_docs = ['main', 'cfp', 'schedule', 'speakers', 'organizers']
        found_docs = []
        
        for doc in all_docs:
            doc_name = doc['name'].lower()
            for expected in expected_docs:
                if expected in doc_name or doc_name in expected:
                    found_docs.append(expected)
                    print(f"✅ Found '{expected}' document: {doc['name']}")
                    break
        
        for doc in expected_docs:
            if doc not in found_docs:
                print(f"❌ Missing '{doc}' document")
        
        # Test reading a document
        print("\n6. Testing document read access...")
        test_doc = None
        for doc in all_docs:
            if doc['mimeType'] == 'application/vnd.google-apps.document':
                test_doc = doc
                break
        
        if test_doc:
            try:
                content = service.files().export(
                    fileId=test_doc['id'], 
                    mimeType='text/plain'
                ).execute()
                print(f"✅ Successfully read '{test_doc['name']}' ({len(content)} bytes)")
            except Exception as e:
                print(f"❌ Failed to read document: {e}")
                print("   Check that the service account has 'Viewer' permission")
                return False
        else:
            print("❌ No Google Docs found to test reading")
                
    except HttpError as e:
        print(f"❌ API Error: {e}")
        if 'does not have sufficient permissions' in str(e):
            print("   Make sure you've shared the folder with the service account email")
        return False
    
    print("\n✅ All tests passed! Your Google Docs sync is configured correctly.")
    print("\nNext steps:")
    print("1. Run the sync script: python scripts/sync_gdocs.py")
    print("2. Or trigger the GitHub Action manually")
    print("3. Check that content files are updated in content/")
    
    return True

if __name__ == '__main__':
    # Load .env file if it exists
    if os.path.exists('.env'):
        from dotenv import load_dotenv
        load_dotenv()
        print("📁 Loaded .env file\n")
    
    success = test_sync()
    sys.exit(0 if success else 1)