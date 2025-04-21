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
                'start': 'e4',
                'end': 'f5',
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
@app.route('/quiz/<int:question_id>')
def quiz(question_id):
    return render_template('quiz.html', question_id=question_id)

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
