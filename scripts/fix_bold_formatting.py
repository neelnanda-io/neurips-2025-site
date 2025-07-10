#!/usr/bin/env python3
"""
Post-processing script to fix bold formatting issues in markdown files.
This is a temporary fix while we improve the HTML parser.
"""

import re
import sys
from pathlib import Path

def fix_bold_formatting(content):
    """Fix common bold formatting issues."""
    
    # Remove bold from entire paragraphs that contain multiple sentences
    # This often happens when Google Docs applies paragraph-level formatting
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Skip headers
        if line.strip().startswith('#'):
            # Remove bold from headers
            line = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
        # Check if entire line is bolded
        elif line.strip().startswith('**') and line.strip().endswith('**'):
            # If it's a multi-sentence paragraph, unbold it
            inner = line.strip()[2:-2]
            if '. ' in inner or len(inner) > 100:
                line = line.replace('**' + inner + '**', inner)
        # Fix cases where bold extends across multiple inline elements
        elif '**' in line:
            # Count ** pairs
            bold_count = line.count('**')
            if bold_count % 2 != 0:
                # Odd number of **, likely a formatting error
                # Remove the last one
                line = line[::-1].replace('**', '', 1)[::-1]
        
        fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    # Fix specific patterns we see in the output
    # Remove bold from list items that span multiple lines
    content = re.sub(r'^\*\s+\*\*([^*]+)\*\*$', r'* \1', content, flags=re.MULTILINE)
    
    # Fix bold that spans across line breaks (common in Google Docs)
    content = re.sub(r'\*\*\s*\n\s*', '\n', content)
    
    # Remove double spaces after fixing
    content = re.sub(r'  +', ' ', content)
    
    return content

def main():
    """Process markdown files to fix bold formatting."""
    content_dir = Path('content')
    
    # Process all markdown files
    for md_file in content_dir.rglob('*.md'):
        print(f"Processing {md_file}")
        
        content = md_file.read_text()
        fixed_content = fix_bold_formatting(content)
        
        if content != fixed_content:
            md_file.write_text(fixed_content)
            print(f"  ✓ Fixed formatting in {md_file}")
        else:
            print(f"  - No changes needed for {md_file}")

if __name__ == '__main__':
    main()