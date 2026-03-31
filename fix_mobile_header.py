#!/usr/bin/env python3
"""
Fix mobile header/navigation for better mobile browsing
"""

import re

# Read current index.html
with open('index.html', 'r') as f:
    content = f.read()

# Find the header/navigation section
# Look for the current header structure
header_pattern = r'(<header[^>]*>.*?</header>)'
match = re.search(header_pattern, content, re.DOTALL | re.IGNORECASE)

if match:
    current_header = match.group(0)
    print(f"Found header: {len(current_header)} characters")
    
    # Check if it has mobile-friendly classes
    if 'navbar-toggler' not in current_header and 'navbar-expand' not in current_header:
        print("Header is not mobile-optimized. Fixing...")
        
        # Create mobile-optimized header
        mobile_header = '''<header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand" href="index.html">
                <strong>Tiny Flex Homes</strong>
                <small class="d-block text-muted" style="font-size: 0.8rem;">Expandable Container Homes</small>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link active" href="index.html">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="gallery.html">Gallery</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="models.html">Models</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="about.html">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="process.html">Process</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="contact.html">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>'''
        
        # Replace the header
        content = content.replace(current_header, mobile_header)
        print("Replaced with mobile-optimized header")
        
        # Add Bootstrap CSS if not present
        if 'bootstrap.min.css' not in content:
            # Add Bootstrap CSS before closing head
            bootstrap_css = '''    <!-- Bootstrap CSS for mobile responsiveness -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">'''
            
            if '</head>' in content:
                content = content.replace('</head>', f'{bootstrap_css}\n</head>')
                print("Added Bootstrap CSS")
        
        # Add Bootstrap JS if not present
        if 'bootstrap.bundle.min.js' not in content:
            # Add Bootstrap JS before closing body
            bootstrap_js = '''    <!-- Bootstrap JS for mobile menu -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>'''
            
            if '</body>' in content:
                content = content.replace('</body>', f'{bootstrap_js}\n</body>')
                print("Added Bootstrap JS")
    else:
        print("Header already has mobile classes")

# Also fix any other mobile issues
# Remove or fix the "top info" that doesn't look good on mobile
# Look for problematic top sections
if 'Welcome to Tiny Flex Homes' in content:
    # This might be the problematic top info
    print("Found potential problematic top info section")
    
    # Let's make sure the hero section is mobile-friendly
    hero_pattern = r'(<section[^>]*class="[^"]*hero[^"]*"[^>]*>.*?</section>)'
    hero_match = re.search(hero_pattern, content, re.DOTALL | re.IGNORECASE)
    
    if hero_match:
        hero_section = hero_match.group(0)
        
        # Ensure hero has proper mobile classes
        if 'py-5' not in hero_section:
            # Add mobile padding
            hero_section = hero_section.replace('class="hero"', 'class="hero py-4 py-lg-5"')
            content = content.replace(hero_match.group(0), hero_section)
            print("Added mobile padding to hero section")

# Write fixed file
with open('index.html', 'w') as f:
    f.write(content)

print("✅ Mobile header fixes applied")

# Also update other pages
pages = ['about.html', 'contact.html', 'gallery.html', 'models.html', 'process.html']
for page in pages:
    try:
        with open(page, 'r') as f:
            page_content = f.read()
        
        # Apply similar fixes to other pages
        if '<header>' in page_content:
            # Simple fix: ensure consistent header
            page_content = re.sub(header_pattern, mobile_header, page_content, flags=re.DOTALL | re.IGNORECASE)
            
            # Add Bootstrap if missing
            if 'bootstrap.min.css' not in page_content:
                page_content = page_content.replace('</head>', f'{bootstrap_css}\n</head>')
            
            if 'bootstrap.bundle.min.js' not in page_content:
                page_content = page_content.replace('</body>', f'{bootstrap_js}\n</body>')
            
            with open(page, 'w') as f:
                f.write(page_content)
            print(f"Updated {page} with mobile fixes")
    except Exception as e:
        print(f"Could not update {page}: {e}")
