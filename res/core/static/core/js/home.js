// Responsive & interactive behaviors for home page
(function () {
    'use strict';

    // Utilities
    const qs = (sel, ctx = document) => ctx.querySelector(sel);
    const qsa = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

    // DOM elements
    const navbar = qs('.navbar');
    const hero = qs('.hero-section');
    const scrollIndicator = qs('.scroll-indicator');
    const cartSidebar = qs('#cartSidebar');
    const cartOverlay = qs('#cartOverlay');
    const cartCountEl = qs('#cartCount');
    const cartItemsEl = qs('#cartItems');
    const cartTotalEl = qs('#cartTotal');

    // Local storage key
    const CART_KEY = 'ember_olive_cart_v1';

    // Initialize
    function init() {
        adjustHeroHeight();
        bindUIActions();
        renderCart();
        hideScrollIndicatorOnScroll();
        autoCloseNavbarOnNav();
        window.addEventListener('resize', throttle(adjustHeroHeight, 150));
    }

    // Throttle helper
    function throttle(fn, wait) {
        let t = null;
        return function () {
            if (t) return;
            t = setTimeout(() => {
                fn();
                t = null;
            }, wait);
        };
    }

    // Make hero fill available viewport (account for fixed navbar)
    function adjustHeroHeight() {
        if (!hero) return;
        const navHeight = navbar ? navbar.offsetHeight : 0;
        hero.style.minHeight = `calc(100vh - ${navHeight}px)`;
    }

    // Smooth scroll for internal links
    function smoothScroll() {
        qsa('a[href^="#"]').forEach(a => {
            a.addEventListener('click', function (e) {
                const href = this.getAttribute('href');
                if (!href || href === '#') return;
                if (href.startsWith('#')) {
                    const target = document.querySelector(href);
                    if (target) {
                        e.preventDefault();
                        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }
                }
            });
        });
    }

    // Hide the scroll indicator once user starts scrolling
    function hideScrollIndicatorOnScroll() {
        if (!scrollIndicator) return;
        const onScroll = () => {
            if (window.scrollY > 50) {
                scrollIndicator.classList.add('hidden');
                window.removeEventListener('scroll', onScroll);
            }
        };
        window.addEventListener('scroll', onScroll);
    }

    // Auto-close mobile navbar after clicking a nav link
    function autoCloseNavbarOnNav() {
        const collapse = qs('.navbar-collapse');
        if (!collapse) return;
        qsa('.navbar-nav .nav-link').forEach(link => {
            link.addEventListener('click', () => {
                if (collapse.classList.contains('show')) {
                    // Use Bootstrap collapse if available
                    if (typeof bootstrap !== 'undefined' && bootstrap.Collapse) {
                        const bsCollapse = bootstrap.Collapse.getInstance(collapse) || new bootstrap.Collapse(collapse);
                        bsCollapse.hide();
                    } else {
                        collapse.classList.remove('show');
                    }
                }
            });
        });
    }

    // CART - simple cart stored in localStorage
    function getCart() {
        try {
            return JSON.parse(localStorage.getItem(CART_KEY) || '{}');
        } catch (e) {
            return {};
        }
    }

    function saveCart(cart) {
        localStorage.setItem(CART_KEY, JSON.stringify(cart));
    }

    function updateQuantity(itemId, delta) {
        const input = qs(`#qty-${itemId}`);
        if (!input) return;
        let val = parseInt(input.value, 10) || 1;
        val += delta;
        if (val < parseInt(input.min || 1, 10)) val = parseInt(input.min || 1, 10);
        if (input.max && val > parseInt(input.max, 10)) val = parseInt(input.max, 10);
        input.value = val;
    }

    // Add item to cart
    function addToCart(id, name, price, imageUrl) {
        const qtyInput = qs(`#qty-${id}`);
        const qty = qtyInput ? Math.max(1, parseInt(qtyInput.value, 10) || 1) : 1;
        const cart = getCart();
        if (!cart[id]) {
            cart[id] = { id, name, price: Number(price), qty, image: imageUrl || '' };
        } else {
            cart[id].qty = Math.min((cart[id].qty || 0) + qty, 99);
        }
        saveCart(cart);
        renderCart();
        flashCartIcon();
    }

    function flashCartIcon() {
        const icon = qs('.cart-icon');
        if (!icon) return;
        icon.classList.add('flash');
        setTimeout(() => icon.classList.remove('flash'), 400);
    }

    function renderCart() {
        const cart = getCart();
        const items = Object.values(cart);
        cartItemsEl.innerHTML = '';
        let total = 0;
        let count = 0;
        if (items.length === 0) {
            cartItemsEl.innerHTML = '<p class="empty-cart">Your cart is empty.</p>';
        } else {
            items.forEach(item => {
                const row = document.createElement('div');
                row.className = 'cart-item d-flex align-items-center';
                row.innerHTML = `
                    <div class="cart-item-image me-3"><img src="${item.image || '/static/core/images/placeholder-dish.jpg'}" alt="${escapeHtml(item.name)}"></div>
                    <div class="cart-item-content flex-grow-1">
                        <div class="d-flex justify-content-between align-items-start">
                            <strong>${escapeHtml(item.name)}</strong>
                            <span class="cart-item-price">$${(item.price * item.qty).toFixed(2)}</span>
                        </div>
                        <div class="cart-item-controls d-flex align-items-center mt-2">
                            <button class="btn btn-sm btn-outline-secondary me-2" data-action="dec" data-id="${item.id}">-</button>
                            <input class="cart-qty-input" data-id="${item.id}" value="${item.qty}" min="1" max="99" type="number">
                            <button class="btn btn-sm btn-outline-secondary ms-2" data-action="inc" data-id="${item.id}">+</button>
                            <button class="btn btn-sm btn-link ms-3 text-danger" data-action="remove" data-id="${item.id}">Remove</button>
                        </div>
                    </div>
                `;
                cartItemsEl.appendChild(row);
                total += item.price * item.qty;
                count += item.qty;
            });
        }
        cartTotalEl.textContent = `$${total.toFixed(2)}`;
        cartCountEl.textContent = count;

        // Attach cart item listeners
        qsa('[data-action]', cartItemsEl).forEach(btn => {
            btn.addEventListener('click', e => {
                const aid = btn.getAttribute('data-action');
                const id = btn.getAttribute('data-id');
                if (aid === 'inc') changeCartQty(id, 1);
                if (aid === 'dec') changeCartQty(id, -1);
                if (aid === 'remove') removeFromCart(id);
            });
        });
        qsa('.cart-qty-input', cartItemsEl).forEach(input => {
            input.addEventListener('change', () => {
                const id = input.getAttribute('data-id');
                let v = parseInt(input.value, 10) || 1;
                if (v < 1) v = 1;
                changeCartQtyTo(id, v);
            });
        });
    }

    function changeCartQty(id, delta) {
        const cart = getCart();
        if (!cart[id]) return;
        cart[id].qty = Math.max(1, (cart[id].qty || 1) + delta);
        saveCart(cart);
        renderCart();
    }

    function changeCartQtyTo(id, val) {
        const cart = getCart();
        if (!cart[id]) return;
        cart[id].qty = Math.max(1, Math.min(99, parseInt(val, 10) || 1));
        saveCart(cart);
        renderCart();
    }

    function removeFromCart(id) {
        const cart = getCart();
        if (!cart[id]) return;
        delete cart[id];
        saveCart(cart);
        renderCart();
    }

    function toggleCart() {
        if (!cartSidebar || !cartOverlay) return;
        const isOpen = cartSidebar.classList.toggle('open');
        cartOverlay.classList.toggle('visible', isOpen);
        document.body.classList.toggle('no-scroll', isOpen);
    }

    function checkout() {
        const cart = getCart();
        if (Object.keys(cart).length === 0) {
            alert('Your cart is empty.');
            return;
        }
        // Example: proceed to checkout flow
        alert('Proceeding to checkout. (Demo)');
        localStorage.removeItem(CART_KEY);
        renderCart();
        toggleCart();
    }

    // Quick view: clone dish card content into modal
    function openQuickView(id) {
        const card = qs(`.dish-card[data-id="${id}"]`);
        const modalContent = qs('#quickViewContent');
        if (!card || !modalContent) return;
        const image = card.querySelector('img')?.src || '';
        const name = card.querySelector('.dish-name')?.textContent || '';
        const price = card.querySelector('.dish-price')?.textContent || '';
        const desc = card.querySelector('.dish-description')?.textContent || '';

        modalContent.innerHTML = `
            <div class="row">
                <div class="col-md-6">
                    <img src="${image}" alt="${escapeHtml(name)}" class="img-fluid">
                </div>
                <div class="col-md-6">
                    <h3>${escapeHtml(name)}</h3>
                    <p class="h5 text-muted">${escapeHtml(price)}</p>
                    <p>${escapeHtml(desc)}</p>
                    <div class="d-flex align-items-center mt-3">
                        <div class="quantity-selector me-3">
                            <button class="qty-btn minus" onclick="updateQuantity(${id}, -1)">-</button>
                            <input type="number" class="qty-input" id="modal-qty-${id}" value="1" min="1" max="10">
                            <button class="qty-btn plus" onclick="updateQuantity(${id}, 1)">+</button>
                        </div>
                        <button class="btn btn-primary" id="modalAddBtn">Add to Cart</button>
                    </div>
                </div>
            </div>
        `;

        // Show bootstrap modal if available
        if (typeof bootstrap !== 'undefined' && bootstrap.Modal) {
            const modalEl = document.getElementById('quickViewModal');
            const bsModal = new bootstrap.Modal(modalEl);
            bsModal.show();
            qs('#modalAddBtn').addEventListener('click', () => {
                const qty = parseInt(qs(`#modal-qty-${id}`).value, 10) || 1;
                addToCart(id, name, parseFloat(price.replace(/[^0-9.]/g, '')) || 0, image);
                bsModal.hide();
            });
        }
    }

    // Escape HTML for safety
    function escapeHtml(s) {
        return String(s).replace(/[&"'<>]/g, c => ({'&':'&amp;','"':'&quot;','\'':'&#39;','<':'&lt;','>':'&gt;'})[c]);
    }

    // Bind UI actions
    function bindUIActions() {
        smoothScroll();

        // expose functions used by inline handlers
        window.updateQuantity = updateQuantity;
        window.addToCart = addToCart;
        window.toggleCart = toggleCart;
        window.checkout = checkout;
        window.openQuickView = openQuickView;

        // Cart overlay click
        if (cartOverlay) cartOverlay.addEventListener('click', () => {
            if (cartSidebar.classList.contains('open')) toggleCart();
        });

        // Global escape to close overlays/modals
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                if (cartSidebar.classList.contains('open')) toggleCart();
                const bsModalEl = document.querySelector('#quickViewModal.show');
                if (bsModalEl && typeof bootstrap !== 'undefined' && bootstrap.Modal) {
                    const bsModal = bootstrap.Modal.getInstance(bsModalEl);
                    if (bsModal) bsModal.hide();
                }
            }
        });
    }

    // Safe init on DOMContentLoaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
