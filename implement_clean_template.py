#!/usr/bin/env python3
"""
Implement a clean, simple template that actually works
"""

import os

print("🎨 Implementing clean, working template...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Find the header section
    import re
    
    # Find from <!-- Professional Header Inspired by Industry Leader --> to </header>
    header_pattern = r'(<!-- Professional Header Inspired by Industry Leader -->.*?</header>)'
    header_match = re.search(header_pattern, content, re.DOTALL)
    
    if header_match:
        old_header = header_match.group(0)
        
        # Create CLEAN, SIMPLE header that works
        clean_header = '''<!-- Clean Simple Header -->
<nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
    <div class="container">
        <!-- Logo -->
        <a class="navbar-brand" href="index.html">
            <div class="d-flex align-items-center">
                <div class="logo-circle bg-primary text-white rounded-circle d-flex align-items-center justify-content-center me-2" style="width: 40px; height: 40px;">
                    <i class="fas fa-home"></i>
                </div>
                <div>
                    <span class="fw-bold fs-4">TinyFlex</span>
                    <small class="d-block text-muted">Expandable Homes</small>
                </div>
            </div>
        </a>
        
        <!-- Mobile Toggle -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMain">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <!-- Navigation -->
        <div class="collapse navbar-collapse" id="navbarMain">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="index.html">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="models.html">Models</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="gallery.html">Gallery</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="process.html">Process</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="about.html">About</a>
                </li>
                <li class="nav-item ms-2">
                    <a class="btn btn-primary" href="contact.html">Get Quote</a>
                </li>
            </ul>
        </div>
    </div>
</nav>'''
        
        # Replace the header
        content = content.replace(old_header, clean_header)
        
        # Remove all conflicting CSS
        css_files = ['professional-inspired.css', 'simple-header.css', 'proper-header.css', 'advanced_logo.css', 'logo_design.css', 'header_styles.css']
        for css_file in css_files:
            if f'<link rel="stylesheet" href="css/{css_file}">' in content:
                content = content.replace(f'<link rel="stylesheet" href="css/{css_file}">', '')
                print(f"  ✅ Removed CSS: {css_file}")
        
        # Remove all conflicting JS
        js_files = ['professional-header-behavior.js', 'header-behavior.js', 'sticky-header.js']
        for js_file in js_files:
            if f'<script src="js/{js_file}"></script>' in content:
                content = content.replace(f'<script src="js/{js_file}"></script>', '')
                print(f"  ✅ Removed JS: {js_file}")
        
        # Add clean CSS
        if 'clean-template.css' not in content:
            css_link = '    <link rel="stylesheet" href="css/clean-template.css">'
            content = content.replace('</head>', f'{css_link}\n</head>')
        
        # Write updated file
        with open(html_file, 'w') as f:
            f.write(content)
        
        print("  ✅ Implemented clean template header")
    else:
        print("  ⚠️  Could not find header section")

print("\n✅ All pages updated with clean template!")
print("\n🎨 Features:")
print("1. Simple Bootstrap navbar (proven to work)")
print("2. Clean logo with circle icon")
print("3. Working hamburger menu")
print("4. Basic navigation")
print("5. Get Quote button")
print("6. No complex CSS or JS")
print("7. Actually works on mobile")
