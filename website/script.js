// VetAI Academy — script.js

/* ---- Navbar scroll effect ---- */
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 40) {
    navbar.style.background = 'rgba(13, 17, 23, 0.98)';
  } else {
    navbar.style.background = 'rgba(13, 17, 23, 0.85)';
  }
});

/* ---- Hamburger menu ---- */
const hamburger = document.getElementById('hamburger');
const navLinks = document.querySelector('.nav-links');
hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});

// Close nav when a link is clicked
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => navLinks.classList.remove('open'));
});

/* ---- Smooth active nav link highlighting ---- */
const sections = document.querySelectorAll('section[id]');
const navItems = document.querySelectorAll('.nav-links a[href^="#"]');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navItems.forEach(a => a.classList.remove('active'));
      const active = document.querySelector(`.nav-links a[href="#${entry.target.id}"]`);
      if (active) active.classList.add('active');
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => observer.observe(s));

/* ---- FAQ accordion ---- */
document.querySelectorAll('.faq-question').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const isOpen = item.classList.contains('open');

    // Close all
    document.querySelectorAll('.faq-item').forEach(el => el.classList.remove('open'));

    // Toggle clicked
    if (!isOpen) item.classList.add('open');
  });
});

/* ---- Animate elements on scroll ---- */
const animateEls = document.querySelectorAll(
  '.card, .module, .benefit, .testimonial, .track, .faq-item'
);

const fadeObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      fadeObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

animateEls.forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  fadeObserver.observe(el);
});

/* ---- Hero stat counter animation ---- */
function animateCounter(el, target, suffix = '') {
  let current = 0;
  const step = Math.max(1, Math.ceil(target / 60));
  const interval = setInterval(() => {
    current = Math.min(current + step, target);
    el.textContent = (suffix === '$' ? '$' : '') + current.toLocaleString() + (suffix !== '$' ? suffix : '');
    if (current >= target) clearInterval(interval);
  }, 24);
}

const statsObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const nums = entry.target.querySelectorAll('.stat-num');
      nums.forEach(num => {
        const text = num.textContent;
        if (text.includes('$')) {
          animateCounter(num, parseInt(text.replace(/\D/g, '')), '$K');
        } else if (text.includes('%')) {
          animateCounter(num, parseInt(text), '%');
        } else {
          animateCounter(num, parseInt(text));
        }
      });
      statsObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

const heroStats = document.querySelector('.hero-stats');
if (heroStats) statsObserver.observe(heroStats);

/* ---- Application form ---- */
const applyForm = document.getElementById('applyForm');
const formSuccess = document.getElementById('formSuccess');

if (applyForm) {
  applyForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Basic validation
    const required = applyForm.querySelectorAll('[required]');
    let valid = true;
    required.forEach(field => {
      if (!field.value.trim()) {
        field.style.borderColor = '#e05252';
        valid = false;
      } else {
        field.style.borderColor = '';
      }
    });

    if (!valid) return;

    // Collect form data (in production: send to backend / CRM)
    const data = Object.fromEntries(new FormData(applyForm).entries());
    console.log('Application submitted:', data);

    // Show success state
    applyForm.style.display = 'none';
    formSuccess.style.display = 'block';

    // Scroll to success message
    formSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
  });
}
