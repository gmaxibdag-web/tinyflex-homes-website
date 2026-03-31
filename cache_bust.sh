#!/bin/bash
# Simple cache busting script

echo "🔄 Adding cache busting to force browser updates"
echo "================================================"

# Generate version based on timestamp
VERSION=$(date +%Y%m%d%H%M)
echo "Cache busting version: v$VERSION"

# Process all HTML files
for file in *.html; do
    echo ""
    echo "Processing: $file"
    
    # Create backup
    cp "$file" "$file.bak"
    
    # Add cache busting to CSS files
    sed -i "s|\.css\"|.css?v=$VERSION\"|g" "$file"
    sed -i "s|\.css?v=[0-9]*\"|.css?v=$VERSION\"|g" "$file"
    
    # Add cache busting to JS files  
    sed -i "s|\.js\"|.js?v=$VERSION\"|g" "$file"
    sed -i "s|\.js?v=[0-9]*\"|.js?v=$VERSION\"|g" "$file"
    
    # Add cache busting to images that already have versions
    sed -i "s|\.\(jpg\|jpeg\|png\|gif\|webp\)?v=[0-9]*\"|.\1?v=$VERSION\"|g" "$file"
    
    echo "✅ Added cache busting to $file"
done

echo ""
echo "🎯 Cache busting complete!"
echo "Version: v$VERSION"
echo ""
echo "📋 Updated files:"
ls *.html
