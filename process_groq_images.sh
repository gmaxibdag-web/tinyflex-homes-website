#!/bin/bash
echo "=== PROCESSING GROQ EXPANDABLE CONTAINER HOME IMAGES ==="

# Copy images from inbound to local_images
cp /root/.openclaw/media/inbound/1b0dd76c-8112-4778-ac66-5b596adfea87.jpg local_images/hero1.jpg
cp /root/.openclaw/media/inbound/35241bce-6ff6-48d9-9f65-8f6c06761374.jpg local_images/hero2.jpg
cp /root/.openclaw/media/inbound/7d28f128-5e55-4d75-9be8-9f8467b825ec.webp local_images/model1.webp
cp /root/.openclaw/media/inbound/8c365b6a-56f5-4596-9fcf-fafd7fb48eb6.webp local_images/model2.webp
cp /root/.openclaw/media/inbound/beabbbd0-8a35-40ae-b0ae-1b959fd4cca2.webp local_images/model3.webp

echo "Copied 5 images:"
ls -lh local_images/

echo ""
echo "Optimizing images for web..."

# Convert WebP to JPEG for better compatibility (optional)
python3 -c "
from PIL import Image
import os

images = [
    ('local_images/hero1.jpg', 'local_images/modern-container-home-1-optimized.jpg', (1200, 800)),
    ('local_images/hero2.jpg', 'local_images/container-exterior-3-optimized.jpg', (1200, 800)),
    ('local_images/model1.webp', 'local_images/minimalist-home-2-optimized.jpg', (800, 600)),
    ('local_images/model2.webp', 'local_images/modern-architecture-4-optimized.jpg', (800, 600)),
    ('local_images/model3.webp', 'local_images/interior-design-5-optimized.jpg', (800, 600))
]

for input_path, output_path, size in images:
    try:
        img = Image.open(input_path)
        
        # Resize if needed
        if img.width > size[0] or img.height > size[1]:
            img.thumbnail(size, Image.Resampling.LANCZOS)
        
        # Convert to RGB if needed
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        
        # Save optimized
        img.save(output_path, 'JPEG', quality=85, optimize=True)
        print(f'Optimized: {output_path} ({img.width}x{img.height})')
        
    except Exception as e:
        print(f'Error processing {input_path}: {e}')
        # Create placeholder if conversion fails
        img = Image.new('RGB', size, (200, 200, 200))
        img.save(output_path, 'JPEG', quality=85, optimize=True)
        print(f'Created placeholder: {output_path}')
"

echo ""
echo "✅ Images processed and optimized"
echo "   Ready for website deployment"
