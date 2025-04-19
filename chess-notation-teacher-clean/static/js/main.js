// Track page visits
$(document).ready(function() {
    // Send page visit data to server
    $.ajax({
        url: '/track',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            page_name: window.location.pathname,
            timestamp: new Date().toISOString()
        })
    });
});

// Quiz functionality
function initQuiz() {
    $('.quiz-option').click(function() {
        $('.quiz-option').removeClass('selected');
        $(this).addClass('selected');
    });

    $('#submit-answer').click(function() {
        const selected = $('.quiz-option.selected');
        if (selected.length === 0) {
            alert('Please select an answer');
            return;
        }
        
        $('#quiz-form').submit();
    });
}

// Chessboard functionality
function createChessboard(containerId, perspective = 'white') {
    const container = document.getElementById(containerId);
    if (!container) return;

    const board = document.createElement('div');
    board.className = 'chessboard';
    
    const files = perspective === 'white' ? 'abcdefgh' : 'hgfedcba';
    const ranks = perspective === 'white' ? '87654321' : '12345678';

    for (let rank = 0; rank < 8; rank++) {
        for (let file = 0; file < 8; file++) {
            const square = document.createElement('div');
            square.className = `square ${(rank + file) % 2 === 0 ? 'white' : 'black'}`;
            
            // Add file label on last rank
            if (rank === 7) {
                const fileLabel = document.createElement('span');
                fileLabel.className = 'notation-label file-label';
                fileLabel.textContent = files[file];
                square.appendChild(fileLabel);
            }
            
            // Add rank label on first file
            if (file === 0) {
                const rankLabel = document.createElement('span');
                rankLabel.className = 'notation-label rank-label';
                rankLabel.textContent = ranks[rank];
                square.appendChild(rankLabel);
            }
            
            board.appendChild(square);
        }
    }
    
    container.appendChild(board);
}

// Progress tracking
function updateProgress(current, total) {
    const container = document.querySelector('.progress-indicator');
    if (!container) return;
    
    container.innerHTML = '';
    for (let i = 1; i <= total; i++) {
        const dot = document.createElement('div');
        dot.className = `progress-dot ${i <= current ? 'active' : ''}`;
        container.appendChild(dot);
    }
}

// Navigation
function setupNavigation() {
    const backButton = document.querySelector('.nav-back');
    if (backButton) {
        backButton.addEventListener('click', () => {
            window.history.back();
        });
    }
} 