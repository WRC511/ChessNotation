from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from datetime import datetime

app = Flask(__name__)

lessons = [
    {
        'id': 1,
        'title': 'Learn the Board - Files',
        'type': 'board',
        'notation_type': 'files',
        'banner': 'Files are Vertical Columns. They are labeled from left to right, a - h for the white player, and h - a for the black player.',
        'practice_questions': [
            {
                'question': "How is White's leftmost file notated?",
                'answer': 'a'
            },
            {
                'question': "How is Black's leftmost file notated?",
                'answer': 'h'
            }
        ]
    },
    {
        'id': 2,
        'title': 'Learn the Board - Ranks',
        'type': 'board',
        'notation_type': 'ranks',
        'banner': 'Ranks are Horizontal Rows. They are labeled from bottom to top, 1 - 8 for the white player, and 8 - 1 for the black player.',
        'practice_questions': [
            {
                'question': 'What rank is 2 squares above White\'s 4th rank?',
                'answer': '6'
            },
            {
                'question': 'What rank is 2 squares above Black\'s 4th rank?',
                'answer': '2'
            }
        ]
    },
    {
        'id': 3,
        'title': 'Learn the Pieces',
        'type': 'pieces',
        'banner': 'Each piece has a unique CAPITAL letter notation, except pawns which use the square they move to.',
        'practice_questions': [
            {
                'question': 'What is the notation for a Knight?',
                'answer': 'N'
            },
            {
                'question': 'How do you notate the Pawn?',
                'answer': 'the file/rank of its square'
            }
        ]
    },
    {
        'id': 4,
        'title': 'Learn the Moves - Basic Movement',
        'type': 'moves',
        'banner': "Let's learn how to notate basic piece movements on the board.",
        'moves': [
            {
                'description': 'Pawn moves 2 squares forward',
                'start': 'e2',
                'end': 'e4',
                'notation': 'e4'
            }
        ],
        'practice_questions': [
            {
                'question': 'How would you notate a pawn moving from c2 to c4?',
                'answer': 'c4'
            }
        ]
    },
    {
        'id': 5,
        'title': 'Learn the Moves - Pawn Captures',
        'type': 'moves',
        'banner': 'When a pawn captures, we notate the starting file, then \'x\', then the destination square.',
        'moves': [
            {
                'description': 'Pawn captures diagonally',
                'start': 'd4',
                'end': 'e5',
                'notation': 'exf5',
                'notation_format': 'starting file x file/rank'
            }
        ],
        'practice_questions': [
            {
                'question': 'How would you notate a pawn on the d-file capturing on e5?',
                'answer': 'dxe5'
            }
        ]
    },
    {
        'id': 6,
        'title': 'Learn the Moves - Captures',
        'type': 'moves',
        'banner': 'Captures are notated with an \'x\' between the piece and the destination square.',
        'moves': [
            {
                'description': 'Bishop captures Knight',
                'start': 'c3',
                'end': 'e5',
                'notation': 'Bxe5'
            }
        ],
        'practice_questions': [
            {
                'question': 'How would you notate a Bishop capturing on g7?',
                'answer': 'Bxg7'
            }
        ]
    },
    {
        'id': 7,
        'title': 'Learn the Moves - Check',
        'type': 'moves',
        'banner': 'Check is notated with \'+\' at the end of the move.',
        'moves': [
            {
                'description': 'Queen gives check',
                'start': 'd1',
                'end': 'h5',
                'notation': 'Qh5+'
            }
        ],
        'practice_questions': [
            {
                'question': 'How would you notate a Queen giving check on f7?',
                'answer': 'Qf7+'
            }
        ]
    },
    {
        'id': 8,
        'title': 'Learn the Moves - Checkmate',
        'type': 'moves',
        'banner': 'Checkmate is notated with \'#\' at the end of the move.',
        'moves': [
            {
                'description': 'Queen delivers checkmate',
                'start': 'd1',
                'end': 'h7',
                'notation': 'Qh7#'
            }
        ],
        'practice_questions': [
            {
                'question': 'How would you notate a Queen giving checkmate on h7?',
                'answer': 'Qh7#'
            }
        ]
    }
]

