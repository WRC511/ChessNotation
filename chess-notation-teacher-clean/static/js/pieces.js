document.addEventListener('DOMContentLoaded', () => {
    const pieces = [
        { name: 'King', symbol: '♔', notation: 'K' },
        { name: 'Queen', symbol: '♕', notation: 'Q' },
        { name: 'Rook', symbol: '♖', notation: 'R' },
        { name: 'Bishop', symbol: '♗', notation: 'B' },
        { name: 'Knight', symbol: '♘', notation: 'N' },
        { name: 'Pawn', symbol: '♙', notation: 'File + Rank' }
    ];

    // Generate piece cards
    const piecesGrid = document.querySelector('.pieces-grid');
    pieces.forEach(piece => {
        const card = document.createElement('div');
        card.className = 'piece-card';
        card.innerHTML = `
            <div class="piece-symbol">${piece.symbol}</div>
            <div class="piece-name">${piece.name}</div>
            <div class="piece-notation">${piece.notation}</div>
        `;
        piecesGrid.appendChild(card);
    });

    // Practice questions
    const practiceQuestions = [
        {
            question: "Which piece uses 'N' instead of 'K'?",
            answer: "Knight"
        },
        {
            question: "How do we write a pawn move?",
            answer: "Just write the square it moves to (example: e4)"
        }
    ];

    const practiceSection = document.querySelector('.practice-section');
    practiceQuestions.forEach((q, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.className = 'practice-question';
        questionDiv.innerHTML = `
            <div class="question-text">${q.question}</div>
            <div class="answer-section">
                <button class="reveal-button" onclick="revealAnswer(${index})">Show Answer</button>
                <div class="answer" id="answer-${index}">${q.answer}</div>
            </div>
        `;
        practiceSection.appendChild(questionDiv);
    });

    // Add hover effects for piece cards
    const pieceCards = document.querySelectorAll('.piece-card');
    pieceCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-5px)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
});

function revealAnswer(index) {
    const answer = document.getElementById(`answer-${index}`);
    answer.classList.toggle('visible');
    const button = answer.previousElementSibling;
    button.textContent = answer.classList.contains('visible') ? 'Hide Answer' : 'Show Answer';
} 