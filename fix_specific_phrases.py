#!/usr/bin/env python3
"""
Fix specific phrases in index.html that the regex might have missed
"""

print("🔍 Fixing specific phrases in index.html...")

with open('index.html', 'r') as f:
    content = f.read()

# List of specific fixes with exact text
fixes = [
    # Hero section
    ('Premium Expandable<br><span class="highlight">Shipping Container Homes</span>',
     'Premium Expandable<br><span class="highlight">Container Homes</span>'),
    
    ('<p class="hero-subtitle"><strong>Actual shipping containers that expand</strong> - not regular houses.',
     '<p class="hero-subtitle"><strong>Premium expandable homes that transform</strong> - innovative living spaces.'),
    
    ('<p class="hero-subtitle"><strong>Real expandable shipping containers</strong> - slides open to double your living space.',
     '<p class="hero-subtitle"><strong>Premium expandable homes</strong> - slides open to double your living space.'),
    
    # Section titles
    ('<h2 class="section-title">Our Shipping Container Models</h2>',
     '<h2 class="section-title">Our Expandable Home Models</h2>'),
    
    ('<p class="section-subtitle"><strong>Actual expandable shipping containers</strong> - not regular houses</p>',
     '<p class="section-subtitle"><strong>Premium expandable home designs</strong> - innovative living solutions</p>'),
    
    # Model badges
    ('<div class="model-badge">Shipping Container</div>',
     '<div class="model-badge">Expandable Design</div>'),
    
    # Model titles
    ('<h3>20FT Expandable Shipping Container</h3>',
     '<h3>20FT Expandable Home</h3>'),
    
    ('<h3>Studio Shipping Container</h3>',
     '<h3>Studio Expandable Home</h3>'),
    
    ('<h3>40FT Expandable Shipping Container</h3>',
     '<h3>40FT Expandable Home</h3>'),
    
    # Model descriptions
    ('<p class="model-desc"><strong>Actual 20ft shipping container</strong> that slides open to double living space.',
     '<p class="model-desc"><strong>20ft expandable home</strong> that slides open to double living space.'),
    
    ('<p class="model-desc"><strong>Compact shipping container</strong> perfect for home office, guest house, or rental income.',
     '<p class="model-desc"><strong>Compact expandable home</strong> perfect for home office, guest house, or rental income.'),
    
    ('<p class="model-desc"><strong>Large 40ft shipping container</strong> with multiple expansion modules.',
     '<p class="model-desc"><strong>Large 40ft expandable home</strong> with multiple expansion modules.'),
    
    # Feature lists
    ('<span><i class="fas fa-check"></i> <strong>Shipping Container Design</strong></span>',
     '<span><i class="fas fa-check"></i> <strong>Expandable Design</strong></span>'),
    
    ('<span><i class="fas fa-check"></i> <strong>Shipping Container Base</strong></span>',
     '<span><i class="fas fa-check"></i> <strong>Expandable Base</strong></span>'),
    
    ('<span><i class="fas fa-check"></i> <strong>40ft Shipping Container</strong></span>',
     '<span><i class="fas fa-check"></i> <strong>40ft Expandable</strong></span>'),
    
    # Note section
    ('<p><i class="fas fa-home"></i> <strong>Note:</strong> These are <strong>actual shipping container homes</strong> - not regular houses.',
     '<p><i class="fas fa-home"></i> <strong>Note:</strong> These are <strong>premium expandable homes</strong> - innovative living solutions.'),
    
    # Process section
    ('<p class="section-subtitle">From shipping container to your dream home</p>',
     '<p class="section-subtitle">From concept to your dream home</p>'),
    
    # Footer
    ('Shipping Container Home Specialists',
     'Expandable Home Specialists'),
    
    ('premium expandable shipping container homes',
     'premium expandable homes'),
]

changes = 0
for old_text, new_text in fixes:
    if old_text in content:
        content = content.replace(old_text, new_text)
        changes += 1
        print(f"✅ Fixed: {old_text[:50]}...")

# Also check for any remaining "shipping" references
import re
shipping_count = len(re.findall(r'shipping', content, re.IGNORECASE))
if shipping_count > 0:
    print(f"\n⚠️  Warning: Still found {shipping_count} 'shipping' references")
    # Show them
    matches = re.finditer(r'shipping', content, re.IGNORECASE)
    for match in list(matches)[:5]:  # Show first 5
        start = max(0, match.start() - 30)
        end = min(len(content), match.end() + 30)
        context = content[start:end].replace('\n', ' ')
        print(f"   ...{context}...")

# Write updated file
with open('index.html', 'w') as f:
    f.write(content)

print(f"\n🎯 Applied {changes} specific fixes to index.html")
print("✅ index.html updated with professional terminology")
