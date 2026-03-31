// Clean Template JavaScript - Simple and Working
document.addEventListener('DOMContentLoaded', function() {
    // Set active page
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const pageName = currentPage.replace('.html', '');
    
    // Add body class
    if (pageName && pageName !== 'index') {
        document.body.classList.add(`${pageName}-page`);
    } else {
        document.body.classList.add('home-page');
    }
    
    // Mobile menu close on click
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function() {
            const navbarCollapse = document.querySelector('.navbar-collapse');
            if (navbarCollapse && navbarCollapse.classList.contains('show')) {
                const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                bsCollapse.hide();
            }
        });
    });
    
    console.log('Clean template loaded');
});
