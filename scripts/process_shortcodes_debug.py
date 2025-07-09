#!/usr/bin/env python3
"""
Debug version of shortcode processor to identify issues
"""
import re
import yaml
import os
import sys

def load_data_file(filename):
    """Load YAML data file"""
    filepath = os.path.join('data', filename)
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} not found")
        return {}
    
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f) or {}
            print(f"✓ Loaded {filename}: {len(data.get('organizers', data.get('speakers', [])))} entries")
            return data
    except Exception as e:
        print(f"✗ Error loading {filename}: {e}")
        return {}

def generate_speakers_html():
    """Generate HTML for speakers section"""
    print("Generating speakers HTML...")
    data = load_data_file('speakers.yaml')
    if not data or 'speakers' not in data:
        return '<!-- No speakers data found -->'
    
    html = '<section class="embedded-speakers">\n'
    html += '<h2>Keynote Speakers</h2>\n'
    html += '<div class="speakers">\n'
    
    for speaker in data['speakers']:
        html += '  <div class="speaker">\n'
        html += f'    <img src="/img/{speaker.get("image", "")}" alt="{speaker.get("name", "")}" />\n'
        html += '    <div>\n'
        if speaker.get('website'):
            html += f'      <h3><a href="{speaker["website"]}">{speaker.get("name", "")}</a></h3>\n'
        else:
            html += f'      <h3>{speaker.get("name", "")}</h3>\n'
        html += f'      <p>{speaker.get("affiliation", "")}</p>\n'
        html += '    </div>\n'
        html += '  </div>\n'
    
    html += '</div>\n</section>\n'
    print(f"✓ Generated speakers HTML: {len(html)} chars")
    return html

def generate_organizers_html():
    """Generate HTML for organizers section"""
    print("Generating organizers HTML...")
    data = load_data_file('organizers.yaml')
    if not data or 'organizers' not in data:
        return '<!-- No organizers data found -->'
    
    html = '<section class="embedded-organizers">\n'
    html += '<h2>Organizing Committee</h2>\n'
    html += '<div class="organizers speakers">\n'
    
    for organizer in data['organizers']:
        html += '  <div class="speaker">\n'
        html += f'    <img src="/img/{organizer.get("image", "")}" alt="{organizer.get("name", "")}" />\n'
        html += '    <div>\n'
        if organizer.get('website'):
            html += f'      <h3><a href="{organizer["website"]}">{organizer.get("name", "")}</a></h3>\n'
        else:
            html += f'      <h3>{organizer.get("name", "")}</h3>\n'
        html += f'      <p>{organizer.get("affiliation", "")}</p>\n'
        html += '    </div>\n'
        html += '  </div>\n'
    
    html += '</div>\n</section>\n'
    print(f"✓ Generated organizers HTML: {len(html)} chars")
    return html

def generate_schedule_html():
    """Generate HTML for schedule table"""
    print("Generating schedule HTML...")
    html = '''<section class="embedded-schedule">
<h2>Schedule (Provisional)</h2>
<table>
<thead>
<tr>
<th>Time</th>
<th>Activity</th>
</tr>
</thead>
<tbody>
<tr><td>09:00 - 09:30</td><td>Welcome and survey talk</td></tr>
<tr><td>09:30 - 10:00</td><td>Talk: Been Kim</td></tr>
<tr><td>10:00 - 11:00</td><td>Contributed talks 1</td></tr>
<tr><td>11:00 - 12:00</td><td>Poster session 1, coffee</td></tr>
<tr><td>12:00 - 13:00</td><td>Lunch with organised discussions</td></tr>
<tr><td>13:00 - 13:30</td><td>Talk: Sarah Schwettmann</td></tr>
<tr><td>13:30 - 14:30</td><td>Contributed talks 2</td></tr>
<tr><td>14:30 - 15:30</td><td>Poster session 2, coffee</td></tr>
<tr><td>15:30 - 16:00</td><td>Talk: Chris Olah</td></tr>
<tr><td>16:00 - 16:30</td><td>Coffee & Networking break</td></tr>
<tr><td>16:30 - 17:20</td><td>Panel discussion</td></tr>
<tr><td>17:20 - 17:30</td><td>Awards & closing</td></tr>
<tr><td>19:00 - 22:00</td><td>Evening social (invite-only)</td></tr>
</tbody>
</table>
</section>
'''
    print(f"✓ Generated schedule HTML: {len(html)} chars")
    return html

