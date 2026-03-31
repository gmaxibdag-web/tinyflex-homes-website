#!/bin/bash
echo "Downloading actual expandable container home images..."

# Try to get images from various sources
urls=(
  # These are example URLs - in reality would need actual image URLs
  "https://myhappytinyhome.com/wp-content/uploads/2024/09/glass-front-expandable-home.webp"
  "https://expressportables.com.au/cdn/shop/files/Expandable_Container_Home_1.jpg"
  "https://shippingcontainerservices.com.au/wp-content/uploads/2023/05/expandable-container-home-1.jpg"
)

# Create placeholder images with descriptive text for now
echo "Creating realistic placeholder images..."

python3 -c "
from PIL import Image, ImageDraw, ImageFont
import os

images = [
    ('modern-container-home-1-optimized.jpg', (1200, 800), 'Expandable Container Home', 'Exterior view of modern expandable shipping container home', (100, 150, 200)),
    ('container-exterior-3-optimized.jpg', (1200, 800), 'Shipping Container Expansion', 'Container home with expanded living space', (120, 140, 160)),
    ('minimalist-home-2-optimized.jpg', (800, 600), 'Modern Container Interior', 'Clean minimalist interior of expandable container', (200, 190, 180)),
    ('modern-architecture-4-optimized.jpg', (800, 600), 'Expandable Design', 'Container showing expansion mechanism', (180, 170, 160)),
    ('interior-design-5-optimized.jpg', (800, 600), 'Container Living Space', 'Spacious interior of expandable container home', (220, 210, 200))
]

for filename, size, title, desc, color in images:
    img = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(img)
    
    # Add title
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 36)
        small_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Title
    title_bbox = draw.textbbox((0, 0), title, font=font)
    title_width = title_bbox[2] - title_bbox[0]
    title_pos = ((size[0] - title_width) // 2, size[1] // 2 - 40)
    draw.text((title_pos[0]+2, title_pos[1]+2), title, fill=(0,0,0), font=font)
    draw.text(title_pos, title, fill=(255,255,255), font=font)
    
    # Description
    desc_bbox = draw.textbbox((0, 0), desc, font=small_font)
    desc_width = desc_bbox[2] - desc_bbox[0]
    desc_pos = ((size[0] - desc_width) // 2, size[1] // 2 + 20)
    draw.text((desc_pos[0]+1, desc_pos[1]+1), desc, fill=(0,0,0), font=small_font)
    draw.text(desc_pos, desc, fill=(240,240,240), font=small_font)
    
    # Save
    img.save(f'local_images/{filename}', 'JPEG', quality=90, optimize=True)
    print(f'Created: {filename}')

print('✅ Created realistic placeholder images')
print('⚠️  Note: These are placeholders. For production, use:')
print('   1. AI-generated expandable container home images')
print('   2. Purchased stock photos')
print('   3. Actual product photos')
"

