document.addEventListener('DOMContentLoaded', () => {
    initMobileMenu();
    initNavbarScroll();
    initStatsCounter();
    initSmoothAnchors();
});

function initMobileMenu() {
    const toggle = document.getElementById('mobileToggle');
    const menu = document.getElementById('navbarMenu');
    if (!toggle || !menu) return;

    toggle.addEventListener('click', () => {
        const open = menu.classList.toggle('active');
        toggle.classList.toggle('active', open);
        toggle.setAttribute('aria-expanded', open);
        document.body.style.overflow = open ? 'hidden' : '';
    });

    menu.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', () => {
            menu.classList.remove('active');
            toggle.classList.remove('active');
            toggle.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        });
    });
}

function initNavbarScroll() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;
    const onScroll = () => navbar.classList.toggle('scrolled', window.scrollY > 20);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
}

function initStatsCounter() {
    const counters = document.querySelectorAll('.stat-number[data-target]');
    if (!counters.length) return;

    const animate = (el) => {
        const target = parseInt(el.dataset.target, 10);
        const start = performance.now();
        const duration = 2000;
        const step = (now) => {
            const p = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.floor(eased * target).toLocaleString();
            if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
            if (e.isIntersecting) {
                animate(e.target);
                observer.unobserve(e.target);
            }
        });
    }, { threshold: 0.3 });

    counters.forEach((c) => observer.observe(c));
}

function initSmoothAnchors() {
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener('click', (e) => {
            const id = anchor.getAttribute('href');
            if (id === '#') return;
            const target = document.querySelector(id);
            if (!target) return;
            e.preventDefault();
            window.scrollTo({
                top: target.getBoundingClientRect().top + window.scrollY - 80,
                behavior: 'smooth',
            });
        });
    });
}
