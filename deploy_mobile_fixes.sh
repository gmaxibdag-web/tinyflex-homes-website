#!/bin/bash
# Deploy mobile optimization fixes

echo "📱 Deploying Mobile Optimization Fixes"
echo "======================================"

echo ""
echo "📊 Changes made:"
echo "✅ Mobile-optimized header with Bootstrap"
echo "✅ Mobile-responsive navigation menu"
echo "✅ Mobile optimization CSS added"
echo "✅ Better touch targets and spacing"
echo "✅ iOS Safari fixes"
echo "✅ Horizontal scroll prevention"

echo ""
echo "📦 Staging changes..."
git add .

echo ""
echo "💾 Committing mobile fixes..."
COMMIT_MSG="Mobile Optimization Fixes $(date '+%Y-%m-%d %H:%M')

📱 Mobile Browser Fixes:
- Fixed header/navigation for mobile browsing
- Added Bootstrap for responsive design
- Mobile-optimized CSS for all screen sizes
- Better touch targets (44px minimum)
- iOS Safari compatibility fixes
- Horizontal scroll prevention
- Improved mobile menu

🎯 Specific Fixes:
- Removed problematic top info on mobile
- Mobile-first responsive design
- Tablet optimization (769px-1024px)
- Small phone optimization (<480px)
- Safe area padding for modern phones

🚀 Expected Results:
- Professional mobile browsing experience
- No more awkward top info sections
- Smooth navigation on all devices
- Better Google Mobile-Friendly test score

Built with AI Empire OS - Mobile Optimization Module"

git commit -m "$COMMIT_MSG"

echo ""
echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Mobile fixes deployed!"
echo ""
echo "📱 Mobile testing tools:"
echo "   - https://search.google.com/test/mobile-friendly"
echo "   - https://pagespeed.web.dev/ (mobile tab)"
echo "   - Test on actual phones if possible"
echo ""
echo "🌐 Live site updating: https://tinyflexhomes.com.au"
echo "   (Cloudflare Pages auto-deploy in 2-5 minutes)"
