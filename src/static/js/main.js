/**
 * Projeto Lista - Main JavaScript
 * Interatividade e funcionalidades do site
 */

(function() {
    'use strict';

    // ============================================
    // SMOOTH SCROLLING
    // ============================================
    
    /**
     * Ativa smooth scrolling para links âncora
     */
    function setupSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    // ============================================
    // NAVIGATION ACTIVE STATE
    // ============================================
    
    /**
     * Atualiza o estado ativo da navegação baseado na seção visível
     */
    function setupNavigationActive() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('nav a[href^="#"]');

        window.addEventListener('scroll', throttle(() => {
            let current = '';

            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;

                if (pageYOffset >= sectionTop - 200) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href').slice(1) === current) {
                    link.classList.add('active');
                }
            });
        }, 100));
    }

    // ============================================
    // LAZY LOADING IMAGES
    // ============================================
    
    /**
     * Carrega imagens lazy loading
     */
    function setupLazyLoading() {
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                            img.removeAttribute('data-src');
                        }
                        observer.unobserve(img);
                    }
                });
            });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }
    }

    // ============================================
    // BUTTON HANDLERS
    // ============================================
    
    /**
     * Configurar handlers para botões
     */
    function setupButtonHandlers() {
        const buttons = document.querySelectorAll('button, a[data-action]');

        buttons.forEach(button => {
            button.addEventListener('click', function(e) {
                // Adicionar ripple effect
                createRipple.call(this, e);
            });

            // Focus visible
            button.addEventListener('focus', function() {
                this.classList.add('focus-visible');
            });

            button.addEventListener('blur', function() {
                this.classList.remove('focus-visible');
            });
        });
    }

    /**
     * Efeito ripple ao clicar em botões
     */
    function createRipple(e) {
        const button = this;
        const ripple = document.createElement('span');
        const rect = button.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;

        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');

        this.appendChild(ripple);

        setTimeout(() => ripple.remove(), 600);
    }

    // ============================================
    // PERFORMANCE UTILITIES
    // ============================================
    
    /**
     * Throttle function para melhorar performance
     */
    function throttle(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    /**
     * Debounce function
     */
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // ============================================
    // ACCESSIBILITY IMPROVEMENTS
    // ============================================
    
    /**
     * Melhorar acessibilidade do keyboard navigation
     */
    function setupKeyboardNavigation() {
        // Permitir navegação com Tab
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                // Fechar modais, se existirem
                const modals = document.querySelectorAll('[role="dialog"][aria-hidden="false"]');
                modals.forEach(modal => {
                    modal.setAttribute('aria-hidden', 'true');
                });
            }
        });
    }

    // ============================================
    // PERFORMANCE MONITORING
    // ============================================
    
    /**
     * Log simples de performance
     */
    function logPerformance() {
        if (window.performance && window.performance.timing) {
            const timing = window.performance.timing;
            const navigationStart = timing.navigationStart;
            const responseEnd = timing.responseEnd;
            const domComplete = timing.domComplete;
            const loadComplete = timing.loadEventEnd;

            const responseTime = responseEnd - navigationStart;
            const domTime = domComplete - navigationStart;
            const loadTime = loadComplete - navigationStart;

            if (process?.env?.NODE_ENV === 'development') {
                console.log(`
                    📊 Performance Metrics:
                    - Response Time: ${responseTime}ms
                    - DOM Complete: ${domTime}ms
                    - Page Load: ${loadTime}ms
                `);
            }
        }
    }

    // ============================================
    // INITIALIZATION
    // ============================================
    
    /**
     * Inicializar todos os módulos
     */
    function init() {
        // Verificar se o DOM está pronto
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
            return;
        }

        setupSmoothScroll();
        setupNavigationActive();
        setupLazyLoading();
        setupButtonHandlers();
        setupKeyboardNavigation();
        logPerformance();

        console.log('✅ Projeto Lista - Scripts inicializados com sucesso');
    }

    // Iniciar
    init();

})();
