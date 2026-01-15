document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initGallery();
    initLightbox();
    initContactForm();
    initScrollAnimations();
});

function initNavbar() {
    const navbar = document.querySelector('.navbar');
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

function initGallery() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const loadMoreItems = document.querySelectorAll('.gallery-item.load-more');
    let allLoaded = false;

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.filter;

            galleryItems.forEach(item => {
                if (filter === 'all' || item.dataset.category === filter) {
                    item.classList.remove('hidden');
                    if (!item.classList.contains('load-more') || allLoaded) {
                        item.classList.add('visible');
                    } else {
                        item.classList.remove('visible');
                    }
                } else {
                    item.classList.add('hidden');
                    item.classList.remove('visible');
                }
            });

            updateLoadMoreButton(filter, allLoaded);
        });
    });

    loadMoreBtn.addEventListener('click', () => {
        const activeFilter = document.querySelector('.filter-btn.active').dataset.filter;
        allLoaded = true;

        loadMoreItems.forEach(item => {
            if (activeFilter === 'all' || item.dataset.category === activeFilter) {
                item.classList.remove('hidden');
                item.classList.add('visible');
            }
        });

        loadMoreBtn.classList.add('hidden');
    });
}

function updateLoadMoreButton(filter, allLoaded) {
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const loadMoreItems = document.querySelectorAll('.gallery-item.load-more');

    if (allLoaded) {
        loadMoreBtn.classList.add('hidden');
        return;
    }

    let visibleCount = 0;
    loadMoreItems.forEach(item => {
        if (filter === 'all' || item.dataset.category === filter) {
            visibleCount++;
        }
    });

    if (visibleCount > 0) {
        loadMoreBtn.classList.remove('hidden');
        loadMoreBtn.textContent = `Ver Más (+${visibleCount} trabajos)`;
    } else {
        loadMoreBtn.classList.add('hidden');
    }
}

function initLightbox() {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = lightbox.querySelector('img');
    const lightboxTitle = lightbox.querySelector('h3');
    const lightboxDesc = lightbox.querySelector('p');
    const lightboxClose = lightbox.querySelector('.lightbox-close');
    const lightboxPrev = lightbox.querySelector('.lightbox-prev');
    const lightboxNext = lightbox.querySelector('.lightbox-next');
    const galleryItems = document.querySelectorAll('.gallery-item');

    let currentIndex = 0;
    let images = [];

    function updateImages() {
        images = [];
        galleryItems.forEach((item) => {
            if (!item.classList.contains('hidden') && (item.classList.contains('visible') || !item.classList.contains('load-more'))) {
                images.push({
                    src: item.querySelector('img').src,
                    title: item.querySelector('.gallery-overlay h3').textContent,
                    desc: item.querySelector('.gallery-overlay p').textContent
                });
            }
        });
    }

    galleryItems.forEach((item, index) => {
        item.addEventListener('click', () => {
            updateImages();
            currentIndex = images.findIndex(img => img.src === item.querySelector('img').src);
            openLightbox(currentIndex);
        });
    });

    function openLightbox(index) {
        if (images.length === 0) return;
        const image = images[index];
        lightboxImg.src = image.src;
        lightboxTitle.textContent = image.title;
        lightboxDesc.textContent = image.desc;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }

    function showPrev() {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        openLightbox(currentIndex);
    }

    function showNext() {
        currentIndex = (currentIndex + 1) % images.length;
        openLightbox(currentIndex);
    }

    lightboxClose.addEventListener('click', closeLightbox);
    lightboxPrev.addEventListener('click', showPrev);
    lightboxNext.addEventListener('click', showNext);

    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (!lightbox.classList.contains('active')) return;

        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowLeft') showPrev();
        if (e.key === 'ArrowRight') showNext();
    });
}

function initContactForm() {
    const form = document.getElementById('contactForm');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        console.log('Form submitted:', data);

        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Enviando...';
        submitBtn.disabled = true;

        setTimeout(() => {
            submitBtn.textContent = '¡Enviado!';
            submitBtn.style.background = '#2d5a3d';

            setTimeout(() => {
                submitBtn.textContent = originalText;
                submitBtn.style.background = '';
                submitBtn.disabled = false;
                form.reset();
            }, 2000);
        }, 1000);
    });
}

function initScrollAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll(
        '.gallery-item, .about-content, .contact-info, .contact-form-wrapper'
    );

    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    const style = document.createElement('style');
    style.textContent = `
        .animate-in {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    `;
    document.head.appendChild(style);
}
