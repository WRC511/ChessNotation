document.addEventListener('DOMContentLoaded', () => {
    const files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
    const ranks = ['8', '7', '6', '5', '4', '3', '2', '1'];

    function generateChessboard(boardId, isWhitePerspective) {
        const chessboard = document.getElementById(boardId);
        chessboard.innerHTML = '';

        const displayFiles = isWhitePerspective ? files : [...files].reverse();

        for (let rank = 0; rank < 8; rank++) {
            for (let file = 0; file < 8; file++) {
                const square = document.createElement('div');
                square.className = `square ${(rank + file) % 2 === 0 ? 'white' : 'black'}`;

                // Add file labels on every rank for emphasis
                const fileLabel = document.createElement('span');
                fileLabel.className = 'file-label';
                fileLabel.textContent = displayFiles[file];
                square.appendChild(fileLabel);

                chessboard.appendChild(square);
            }
        }
    }

    // Initialize both boards
    generateChessboard('white-board', true);
    generateChessboard('black-board', false);

    // Handle practice questions
    const revealButtons = document.querySelectorAll('.reveal-button');
    revealButtons.forEach(button => {
        button.addEventListener('click', () => {
            const answer = button.nextElementSibling;
            answer.classList.toggle('visible');
            button.textContent = answer.classList.contains('visible') ? 'Hide Answer' : 'Show Answer';
        });
    });
}); 