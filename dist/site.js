// High Quality Interactive JavaScript for Meryem El Osmani Portfolio

// 1. Mouse Spotlight Tracker
window.addEventListener('mousemove', (e) => {
  document.body.style.setProperty('--mouse-x', `${e.clientX}px`);
  document.body.style.setProperty('--mouse-y', `${e.clientY}px`);
});

// 2. Language Switcher Engine
function getInitialLanguage() {
  const urlParams = new URLSearchParams(window.location.search);
  const langParam = urlParams.get('lang');
  if (langParam === 'en' || langParam === 'fr') return langParam;
  
  if (window.location.hash === '#en') return 'en';
  if (window.location.hash === '#fr') return 'fr';
  
  try {
    const saved = localStorage.getItem('portfolio_lang');
    if (saved === 'en' || saved === 'fr') return saved;
  } catch (e) {}
  
  return 'fr'; // default to French
}

function updateProjectCount() {
  const lang = document.documentElement.lang || 'fr';
  const label = lang === 'en' ? 'projects' : 'projets';
  const countEl = document.getElementById('project-count');
  if (!countEl) return;
  
  const visible = document.querySelectorAll('.project:not([hidden])').length;
  countEl.textContent = `${visible} ${label}`;
}

function setLanguage(lang) {
  if (lang !== 'fr' && lang !== 'en') return;
  
  document.documentElement.lang = lang;
  try {
    localStorage.setItem('portfolio_lang', lang);
  } catch (e) {}

  // Update active state on toggle buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    const isActive = btn.dataset.lang === lang;
    btn.classList.toggle('active', isActive);
    btn.setAttribute('aria-pressed', String(isActive));
  });

  // Update page title & meta description
  if (lang === 'en') {
    document.title = 'Meryem El Osmani — AI, Data & Software Engineer';
    const meta = document.querySelector('meta[name="description"]');
    if (meta) {
      meta.setAttribute('content', 'Meryem El Osmani: AI master’s student, developer and internship team leader. I build applications, explore models and turn business problems into practical solutions.');
    }
    const headerCv = document.getElementById('headerCvBtn');
    if (headerCv) headerCv.setAttribute('href', 'Meryem_El_Osmani_CV_EN.pdf');
    const heroCv = document.getElementById('heroCvBtn');
    if (heroCv) heroCv.setAttribute('href', 'Meryem_El_Osmani_CV_EN.pdf');
    const cvOpen = document.getElementById('cvOpenTabBtn');
    if (cvOpen) cvOpen.setAttribute('href', 'Meryem_El_Osmani_CV_EN.pdf');
    const cardEn = document.getElementById('cvCardEn');
    const cardFr = document.getElementById('cvCardFr');
    if (cardEn) cardEn.classList.add('active-card');
    if (cardFr) cardFr.classList.remove('active-card');
  } else {
    document.title = 'Meryem El Osmani — Ingénieure IA, Data & Logiciel';
    const meta = document.querySelector('meta[name="description"]');
    if (meta) {
      meta.setAttribute('content', 'Meryem El Osmani. Étudiante en master IA, développeuse et team leader en stage. Je construis des applications, explore des modèles et transforme des problèmes métier en solutions concrètes.');
    }
    const headerCv = document.getElementById('headerCvBtn');
    if (headerCv) headerCv.setAttribute('href', 'Meryem_El_Osmani_CV_FR.pdf');
    const heroCv = document.getElementById('heroCvBtn');
    if (heroCv) heroCv.setAttribute('href', 'Meryem_El_Osmani_CV_FR.pdf');
    const cvOpen = document.getElementById('cvOpenTabBtn');
    if (cvOpen) cvOpen.setAttribute('href', 'Meryem_El_Osmani_CV_FR.pdf');
    const cardEn = document.getElementById('cvCardEn');
    const cardFr = document.getElementById('cvCardFr');
    if (cardFr) cardFr.classList.add('active-card');
    if (cardEn) cardEn.classList.remove('active-card');
  }

  updateProjectCount();
}

// 3. Category Filtering
const filterButtons = document.querySelectorAll('.filters-wrapper button');
const cards = document.querySelectorAll('.project');

filterButtons.forEach(button => {
  button.addEventListener('click', () => {
    const selected = button.dataset.filter;
    filterButtons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    
    cards.forEach(card => {
      const isHidden = selected !== 'all' && card.dataset.category !== selected;
      card.hidden = isHidden;
      
      if (!isHidden) {
        card.classList.remove('visible');
        void card.offsetWidth; // Force reflow
        card.classList.add('visible');
      } else {
        card.classList.remove('visible');
      }
    });
    
    updateProjectCount();
  });
});

// Setup Language Switcher Button Events
document.querySelectorAll('.lang-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    setLanguage(btn.dataset.lang);
  });
});

// 4. Scroll Reveal Animations
const observerOptions = {
  root: null,
  rootMargin: '0px',
  threshold: 0.08
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

// 5. Initialize on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  // Set initial language
  const initialLang = getInitialLanguage();
  setLanguage(initialLang);

  // Initialize reveal animations
  const elementsToReveal = document.querySelectorAll(
    '.project, .expertise-card, .timeline-item, .education-item, .identity-card, .role-card, .heading, .spotlight-card, .proof-card, .certificates-box'
  );
  
  elementsToReveal.forEach((el, index) => {
    el.classList.add('reveal');
    el.style.transitionDelay = `${(index % 4) * 0.06}s`; 
    observer.observe(el);
  });

  // 3D Tilt on Identity Card
  const idCard = document.querySelector('.identity-card');
  if (idCard) {
    idCard.addEventListener('mousemove', (e) => {
      const rect = idCard.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      idCard.style.transform = `perspective(1000px) rotateY(${x * 0.035}deg) rotateX(${-y * 0.035}deg) translateY(-6px)`;
    });
    idCard.addEventListener('mouseleave', () => {
      idCard.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateY(0px)';
    });
  }

  // Copy Email to Clipboard
  const copyBtn = document.getElementById('copyEmailBtn');
  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      const email = 'maryamelosmani@gmail.com';
      navigator.clipboard.writeText(email).then(() => {
        const lang = document.documentElement.lang || 'fr';
        const copiedMsg = lang === 'en' ? '✓ Copied to clipboard!' : '✓ E-mail copié !';
        const originalHTML = copyBtn.innerHTML;
        copyBtn.classList.add('copied');
        copyBtn.innerHTML = `<span>${copiedMsg}</span>`;
        setTimeout(() => {
          copyBtn.classList.remove('copied');
          copyBtn.innerHTML = originalHTML;
        }, 2200);
      });
    });
  }

  // Case Study Modal Open / Close Handlers (Section 11)
  document.querySelectorAll('.open-case-study').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const caseId = btn.dataset.case;
      const modal = document.getElementById(`modal-${caseId}`);
      if (modal) {
        modal.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  document.querySelectorAll('.close-case-study').forEach(el => {
    el.addEventListener('click', () => {
      document.querySelectorAll('.case-study-modal.open').forEach(modal => {
        modal.classList.remove('open');
      });
      document.body.style.overflow = '';
    });
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.case-study-modal.open').forEach(modal => {
        modal.classList.remove('open');
      });
      document.body.style.overflow = '';
    }
  });

  // Smooth Project Jump with Card Glow Highlight
  document.querySelectorAll('.project-jump').forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'center' });
          target.classList.remove('highlight-card');
          void target.offsetWidth;
          target.classList.add('highlight-card');
          setTimeout(() => target.classList.remove('highlight-card'), 2200);
        }
      }
    });
  });
});

