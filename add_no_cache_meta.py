#!/usr/bin/env python3
"""
Add no-cache meta tags to prevent browser caching during updates
"""

import os

print("🔄 Adding no-cache meta tags to prevent browser caching")

# Process all HTML files except test file
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\nProcessing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Check if no-cache meta tags already exist
    if 'no-cache' in content or 'no-store' in content:
        print(f"  ⚠️  No-cache meta tags already exist in {html_file}")
        continue
    
    # Add no-cache meta tags in the head section
    no_cache_meta = '''    <!-- Prevent caching during updates -->
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">'''
    
    # Insert before closing head tag
    if '</head>' in content:
        content = content.replace('</head>', f'{no_cache_meta}\n</head>')
        
        with open(html_file, 'w') as f:
            f.write(content)
        
        print(f"  ✅ Added no-cache meta tags to {html_file}")
    else:
        print(f"  ❌ Could not find </head> tag in {html_file}")

print("\n🎯 No-cache meta tags added!")
print("\n📋 This will force browsers to fetch fresh files on each visit.")
print("   Once the site is stable, these can be removed for better performance.")
