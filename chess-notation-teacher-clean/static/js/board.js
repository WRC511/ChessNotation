document.addEventListener('DOMContentLoaded', () => {
    const files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

    function generateChessboard(boardId, isWhitePerspective) {
        const chessboard = document.getElementById(boardId);
        if (!chessboard) return;

        // Clear any existing content
        chessboard.innerHTML = '';

        // Create squares
        for (let rank = 0; rank < 8; rank++) {
            for (let file = 0; file < 8; file++) {
                const square = document.createElement('div');
                square.className = `square ${(rank + file) % 2 === 0 ? 'white' : 'black'}`;
                chessboard.appendChild(square);
            }
        }
    }

    function addFileNotation(notationId, isWhitePerspective) {
        const notationRow = document.getElementById(notationId);
        if (!notationRow) return;

        notationRow.innerHTML = '';
        const displayFiles = isWhitePerspective ? files : [...files].reverse();
        displayFiles.forEach(file => {
            const notation = document.createElement('div');
            notation.className = 'file-notation';
            notation.textContent = file;
            notationRow.appendChild(notation);
        });
    }

    // Initialize boards
    if (document.getElementById('white-board')) {
        // Generate boards
        generateChessboard('white-board', true);
        generateChessboard('black-board', false);

        // Add file notation if we're on the files page
        if (document.getElementById('white-notation')) {
            addFileNotation('white-notation', true);
            addFileNotation('black-notation', false);
        }
    }

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

function setupFilesPage() {
    // Generate chessboards with only file notation
    generateChessboard('white', 'white-notation', true, false);
    generateChessboard('black', 'black-notation', true, false);
    
    // Add event listeners for practice questions
    setupPracticeQuestions();
}

function setupRanksPage() {
    // Generate chessboards with both file and rank notation
    generateChessboard('white', 'white-notation', true, true);
    generateChessboard('black', 'black-notation', true, true);
    
    // Add event listeners for practice questions
    setupPracticeQuestions();
}

function generateChessboard(perspective, notationId, showFiles = true, showRanks = true) {
    // Find the correct board container
    const boards = document.querySelectorAll('.board');
    const board = Array.from(boards).find(board => 
        board.querySelector('h3').textContent.includes(perspective === 'white' ? "White's" : "Black's")
    );
    
    if (!board) {
        console.error('Board not found for perspective:', perspective);
        return;
    }

    const chessboard = board.querySelector('.chessboard');
    const notationRow = board.querySelector('.notation-row');
    if (!chessboard || !notationRow) {
        console.error('Chessboard container or notation row not found');
        return;
    }

    const files = perspective === 'white' ? ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] : ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'];
    const ranks = [1, 2, 3, 4, 5, 6, 7, 8];
    
    // Clear any existing content
    chessboard.innerHTML = '';
    notationRow.innerHTML = '';
    
    // Create squares
    for (let i = ranks.length - 1; i >= 0; i--) {
        for (let j = 0; j < files.length; j++) {
            const square = document.createElement('div');
            square.className = `square ${(i + j) % 2 === 0 ? 'white' : 'black'}`;
            square.dataset.position = `${files[j]}${ranks[i]}`;
            chessboard.appendChild(square);
        }
    }
    
    // Add file notation below the board
    files.forEach(file => {
        const notation = document.createElement('div');
        notation.className = 'file-notation';
        notation.textContent = file;
        notationRow.appendChild(notation);
    });
    
    // Add rank labels (leftmost column)
    if (showRanks) {
        const squares = chessboard.querySelectorAll('.square');
        const displayRanks = perspective === 'white' ? ranks : [...ranks].reverse();
        for (let i = 0; i < ranks.length; i++) {
            const square = squares[i * files.length];
            const label = document.createElement('div');
            label.className = 'notation rank-label';
            label.textContent = displayRanks[ranks.length - 1 - i];
            square.appendChild(label);
        }
    }
}

function setupRevealButtons() {
    const revealButtons = document.querySelectorAll('.reveal-button');
    
    revealButtons.forEach(button => {
        button.addEventListener('click', () => {
            const card = button.closest('.explanation-card');
            const title = card.querySelector('h3').textContent;
            
            if (title.includes('Files')) {
                revealFiles();
            } else if (title.includes('Ranks')) {
                revealRanks();
            }
            
            // Disable button after first click
            button.disabled = true;
            button.style.opacity = '0.5';
        });
    });
}

function revealFiles() {
    const files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
    const boards = document.querySelectorAll('.chessboard');
    
    boards.forEach(board => {
        const squares = board.querySelectorAll('.square');
        squares.forEach((square, index) => {
            if (index % 8 === 0) {
                const file = files[index / 8];
                square.textContent = file;
            }
        });
    });
}

function revealRanks() {
    const boards = document.querySelectorAll('.chessboard');
    
    boards.forEach((board, boardIndex) => {
        const squares = board.querySelectorAll('.square');
        squares.forEach((square, index) => {
            if (index < 8) {
                const rank = boardIndex === 0 ? 8 - index : index + 1;
                square.textContent = rank;
            }
        });
    });
}

function setupPracticeQuestions() {
    const revealButtons = document.querySelectorAll('.reveal-button');
    
    revealButtons.forEach(button => {
        button.addEventListener('click', () => {
            const answer = button.nextElementSibling;
            answer.classList.toggle('visible');
            button.textContent = answer.classList.contains('visible') ? 'Hide Answer' : 'Show Answer';
        });
    });
}

// Helper function to find elements by text content
Element.prototype.contains = function(text) {
    return this.textContent.includes(text);
}; 