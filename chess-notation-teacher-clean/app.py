from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from datetime import datetime
import json
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chess_notation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), nullable=False)
    page_name = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    data = db.Column(db.JSON)

class QuizResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), nullable=False)
    question_number = db.Column(db.Integer, nullable=False)
    user_answer = db.Column(db.String(100), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Create tables
with app.app_context():
    db.create_all()

# Load lesson data
def load_lessons():
    with open('static/data/lessons.json', 'r') as f:
        return json.load(f)

@app.route('/')
def home():
    if 'session_id' not in session:
        session['session_id'] = os.urandom(16).hex()
    return render_template('home.html')

@app.route('/learn/<int:lesson_number>')
def learn(lesson_number):
    try:
        # Load lesson data from JSON
        with open('static/data/lessons.json') as f:
            lessons = json.load(f)['lessons']
        
        if lesson_number < 1 or lesson_number > len(lessons):
            return redirect(url_for('home'))
        
        # Record page visit
        progress = UserProgress(
            session_id=session['session_id'],
            page_name=f'learn_{lesson_number}',
            data={'lesson_number': lesson_number}
        )
        db.session.add(progress)
        db.session.commit()
        
        return render_template('learn.html', 
                             lesson=lessons[lesson_number-1],
                             current_lesson=lesson_number,
                             total_lessons=len(lessons))
    except Exception as e:
        app.logger.error(f"Error loading lesson {lesson_number}: {str(e)}")
        return redirect(url_for('home'))

@app.route('/quiz/<int:question_number>', methods=['GET', 'POST'])
def quiz(question_number):
    with open('static/data/quiz.json') as f:
        quiz_data = json.load(f)
    
    if question_number < 1 or question_number > len(quiz_data):
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        correct_answer = quiz_data[question_number-1]['correct_answer']
        
        # Record quiz response
        response = QuizResponse(
            session_id=session['session_id'],
            question_number=question_number,
            user_answer=user_answer,
            is_correct=(user_answer == correct_answer)
        )
        db.session.add(response)
        db.session.commit()
        
        if question_number == len(quiz_data):
            return redirect(url_for('quiz_results'))
        return redirect(url_for('quiz', question_number=question_number+1))
    
    return render_template('quiz.html',
                         question=quiz_data[question_number-1],
                         current_question=question_number,
                         total_questions=len(quiz_data))

@app.route('/quiz/results')
def quiz_results():
    # Calculate quiz results
    responses = QuizResponse.query.filter_by(session_id=session['session_id']).all()
    total_questions = len(responses)
    correct_answers = sum(1 for r in responses if r.is_correct)
    score = (correct_answers / total_questions * 100) if total_questions > 0 else 0
    
    return render_template('quiz_results.html',
                         score=score,
                         correct_answers=correct_answers,
                         total_questions=total_questions)

@app.route('/track', methods=['POST'])
def track_progress():
    data = request.get_json()
    progress = UserProgress(
        session_id=session['session_id'],
        page_name=data.get('page_name'),
        data=data
    )
    db.session.add(progress)
    db.session.commit()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True) 