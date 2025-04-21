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
FILE DESCRIPTIONS:<br><br>
1. app.py<br>
- Purpose: Main Flask application file that serves as the backend controller<br>
Key Functions:<br>
  - Defines all lesson data and structure<br>
  - Handles routing for different pages (/home, /learn, /quiz)<br>
  - Manages user activity logging<br>
  - Controls lesson progression<br>
Assignment Requirements Met:<br>
  - Implements a structured learning path<br>
  - Manages state and progression through lessons<br>
  - Handles user interactions and navigation<br>
  - Provides data for interactive learning content<br><br>
2. templates/layout.html<br>
- Purpose: Base template that provides the common structure for all pages<br>
Key Features:<br>
  - Contains the navigation bar<br>
  - Loads all necessary CSS and JavaScript dependencies<br>
  - Provides consistent branding and layout<br>
Assignment Requirements Met:<br>
  - Ensures consistent user interface across the application<br>
  - Implements responsive design principles<br>
  - Integrates required external libraries (Bootstrap, jQuery, Chessboard.js)<br><br>
3. templates/home.html<br>
- Purpose: Landing page that introduces users to the application<br>
Key Features:<br>
  - Displays main learning sections in a clear, minimal design<br>
  - Highlights the starting point with "Start Here" arrow<br>
  - Shows clear progression path<br>
Assignment Requirements Met:<br>
  - Provides clear user onboarding<br>
  - Implements intuitive navigation<br>
  - Uses visual cues to guide users<br><br>
4. templates/lesson.html<br>
- Purpose: Template for all lesson pages<br>
Key Features:<br>
  - Displays interactive chessboards<br>
  - Shows lesson content and explanations<br>
  - Presents practice questions<br>
  - Handles different lesson types (board, pieces, moves)<br>
Assignment Requirements Met:<br>
  - Delivers interactive learning content<br>
  - Implements practice exercises<br>
  - Provides immediate feedback through reveal answers<br>
  - Shows visual demonstrations of concepts<br><br>
5. static/css/style.css<br>
- Purpose: Custom styling for the application<br>
Key Features:<br>
  - Defines layout and appearance of all components<br>
  - Handles responsive design<br>
  - Styles interactive elements<br>
Assignment Requirements Met:<br>
  - Creates engaging user interface<br>
  - Ensures consistent visual design<br>
  - Implements proper spacing and hierarchy<br>
  - Makes content easily readable<br><br>
6. static/js/lesson.js<br>
- Purpose**: Handles client-side interactivity<br>
Key Features:<br>
  - Initializes and manages chessboards<br>
  - Handles practice question interactions<br>
  - Manages move demonstrations with arrows<br>
  - Logs user activity<br>
Assignment Requirements Met:<br>
  - Implements interactive learning features<br>
  - Provides immediate feedback<br>
  - Creates engaging visual demonstrations<br>
  - Tracks user progress<br>

