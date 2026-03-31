#!/usr/bin/env python3
"""
Fix header background and menu button styling
"""

import os

print("🎨 Fixing header background and menu button...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    changes = 0
    
    # 1. Fix navbar classes for proper styling
    if 'navbar-light' in content:
        # Update to better styling
        content = content.replace('navbar-light', 'navbar-dark bg-primary')
        changes += 1
        print("  ✅ Updated navbar to dark theme with primary background")
    
    # 2. Ensure proper container classes
    if 'class="container"' in content and 'navbar' in content:
        # Check if we need to add padding
        if 'py-3' not in content[content.find('class="container"'):content.find('class="container"')+100]:
            # Add padding to container
            content = content.replace('class="container"', 'class="container py-3"')
            changes += 1
            print("  ✅ Added padding to container")
    
    # 3. Fix menu button styling
    if 'navbar-toggler' in content:
        # Ensure proper aria attributes and styling
        if 'data-bs-toggle="collapse"' not in content:
            # Fix toggle attributes
            import re
            button_pattern = r'(<button[^>]*navbar-toggler[^>]*>)'
            button_match = re.search(button_pattern, content)
            if button_match:
                old_button = button_match.group(0)
                new_button = '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">'
                content = content.replace(old_button, new_button)
                changes += 1
                print("  ✅ Fixed menu button attributes")
    
    # Write updated file
    if changes > 0:
        with open(html_file, 'w') as f:
            f.write(content)
        print(f"  🎯 Applied {changes} fixes")
    else:
        print("  ⚠️  No fixes needed")

print(f"\n{'='*50}")
print("✅ Header styling fixes applied!")
print("\n📋 What was fixed:")
print("1. Navbar: Changed to dark theme with primary background")
print("2. Container: Added padding (py-3)")
print("3. Menu button: Ensured proper Bootstrap attributes")
print("4. Overall: Professional header styling")
