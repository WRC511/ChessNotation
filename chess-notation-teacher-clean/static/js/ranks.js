document.addEventListener('DOMContentLoaded', () => {
    // Generate boards for both White and Black perspectives
    generateChessboard('white-perspective-board', 'white');
    generateChessboard('black-perspective-board', 'black');
});

function generateChessboard(containerId, perspective) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Create board container
    const boardContainer = document.createElement('div');
    boardContainer.className = 'board-container';

    // Create rank labels container
    const rankLabels = document.createElement('div');
    rankLabels.className = 'rank-labels';

    // Create squares container
    const squares = document.createElement('div');
    squares.className = 'squares';

    // Generate rank numbers based on perspective
    const ranks = perspective === 'white' 
        ? Array.from({length: 8}, (_, i) => 8 - i)  // White: 8 to 1 from top
        : Array.from({length: 8}, (_, i) => i + 1); // Black: 1 to 8 from top

    // Add rank labels
    ranks.forEach(rank => {
        const label = document.createElement('div');
        label.className = 'rank-label';
        label.textContent = rank;
        rankLabels.appendChild(label);
    });

    // Generate squares
    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            const square = document.createElement('div');
            square.className = `square ${(row + col) % 2 === 0 ? 'light' : 'dark'}`;
            squares.appendChild(square);
        }
    }

    // Assemble the board
    boardContainer.appendChild(rankLabels);
    boardContainer.appendChild(squares);
    container.appendChild(boardContainer);
}

// Practice functionality
document.querySelectorAll('.reveal-button').forEach(button => {
    button.addEventListener('click', () => {
        const answer = button.nextElementSibling;
        if (answer && answer.classList.contains('answer')) {
            answer.style.display = answer.style.display === 'none' ? 'block' : 'none';
            button.textContent = answer.style.display === 'none' ? 'Show Answer' : 'Hide Answer';
        }
    });
}); 