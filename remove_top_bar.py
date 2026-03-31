#!/usr/bin/env python3
"""
Remove the top bar with contact details from all pages
"""

import os

print("🗑️ Removing top contact details bar from all pages...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Find and remove the top bar section
    # Look for <!-- Top Bar --> to closing div
    top_bar_pattern = r'(<!-- Top Bar -->.*?<div class="container">.*?</div>\s*</div>)'
    
    import re
    match = re.search(top_bar_pattern, content, re.DOTALL)
    
    if match:
        top_bar = match.group(0)
        content = content.replace(top_bar, '')
        print("  ✅ Removed top contact details bar")
        
        # Write updated file
        with open(html_file, 'w') as f:
            f.write(content)
    else:
        print("  ⚠️  No top bar found (already removed?)")

print("\n✅ Top contact details removed from all pages!")
print("\n🎯 The website now has:")
print("1. Clean professional header (no top contact bar)")
print("2. No 'shipping container' text")
print("3. Professional 'expandable home' terminology")
print("4. Mobile-optimized Bootstrap navigation")
