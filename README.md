# Sudoko-Sensei
Sudoku Solver is a web-based application built using Flask that allows users to solve Sudoku puzzles. The application accepts an unsolved Sudoku grid and returns the solved puzzle using a backtracking algorithm. Additionally, the project includes an optional image processing feature for OCR-based Sudoku puzzle extraction from images.

Features:
- Solve Sudoku Puzzles: Input a 9x9 Sudoku grid with empty cells represented by 0s, and the application will return the solved puzzle.
- Image Processing: Upload an image of a Sudoku puzzle, and the application will extract the puzzle using OCR and return the solved grid.
- Web Interface: A user-friendly interface for easy interaction.

Setup:

Prerequisites:
- Python 3.x
- Flask
- Flask-CORS
- MoviePy
- NumPy
- SpeechRecognition (for potential future enhancements involving speech input)
- Requests (for potential API requests in future enhancements)

Installation:
1. Clone the repository:
   git clone https://github.com/your-repository/sudoku-solver.git
   cd sudoku-solver

2. Install the required packages:
  pip install -r requirements.txt

3. Run the appliication:
   python server.py

4. Access the application at http://localhost:5000.

Usage:
1. Solve a Sudoku Puzzle
2. Open the web interface.
3. Input the Sudoku puzzle grid, using 0s for empty cells.
4. Click on the "Solve" button to get the solved Sudoku puzzle.

Image Upload:
1. Click on the "Upload Image" button.
2. Select an image of a Sudoku puzzle.
3. The application will process the image, extract the puzzle, and display the solved grid.
