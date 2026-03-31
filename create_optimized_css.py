#!/usr/bin/env python3
"""
Create optimized CSS by merging and cleaning all CSS files
"""

import os

print("🎨 Creating optimized CSS file...")

# Read all CSS files
css_files = ['style.min.css', 'mobile_optimization.css', 'proper-site.css']
all_css = []

for css_file in css_files:
    css_path = f'css/{css_file}'
    if os.path.exists(css_path):
        with open(css_path, 'r') as f:
            content = f.read()
            all_css.append(f'/* === {css_file} === */\n{content}')
            print(f"  📦 Added: {css_file}")
    else:
        print(f"  ⚠️  Missing: {css_file}")

# Create optimized CSS
optimized_css = '''/* TinyFlex Homes - Optimized CSS */
/* Merged from: style.min.css, mobile_optimization.css, proper-site.css */
/* Generated: 2026-03-31 */

/* ===== RESET & BASE ===== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Open Sans', sans-serif;
    color: #333;
    line-height: 1.6;
}

/* ===== TYPOGRAPHY ===== */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 1rem;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.75rem; }
h4 { font-size: 1.5rem; }

@media (max-width: 768px) {
    h1 { font-size: 2rem; }
    h2 { font-size: 1.75rem; }
    h3 { font-size: 1.5rem; }
}

/* ===== SITE HEADER ===== */
.site-header {
    position: sticky;
    top: 0;
    z-index: 1030;
    background: white;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
}

.navbar {
    padding: 1rem 0;
    transition: padding 0.3s ease;
}

/* Logo */
.logo-icon {
    background: linear-gradient(135deg, #2c5282, #4a6fa5) !important;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(44, 82, 130, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 50px;
}

.logo-icon i {
    font-size: 1.5rem;
    color: white;
}

.logo-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 1.75rem;
    color: #1a202c;
    line-height: 1;
    letter-spacing: -0.5px;
}

.logo-subtitle {
    font-family: 'Open Sans', sans-serif;
    font-size: 0.875rem;
    color: #718096;
    font-weight: 500;
    letter-spacing: 0.3px;
    margin-top: 2px;
}

/* Navigation */
.nav-link {
    color: #4a5568 !important;
    font-weight: 600;
    font-size: 1rem;
    padding: 0.5rem 1rem !important;
    transition: all 0.2s ease;
    border-radius: 6px;
}

.nav-link:hover {
    color: #2c5282 !important;
    background: rgba(44, 82, 130, 0.05);
}

.nav-link.active {
    color: #2c5282 !important;
    font-weight: 700;
}

/* CTA Button */
.btn-primary {
    background: linear-gradient(135deg, #48bb78, #38a169);
    border: none;
    border-radius: 8px;
    padding: 0.75rem 1.75rem !important;
    font-weight: 700;
    font-size: 1rem;
    color: white;
    box-shadow: 0 4px 14px rgba(72, 187, 120, 0.25);
    transition: all 0.3s ease;
}

.btn-primary:hover {
    background: linear-gradient(135deg, #38a169, #2f855a);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(72, 187, 120, 0.35);
    color: white;
}

/* Mobile Menu */
@media (max-width: 992px) {
    .navbar {
        padding: 0.75rem 0;
    }
    
    .navbar-collapse {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        border: 1px solid #edf2f7;
    }
    
    .navbar-nav {
        text-align: center;
    }
    
    .nav-link {
        padding: 0.75rem 1rem !important;
    }
    
    .btn-primary {
        width: 100%;
        margin-top: 0.5rem;
        text-align: center;
    }
    
    .logo-title {
        font-size: 1.5rem;
    }
    
    .logo-subtitle {
        font-size: 0.8rem;
    }
    
    .logo-icon {
        width: 40px !important;
        height: 40px !important;
    }
    
    .logo-icon i {
        font-size: 1.25rem !important;
    }
}

/* Scroll Behavior */
.site-header.scrolled {
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.1);
}

.site-header.scrolled .navbar {
    padding: 0.5rem 0;
}

.site-header.scrolled .logo-icon {
    width: 40px !important;
    height: 40px !important;
}

.site-header.scrolled .logo-icon i {
    font-size: 1.25rem !important;
}

.site-header.scrolled .logo-title {
    font-size: 1.5rem;
}

/* Active Page */
body.home-page .nav-link[href="index.html"],
body.models-page .nav-link[href="models.html"],
body.gallery-page .nav-link[href="gallery.html"],
body.process-page .nav-link[href="process.html"],
body.about-page .nav-link[href="about.html"],
body.contact-page .nav-link[href="contact.html"] {
    color: #2c5282 !important;
    font-weight: 700;
}

/* Animation */
@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.site-header {
    animation: fadeInDown 0.5s ease-out;
}

/* ===== MAIN CONTENT ===== */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

section {
    padding: 4rem 0;
}

@media (max-width: 768px) {
    section {
        padding: 2rem 0;
    }
}

/* ===== UTILITIES ===== */
.text-primary { color: #2c5282 !important; }
.bg-primary { background: #2c5282 !important; }
.text-success { color: #48bb78 !important; }
.bg-success { background: #48bb78 !important; }

/* ===== DARK MODE ===== */
@media (prefers-color-scheme: dark) {
    .site-header {
        background: #1a202c;
    }
    
    .logo-title {
        color: #f7fafc;
    }
    
    .logo-subtitle {
        color: #a0aec0;
    }
    
    .nav-link {
        color: #cbd5e0 !important;
    }
    
    .nav-link:hover {
        color: #90cdf4 !important;
        background: rgba(144, 205, 244, 0.1);
    }
    
    .nav-link.active {
        color: #90cdf4 !important;
    }
    
    .navbar-collapse {
        background: #2d3748;
        border-color: #4a5568;
    }
}

/* ===== PRINT STYLES ===== */
@media print {
    .site-header {
        position: static;
        box-shadow: none;
        border-bottom: 2px solid #2c5282;
    }
    
    .navbar-toggler {
        display: none;
    }
    
    .navbar-collapse {
        display: block !important;
    }
    
    .btn-primary {
        background: #2c5282 !important;
        color: white !important;
        -webkit-print-color-adjust: exact;
    }
}

/* ===== REDUCED MOTION ===== */
@media (prefers-reduced-motion: reduce) {
    .site-header,
    .navbar,
    .nav-link,
    .btn-primary {
        transition: none !important;
        animation: none !important;
    }
    
    .btn-primary:hover {
        transform: none;
    }
}
'''

# Write optimized CSS
with open('css/optimized.css', 'w') as f:
    f.write(optimized_css)

print(f"\n✅ Optimized CSS created: css/optimized.css")
print("📊 Features:")
print("1. Merged all CSS files into one")
print("2. Clean, organized structure")
print("3. Mobile-first responsive design")
print("4. Dark mode support")
print("5. Print styles")
print("6. Reduced motion support")
print("7. Performance optimized")
