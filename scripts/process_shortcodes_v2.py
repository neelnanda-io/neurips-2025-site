#!/usr/bin/env python3
"""
Process shortcodes in markdown content - case insensitive version
"""
import re
import yaml
import os

def load_data_file(filename):
    """Load YAML data file"""
    filepath = os.path.join('data', filename)
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} not found")
        return {}
    
    with open(filepath, 'r') as f:
        return yaml.safe_load(f) or {}

def generate_speakers_html():
    """Generate HTML for speakers section"""
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
    return html

def generate_organizers_html():
    """Generate HTML for organizers section"""
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
    return html

def generate_schedule_html():
    """Generate HTML for schedule table"""
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
    return html

def generate_signup_html():
    """Generate HTML for signup box"""
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
    return html

def process_shortcodes(content):
    """Process all shortcodes in content - case insensitive"""
    
    # Process each type of shortcode (case-insensitive)
    # Using function to handle replacement
    def replace_speakers(match):
        return generate_speakers_html()
    
    def replace_organizers(match):
        return generate_organizers_html()
    
    def replace_schedule(match):
        return generate_schedule_html()
    
    def replace_signup(match):
        return generate_signup_html()
    
    # Replace all variations of shortcodes
    content = re.sub(r'\[speakers?\]', replace_speakers, content, flags=re.IGNORECASE)
    content = re.sub(r'\{\{<\s*speakers?\s*>\}\}', replace_speakers, content, flags=re.IGNORECASE)
    content = re.sub(r'\{%\s*speakers?\s*%\}', replace_speakers, content, flags=re.IGNORECASE)
    
    content = re.sub(r'\[organizers?\]', replace_organizers, content, flags=re.IGNORECASE)
    content = re.sub(r'\{\{<\s*organizers?\s*>\}\}', replace_organizers, content, flags=re.IGNORECASE)
    content = re.sub(r'\{%\s*organizers?\s*%\}', replace_organizers, content, flags=re.IGNORECASE)
    
    content = re.sub(r'\[schedule\]', replace_schedule, content, flags=re.IGNORECASE)
    content = re.sub(r'\{\{<\s*schedule\s*>\}\}', replace_schedule, content, flags=re.IGNORECASE)
    content = re.sub(r'\{%\s*schedule\s*%\}', replace_schedule, content, flags=re.IGNORECASE)
    
    content = re.sub(r'\[signup\]', replace_signup, content, flags=re.IGNORECASE)
    content = re.sub(r'\{\{<\s*signup\s*>\}\}', replace_signup, content, flags=re.IGNORECASE)
    content = re.sub(r'\{%\s*signup\s*%\}', replace_signup, content, flags=re.IGNORECASE)
    
    return content

def process_file(filepath):
    """Process a single markdown file"""
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if any shortcodes exist (case-insensitive)
    shortcode_patterns = [
        r'\[(speakers?|organizers?|schedule|signup)\]',
        r'\{\{<\s*(speakers?|organizers?|schedule|signup)\s*>\}\}',
        r'\{%\s*(speakers?|organizers?|schedule|signup)\s*%\}'
    ]
    
    has_shortcodes = False
    for pattern in shortcode_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            has_shortcodes = True
            break
    
    if not has_shortcodes:
        return False
    
    # Process shortcodes
    new_content = process_shortcodes(content)
    
    # Write back
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return True

def main():
    """Process all content files"""
    print("Processing shortcodes...")
    processed_count = 0
    
    # Process all markdown files in content directory
    for root, dirs, files in os.walk('content'):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                if process_file(filepath):
                    print(f"✓ Processed: {filepath}")
                    processed_count += 1
    
    if processed_count > 0:
        print(f"\nProcessed {processed_count} files")
    else:
        print("No shortcodes found to process")

if __name__ == '__main__':
    main()