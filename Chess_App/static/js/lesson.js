// static/js/lesson.js
document.addEventListener("DOMContentLoaded", () => {
  // ─── 1) WHITE BOARD ─────────────────────────────────────────────
  if (document.getElementById('white-board')) {
    Chessboard('white-board', {
      position: 'start',
      orientation: 'white',
      pieceTheme: 'https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png',
      showNotation: false
    });
  }

  // ─── 2) BLACK BOARD ─────────────────────────────────────────────
  if (document.getElementById('black-board')) {
    Chessboard('black-board', {
      position: 'start',
      orientation: 'black',
      pieceTheme: 'https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png',
      showNotation: false
    });
  }

  // ─── 3) MOVE BOARD + LOOP ────────────────────────────────────────
  const el = document.getElementById('move-board');
  if (el) {
    // read your data-attributes
    const startFen      = el.dataset.startFen;
    const endFen        = el.dataset.endFen;
    const fromSq        = el.dataset.from;
    const toSq          = el.dataset.to;
    const cycleInterval = 2000;  // total time per cycle (ms)
    const arrowDrawTime =  500;  // how long the arrow “grows” (ms)
    const slideTime     =  400;  // Chessboard.js moveSpeed (ms)

    // initialize at start position
    const board = Chessboard('move-board', {
      position:    startFen,
      orientation: 'white',
      showNotation:true,
      moveSpeed:   slideTime,
      snapSpeed:   150,
      pieceTheme:  'https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png'
    });

    // draw one arrow instantly (returns the arrow DIV so you can fade / remove it)
    function drawArrow() {
      const s = el.querySelector(`[data-square="${fromSq}"]`);
      const e = el.querySelector(`[data-square="${toSq}"]`);
      if (!s || !e) return null;

      const hostRect = el.parentElement.getBoundingClientRect();
      const a = s.getBoundingClientRect();
      const b = e.getBoundingClientRect();
      const x1 = a.left + a.width/2  - hostRect.left;
      const y1 = a.top  + a.height/2 - hostRect.top;
      const x2 = b.left + b.width/2  - hostRect.left;
      const y2 = b.top  + b.height/2 - hostRect.top;
      const dx = x2 - x1, dy = y2 - y1;
      const length = Math.hypot(dx, dy);
      const angle  = Math.atan2(dy, dx) * 180 / Math.PI;

      const arrow = document.createElement('div');
      arrow.className = 'move-arrow';
      arrow.style.width     = `${length}px`;
      arrow.style.left      = `${x1}px`;
      arrow.style.top       = `${y1}px`;
      arrow.style.transform = `rotate(${angle}deg) scaleX(0)`;
      el.parentElement.appendChild(arrow);

      // trigger the CSS animation
      requestAnimationFrame(() => {
        arrow.style.opacity   = '1';
        arrow.style.transform = `rotate(${angle}deg) scaleX(1)`;
      });

      return arrow;
    }

    // build a simple toggle loop
    let showingMove = false;
    setInterval(() => {
      if (!showingMove) {
        // → reset board, clear any old arrows
        board.position(startFen, false);
        document.querySelectorAll('.move-arrow').forEach(a => a.remove());

        // → draw the arrow, then slide the piece
        const arrow = drawArrow();
        if (arrow) {
          setTimeout(() => {
            board.position(endFen, true);
          }, arrowDrawTime);
        } else {
          // fallback: no arrow? just slide
          board.position(endFen, true);
        }

      } else {
        // ← clear arrow & reset board back
        document.querySelectorAll('.move-arrow').forEach(a => a.remove());
        board.position(startFen, true);
      }

      showingMove = !showingMove;
    }, cycleInterval);
  }

  // ─── 4) PRACTICE “REVEAL” BUTTONS ─────────────────────────────────
  document.querySelectorAll('.reveal-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const ans = this.dataset.answer;
      const sp  = this.nextElementSibling;
      sp.textContent = ans;
      sp.style.display = 'inline';
      sp.style.opacity = '0';
      setTimeout(() => {
        sp.style.transition = 'opacity 0.5s ease-in';
        sp.style.opacity = '1';
      }, 10);
      this.disabled = true;
      this.classList.replace('btn-outline-primary','btn-secondary');
    });
  });

  // ─── 5) LOGGING ───────────────────────────────────────────────────
  fetch('/log', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({
      event: 'page_view',
      lesson_id: document.querySelector('.progress-bar')?.getAttribute('aria-valuenow'),
      timestamp: new Date().toISOString()
    })
  }).catch(e => console.warn('Log error:', e));
});