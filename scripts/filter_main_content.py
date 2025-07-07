#!/usr/bin/env python3
"""
Filter the main content to remove speakers/organizers sections
since they're handled by data files
"""
import re

def filter_main_content(content):
    """Remove speakers and organizers sections from main content"""
    
    # Find where "Speakers and Panelists" or similar section starts
    speaker_patterns = [
        r'Speakers and Panelists',
        r'Keynote Speakers',
        r'Organizing Committee',
        r'Organizers'
    ]
    
    # Find the earliest occurrence
    earliest_pos = len(content)
    for pattern in speaker_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match and match.start() < earliest_pos:
            earliest_pos = match.start()
    
    # If we found a section to remove, truncate there
    if earliest_pos < len(content):
        content = content[:earliest_pos].rstrip()
    
    return content

if __name__ == '__main__':
    # Read the current content
    with open('content/_index.md', 'r') as f:
        lines = f.readlines()
    
    # Keep the frontmatter
    frontmatter_end = 0
    for i, line in enumerate(lines):
        if line.strip() == '---' and i > 0:
            frontmatter_end = i + 1
            break
    
    # Get the content after frontmatter
    content = ''.join(lines[frontmatter_end:])
    
    # Filter it
    filtered = filter_main_content(content)
    
    # Write it back
    with open('content/_index.md', 'w') as f:
        f.writelines(lines[:frontmatter_end])
        f.write(filtered)
        f.write('\n')
    
    print("Filtered main content to remove duplicate speaker/organizer sections")