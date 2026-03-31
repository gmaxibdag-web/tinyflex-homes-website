// Proper Site JavaScript - Clean and Working
document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('.site-header');
    const navLinks = document.querySelectorAll('.nav-link');
    
    if (header) {
        // Scroll behavior
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
        
        // Set active page
        const currentPage = window.location.pathname.split('/').pop() || 'index.html';
        const pageName = currentPage.replace('.html', '');
        
        // Add body class for current page
        if (pageName && pageName !== 'index') {
            document.body.classList.add(`${pageName}-page`);
        } else {
            document.body.classList.add('home-page');
        }
        
        // Set active nav link
        navLinks.forEach(link => {
            const linkPage = link.getAttribute('href');
            
            // Remove active class from all
            link.classList.remove('active');
            
            // Add active class to current
            if (linkPage === currentPage || 
                (currentPage === '' && linkPage === 'index.html') ||
                (currentPage === 'index.html' && linkPage === 'index.html')) {
                link.classList.add('active');
            }
        });
        
        // Mobile menu close on click
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                const navbarCollapse = document.querySelector('.navbar-collapse');
                if (navbarCollapse && navbarCollapse.classList.contains('show')) {
                    const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                    bsCollapse.hide();
                }
            });
        });
        
        console.log('Proper site loaded');
    }
});

// Reduced motion support
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.documentElement.style.setProperty('--scroll-behavior', 'auto');
}
