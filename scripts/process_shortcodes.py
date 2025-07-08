#!/usr/bin/env python3
"""
Process shortcodes in markdown content to include dynamic sections
"""
import re
import yaml
import os

def load_organizers_html():
    """Generate HTML for organizers section from data file"""
    # Load organizers data
    with open('data/organizers.yaml', 'r') as f:
        data = yaml.safe_load(f)
    
    if not data or 'organizers' not in data:
        return ''
    
    html = '<section class="embedded-organizers">\n'
    html += '<h2>Organizing Committee</h2>\n'
    html += '<div class="organizers speakers">\n'
    
    for organizer in data['organizers']:
        html += '  <div class="speaker">\n'
        html += f'    <img src="/img/{organizer["image"]}" alt="{organizer["name"]}" />\n'
        html += '    <div>\n'
        
        if organizer.get('website'):
            html += f'      <h3><a href="{organizer["website"]}">{organizer["name"]}</a></h3>\n'
        else:
            html += f'      <h3>{organizer["name"]}</h3>\n'
        
        html += f'      <p>{organizer["affiliation"]}</p>\n'
        html += '    </div>\n'
        html += '  </div>\n'
    
    html += '</div>\n'
    html += '</section>\n'
    
    return html

def load_speakers_html():
    """Generate HTML for speakers section from data file"""
    # Load speakers data
    with open('data/speakers.yaml', 'r') as f:
        data = yaml.safe_load(f)
    
    if not data or 'speakers' not in data:
        return ''
    
    html = '<section class="embedded-speakers">\n'
    html += '<h2>Keynote Speakers</h2>\n'
    html += '<div class="speakers">\n'
    
    for speaker in data['speakers']:
        html += '  <div class="speaker">\n'
        html += f'    <img src="/img/{speaker["image"]}" alt="{speaker["name"]}" />\n'
        html += '    <div>\n'
        
        if speaker.get('website'):
            html += f'      <h3><a href="{speaker["website"]}">{speaker["name"]}</a></h3>\n'
        else:
            html += f'      <h3>{speaker["name"]}</h3>\n'
        
        html += f'      <p>{speaker["affiliation"]}</p>\n'
        html += '    </div>\n'
        html += '  </div>\n'
    
    html += '</div>\n'
    html += '</section>\n'
    
    return html

def process_shortcodes(content):
    """Process shortcodes in markdown content"""
    
    # Pattern: {{< organizers >}} or {{% organizers %}}
    if '{{< organizers >}}' in content or '{{% organizers %}}' in content:
        organizers_html = load_organizers_html()
        content = content.replace('{{< organizers >}}', organizers_html)
        content = content.replace('{{% organizers %}}', organizers_html)
    
    # Pattern: {{< speakers >}} or {{% speakers %}}
    if '{{< speakers >}}' in content or '{{% speakers %}}' in content:
        speakers_html = load_speakers_html()
        content = content.replace('{{< speakers >}}', speakers_html)
        content = content.replace('{{% speakers %}}', speakers_html)
    
    # Pattern: [ORGANIZERS] or [SPEAKERS] (simpler syntax)
    if '[ORGANIZERS]' in content:
        organizers_html = load_organizers_html()
        content = content.replace('[ORGANIZERS]', organizers_html)
    
    if '[SPEAKERS]' in content:
        speakers_html = load_speakers_html()
        content = content.replace('[SPEAKERS]', speakers_html)
    
    return content

def process_file(file_path):
    """Process shortcodes in a single file"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Skip if no shortcodes found
    if not any(shortcode in content for shortcode in ['[ORGANIZERS]', '[SPEAKERS]', '{{< organizers', '{{< speakers', '{{% organizers', '{{% speakers']):
        return False
    
    # Process shortcodes
    new_content = process_shortcodes(content)
    
    # Write back if changed
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        return True
    
    return False

def main():
    """Process all markdown files"""
    processed = 0
    
    for root, dirs, files in os.walk('content'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if process_file(file_path):
                    print(f"✓ Processed shortcodes in {file_path}")
                    processed += 1
    
    if processed > 0:
        print(f"\nProcessed {processed} files")
    else:
        print("No shortcodes found to process")

if __name__ == '__main__':
    main()