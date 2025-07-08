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

def load_schedule_html():
    """Generate HTML for schedule table"""
    # Read schedule content
    schedule_content = """
<section class="embedded-schedule">
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
"""
    return schedule_content

def load_signup_html():
    """Generate HTML for signup box"""
    signup_html = """
<div class="embedded-signup">
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
"""
    return signup_html

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
    
    # Pattern: {{< schedule >}} or {{% schedule %}}
    if '{{< schedule >}}' in content or '{{% schedule %}}' in content:
        schedule_html = load_schedule_html()
        content = content.replace('{{< schedule >}}', schedule_html)
        content = content.replace('{{% schedule %}}', schedule_html)
    
    # Pattern: {{< signup >}} or {{% signup %}}
    if '{{< signup >}}' in content or '{{% signup %}}' in content:
        signup_html = load_signup_html()
        content = content.replace('{{< signup >}}', signup_html)
        content = content.replace('{{% signup %}}', signup_html)
    
    # Pattern: [ORGANIZERS] or [SPEAKERS] (simpler syntax) - case insensitive
    content_upper = content.upper()
    
    if '[ORGANIZERS]' in content_upper:
        organizers_html = load_organizers_html()
        content = re.sub(r'\[ORGANIZERS\]', organizers_html, content, flags=re.IGNORECASE)
    
    if '[SPEAKERS]' in content_upper:
        speakers_html = load_speakers_html()
        content = re.sub(r'\[SPEAKERS\]', speakers_html, content, flags=re.IGNORECASE)
    
    if '[SCHEDULE]' in content_upper:
        schedule_html = load_schedule_html()
        content = re.sub(r'\[SCHEDULE\]', schedule_html, content, flags=re.IGNORECASE)
    
    if '[SIGNUP]' in content_upper:
        signup_html = load_signup_html()
        content = re.sub(r'\[SIGNUP\]', signup_html, content, flags=re.IGNORECASE)
    
    return content

def process_file(file_path):
    """Process shortcodes in a single file"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Skip if no shortcodes found (case insensitive for bracket shortcodes)
    content_upper = content.upper()
    if not any(shortcode in content_upper for shortcode in ['[ORGANIZERS]', '[SPEAKERS]', '[SCHEDULE]', '[SIGNUP]']) and \
       not any(shortcode in content for shortcode in ['{{< organizers', '{{< speakers', '{{< schedule', '{{< signup', '{{% organizers', '{{% speakers', '{{% schedule', '{{% signup']):
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