def generate_signup_html():
    """Generate HTML for signup form"""
    print("Generating signup HTML...")
    html = '''<div class="embedded-signup">
  <h2>Stay Updated</h2>
  <div class="mailing-list-form">
    <form action="https://buttondown.com/api/emails/embed-subscribe/mechinterpworkshop"
          method="post" target="popupwindow"
          onsubmit="window.open('https://buttondown.com/mechinterpworkshop', 'popupwindow')"
          class="embeddable-buttondown-form">
      <input type="email" name="email" placeholder="Email" required />
      <input type="submit" value="Subscribe for updates" />
    </form>
  </div>
</div>
'''
    print(f"✓ Generated signup HTML: {len(html)} chars")
    return html

def process_shortcodes(content):
    """Process all shortcodes in content"""
    print(f"\nProcessing content ({len(content)} chars)...")
    
    # Create replacement functions
    shortcode_count = 0
    
    def replace_speakers(match):
        nonlocal shortcode_count
        shortcode_count += 1
        print(f"  → Replacing [SPEAKERS] at position {match.start()}")
        return generate_speakers_html()
    
    def replace_organizers(match):
        nonlocal shortcode_count
        shortcode_count += 1
        print(f"  → Replacing [ORGANIZERS] at position {match.start()}")
        return generate_organizers_html()
    
    def replace_schedule(match):
        nonlocal shortcode_count
        shortcode_count += 1
        print(f"  → Replacing [SCHEDULE] at position {match.start()}")
        return generate_schedule_html()
    
    def replace_signup(match):
        nonlocal shortcode_count
        shortcode_count += 1
        print(f"  → Replacing [SIGNUP] at position {match.start()}")
        return generate_signup_html()
    
    # Process each shortcode type with case-insensitive regex
    print("\nSearching for shortcodes...")
    
    # Find all shortcodes first
    all_shortcodes = re.findall(r'\[(?:speakers?|organizers?|schedule|signup)\]', content, flags=re.IGNORECASE)
    print(f"Found {len(all_shortcodes)} shortcodes: {all_shortcodes}")
    
    # Replace them
    content = re.sub(r'\[speakers?\]', replace_speakers, content, flags=re.IGNORECASE)
    content = re.sub(r'\[organizers?\]', replace_organizers, content, flags=re.IGNORECASE)
    content = re.sub(r'\[schedule\]', replace_schedule, content, flags=re.IGNORECASE)
    content = re.sub(r'\[signup\]', replace_signup, content, flags=re.IGNORECASE)
    
    print(f"\n✓ Replaced {shortcode_count} shortcodes")
    print(f"✓ Final content size: {len(content)} chars")
    
    return content

def process_file(file_path):
    """Process shortcodes in a single file"""
    print(f"\n{'='*60}")
    print(f"Processing: {file_path}")
    print(f"{'='*60}")
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        print(f"✓ Read file: {len(content)} chars")
        
        # Check if file seems truncated
        if content.rstrip().endswith('['):
            print("⚠️  WARNING: File appears to be truncated (ends with '[')!")
        
        # Process shortcodes
        new_content = process_shortcodes(content)
        
        # Write back if changed
        if new_content != content:
            with open(file_path, 'w') as f:
                f.write(new_content)
            print(f"✓ Wrote updated file: {len(new_content)} chars")
            return True
        else:
            print("ℹ️  No changes needed")
            return False
            
    except Exception as e:
        print(f"✗ Error processing file: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Process all markdown files"""
    if len(sys.argv) > 1:
        # Process specific file
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            process_file(file_path)
        else:
            print(f"File not found: {file_path}")
    else:
        # Process all content files
        processed = 0
        
        for root, dirs, files in os.walk('content'):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    if process_file(file_path):
                        processed += 1
        
        print(f"\n{'='*60}")
        print(f"Summary: Processed {processed} files")
        print(f"{'='*60}")

if __name__ == '__main__':
    main()