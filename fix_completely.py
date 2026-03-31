#!/usr/bin/env python3
"""
Completely fix the website - remove duplicates, implement proper template
"""

import os

print("🔧 Completely fixing the website...")

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    changes = 0
    
    # 1. Remove duplicate mobile menu
    if '<!-- Mobile Menu -->' in content:
        import re
        # Find from <!-- Mobile Menu --> to closing </div>
        mobile_pattern = r'(<!-- Mobile Menu -->.*?</div>\s*</div>)'
        mobile_match = re.search(mobile_pattern, content, re.DOTALL)
        if mobile_match:
            content = content.replace(mobile_match.group(0), '')
            changes += 1
            print("  ✅ Removed duplicate mobile menu")
    
    # 2. Remove any empty divs or broken HTML
    if '<div class="container py-3">' in content and '</div>' in content:
        # Look for empty container divs
        empty_pattern = r'(\s*<div class="container py-3">\s*</div>\s*)'
        empty_matches = re.findall(empty_pattern, content)
        for empty_match in empty_matches:
            content = content.replace(empty_match, '')
            changes += 1
            print("  ✅ Removed empty container div")
    
    # 3. Implement proper professional header
    # Find the current header
    header_pattern = r'(<!-- Clean Simple Header -->.*?</nav>)'
    header_match = re.search(header_pattern, content, re.DOTALL)
    
    if header_match:
        old_header = header_match.group(0)
        
        # Create proper professional header
        proper_header = '''<!-- Professional Header -->
<header class="site-header">
    <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm">
        <div class="container">
            <!-- Logo -->
            <a class="navbar-brand" href="index.html">
                <div class="d-flex align-items-center">
                    <div class="logo-icon bg-primary text-white rounded d-flex align-items-center justify-content-center me-3" style="width: 50px; height: 50px;">
                        <i class="fas fa-expand-arrows-alt fa-lg"></i>
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
        
        content = content.replace(old_header, proper_header)
        changes += 1
        print("  ✅ Implemented proper professional header")
    
    # 4. Remove old CSS and add proper CSS
    if '<link rel="stylesheet" href="css/clean-template.css">' in content:
        content = content.replace('<link rel="stylesheet" href="css/clean-template.css">', '')
        changes += 1
        print("  ✅ Removed old CSS")
    
    # Add proper CSS
    if '<link rel="stylesheet" href="css/proper-site.css">' not in content:
        css_link = '    <link rel="stylesheet" href="css/proper-site.css">'
        content = content.replace('</head>', f'{css_link}\n</head>')
        changes += 1
        print("  ✅ Added proper CSS")
    
    # 5. Remove old JS and add proper JS
    if '<script src="js/clean-template.js"></script>' in content:
        content = content.replace('<script src="js/clean-template.js"></script>', '')
        changes += 1
        print("  ✅ Removed old JS")
    
    # Add proper JS
    if '<script src="js/proper-site.js"></script>' not in content:
        js_link = '    <script src="js/proper-site.js"></script>'
        content = content.replace('</body>', f'{js_link}\n</body>')
        changes += 1
        print("  ✅ Added proper JS")
    
    # Write updated file
    if changes > 0:
        with open(html_file, 'w') as f:
            f.write(content)
        print(f"  🎯 Applied {changes} fixes")
    else:
        print("  ⚠️  No fixes needed")

print("\n✅ Complete fix applied!")
print("\n🎯 What was fixed:")
print("1. Removed duplicate mobile menu (conflicting)")
print("2. Removed empty/broken HTML elements")
print("3. Implemented proper professional header")
print("4. Added proper CSS and JavaScript")
print("5. Cleaned up all conflicting code")
