#!/usr/bin/env python3
"""
Fix HTML structure and update to use optimized CSS
"""

import os
import re

print("🔧 Fixing HTML structure and updating CSS...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    changes = 0
    
    # 1. Remove old CSS links
    old_css = ['style.min.css', 'mobile_optimization.css', 'proper-site.css', 'clean-template.css']
    for css_file in old_css:
        if f'<link rel="stylesheet" href="css/{css_file}">' in content:
            content = content.replace(f'<link rel="stylesheet" href="css/{css_file}">', '')
            changes += 1
            print(f"  ✅ Removed: {css_file}")
    
    # 2. Add optimized CSS
    if '<link rel="stylesheet" href="css/optimized.css">' not in content:
        # Find the position after favicon
        favicon_pos = content.find('<link rel="icon"')
        if favicon_pos != -1:
            # Insert after favicon line
            insert_pos = content.find('\n', favicon_pos) + 1
            optimized_css = '    <link rel="stylesheet" href="css/optimized.css">\n'
            content = content[:insert_pos] + optimized_css + content[insert_pos:]
            changes += 1
            print("  ✅ Added optimized CSS")
    
    # 3. Remove empty divs and broken HTML
    # Remove empty container divs
    empty_patterns = [
        r'\s*<div class="container">\s*</div>\s*',
        r'\s*<div class="container py-3">\s*</div>\s*',
        r'\s*<div>\s*</div>\s*'
    ]
    
    for pattern in empty_patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        for match in matches:
            content = content.replace(match, '')
            changes += 1
            print("  ✅ Removed empty div")
    
    # 4. Fix broken "expandable home" text
    if 'expandable home' in content:
        content = content.replace('expandable home', 'Expandable Home')
        content = content.replace('expandable homes', 'Expandable Homes')
        content = content.replace('expandable expandable', 'expandable')
        changes += 1
        print("  ✅ Fixed 'expandable home' text")
    
    # 5. Remove duplicate scripts
    old_js = ['clean-template.js', 'professional-header-behavior.js', 'header-behavior.js', 'sticky-header.js']
    for js_file in old_js:
        if f'<script src="js/{js_file}"></script>' in content:
            content = content.replace(f'<script src="js/{js_file}"></script>', '')
            changes += 1
            print(f"  ✅ Removed: {js_file}")
    
    # 6. Add optimized JavaScript
    if '<script src="js/optimized.js"></script>' not in content:
        # Add before closing body tag
        if '</body>' in content:
            optimized_js = '    <script src="js/optimized.js"></script>\n'
            content = content.replace('</body>', optimized_js + '</body>')
            changes += 1
            print("  ✅ Added optimized JS")
    
    # 7. Ensure proper HTML structure
    # Check for proper header closing
    if '</header>' in content and '<section' in content:
        # Make sure there's no content between header and first section
        header_end = content.find('</header>') + 9
        first_section = content.find('<section', header_end)
        
        if first_section > header_end:
            # Check what's between them
            between = content[header_end:first_section].strip()
            if between and not between.startswith('<!--'):
                # Remove any non-comment content
                content = content[:header_end] + '\n\n' + content[first_section:]
                changes += 1
                print("  ✅ Cleaned content between header and sections")
    
    # Write updated file
    if changes > 0:
        with open(html_file, 'w') as f:
            f.write(content)
        print(f"  🎯 Applied {changes} fixes")
    else:
        print("  ⚠️  No fixes needed")

print("\n✅ HTML structure fixed!")
print("\n🎯 What was done:")
print("1. Removed old CSS files")
print("2. Added optimized CSS")
print("3. Removed empty/broken HTML")
print("4. Fixed 'expandable home' text")
print("5. Removed duplicate JavaScript")
print("6. Added optimized JavaScript")
print("7. Cleaned HTML structure")
