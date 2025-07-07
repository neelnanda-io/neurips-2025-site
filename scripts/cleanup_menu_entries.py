#!/usr/bin/env python3
"""
Cleanup script to remove menu entries from content files.
Menu navigation should only be defined in config.yaml.
"""
import os
import re

def cleanup_frontmatter(file_path):
    """Remove menu-related entries from markdown frontmatter"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check if file has frontmatter
    if not content.startswith('---'):
        return False
    
    # Split frontmatter and content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    frontmatter = parts[1]
    body = parts[2]
    
    # Remove menu-related lines
    lines = frontmatter.strip().split('\n')
    cleaned_lines = []
    changed = False
    
    for line in lines:
        # Skip menu, weight, date, and draft entries
        if any(line.strip().startswith(x) for x in ['menu:', 'weight:', 'date:', 'draft:']):
            changed = True
            continue
        cleaned_lines.append(line)
    
    if changed:
        # Reconstruct file
        new_frontmatter = '\n'.join(cleaned_lines)
        new_content = f"---\n{new_frontmatter}\n---{body}"
        
        with open(file_path, 'w') as f:
            f.write(new_content)
        
        print(f"✓ Cleaned {file_path}")
        return True
    
    return False

def main():
    """Clean all content files"""
    content_dir = 'content'
    cleaned_count = 0
    
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if cleanup_frontmatter(file_path):
                    cleaned_count += 1
    
    if cleaned_count > 0:
        print(f"\nCleaned {cleaned_count} files")
    else:
        print("No files needed cleaning")

if __name__ == '__main__':
    main()