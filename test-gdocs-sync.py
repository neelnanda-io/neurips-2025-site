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
    
    # List files in folder
    print("\n4. Checking folder access and contents...")
    try:
        results = service.files().list(
            q=f"'{os.environ['GDOCS_FOLDER_ID']}' in parents",
            fields="files(id, name, mimeType)"
        ).execute()
        
        files = results.get('files', [])
        
        if not files:
            print("❌ No files found in folder - is the folder empty or not shared?")
            return False
        
        print(f"✅ Found {len(files)} files in folder:")
        expected_docs = ['main', 'cfp', 'schedule', 'speakers', 'organizers']
        found_docs = []
        
        for file in files:
            print(f"   - {file['name']} ({file['mimeType']})")
            if file['name'].lower() in expected_docs:
                found_docs.append(file['name'].lower())
        
        print(f"\n5. Checking for expected documents...")
        for doc in expected_docs:
            if doc in found_docs:
                print(f"✅ Found '{doc}' document")
            else:
                print(f"❌ Missing '{doc}' document")
        
        # Test reading a document
        print("\n6. Testing document read access...")
        if files:
            test_file = files[0]
            try:
                content = service.files().export(
                    fileId=test_file['id'], 
                    mimeType='text/plain'
                ).execute()
                print(f"✅ Successfully read '{test_file['name']}' ({len(content)} bytes)")
            except Exception as e:
                print(f"❌ Failed to read document: {e}")
                print("   Check that the service account has 'Viewer' permission")
                return False
                
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