// ===== Cart Management =====
let cart = JSON.parse(localStorage.getItem('emberOliveCart')) || [];

// Initialize cart on page load
document.addEventListener('DOMContentLoaded', function() {
    updateCartUI();
    
    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Smooth scrolling for anchor links
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
    
    // Newsletter form
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            showNotification('Thank you for subscribing!', 'success');
            this.reset();
        });
    }
});

// Toggle Cart Sidebar
function toggleCart() {
    const sidebar = document.getElementById('cartSidebar');
    const overlay = document.getElementById('cartOverlay');
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');
    document.body.style.overflow = sidebar.classList.contains('active') ? 'hidden' : '';
}

// Update Quantity Input
function updateQuantity(itemId, change) {
    const input = document.getElementById(`qty-${itemId}`);
    let value = parseInt(input.value) + change;
    if (value < 1) value = 1;
    if (value > 10) value = 10;
    input.value = value;
}

// Add to Cart
function addToCart(id, name, price, image) {
    const qtyInput = document.getElementById(`qty-${id}`);
    const quantity = parseInt(qtyInput.value);
    
    const existingItem = cart.find(item => item.id === id);
    
    if (existingItem) {
        existingItem.quantity += quantity;
    } else {
        cart.push({
            id: id,
            name: name,
            price: parseFloat(price),
            image: image,
            quantity: quantity
        });
    }
    
    saveCart();
    updateCartUI();
    showNotification(`${name} added to cart!`, 'success');
    
    // Reset quantity
    qtyInput.value = 1;
    
    // Open cart sidebar
    const sidebar = document.getElementById('cartSidebar');
    if (!sidebar.classList.contains('active')) {
        toggleCart();
    }
}

