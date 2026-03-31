#!/usr/bin/env python3
"""
Optimize CSS for better performance
"""

import re

# Read current CSS
with open('style.css', 'r') as f:
    css = f.read()

# Remove comments
css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)

# Remove unnecessary whitespace
css = re.sub(r'\s+', ' ', css)
css = re.sub(r'\s*{\s*', '{', css)
css = re.sub(r'\s*}\s*', '}', css)
css = re.sub(r'\s*;\s*', ';', css)
css = re.sub(r'\s*:\s*', ':', css)
css = re.sub(r'\s*,\s*', ',', css)

# Add critical CSS (above-the-fold styles) inline recommendation
critical_css = """
/* Critical CSS (should be inlined in <head>) */
.hero, .navbar, h1, h2 { opacity: 1; }
body { font-family: 'Open Sans', sans-serif; margin: 0; }
"""

# Create optimized version
optimized_css = f"""/* Optimized CSS - Tiny Flex Homes */
/* Original: {len(css)} chars | Optimized: {len(css)} chars */

{css}

/* Performance optimizations */
@media (prefers-reduced-motion: reduce) {{
  * {{
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }}
}}

/* Print styles */
@media print {{
  .navbar, .footer, .cta-button {{
    display: none !important;
  }}
}}
"""

# Write optimized CSS
with open('style.optimized.css', 'w') as f:
    f.write(optimized_css)

# Also create minified version
minified_css = re.sub(r'\s+', ' ', css).strip()
with open('style.min.css', 'w') as f:
    f.write(minified_css)

print(f"✅ CSS optimized:")
print(f"   Original: {len(css)} characters")
print(f"   Minified: {len(minified_css)} characters")
print(f"   Saved: {len(css) - len(minified_css)} characters ({((len(css) - len(minified_css)) / len(css) * 100):.1f}%)")
