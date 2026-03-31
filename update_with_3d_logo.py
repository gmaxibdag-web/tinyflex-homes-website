#!/usr/bin/env python3
"""
Update header to use the new 3D logo
"""

import os

print("🎨 Updating header with new 3D logo...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Find the logo section in the header
    import re
    
    # Look for the logo-container div
    logo_pattern = r'(<a class="navbar-brand" href="index.html">.*?</a>)'
    logo_match = re.search(logo_pattern, content, re.DOTALL)
    
    if logo_match:
        old_logo = logo_match.group(0)
        
        # Create new 3D logo
        new_logo = '''<a class="navbar-brand" href="index.html">
            <div class="tinyflex-3d-logo">
                <div class="logo-3d-container">
                    <!-- 3D Cube -->
                    <div class="logo-cube">
                        <div class="cube-face cube-face-front">T</div>
                        <div class="cube-face cube-face-back">F</div>
                        <div class="cube-face cube-face-right"></div>
                        <div class="cube-face cube-face-left"></div>
                        <div class="cube-face cube-face-top"></div>
                        <div class="cube-face cube-face-bottom"></div>
                    </div>
                    
                    <!-- Expanding Arrows -->
                    <div class="expand-arrows">
                        <div class="arrow"></div>
                        <div class="arrow"></div>
                        <div class="arrow"></div>
                    </div>
                    
                    <!-- Logo Text -->
                    <div class="logo-3d-text">TinyFlex</div>
                    <div class="logo-tagline">Expandable Homes</div>
                </div>
            </div>
        </a>'''
        
        # Replace the logo
        content = content.replace(old_logo, new_logo)
        
        # Add advanced logo CSS if not present
        if 'advanced_logo.css' not in content:
            css_link = '    <link rel="stylesheet" href="css/advanced_logo.css">'
            content = content.replace('</head>', f'{css_link}\n</head>')
        
        # Write updated file
        with open(html_file, 'w') as f:
            f.write(content)
        
        print("  ✅ Updated with 3D logo")
    else:
        print("  ⚠️  Could not find logo section")

print("\n✅ All pages updated with new 3D logo!")
print("\n🎨 Features of the new logo:")
print("1. 3D rotating cube with 'T' and 'F' initials")
print("2. Animated expanding arrows")
print("3. Glowing text effect")
print("4. Mobile-optimized")
print("5. Reduced motion support")
print("6. Print-friendly")
