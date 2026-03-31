#!/usr/bin/env python3
"""
Add cache busting to all CSS and JS references
"""

import re
import os
from datetime import datetime

# Generate cache busting version (timestamp)
cache_version = datetime.now().strftime("%Y%m%d%H%M")

print(f"🔄 Adding cache busting version: v{cache_version}")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for html_file in html_files:
    print(f"\nProcessing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    changes_made = 0
    
    # Cache bust CSS files
    css_pattern = r'(href="[^"]*\.css)([^"]*)(")'
    def add_css_version(match):
        href = match.group(1)
        existing_query = match.group(2)
        quote = match.group(3)
        
        if '?' in existing_query:
            # Replace existing version parameter
            new_href = re.sub(r'\?v=\d+', f'?v={cache_version}', href + existing_query)
        else:
            # Add version parameter
            new_href = f'{href}?v={cache_version}'
        
        nonlocal changes_made
        changes_made += 1
        return new_href + quote
    
    # Use a different approach since we can't use nonlocal in nested function
    # Let's do it with a loop instead
    
    # Find and replace CSS links
    css_matches = list(re.finditer(css_pattern, content))
    for match in reversed(css_matches):  # Go backwards to avoid index issues
        href = match.group(1)
        existing_query = match.group(2)
        quote = match.group(3)
        
        if '?' in existing_query:
            # Replace existing version parameter
            new_href = re.sub(r'\?v=\d+', f'?v={cache_version}', href + existing_query)
        else:
            # Add version parameter
            new_href = f'{href}?v={cache_version}'
        
        # Replace in content
        start, end = match.span()
        content = content[:start] + new_href + quote + content[end:]
        changes_made += 1
    
    # Find and replace JS links
    js_pattern = r'(src="[^"]*\.js)([^"]*)(")'
    js_matches = list(re.finditer(js_pattern, content))
    for match in reversed(js_matches):
        src = match.group(1)
        existing_query = match.group(2)
        quote = match.group(3)
        
        if '?' in existing_query:
            # Replace existing version parameter
            new_src = re.sub(r'\?v=\d+', f'?v={cache_version}', src + existing_query)
        else:
            # Add version parameter
            new_src = f'{src}?v={cache_version}'
        
        # Replace in content
        start, end = match.span()
        content = content[:start] + new_src + quote + content[end:]
        changes_made += 1
    
    # Write updated file
    if changes_made > 0:
        with open(html_file, 'w') as f:
            f.write(content)
        print(f"  ✅ Updated {changes_made} cache busting references")
    else:
        print(f"  ⚠️  No cache busting needed")

print(f"\n🎯 Cache busting complete! Version: v{cache_version}")
print("\n📋 Files updated with cache busting:")
for html_file in html_files:
    print(f"  - {html_file}")