// Remove from Cart
function removeFromCart(id) {
    cart = cart.filter(item => item.id !== id);
    saveCart();
    updateCartUI();
}

// Update Cart Item Quantity
function updateCartItemQuantity(id, change) {
    const item = cart.find(item => item.id === id);
    if (item) {
        item.quantity += change;
        if (item.quantity < 1) {
            removeFromCart(id);
        } else {
            saveCart();
            updateCartUI();
        }
    }
}

// Save Cart to LocalStorage
function saveCart() {
    localStorage.setItem('emberOliveCart', JSON.stringify(cart));
}

// Update Cart UI
function updateCartUI() {
    const cartCount = document.getElementById('cartCount');
    const cartItems = document.getElementById('cartItems');
    const cartTotal = document.getElementById('cartTotal');
    
    // Update count badge
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    cartCount.textContent = totalItems;
    
    // Update cart items display
    if (cart.length === 0) {
        cartItems.innerHTML = `
            <div class="cart-empty">
                <i class="fas fa-shopping-basket"></i>
                <p>Your cart is empty</p>
                <small>Add some delicious dishes!</small>
            </div>
        `;
    } else {
        cartItems.innerHTML = cart.map(item => `
            <div class="cart-item">
                <img src="${item.image || '/static/core/images/placeholder-dish.jpg'}" alt="${item.name}" class="cart-item-image">
                <div class="cart-item-details">
                    <div class="cart-item-name">${item.name}</div>
                    <div class="cart-item-price">$${item.price.toFixed(2)}</div>
                    <div class="cart-item-qty">
                        <button onclick="updateCartItemQuantity(${item.id}, -1)">-</button>
                        <span>${item.quantity}</span>
                        <button onclick="updateCartItemQuantity(${item.id}, 1)">+</button>
                    </div>
                </div>
                <div class="remove-item" onclick="removeFromCart(${item.id})">
                    <i class="fas fa-trash"></i>
                </div>
            </div>
        `).join('');
    }
    
    // Update total
    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    cartTotal.textContent = `$${total.toFixed(2)}`;
}

