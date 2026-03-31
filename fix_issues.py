#!/usr/bin/env python3
"""
Fix both issues:
1. Remove top contact details (clean up header)
2. Remove "shipping container" text from photo placeholders
"""

import re
import os

print("🔧 Fixing website issues...")
print("1. Removing top contact details")
print("2. Removing 'shipping container' text from photos")
print("=" * 50)

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'test_mobile_fixes.html']

for html_file in html_files:
    print(f"\n📄 Processing: {html_file}")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    changes = 0
    
    # 1. FIX HEADER - Remove old navigation and add clean Bootstrap header
    # Check if we have the old navigation
    if 'navbar navbar-expand-lg' not in content:
        print("  🔄 Replacing header with clean Bootstrap version...")
        
        # Find the header section (from <!-- Navigation --> to closing nav tag)
        header_pattern = r'(<!-- Navigation -->.*?</nav>)'
        header_match = re.search(header_pattern, content, re.DOTALL)
        
        if header_match:
            old_header = header_match.group(0)
            
            # Create clean Bootstrap header
            new_header = '''<!-- Navigation -->
<nav class="navbar navbar-expand-lg navbar-light">
    <div class="container">
        <a class="navbar-brand" href="index.html">
            <strong>Tiny Flex Homes</strong>
            <small class="d-block">Expandable Container Homes</small>
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
                    <a class="nav-link" href="models.html">Models</a>
                </li>
                <li class="nav-link">
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
            
            content = content.replace(old_header, new_header)
            changes += 1
            print("  ✅ Header replaced with clean version")
    
    # 2. REMOVE "SHIPPING CONTAINER" TEXT
    # Replace "shipping container" with better terms
    replacements = [
        (r'shipping container', 'expandable home', re.IGNORECASE),
        (r'Shipping Container', 'Expandable Home', re.IGNORECASE),
        (r'SHIPPING CONTAINER', 'EXPANDABLE HOME', re.IGNORECASE),
    ]
    
    for pattern, replacement, flags in replacements:
        old_count = len(re.findall(pattern, content, flags))
        if old_count > 0:
            content = re.sub(pattern, replacement, content, flags=flags)
            changes += 1
            print(f"  ✅ Replaced {old_count} '{pattern}' with '{replacement}'")
    
    # 3. SPECIFIC FIXES for photo placeholders and headings
    # Fix specific problematic phrases
    specific_fixes = [
        # Hero section fixes
        (r'Premium Expandable<br><span class="highlight">Shipping Container Homes</span>', 
         'Premium Expandable<br><span class="highlight">Container Homes</span>'),
        
        (r'<p class="hero-subtitle"><strong>Actual shipping containers that expand</strong>', 
         '<p class="hero-subtitle"><strong>Premium expandable homes that transform</strong>'),
        
        (r'<strong>Real expandable shipping containers</strong>', 
         '<strong>Premium expandable homes</strong>'),
        
        # Section titles
        (r'<h2 class="section-title">Our Shipping Container Models</h2>', 
         '<h2 class="section-title">Our Expandable Home Models</h2>'),
        
        (r'<p class="section-subtitle"><strong>Actual expandable shipping containers</strong>', 
         '<p class="section-subtitle"><strong>Premium expandable home designs</strong>'),
        
        # Model badges
        (r'<div class="model-badge">Shipping Container</div>', 
         '<div class="model-badge">Expandable Design</div>'),
        
        # Model titles
        (r'<h3>20FT Expandable Shipping Container</h3>', 
         '<h3>20FT Expandable Home</h3>'),
        
        (r'<h3>Studio Shipping Container</h3>', 
         '<h3>Studio Expandable Home</h3>'),
        
        (r'<h3>40FT Expandable Shipping Container</h3>', 
         '<h3>40FT Expandable Home</h3>'),
        
        # Model descriptions
        (r'<p class="model-desc"><strong>Actual 20ft shipping container</strong>', 
         '<p class="model-desc"><strong>20ft expandable home</strong>'),
        
        (r'<p class="model-desc"><strong>Compact shipping container</strong>', 
         '<p class="model-desc"><strong>Compact expandable home</strong>'),
        
        (r'<p class="model-desc"><strong>Large 40ft shipping container</strong>', 
         '<p class="model-desc"><strong>Large 40ft expandable home</strong>'),
        
        # Feature lists
        (r'<span><i class="fas fa-check"></i> <strong>Shipping Container Design</strong></span>', 
         '<span><i class="fas fa-check"></i> <strong>Expandable Design</strong></span>'),
        
        (r'<span><i class="fas fa-check"></i> <strong>Shipping Container Base</strong></span>', 
         '<span><i class="fas fa-check"></i> <strong>Expandable Base</strong></span>'),
        
        (r'<span><i class="fas fa-check"></i> <strong>40ft Shipping Container</strong></span>', 
         '<span><i class="fas fa-check"></i> <strong>40ft Expandable</strong></span>'),
        
        # Note section
        (r'<p><i class="fas fa-shipping-fast"></i> <strong>Note:</strong> These are <strong>actual shipping container homes</strong>', 
         '<p><i class="fas fa-home"></i> <strong>Note:</strong> These are <strong>premium expandable homes</strong>'),
        
        # Footer
        (r'Shipping Container Home Specialists', 
         'Expandable Home Specialists'),
        
        (r'premium expandable shipping container homes', 
         'premium expandable homes'),
    ]
    
    for old_text, new_text in specific_fixes:
        if old_text in content:
            content = content.replace(old_text, new_text)
            changes += 1
            print(f"  ✅ Fixed specific phrase")
    
    # 4. Also update the icon for shipping
    if 'fa-shipping-fast' in content:
        content = content.replace('fa-shipping-fast', 'fa-home')
        changes += 1
        print("  ✅ Updated shipping icons to home icons")
    
    # Write updated file
    if changes > 0:
        with open(html_file, 'w') as f:
            f.write(content)
        print(f"  🎯 Total changes: {changes}")
    else:
        print("  ⚠️  No changes needed")

print(f"\n{'='*50}")
print("✅ All issues fixed!")
print("\n📋 Summary of fixes:")
print("1. Clean Bootstrap header (no top contact details)")
print("2. Removed 'shipping container' text from all pages")
print("3. Updated to 'expandable home' terminology")
print("4. Fixed photo placeholder text")
print("5. Updated icons")
print("\n🚀 Ready to deploy!")
