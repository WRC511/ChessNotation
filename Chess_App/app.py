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
        ],
        'fen_start': '8/8/8/8/8/8/8/8 w - - 0 1',
        'fen_end': '8/8/8/8/8/8/8/8 w - - 0 1'
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
        ],
        'fen_start': '8/8/8/8/8/8/8/8 w - - 0 1',
        'fen_end': '8/8/8/8/8/8/8/8 w - - 0 1'
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
        ],
        'fen_start': '8/8/8/8/8/8/8/8 w - - 0 1',
        'fen_end': '8/8/8/8/8/8/8/8 w - - 0 1'
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
                'question': 'How would you notate a pawn moving from e2 to e4?',
                'answer': 'e4'
            }
        ],
        'fen_start': 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
        'fen_end': 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1'
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
        ],
        'fen_start': 'rnbqkbnr/pppp1ppp/8/4p3/3P4/8/PPP1PPPP/RNBQKBNR w KQkq e6 0 1',
        'fen_end': 'rnbqkbnr/pppp1ppp/8/4P3/8/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1'
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
                'question': 'How would you notate the Bishop capturing the Knight on e5?',
                'answer': 'Bxe5'
            }
        ],
        'fen_start': 'r2qkbnr/p1ppp1p1/bp5p/4n3/1P3p2/2BP4/P1P1PPPP/RN1QKBNR w KQkq - 0 1',
        'fen_end': 'r2qkbnr/p1ppp1p1/bp5p/4B3/1P3p2/3P4/P1P1PPPP/RN1QKBNR b KQkq - 0 1'
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
                'end': 'd7',
                'notation': 'Qd7+'
            }
        ],
        'practice_questions': [
            {
                'question': 'How would you notate a Queen giving check on d7?',
                'answer': 'Qd7+'
            }
        ],
        'fen_start': 'rnb1kb1r/pp1p1ppp/2p2n2/4P3/2B5/7N/PPP3PP/RNBQK2R b KQkq - 0 1',
        'fen_end': 'rnb1kb1r/pp1Q1ppp/2p2n2/4P3/2B5/7N/PPP3PP/RNB1K2R b KQkq - 0 1'
    },
    {
        'id': 8,
        'title': 'Learn the Moves - Checkmate',
        'type': 'moves',
        'banner': 'Checkmate is notated with \'#\' at the end of the move.',
        'moves': [
            {
                'description': 'Queen delivers checkmate',
                'start': 'f3',
                'end': 'f7',
                'notation': 'Qxf7#'
            }
        ],
        'practice_questions': [
            {
                'question': 'How would you notate a Queen giving checkmate on f7?',
                'answer': 'Qf7#'
            }
        ],
        'fen_start': 'r1bqkb1r/p1pp1ppp/nP5n/4p3/2B1P3/5Q2/PP1P1PPP/RNB1K1NR b KQkq - 0 1',
        'fen_end': 'r1bqkb1r/p1pp1Qpp/nP5n/4p3/2B1P3/8/PP1P1PPP/RNB1K1NR b KQkq - 0 1'        
    }
]

