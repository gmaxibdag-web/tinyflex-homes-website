#!/usr/bin/env python3
"""
Update optimized CSS with hero slider and header fixes
"""

print("🎨 Updating optimized CSS with hero slider and header styles...")

# Read current optimized.css
with open('optimized.css', 'r') as f:
    content = f.read()

# Find where to insert hero slider styles (after header styles)
header_end = content.find('/* ===== MAIN CONTENT ===== */')

if header_end != -1:
    # Hero slider styles to insert
    hero_styles = '''
/* ===== HERO SLIDER ===== */
.hero-slider {
    position: relative;
    height: 600px;
    overflow: hidden;
    background: #1a202c;
}

.hero-slider .slides {
    height: 100%;
    position: relative;
}

.hero-slider .slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    opacity: 0;
    transition: opacity 1s ease;
    display: flex;
    align-items: center;
}

.hero-slider .slide.active {
    opacity: 1;
}

.hero-slider .container {
    width: 100%;
}

.hero-content {
    max-width: 800px;
    color: white;
    text-align: center;
    margin: 0 auto;
    padding: 2rem;
    background: rgba(0, 0, 0, 0.5);
    border-radius: 12px;
    backdrop-filter: blur(10px);
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
    line-height: 1.1;
}

.hero-title .highlight {
    color: #48bb78;
    display: block;
    font-size: 2.5rem;
    margin-top: 0.5rem;
}

.hero-subtitle {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    opacity: 0.9;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.hero-buttons .btn {
    padding: 1rem 2rem;
    font-size: 1.1rem;
    font-weight: 600;
    border-radius: 8px;
}

.hero-buttons .btn-outline-light {
    background: transparent;
    border: 2px solid white;
    color: white;
}

.hero-buttons .btn-outline-light:hover {
    background: white;
    color: #2c5282;
}

/* Slider Controls */
.slider-controls {
    position: absolute;
    bottom: 2rem;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
}

.slider-prev,
.slider-next {
    background: rgba(255, 255, 255, 0.2);
    border: none;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    color: white;
    font-size: 1.25rem;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}

.slider-prev:hover,
.slider-next:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: scale(1.1);
}

.slider-dots {
    display: flex;
    gap: 0.5rem;
}

.slider-dots .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    cursor: pointer;
    transition: all 0.3s ease;
}

.slider-dots .dot.active {
    background: white;
    transform: scale(1.2);
}

/* Mobile Hero */
@media (max-width: 768px) {
    .hero-slider {
        height: 500px;
    }
    
    .hero-title {
        font-size: 2rem;
    }
    
    .hero-title .highlight {
        font-size: 1.75rem;
    }
    
    .hero-subtitle {
        font-size: 1rem;
        padding: 0 1rem;
    }
    
    .hero-content {
        padding: 1.5rem;
        margin: 0 1rem;
    }
    
    .hero-buttons {
        flex-direction: column;
        align-items: center;
    }
    
    .hero-buttons .btn {
        width: 100%;
        max-width: 300px;
    }
    
    .slider-controls {
        bottom: 1rem;
    }
    
    .slider-prev,
    .slider-next {
        width: 40px;
        height: 40px;
        font-size: 1rem;
    }
}

/* Logo Container Fix */
.logo-container .logo-icon {
    width: 50px;
    height: 50px;
    background: linear-gradient(135deg, #2c5282, #4a6fa5);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(44, 82, 130, 0.2);
}

.logo-container .logo-icon i {
    font-size: 1.5rem;
    color: white;
}

/* Trust Badges */
.trust-badges {
    background: #f8fafc;
    padding: 3rem 0;
}

.badge-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.badge {
    text-align: center;
    padding: 2rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease;
}

.badge:hover {
    transform: translateY(-5px);
}

.badge i {
    font-size: 2.5rem;
    color: #2c5282;
    margin-bottom: 1rem;
}

.badge h4 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    color: #1a202c;
}

.badge p {
    color: #718096;
    font-size: 0.9rem;
}

@media (max-width: 768px) {
    .trust-badges {
        padding: 2rem 0;
    }
    
    .badge-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
        padding: 0 1rem;
    }
    
    .badge {
        padding: 1.5rem;
    }
}
'''
    
    # Insert hero styles before MAIN CONTENT
    updated_content = content[:header_end] + hero_styles + content[header_end:]
    
    # Write updated CSS
    with open('optimized.css', 'w') as f:
        f.write(updated_content)
    
    print("✅ Updated optimized CSS with hero slider and header fixes")
    print("\n🎯 Added styles for:")
    print("1. Hero slider with animations")
    print("2. Slider controls (prev/next, dots)")
    print("3. Logo container fix")
    print("4. Trust badges section")
    print("5. Mobile responsiveness")
else:
    print("❌ Could not find insertion point in CSS")
