#!/usr/bin/env python3
"""
Restore the logo section while keeping top contact details removed
"""

import os

print("🎨 Restoring logo section with professional design...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Find the current header (starting from <!-- Navigation -->)
    import re
    
    # Look for the navigation section
    nav_pattern = r'(<!-- Navigation -->.*?</nav>)'
    nav_match = re.search(nav_pattern, content, re.DOTALL)
    
    if nav_match:
        current_nav = nav_match.group(0)
        
        # Create new header with logo
        new_header = '''<!-- Navigation -->
<nav class="navbar navbar-expand-lg navbar-light">
    <div class="container">
        <!-- Logo -->
        <a class="navbar-brand" href="index.html">
            <div class="logo-container">
                <div class="logo-icon">
                    <i class="fas fa-expand-arrows-alt"></i>
                </div>
                <div class="logo-text">
                    <strong>Tiny Flex</strong>
                    <small class="d-block">Expandable Homes</small>
                </div>
            </div>
        </a>
        
        <!-- Mobile Menu Button -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <!-- Navigation Menu -->
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link active" href="index.html">Home</a>
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
                <li class="nav-item">
                    <a class="nav-link btn btn-primary" href="contact.html">Get Quote</a>
                </li>
            </ul>
        </div>
    </div>
</nav>'''
        
        # Replace the navigation
        content = content.replace(current_nav, new_header)
        
        # Write updated file
        with open(html_file, 'w') as f:
            f.write(content)
        
        print("  ✅ Restored logo section in header")
    else:
        print("  ⚠️  Could not find navigation section")

print("\n✅ Logo section restored to all pages!")
print("\n🎨 Next: Designing new 3D slick logo...")
