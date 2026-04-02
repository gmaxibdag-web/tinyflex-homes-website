#!/bin/bash
# Deployment script for TinyFlex Homes website

echo "🚀 Deploying TinyFlex Homes Professional Website"
echo "=============================================="

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: Must run from tinyflex_proper directory"
    exit 1
fi

# Backup current website
BACKUP_DIR="/root/.openclaw/workspace/website_backups/tinyflex_backup_$(date +%Y%m%d_%H%M%S)"
echo "📦 Creating backup of current website..."
mkdir -p "$BACKUP_DIR"
cp -r /root/.openclaw/workspace/tinyflex_fixed/* "$BACKUP_DIR/" 2>/dev/null || true
echo "✅ Backup created: $BACKUP_DIR"

# Deploy new website
echo "🔄 Deploying new website..."
rm -rf /root/.openclaw/workspace/tinyflex_fixed/*
cp -r ./* /root/.openclaw/workspace/tinyflex_fixed/

# Create placeholder images if they don't exist
echo "🖼️  Creating placeholder image structure..."
mkdir -p /root/.openclaw/workspace/tinyflex_fixed/images/gallery

# Create simple placeholder images using ImageMagick or fallback
if command -v convert &> /dev/null; then
    # Create hero image
    convert -size 800x600 gradient:#2c5282-#48bb78 \
            -fill white -pointsize 36 -gravity center \
            -annotate +0+0 "TinyFlex Homes\nExpandable Container Homes" \
            /root/.openclaw/workspace/tinyflex_fixed/images/hero-home.jpg 2>/dev/null || true
    
    # Create model images
    convert -size 400x300 gradient:#1a365d-#4299e1 \
            -fill white -pointsize 24 -gravity center \
            -annotate +0+0 "Compact Studio" \
            /root/.openclaw/workspace/tinyflex_fixed/images/model-compact.jpg 2>/dev/null || true
    
    convert -size 400x300 gradient:#2c5282-#48bb78 \
            -fill white -pointsize 24 -gravity center \
            -annotate +0+0 "Family Home" \
            /root/.openclaw/workspace/tinyflex_fixed/images/model-family.jpg 2>/dev/null || true
    
    convert -size 400x300 gradient:#4a5568-#718096 \
            -fill white -pointsize 24 -gravity center \
            -annotate +0+0 "Commercial Unit" \
            /root/.openclaw/workspace/tinyflex_fixed/images/model-commercial.jpg 2>/dev/null || true
    
    # Create gallery images
    for i in {1..8}; do
        convert -size 400x300 gradient:#$((RANDOM % 256)),$((RANDOM % 256)),$((RANDOM % 256)) \
                -fill white -pointsize 20 -gravity center \
                -annotate +0+0 "Project $i" \
                /root/.openclaw/workspace/tinyflex_fixed/images/gallery/project-$i.jpg 2>/dev/null || true
    done
else
    echo "⚠️  ImageMagick not installed, skipping placeholder image creation"
    echo "   Please add real images to /root/.openclaw/workspace/tinyflex_fixed/images/"
fi

# Update cache busting version
CURRENT_DATE=$(date +%Y%m%d%H%M)
echo "🔄 Updating cache busting version to: v$CURRENT_DATE"

# Update CSS and JS cache busting
sed -i "s/v=20260401/v=$CURRENT_DATE/g" /root/.openclaw/workspace/tinyflex_fixed/index.html
sed -i "s/v=20260401/v=$CURRENT_DATE/g" /root/.openclaw/workspace/tinyflex_fixed/models.html
sed -i "s/v=20260401/v=$CURRENT_DATE/g" /root/.openclaw/workspace/tinyflex_fixed/gallery.html
sed -i "s/v=20260401/v=$CURRENT_DATE/g" /root/.openclaw/workspace/tinyflex_fixed/css/style.css
sed -i "s/v=20260401/v=$CURRENT_DATE/g" /root/.openclaw/workspace/tinyflex_fixed/js/main.js

# Deploy to GitHub
echo "📤 Deploying to GitHub..."
cd /root/.openclaw/workspace/tinyflex_fixed

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git not initialized in target directory"
    echo "   Please ensure the website directory is a git repository"
    exit 1
fi

# Commit and push
git add .
git commit -m "Professional website rebuild - $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main

echo ""
echo "✅ DEPLOYMENT COMPLETE!"
echo "======================="
echo "📊 Website deployed to: https://tinyflexhomes.com.au"
echo "🔄 Cache busting version: v$CURRENT_DATE"
echo "📦 Backup saved to: $BACKUP_DIR"
echo ""
echo "🎯 Next steps:"
echo "   1. Visit https://tinyflexhomes.com.au?v=$CURRENT_DATE"
echo "   2. Test on mobile and desktop"
echo "   3. Replace placeholder images with real photos"
echo "   4. Update contact form backend if needed"
echo ""
echo "💡 Tip: Use Ctrl+Shift+R to hard refresh and bypass cache"