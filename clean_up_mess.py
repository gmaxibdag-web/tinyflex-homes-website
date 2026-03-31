#!/usr/bin/env python3
"""
Clean up the mess - remove conflicting elements and go back to basics
"""

import os

print("🧹 Cleaning up the mess...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    changes = 0
    
    # 1. Remove the old mobile menu (conflicting)
    if '<div class="mobile-menu">' in content:
        import re
        mobile_menu_pattern = r'(<div class="mobile-menu">.*?</div>\s*</div>)'
        mobile_match = re.search(mobile_menu_pattern, content, re.DOTALL)
        if mobile_match:
            content = content.replace(mobile_match.group(0), '')
            changes += 1
            print("  ✅ Removed conflicting mobile menu")
    
    # 2. Remove the spacer div (causing layout issues)
    if '<!-- Spacer for fixed navbar -->' in content:
        spacer_pattern = r'(<!-- Spacer for fixed navbar -->.*?</div>)'
        spacer_match = re.search(spacer_pattern, content, re.DOTALL)
        if spacer_match:
            content = content.replace(spacer_match.group(0), '')
            changes += 1
            print("  ✅ Removed spacer div")
    
    # 3. Fix the header to be simple and work
    # Find the header section
    header_pattern = r'(<!-- Navigation - Clean Professional Design -->.*?</header>)'
    header_match = re.search(header_pattern, content, re.DOTALL)
    
    if header_match:
        old_header = header_match.group(0)
        
        # Create SIMPLE working header
        simple_header = '''<!-- Simple Working Header -->
<nav class="navbar navbar-expand-lg navbar-light bg-white border-bottom">
    <div class="container">
        <a class="navbar-brand" href="index.html">
            <span class="fw-bold fs-4 text-primary">TinyFlex</span>
            <small class="d-block text-muted">Expandable Homes</small>
        </a>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarContent">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="models.html">Models</a></li>
                <li class="nav-item"><a class="nav-link" href="gallery.html">Gallery</a></li>
                <li class="nav-item"><a class="nav-link" href="process.html">Process</a></li>
                <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
                <li class="nav-item ms-2">
                    <a class="btn btn-primary" href="contact.html">Get Quote</a>
                </li>
            </ul>
        </div>
    </div>
</nav>'''
        
        content = content.replace(old_header, simple_header)
        changes += 1
        print("  ✅ Replaced with simple working header")
    
    # 4. Remove conflicting CSS
    css_files = ['professional-header.css', 'proper-header.css', 'advanced_logo.css', 'logo_design.css', 'header_styles.css']
    for css_file in css_files:
        if f'<link rel="stylesheet" href="css/{css_file}">' in content:
            content = content.replace(f'<link rel="stylesheet" href="css/{css_file}">', '')
            changes += 1
            print(f"  ✅ Removed conflicting CSS: {css_file}")
    
    # 5. Remove conflicting JS
    js_files = ['professional-header.js', 'header-behavior.js', 'sticky-header.js']
    for js_file in js_files:
        if f'<script src="js/{js_file}"></script>' in content:
            content = content.replace(f'<script src="js/{js_file}"></script>', '')
            changes += 1
            print(f"  ✅ Removed conflicting JS: {js_file}")
    
    # Write updated file
    if changes > 0:
        with open(html_file, 'w') as f:
            f.write(content)
        print(f"  🎯 Applied {changes} cleanup fixes")
    else:
        print("  ⚠️  No cleanup needed")

print("\n✅ Cleanup complete!")
print("\n🎯 What was fixed:")
print("1. Removed conflicting mobile menu")
print("2. Removed spacer div causing layout issues")
print("3. Replaced complex header with simple working one")
print("4. Removed all conflicting CSS files")
print("5. Removed all conflicting JavaScript files")
print("\n📱 Result: Simple, clean header that actually works")
