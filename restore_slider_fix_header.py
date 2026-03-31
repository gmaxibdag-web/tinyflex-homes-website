#!/usr/bin/env python3
"""
Restore hero slider and fix header with proper logo
"""

import os

print("🎨 Restoring hero slider and fixing header...")

# Process index.html first (main page with slider)
html_files = ['index.html'] + [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    changes = 0
    
    # 1. Fix the header with proper logo
    if '<!-- Professional Header -->' in content:
        import re
        
        # Find the header section
        header_pattern = r'(<!-- Professional Header -->.*?</header>)'
        header_match = re.search(header_pattern, content, re.DOTALL)
        
        if header_match:
            old_header = header_match.group(0)
            
            # Create fixed header with better logo
            fixed_header = '''<!-- Professional Header -->
<header class="site-header">
    <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm">
        <div class="container">
            <!-- Logo -->
            <a class="navbar-brand" href="index.html">
                <div class="d-flex align-items-center">
                    <div class="logo-container me-3">
                        <div class="logo-icon">
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
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <!-- Navigation -->
            <div class="collapse navbar-collapse" id="mainNav">
                <ul class="navbar-nav ms-auto align-items-center">
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
                    <li class="nav-item ms-3">
                        <a class="btn btn-primary btn-lg px-4" href="contact.html">
                            <i class="fas fa-comment-dots me-2"></i>Get Quote
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>'''
            
            content = content.replace(old_header, fixed_header)
            changes += 1
            print("  ✅ Fixed header with proper logo")
    
    # 2. For index.html, restore hero slider before trust-badges
    if html_file == 'index.html' and '<section class="trust-badges">' in content:
        # Find position of trust-badges section
        trust_pos = content.find('<section class="trust-badges">')
        
        if trust_pos != -1:
            # Insert hero slider before trust-badges
            hero_slider = '''
    <!-- Hero Slider -->
    <section class="hero-slider">
        <div class="slides">
            <!-- Slide 1 - MAIN HERO -->
            <div class="slide active" style="background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url(\'local_images/modern-container-home-1-optimized.jpg?v=2\');">
                <div class="container">
                    <div class="hero-content">
                        <h1 class="hero-title">Premium Expandable Container Homes</h1>
                        <p class="hero-subtitle"><strong>Australian buying agent</strong> for premium expandable container homes. Customizable designs delivered in 12-14 weeks.</p>
                        <div class="hero-buttons">
                            <a href="models.html" class="btn btn-primary">
                                <i class="fas fa-home"></i> View Models
                            </a>
                            <a href="contact.html" class="btn btn-outline-light">
                                <i class="fas fa-comment-dots"></i> Get Quote
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Slide 2 - EXPANDABLE DESIGN -->
            <div class="slide" style="background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url(\'local_images/container-exterior-3-optimized.jpg?v=2\');">
                <div class="container">
                    <div class="hero-content">
                        <h1 class="hero-title">Expandable Homes<br><span class="highlight">That Actually Expand</span></h1>
                        <p class="hero-subtitle"><strong>Real expandable container homes</strong> - slides open to double your living space. Not regular houses - actual container expandable designs.</p>
                        <div class="hero-buttons">
                            <a href="process.html" class="btn btn-primary">
                                <i class="fas fa-expand-arrows-alt"></i> How It Works
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Slider Controls -->
        <div class="slider-controls">
            <button class="slider-prev"><i class="fas fa-chevron-left"></i></button>
            <div class="slider-dots">
                <span class="dot active"></span>
                <span class="dot"></span>
            </div>
            <button class="slider-next"><i class="fas fa-chevron-right"></i></button>
        </div>
    </section>
'''
            
            content = content[:trust_pos] + hero_slider + content[trust_pos:]
            changes += 1
            print("  ✅ Restored hero slider")
    
    # 3. Remove duplicate CSS files
    duplicate_css = ['style.min.css', 'mobile_optimization.css']
    for css_file in duplicate_css:
        if f'<link rel="stylesheet" href="css/{css_file}">' in content:
            content = content.replace(f'<link rel="stylesheet" href="css/{css_file}">', '')
            changes += 1
            print(f"  ✅ Removed duplicate CSS: {css_file}")
    
    # 4. Ensure optimized.css is loaded
    if '<link rel="stylesheet" href="css/optimized.css">' not in content:
        # Add after favicon
        favicon_pos = content.find('<link rel="icon"')
        if favicon_pos != -1:
            insert_pos = content.find('\n', favicon_pos) + 1
            optimized_css = '    <link rel="stylesheet" href="css/optimized.css">\n'
            content = content[:insert_pos] + optimized_css + content[insert_pos:]
            changes += 1
            print("  ✅ Added optimized CSS")
    
    # Write updated file
    if changes > 0:
        with open(html_file, 'w') as f:
            f.write(content)
        print(f"  🎯 Applied {changes} fixes")
    else:
        print("  ⚠️  No fixes needed")

print("\n✅ Hero slider restored and header fixed!")
print("\n🎯 What was done:")
print("1. Fixed header with proper logo container")
print("2. Restored hero slider on homepage")
print("3. Removed duplicate CSS files")
print("4. Ensured optimized CSS is loaded")
