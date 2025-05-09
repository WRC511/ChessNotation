# ChessNotation
An application that teaches algebraic notation in Chess within 10 minutes.

## Setup and Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation Steps
1. Clone or download this repository to your local machine
2. Navigate to the project directory in your terminal
3. Install the required dependencies:
   ```bash
   pip install flask
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your web browser and go to `http://localhost:5000`

### Project Structure
The project is organized as follows:
```
ChessNotation/
├── Chess_App/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   ├── app.py
│   ├── lessons.json
│   ├── user_activity.log
│   └── user_data.json
├── LICENSE
└── README.md
```

## File Descriptions

1. app.py
- Main Flask application file that serves as the backend controller
- Defines all lesson data and structure
- Handles routing for different pages (/home, /learn, /quiz)
- Manages user activity logging
- Controls lesson progression

2. templates/layout.html
- Base template that provides the common structure for all pages
- Contains the navigation bar
- Loads all necessary CSS and JavaScript dependencies
- Provides consistent branding and layout
- Integrates external libraries (Bootstrap, jQuery, Chessboard.js)

3. templates/home.html
- Landing page that introduces users to the application
- Displays main learning sections in a clear, minimal design
- Highlights the starting point with "Start Here" arrow
- Shows clear progression path

4. templates/lesson.html
- Template for all lesson pages
- Displays interactive chessboards
- Shows lesson content and explanations
- Presents practice questions
- Handles different lesson types (board, pieces, moves)

5. static/css/style.css
- Custom styling for the application
- Defines layout and appearance of all components
- Handles responsive design
- Styles interactive elements
- Ensures consistent visual design

6. static/js/lesson.js
- Handles client-side interactivity
- Initializes and manages chessboards
- Handles practice question interactions
- Manages move demonstrations with arrows
- Logs user activity

7. user_activity.log
- Logs user interactions and activity within the application
- Records timestamps of user actions
- Tracks which lessons users visit
- Stores interaction data in JSON format

8. user_data.json
- Stores persistent user-related data
- Maintains user progress data
- Stores user preferences and settings
- Provides a simple database-like storage solution

9. lessons.json
- Contains all lesson content and structure
- Stores lesson text, examples, and practice questions
- Defines the learning path and progression
- Contains chess positions and moves for demonstrations

