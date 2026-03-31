#!/usr/bin/env python3
"""
Replicate a clean, professional header based on real examples
"""

import os

print("🎨 Replicating professional header from real examples...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Find the entire header section
    import re
    
    # Find the navigation section
    nav_pattern = r'(<!-- Navigation -->.*?</nav>)'
    nav_match = re.search(nav_pattern, content, re.DOTALL)
    
    if nav_match:
        old_nav = nav_match.group(0)
        
        # Create CLEAN professional header based on real examples
        new_header = '''<!-- Navigation - Clean Professional Design -->
<header class="header">
    <nav class="navbar navbar-expand-lg">
        <div class="container">
            <!-- Logo -->
            <a class="navbar-brand" href="index.html">
                <div class="logo-wrapper">
                    <div class="logo-mark">
                        <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="4" y="4" width="24" height="24" rx="4" fill="#2C5282"/>
                            <path d="M12 12H20V20H12V12Z" fill="white"/>
                            <path d="M16 8V24M8 16H24" stroke="white" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </div>
                    <div class="logo-text">
                        <span class="logo-name">TinyFlex</span>
                        <span class="logo-tagline">Expandable Homes</span>
                    </div>
                </div>
            </a>
            
            <!-- Mobile Toggle -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-controls="mainNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <!-- Navigation -->
            <div class="collapse navbar-collapse" id="mainNav">
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
                    <li class="nav-item ms-lg-3">
                        <a class="btn btn-primary btn-cta" href="contact.html">
                            Get Quote
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>'''
        
        # Replace the navigation
        content = content.replace(old_nav, new_header)
        
        # Remove all conflicting CSS
        content = content.replace('<link rel="stylesheet" href="css/proper-header.css">', '')
        content = content.replace('<link rel="stylesheet" href="css/advanced_logo.css">', '')
        content = content.replace('<link rel="stylesheet" href="css/logo_design.css">', '')
        content = content.replace('<link rel="stylesheet" href="css/header_styles.css">', '')
        
        # Add professional header CSS
        if 'professional-header.css' not in content:
            css_link = '    <link rel="stylesheet" href="css/professional-header.css">'
            content = content.replace('</head>', f'{css_link}\n</head>')
        
        # Remove conflicting JS
        content = content.replace('<script src="js/header-behavior.js"></script>', '')
        content = content.replace('<script src="js/sticky-header.js"></script>', '')
        
        # Write updated file
        with open(html_file, 'w') as f:
            f.write(content)
        
        print("  ✅ Replicated professional header")
    else:
        print("  ⚠️  Could not find navigation section")

print("\n✅ All pages updated with professional header!")
print("\n🎨 Based on real professional examples:")
print("1. Clean, minimalist design")
print("2. Simple SVG logo")
print("3. Proper spacing and typography")
print("4. Professional CTA button")
print("5. Mobile-optimized navigation")
