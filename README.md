# ChessNotation
An application that teaches algebraic notation in Chess within 10 minutes.

Current Roles
<br>
Role 1: Learning Module Developer (UI Focus)<br>
Assigned To: Nick<br>
Role 2: Learning Data Architect & Tester<br>
Assigned To: William <br>
Role 3: Quiz Module Developer (UI Focus)<br>
Assigned To: Ed <br>
Role 4: Quiz Data Architect & Tester<br>
Assigned To: Edward<br>
<hr>
FILE DESCRIPTIONS:
1. `app.py`
- **Purpose**: Main Flask application file that serves as the backend controller
- **Key Functions**:
  - Defines all lesson data and structure
  - Handles routing for different pages (/home, /learn, /quiz)
  - Manages user activity logging
  - Controls lesson progression
- **Assignment Requirements Met**:
  - Implements a structured learning path
  - Manages state and progression through lessons
  - Handles user interactions and navigation
  - Provides data for interactive learning content

2. `templates/layout.html`
- **Purpose**: Base template that provides the common structure for all pages
- **Key Features**:
  - Contains the navigation bar
  - Loads all necessary CSS and JavaScript dependencies
  - Provides consistent branding and layout
- **Assignment Requirements Met**:
  - Ensures consistent user interface across the application
  - Implements responsive design principles
  - Integrates required external libraries (Bootstrap, jQuery, Chessboard.js)

3. `templates/home.html`
- **Purpose**: Landing page that introduces users to the application
- **Key Features**:
  - Displays main learning sections in a clear, minimal design
  - Highlights the starting point with "Start Here" arrow
  - Shows clear progression path
- **Assignment Requirements Met**:
  - Provides clear user onboarding
  - Implements intuitive navigation
  - Uses visual cues to guide users

4. `templates/lesson.html`
- **Purpose**: Template for all lesson pages
- **Key Features**:
  - Displays interactive chessboards
  - Shows lesson content and explanations
  - Presents practice questions
  - Handles different lesson types (board, pieces, moves)
- **Assignment Requirements Met**:
  - Delivers interactive learning content
  - Implements practice exercises
  - Provides immediate feedback through reveal answers
  - Shows visual demonstrations of concepts

5. `static/css/style.css`
- **Purpose**: Custom styling for the application
- **Key Features**:
  - Defines layout and appearance of all components
  - Handles responsive design
  - Styles interactive elements
- **Assignment Requirements Met**:
  - Creates engaging user interface
  - Ensures consistent visual design
  - Implements proper spacing and hierarchy
  - Makes content easily readable

6. `static/js/lesson.js`
- **Purpose**: Handles client-side interactivity
- **Key Features**:
  - Initializes and manages chessboards
  - Handles practice question interactions
  - Manages move demonstrations with arrows
  - Logs user activity
- **Assignment Requirements Met**:
  - Implements interactive learning features
  - Provides immediate feedback
  - Creates engaging visual demonstrations
  - Tracks user progress