quiz_questions = [
        {
        'index': 1,
        'question': "This is an example of a: ",
        'options': ["Rank", "File"],
        'correct': 1,
        'explanation': "The letter 'a' represents a file in chess notation. Files are the horizontal columns on the chessboard, labeled from a to h from left to right from White's perspective.",
        'startFen': "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        'move': None,
        'highlight': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
        'animated': False,
        'lesson_id': 1
    },
    {
        'index': 2,
        'question': "This is an example of a:",
        'options': ["Rank", "File"],
        'correct': 0,
        'explanation': "The number '4' represents a rank in chess notation. Ranks are the horizontal rows on the chessboard, labeled from 1 to 8 from bottom to top from White's perspective.",
        'startFen': "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        'move': None,
        'highlight': ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
        'animated': False,
        'lesson_id': 2
    },
    {
        'index': 3,
        'question': "How would you write this move in algebraic notation? (White's move)",
        'options': ["Ng1-f3", "Nf3", "N1-f3", "Nf1-f3"],
        'correct': 1,
        'explanation': "The correct notation is Nf3. In algebraic notation, we don't need to specify the starting square when there's only one knight that can move to f3.",
        'startFen': "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        'move': {'from': 'g1', 'to': 'f3'},
        'animated': True,
        'lesson_id': 3
    },
    {
        'index': 4,
        'question': "How would you write this move in algebraic notation? (Black's move)",
        'options': ["Nxc3", "Nf6xc3", "Nxc3+", "Nf6-c3"],
        'correct': 0,
        'explanation': "The correct notation is Nxc3. The 'x' indicates a capture, and we don't need to specify the starting square (d5) since there's only one knight that can capture on c3.",
        'startFen': "r1b1kb1r/ppp1p1pp/8/3n1n2/4P3/2B5/PPPP1PPP/RNBQK1NR b KQkq - 0 1",
        'move': {'from': 'd5', 'to': 'c3'},
        'animated': True,
        'lesson_id': 6
    },
    {
        'index': 5,
        'question': "How would you write this move in algebraic notation? (White's move)",
        'options': ["Qd1-h5+", "Qh5", "Qh5+", "Qxh5+"],
        'correct': 1,
        'explanation': "The correct notation is Qh5. The '+' would indicate a check, and we don't need to specify the starting square since there's only one queen that can move to h5.",
        'startFen': "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2",
        'move': {'from': 'd1', 'to': 'h5'},
        'animated': True,
        'lesson_id': 7
    },
    {
        'index': 6,
        'question': "How would you write this move in algebraic notation? (Black's move)",
        'options': ["e5xd4", "e5-d4", "exd4+", "exd4"],
        'correct': 3,
        'explanation': "The correct notation is exd4. When a pawn captures, we use the file letter of the pawn followed by 'x' and the destination square. We don't need to specify the starting rank.",
        'startFen': "rnbqkbnr/pppp1ppp/8/4p3/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 2",
        'move': {'from': 'e5', 'to': 'd4'},
        'animated': True,
        'lesson_id': 5
    },
    {
        'index': 7,
        'question': "What is the correct notation for a Bishop moving to d3? (White's move)",
        'options': ["Bd3", "Bxd3", "BD3", "d3"],
        'correct': 0,
        'explanation': "The correct notation is Bd3. For pieces other than pawns, we use the piece's letter (B for Bishop) followed by the destination square.",
        'startFen': "rnbqkbnr/pppp1ppp/5n2/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 1 2",
        'move': {'from': 'f1', 'to': 'd3'},
        'animated': True,
        'lesson_id': 3
    },
    {
        'index': 8,
        'question': "What is the name of this square?",
        'options': ["D3", "d3", "3d", "d"],
        'correct': 1,
        'explanation': "The correct notation is d3. For board locations, we use the file letter in lower case followed by the rank number.",
        'startFen': "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        'move': None,
        'highlight': ['d3'],
        'animated': False,
        'lesson_id': 1
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

@app.route('/quiz')
@app.route('/quiz/<int:question_id>')
def quiz(question_id=None):
    return render_template('quiz.html', 
                         quiz_questions=quiz_questions, 
                         lessons=lessons,
                         current_question=question_id)

@app.route('/lesson_content/<int:lesson_id>')
def lesson_content(lesson_id):
    if 1 <= lesson_id <= len(lessons):
        lesson = lessons[lesson_id-1]
        # Prepare the lesson data for the modal
        lesson_data = {
            'title': lesson['title'],
            'content': lesson['banner'],
            'board_fen': 'start' if lesson['type'] in ['board', 'moves'] else None,
            'practice_questions': lesson['practice_questions']
        }
        return jsonify(lesson_data)
    return jsonify({'error': 'Lesson not found'}), 404

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
