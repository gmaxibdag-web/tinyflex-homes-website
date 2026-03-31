#!/bin/bash
# Deploy professional header inspired by industry leader

echo="🎨 DEPLOYING PROFESSIONAL INSPIRED HEADER"
echo="========================================="
echo=""
echo="📚 Inspired by: https://www.expandablehomes.com.au/"
echo="✨ Improvements made:"
echo="1. ✅ Cleaner, more modern design"
echo="2. ✅ Better typography hierarchy"
echo="3. ✅ Professional top bar with credentials"
echo="4. ✅ Prominent CTA button"
echo="5. ✅ Mobile-optimized navigation"
echo="6. ✅ Sticky header with scroll behavior"
echo=""

echo="🎯 What makes this professional:"
echo="1. Top Bar: Contact info + business credentials"
echo="2. Logo: Icon + 'TinyFlex' + 'Expandable Container Homes'"
echo="3. Navigation: Clear labels with active states"
echo="4. CTA: 'Get Free Quote' with icon"
echo="5. Mobile: Proper hamburger menu with backdrop"
echo="6. Design: Consistent spacing, professional colors"
echo=""

VERSION=$(date +%Y%m%d%H%M)
echo="📊 Cache busting version: v$VERSION"
echo=""

echo="🎨 Visual design:"
echo="┌─────────────────────────────────────────────────┐"
echo="│ 📞 Contact for Quote  🕐 Mon-Fri 9am-5pm        │"
echo="│ ✅ NSW Building Compliant  👔 Australian Owned │"
echo="├─────────────────────────────────────────────────┤"
echo="│ [🔷] TinyFlex                       [≡]         │"
echo="│     Expandable Container Homes                 │"
echo="│                                                 │"
echo="│ Home  Models & Pricing  Gallery  Our Process   │"
echo="│ About Us                    [💬 Get Free Quote]│"
echo="└─────────────────────────────────────────────────┘"
echo=""

echo="📦 Staging changes..."
git add .

echo=""
echo="💾 Committing professional inspired header..."
COMMIT_MSG="Professional Header Inspired by Industry Leader $(date '+%Y-%m-%d %H:%M')

🎨 INSPIRED BY INDUSTRY LEADER:

📚 Reference: https://www.expandablehomes.com.au/
✨ Improvements: Cleaner, more modern, better UX

🎯 PROFESSIONAL ELEMENTS:

1. TOP BAR:
   - Contact for Quote (phone icon)
   - Business Hours (clock icon)
   - NSW Building Compliant (check icon)
   - Australian Owned (suit icon)
   - Dark gradient background

2. LOGO:
   - Blue gradient icon (expand arrows)
   - 'TinyFlex' bold title
   - 'Expandable Container Homes' subtitle
   - Professional typography hierarchy

3. NAVIGATION:
   - Clear, descriptive labels
   - Active state with underline
   - Hover effects with background
   - Proper spacing and alignment

4. CALL TO ACTION:
   - 'Get Free Quote' with chat icon
   - Green gradient button
   - Prominent positioning
   - Hover animation

5. MOBILE OPTIMIZATION:
   - Responsive top bar
   - Working hamburger menu
   - Touch-friendly buttons
   - Collapsible with backdrop

6. DESIGN SYSTEM:
   - Consistent color scheme
   - Professional typography
   - Proper spacing (8px grid)
   - Shadow and elevation

🔧 TECHNICAL EXCELLENCE:

✅ HTML:
   - Semantic header structure
   - Proper Bootstrap classes
   - Accessible aria labels
   - Clean, maintainable code

✅ CSS:
   - Modular architecture
   - CSS variables for theming
   - Responsive breakpoints
   - Performance optimized
   - Dark mode support
   - Print styles

✅ JAVASCRIPT:
   - Scroll behavior (sticky header)
   - Active page detection
   - Mobile menu handling
   - Reduced motion support

📱 MOBILE FIRST:
   - Touch-optimized interface
   - Proper viewport handling
   - Fast loading on mobile
   - Off-canvas navigation

♿ ACCESSIBILITY:
   - Proper color contrast
   - Keyboard navigation
   - Screen reader support
   - Focus management
   - Reduced motion

🚀 PERFORMANCE:
   - Optimized CSS (no bloat)
   - Efficient JavaScript
   - Fast rendering
   - Cache friendly

📊 CACHE BUSTING:
   - Version: v$VERSION
   - Forces fresh load
   - Immediate visibility

🔍 TESTING:
   - Test: https://tinyflexhomes.com.au?v=$VERSION
   - Verify: Professional appearance
   - Verify: Mobile menu works
   - Verify: Scroll behavior
   - Verify: Active states

🎯 EXPECTED RESULT:
A professional header that matches industry standards
while being cleaner and more modern than the reference.

Inspired by the best, built better."

git commit -m "$COMMIT_MSG"

echo=""
echo="🚀 Pushing to GitHub..."
git push origin main

echo=""
echo="✅ PROFESSIONAL INSPIRED HEADER DEPLOYED!"
echo=""
echo="📋 What to check:"
echo="1. Wait 2-5 minutes for Cloudflare deployment"
echo="2. Visit: https://tinyflexhomes.com.au?v=$VERSION"
echo="3. Verify: Professional top bar with credentials"
echo="4. Verify: Clean logo with proper typography"
echo="5. Verify: Mobile hamburger menu works"
echo="6. Verify: Header shrinks when scrolling"
echo="7. Verify: Active page highlighting"
echo=""
echo="🎯 This should look professional and match industry standards."
