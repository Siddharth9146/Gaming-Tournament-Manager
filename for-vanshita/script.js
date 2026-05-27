// ---------- Floating Hearts ----------
(function spawnHearts() {
  const layer = document.getElementById('heartsLayer');
  if (!layer) return;

  const symbols = ['❤', '♥', '\u{1F496}', '\u{1F49E}', '\u{1F90D}'];

  function spawn() {
    const heart = document.createElement('span');
    heart.className = 'heart';
    heart.textContent = symbols[Math.floor(Math.random() * symbols.length)];

    const size = 12 + Math.random() * 24;
    const duration = 8 + Math.random() * 9;
    const left = Math.random() * 100;
    const delay = Math.random() * 2;
    const hue = 330 + Math.random() * 25;

    heart.style.left = left + 'vw';
    heart.style.fontSize = size + 'px';
    heart.style.animationDuration = duration + 's';
    heart.style.animationDelay = delay + 's';
    heart.style.color = `hsl(${hue}, 80%, ${65 + Math.random() * 15}%)`;

    layer.appendChild(heart);

    setTimeout(() => heart.remove(), (duration + delay) * 1000 + 200);
  }

  // initial burst
  for (let i = 0; i < 8; i++) spawn();
  // ongoing spawn
  setInterval(spawn, 900);
})();

// ---------- Reveal on scroll ----------
(function revealOnScroll() {
  const items = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    items.forEach(el => el.classList.add('visible'));
    return;
  }

  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry, idx) => {
      if (entry.isIntersecting) {
        // small stagger based on position in viewport
        const el = entry.target;
        const delay = (idx % 6) * 80;
        setTimeout(() => el.classList.add('visible'), delay);
        io.unobserve(el);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

  items.forEach(el => io.observe(el));
})();

// ---------- Envelope open ----------
(function envelope() {
  const env = document.getElementById('envelope');
  const hint = document.getElementById('envelopeHint');
  if (!env) return;

  let opened = false;

  env.addEventListener('click', () => {
    opened = !opened;
    env.classList.toggle('open', opened);
    if (hint) {
      hint.textContent = opened ? 'tap to close' : 'click to open';
      hint.classList.toggle('hidden', false);
    }

    // burst of hearts on open
    if (opened) heartBurst(env);
  });
})();

// ---------- Heart burst (on envelope open) ----------
function heartBurst(originEl) {
  const rect = originEl.getBoundingClientRect();
  const layer = document.getElementById('heartsLayer');
  if (!layer) return;

  const cx = rect.left + rect.width / 2;
  const cy = rect.top + rect.height / 2;

  for (let i = 0; i < 18; i++) {
    const h = document.createElement('span');
    h.textContent = '❤';
    h.style.position = 'fixed';
    h.style.left = cx + 'px';
    h.style.top = cy + 'px';
    h.style.fontSize = (14 + Math.random() * 18) + 'px';
    h.style.color = `hsl(${330 + Math.random() * 25}, 80%, 65%)`;
    h.style.pointerEvents = 'none';
    h.style.transform = 'translate(-50%, -50%) scale(0.4)';
    h.style.transition = 'transform 1.2s cubic-bezier(.2,.8,.2,1), opacity 1.2s ease';
    h.style.zIndex = 50;

    layer.appendChild(h);

    const angle = (Math.PI * 2 * i) / 18 + Math.random() * 0.3;
    const distance = 80 + Math.random() * 140;
    const dx = Math.cos(angle) * distance;
    const dy = Math.sin(angle) * distance - 60;

    requestAnimationFrame(() => {
      h.style.transform = `translate(calc(-50% + ${dx}px), calc(-50% + ${dy}px)) scale(1)`;
      h.style.opacity = '0';
    });

    setTimeout(() => h.remove(), 1300);
  }
}