quiz_questions = [
    {
        'index': 1,
        'question': "How would you write this move in algebraic notation? (White's move)",
        'options': ["Ng1-f3", "Nf3", "N1-f3", "Nf1-f3"],
        'correct': 1,
        'explanation': "The correct notation is Nf3. In algebraic notation, we don't need to specify the starting square when there's only one knight that can move to f3.",
        'startFen': "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        'move': {'from': 'g1', 'to': 'f3'}
    },
    {
        'index': 2,
        'question': "How would you write this move in algebraic notation? (Black's move)",
        'options': ["Nxc3", "Nf6xc3", "Nxc3+", "Nf6-c3"],
        'correct': 0,
        'explanation': "The correct notation is Nxc3. The 'x' indicates a capture, and we don't need to specify the starting square (d5) since there's only one knight that can capture on c3.",
        'startFen': "r1b1kb1r/ppp1p1pp/8/3n1n2/4P3/2B5/PPPP1PPP/RNBQK1NR b KQkq - 0 1",
        'move': {'from': 'd5', 'to': 'c3'}
    },
    {
        'index': 3,
        'question': "How would you write this move in algebraic notation? (White's move)",
        'options': ["Qd1-h5+", "Qh5", "Qh5+", "Qxh5+"],
        'correct': 2,
        'explanation': "The correct notation is Qh5+. The '+' indicates a check, and we don't need to specify the starting square since there's only one queen that can move to h5.",
        'startFen': "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2",
        'move': {'from': 'd1', 'to': 'h5'}
    },
    {
        'index': 4,
        'question': "How would you write this move in algebraic notation? (Black's move)",
        'options': ["e5xd4", "e5-d4", "exd4+", "exd4"],
        'correct': 3,
        'explanation': "The correct notation is exd4. When a pawn captures, we use the file letter of the pawn followed by 'x' and the destination square. We don't need to specify the starting rank.",
        'startFen': "rnbqkbnr/pppp1ppp/8/4p3/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 2",
        'move': {'from': 'e5', 'to': 'd4'}
    },
    {
        'index': 5,
        'question': "How would you write this move in algebraic notation? (White's move)",
        'options': ["e7-e8=Q", "e8=Q", "e8Q", "e7-e8Q"],
        'correct': 1,
        'explanation': "The correct notation is e8=Q. When a pawn promotes, we write the destination square followed by '=' and the piece it promotes to. We don't need to specify the starting square.",
        'startFen': "8/4P3/8/8/3k4/8/8/4K3 w - - 0 1",
        'move': {'from': 'e7', 'to': 'e8', 'promotion': 'q'}
    }
]

# Home route
@app.route('/')
def home():
    return render_template('home.html', lessons=lessons)

# Learning route: /learn/1, /learn/2, etc.
@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    if 1 <= lesson_id <= len(lessons):
        return render_template('lesson.html', 
                            lesson=lessons[lesson_id-1], 
                            lesson_id=lesson_id,
                            total_lessons=len(lessons))
    return 'Lesson not found', 404

# (Placeholder) Quiz route: will flesh out in next assignment
@app.route('/quiz')
def quiz():
    return render_template('quiz.html', quiz_questions=quiz_questions)

# (Placeholder) Quiz results route
@app.route('/results')
def results():
    return render_template('results.html')

# Endpoint to log user data (e.g. when entering a lesson)
@app.route('/log', methods=['POST'])
def log_event():
    data = request.get_json()
    data['timestamp'] = str(datetime.utcnow())
    
    try:
        with open('user_activity.log', 'a') as f:
            json.dump(data, f)
            f.write('\n')
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
