#!/usr/bin/env python3
"""
Build a proper, clean, professional header from scratch
"""

import os

print("🎨 Building proper professional header...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Find the entire header section (from <!-- Navigation --> to </nav>)
    import re
    
    # Find the navigation section
    nav_pattern = r'(<!-- Navigation -->.*?</nav>)'
    nav_match = re.search(nav_pattern, content, re.DOTALL)
    
    if nav_match:
        old_nav = nav_match.group(0)
        
        # Create PROPER professional header
        new_header = '''<!-- Navigation -->
<nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm fixed-top">
    <div class="container">
        <!-- Logo - Simple and Professional -->
        <a class="navbar-brand" href="index.html">
            <div class="d-flex align-items-center">
                <div class="logo-simple me-2">
                    <div class="logo-icon">
                        <i class="fas fa-expand-arrows-alt text-primary"></i>
                    </div>
                </div>
                <div>
                    <span class="fw-bold fs-4 text-dark">TinyFlex</span>
                    <small class="d-block text-muted">Expandable Homes</small>
                </div>
            </div>
        </a>
        
        <!-- Mobile Menu Button -->
        <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <!-- Navigation Menu -->
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto align-items-center">
                <li class="nav-item mx-2">
                    <a class="nav-link text-dark fw-medium" href="index.html">Home</a>
                </li>
                <li class="nav-item mx-2">
                    <a class="nav-link text-dark fw-medium" href="models.html">Models</a>
                </li>
                <li class="nav-item mx-2">
                    <a class="nav-link text-dark fw-medium" href="gallery.html">Gallery</a>
                </li>
                <li class="nav-item mx-2">
                    <a class="nav-link text-dark fw-medium" href="process.html">Process</a>
                </li>
                <li class="nav-item mx-2">
                    <a class="nav-link text-dark fw-medium" href="about.html">About</a>
                </li>
                <li class="nav-item mx-2 ms-lg-3">
                    <a class="btn btn-primary px-4 py-2 fw-bold" href="contact.html">
                        <i class="fas fa-comment-dots me-2"></i>Get Quote
                    </a>
                </li>
            </ul>
        </div>
    </div>
</nav>

<!-- Spacer for fixed navbar -->
<div style="height: 80px;"></div>'''
        
        # Replace the navigation
        content = content.replace(old_nav, new_header)
        
        # Remove conflicting CSS files
        content = content.replace('<link rel="stylesheet" href="css/advanced_logo.css">', '')
        content = content.replace('<link rel="stylesheet" href="css/logo_design.css">', '')
        content = content.replace('<link rel="stylesheet" href="css/header_styles.css">', '')
        
        # Add proper header CSS
        if 'proper-header.css' not in content:
            css_link = '    <link rel="stylesheet" href="css/proper-header.css">'
            content = content.replace('</head>', f'{css_link}\n</head>')
        
        # Remove conflicting JS
        content = content.replace('<script src="js/sticky-header.js"></script>', '')
        
        # Write updated file
        with open(html_file, 'w') as f:
            f.write(content)
        
        print("  ✅ Built proper professional header")
    else:
        print("  ⚠️  Could not find navigation section")

print("\n✅ All pages updated with proper header!")
print("\n🎨 Features of the new header:")
print("1. Clean white background with subtle shadow")
print("2. Simple professional logo (no complex 3D)")
print("3. Proper spacing and alignment")
print("4. Fixed top positioning")
print("5. Clean mobile menu button")
print("6. Professional 'Get Quote' button")
