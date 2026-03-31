#!/usr/bin/env python3
"""
Build professional header inspired by expandablehomes.com.au
"""

import os

print("🎨 Building professional header inspired by industry leader...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Find the current header
    import re
    
    # Find the navbar
    nav_pattern = r'(<!-- Simple Working Header -->.*?</nav>)'
    nav_match = re.search(nav_pattern, content, re.DOTALL)
    
    if nav_match:
        old_nav = nav_match.group(0)
        
        # Create professional header inspired by industry site
        new_header = '''<!-- Professional Header Inspired by Industry Leader -->
<header class="site-header">
    <!-- Top Bar -->
    <div class="top-bar bg-dark text-white py-2">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-6">
                    <div class="d-flex align-items-center gap-3">
                        <div class="d-flex align-items-center gap-2">
                            <i class="fas fa-phone-alt fa-sm"></i>
                            <span>Contact for Quote</span>
                        </div>
                        <div class="d-flex align-items-center gap-2">
                            <i class="fas fa-clock fa-sm"></i>
                            <span>Mon-Fri 9am-5pm</span>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 text-md-end">
                    <div class="d-flex align-items-center justify-content-md-end gap-3">
                        <div class="d-flex align-items-center gap-2">
                            <i class="fas fa-check-circle fa-sm text-success"></i>
                            <span>NSW Building Compliant</span>
                        </div>
                        <div class="d-flex align-items-center gap-2">
                            <i class="fas fa-user-tie fa-sm"></i>
                            <span>Australian Owned</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Main Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm">
        <div class="container">
            <!-- Logo -->
            <a class="navbar-brand" href="index.html">
                <div class="d-flex align-items-center">
                    <div class="logo-icon me-2">
                        <div class="logo-square">
                            <i class="fas fa-expand-arrows-alt"></i>
                        </div>
                    </div>
                    <div>
                        <h1 class="logo-title mb-0">TinyFlex</h1>
                        <p class="logo-subtitle mb-0">Expandable Container Homes</p>
                    </div>
                </div>
            </a>
            
            <!-- Mobile Toggle -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <!-- Navigation Menu -->
            <div class="collapse navbar-collapse" id="mainNav">
                <ul class="navbar-nav ms-auto align-items-lg-center">
                    <li class="nav-item">
                        <a class="nav-link active" href="index.html">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="models.html">Models & Pricing</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="gallery.html">Gallery</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="process.html">Our Process</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="about.html">About Us</a>
                    </li>
                    <li class="nav-item ms-lg-3">
                        <a class="btn btn-primary btn-lg px-4" href="contact.html">
                            <i class="fas fa-comment-dots me-2"></i>Get Free Quote
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>'''
        
        # Replace the navigation
        content = content.replace(old_nav, new_header)
        
        # Remove old CSS
        content = content.replace('<link rel="stylesheet" href="css/simple-header.css">', '')
        
        # Add professional CSS
        if 'professional-inspired.css' not in content:
            css_link = '    <link rel="stylesheet" href="css/professional-inspired.css">'
            content = content.replace('</head>', f'{css_link}\n</head>')
        
        # Write updated file
        with open(html_file, 'w') as f:
            f.write(content)
        
        print("  ✅ Built professional inspired header")
    else:
        print("  ⚠️  Could not find header section")

print("\n✅ All pages updated with professional inspired header!")
print("\n🎨 Inspired by industry leader with improvements:")
print("1. Professional top bar with contact info")
print("2. Clean logo with icon and proper typography")
print("3. 'Expandable Container Homes' subtitle")
print("4. Improved navigation labels")
print("5. Prominent 'Get Free Quote' button")
print("6. Professional spacing and layout")
