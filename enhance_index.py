#!/usr/bin/env python3
"""
Enhance index.html with better SEO and structure
"""

import re

# Read current index.html
with open('index.html', 'r') as f:
    content = f.read()

# Add H1 tag if missing
if '<h1>' not in content:
    # Find the hero section and add H1
    hero_pattern = r'(<section[^>]*class="[^"]*hero[^"]*"[^>]*>)(.*?)(</section>)'
    match = re.search(hero_pattern, content, re.DOTALL | re.IGNORECASE)
    
    if match:
        hero_section = match.group(0)
        # Add H1 inside hero section
        enhanced_hero = hero_section.replace(
            '<div class="hero-content">',
            '<div class="hero-content">\n        <h1>Premium Expandable Container Homes in Australia</h1>'
        )
        content = content.replace(hero_section, enhanced_hero)
        print("Added H1 tag to hero section")

# Add alt tags to images
img_pattern = r'<img([^>]*)>'
def add_alt_tag(match):
    img_tag = match.group(0)
    if 'alt=' not in img_tag:
        # Extract filename for alt text
        src_match = re.search(r'src="([^"]*)"', img_tag)
        if src_match:
            src = src_match.group(1)
            filename = src.split('/')[-1].split('.')[0]
            alt_text = filename.replace('-', ' ').title()
            img_tag = img_tag.replace('<img', f'<img alt="{alt_text}"')
    return img_tag

content = re.sub(img_pattern, add_alt_tag, content)
print("Added alt tags to images")

# Add structured data (JSON-LD)
structured_data = '''
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Tiny Flex Homes",
  "image": "https://tinyflexhomes.com.au/local_images/modern-container-home-1-optimized.jpg",
  "description": "Australian buying agent for premium expandable container homes. Customizable designs delivered in 12-14 weeks.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Sydney",
    "addressRegion": "NSW",
    "addressCountry": "AU"
  },
  "telephone": "+61-XXX-XXX-XXX",
  "openingHours": "Mo-Fr 09:00-17:00",
  "url": "https://tinyflexhomes.com.au"
}
</script>
'''

# Add before closing head tag
if '</head>' in content and 'schema.org' not in content:
    content = content.replace('</head>', f'{structured_data}\n</head>')
    print("Added structured data")

# Write enhanced file
with open('index.html', 'w') as f:
    f.write(content)

print("✅ index.html enhanced with SEO improvements")
