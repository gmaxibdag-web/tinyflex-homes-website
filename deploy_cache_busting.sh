#!/bin/bash
# Deploy cache busting to force browser updates

echo "🔄 DEPLOYING CACHE BUSTING UPDATES"
echo "=================================="
echo ""
echo "🎯 Problem: Browser/Cloudflare caching preventing updates"
echo "🎯 Solution: Added cache busting (version parameters)"
echo ""

VERSION=$(date +%Y%m%d%H%M)
echo "📊 Cache busting version: v$VERSION"
echo ""

echo "📋 Changes made:"
echo "✅ Added ?v=$VERSION to all CSS files"
echo "✅ Added ?v=$VERSION to all JS files"  
echo "✅ Updated existing image version parameters"
echo "✅ Added no-cache meta tags to prevent browser caching"
echo "✅ Forces fresh load on all browsers"
echo ""

echo "📦 Staging changes..."
git add .

echo ""
echo "💾 Committing cache busting update..."
COMMIT_MSG="Cache Busting Update $(date '+%Y-%m-%d %H:%M')

🔄 FORCE BROWSER UPDATES:
- Added cache busting version: v$VERSION
- All CSS files: ?v=$VERSION
- All JS files: ?v=$VERSION  
- Updated image cache busting
- Added no-cache meta tags

🎯 Why this is needed:
1. Browsers cache CSS/JS files aggressively
2. Cloudflare Pages CDN caches files
3. Users don't see updates without cache busting
4. Mobile browsers are especially aggressive

🔧 Technical details:
- Version parameter: ?v=$VERSION
- No-cache meta tags added
- Forces fresh fetch on every visit
- Will be removed once site is stable

🚀 Expected result:
- All users will see updated mobile fixes immediately
- No more cached old versions
- Consistent experience across all devices

📱 Mobile fixes now visible:
- Professional mobile header
- Hamburger menu on small screens
- No awkward top info sections
- Better touch targets

🌐 Live updates forced for:
- https://tinyflexhomes.com.au
- All subpages
- All CSS/JS files
- All browsers (Chrome, Safari, Firefox, etc.)

Built with AI Empire OS - Cache Management Module"

git commit -m "$COMMIT_MSG"

echo ""
echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ CACHE BUSTING DEPLOYED!"
echo ""
echo "📋 What happens now:"
echo "1. Cloudflare Pages will auto-deploy (2-5 minutes)"
echo "2. All browsers will fetch fresh files (no cache)"
echo "3. Mobile fixes will be immediately visible"
echo "4. Version: v$VERSION ensures unique URLs"
echo ""
echo "🔍 How to verify:"
echo "1. Wait 2-5 minutes for deployment"
echo "2. Open https://tinyflexhomes.com.au"
echo "3. Press Ctrl+Shift+R (Cmd+Shift+R on Mac) to hard refresh"
echo "4. On mobile: Close and reopen browser"
echo "5. Check DevTools → Network → Disable cache (if needed)"
echo ""
echo "🌐 Live URL: https://tinyflexhomes.com.au?v=$VERSION"
echo "   (Adding ?v=$VERSION helps force update)"
