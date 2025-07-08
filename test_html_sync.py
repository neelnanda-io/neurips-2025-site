#!/usr/bin/env python3
"""Test the HTML sync locally"""

# First, let's test the HTML parser
from scripts.sync_gdocs_html import GoogleDocsHTMLToMarkdown

# Test HTML
test_html = """
<h1>Main Header</h1>
<p>This is a paragraph with <b>bold text</b> and <i>italic text</i>.</p>
<p>This is a <a href="https://example.com">link to example</a>.</p>
<h2>Subheader</h2>
<ul>
<li>First bullet point</li>
<li>Second bullet point</li>
<li>Third bullet point with <b>bold</b></li>
</ul>
<p>Another paragraph after the list.</p>
<p>[SPEAKERS]</p>
<p>Final paragraph.</p>
"""

# Parse it
parser = GoogleDocsHTMLToMarkdown()
parser.feed(test_html)
markdown = parser.get_markdown()

print("=== Converted Markdown ===")
print(markdown)
print("=== End ===")