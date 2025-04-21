// Run once the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Initialize chessboards if they exist
  if (document.getElementById('white-board')) {
    const whiteBoard = Chessboard('white-board', {
      position: 'start',
      orientation: 'white',
      pieceTheme: 'https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png',
      showNotation: false
    });
  }

  if (document.getElementById('black-board')) {
    const blackBoard = Chessboard('black-board', {
      position: 'start',
      orientation: 'black',
      pieceTheme: 'https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png',
      showNotation: false
    });
  }

  if (document.getElementById('move-board')) {
    const moveBoard = Chessboard('move-board', {
      position: 'start',
      orientation: 'white',
      pieceTheme: 'https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png',
      showNotation: true
    });

    // Get move data from the page
    const moveDescription = document.querySelector('.move-description');
    if (moveDescription) {
      const start = moveDescription.dataset.start;
      const end = moveDescription.dataset.end;
      
      // Draw arrow from start to end square
      const arrow = document.createElement('div');
      arrow.className = 'move-arrow';
      
      // Calculate arrow position and rotation
      const startSquare = document.querySelector(`#move-board [data-square="${start}"]`);
      const endSquare = document.querySelector(`#move-board [data-square="${end}"]`);
      
      if (startSquare && endSquare) {
        const startRect = startSquare.getBoundingClientRect();
        const endRect = endSquare.getBoundingClientRect();
        
        const boardContainer = document.querySelector('.board-container');
        const boardRect = boardContainer.getBoundingClientRect();
        
        // Position arrow relative to the board container
        const startX = startRect.left + startRect.width / 2 - boardRect.left;
        const startY = startRect.top + startRect.height / 2 - boardRect.top;
        const endX = endRect.left + endRect.width / 2 - boardRect.left;
        const endY = endRect.top + endRect.height / 2 - boardRect.top;
        
        // Calculate arrow length and angle
        const dx = endX - startX;
        const dy = endY - startY;
        const length = Math.sqrt(dx * dx + dy * dy);
        const angle = Math.atan2(dy, dx) * 180 / Math.PI;
        
        // Style the arrow
        arrow.style.position = 'absolute';
        arrow.style.left = `${startX}px`;
        arrow.style.top = `${startY}px`;
        arrow.style.width = `${length}px`;
        arrow.style.height = '10px';
        arrow.style.transformOrigin = '0 50%';
        arrow.style.transform = `rotate(${angle}deg)`;
        arrow.style.backgroundColor = 'rgba(255, 0, 0, 0.7)';
        arrow.style.clipPath = 'polygon(0 35%, 85% 35%, 85% 0%, 100% 50%, 85% 100%, 85% 65%, 0 65%)';
        arrow.style.zIndex = '100';
        
        boardContainer.appendChild(arrow);
      }
    }
  }

  // Handle reveal answer buttons
  const revealButtons = document.querySelectorAll('.reveal-btn');
  revealButtons.forEach(button => {
    button.addEventListener('click', function() {
      // Get the answer from the data attribute
      const answer = this.getAttribute('data-answer');
      
      // Find the answer span that follows this button
      const answerSpan = this.nextElementSibling;
      
      if (answerSpan && answerSpan.classList.contains('answer')) {
        // Show the answer text
        answerSpan.textContent = answer;
        answerSpan.style.display = 'inline';
        
        // Add fade-in effect
        answerSpan.style.opacity = '0';
        setTimeout(() => {
          answerSpan.style.transition = 'opacity 0.5s ease-in-out';
          answerSpan.style.opacity = '1';
        }, 10);
        
        // Disable the button and update its appearance
        this.disabled = true;
        this.classList.remove('btn-outline-primary');
        this.classList.add('btn-secondary');
      }
    });
  });

  // Log page visit
  fetch('/log', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      event: 'page_view',
      lesson_id: document.querySelector('.progress-bar')?.getAttribute('aria-valuenow'),
      timestamp: new Date().toISOString()
    })
  }).catch(error => console.log('Error logging page visit:', error));
});