// Quick View Modal
function openQuickView(itemId) {
    // In a real implementation, you'd fetch item details via AJAX
    // For now, we'll use the data from the card
    const card = document.querySelector(`[data-id="${itemId}"]`);
    const name = card.querySelector('.dish-name').textContent;
    const price = card.querySelector('.dish-price').textContent;
    const description = card.querySelector('.dish-description').textContent;
    const image = card.querySelector('.dish-image').src;
    
    const modalContent = document.getElementById('quickViewContent');
    modalContent.innerHTML = `
        <div class="row">
            <div class="col-md-6">
                <img src="${image}" alt="${name}" class="img-fluid rounded">
            </div>
            <div class="col-md-6">
                <h3>${name}</h3>
                <h4 class="text-primary">${price}</h4>
                <p>${description}</p>
                <div class="mt-4">
                    <button class="btn btn-primary btn-lg" onclick="addToCart(${itemId}, '${name}', ${price.replace('$', '')}, '${image}')" data-bs-dismiss="modal">
                        Add to Cart
                    </button>
                </div>
            </div>
        </div>
    `;
    
    const modal = new bootstrap.Modal(document.getElementById('quickViewModal'));
    modal.show();
}

// Checkout
function checkout() {
    if (cart.length === 0) {
        showNotification('Your cart is empty!', 'error');
        return;
    }
    
    // In a real implementation, this would proceed to checkout
    showNotification('Proceeding to checkout...', 'success');
    // window.location.href = '/checkout/';
}

// Notification System
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existing = document.querySelector('.custom-notification');
    if (existing) existing.remove();
    
    const notification = document.createElement('div');
    notification.className = `custom-notification notification-${type}`;
    notification.innerHTML = `
        <i class="fas ${type === 'success' ? 'fa-check-circle' : type === 'error' ? 'fa-exclamation-circle' : 'fa-info-circle'}"></i>
        <span>${message}</span>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? '#28a745' : type === 'error' ? '#dc3545' : '#17a2b8'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 3000;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add animation styles
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.dish-card, .testimonial-card, .info-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});