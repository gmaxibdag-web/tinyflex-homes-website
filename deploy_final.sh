#!/bin/bash
# Deploy final fixes

VERSION=$(date +%Y%m%d%H%M)
echo "Deploying hero slider and header fix - Version: v$VERSION"

git add .
git commit -m "Restore Hero Slider & Fix Header $(date '+%Y-%m-%d %H:%M')

- Restored hero slider with 2 slides
- Fixed header with proper logo container
- Removed duplicate CSS files
- Updated optimized CSS with slider styles
- Mobile optimized design
- Cache busting: v$VERSION"

git push origin main

echo "✅ Deployed! Check: https://tinyflexhomes.com.au?v=$VERSION"
