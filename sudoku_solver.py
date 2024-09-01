def solve_sudoku(sudoku):
    """
    Solves a Sudoku puzzle using backtracking algorithm.
    Args:
        sudoku (list): A nested list representing the Sudoku grid.
    Returns:
        bool: True if the Sudoku puzzle is solved, False otherwise.
    """
    def is_valid(row, col, num):
        # Check if the number already exists in the row
        for i in range(9):
            if sudoku[row][i] == num:
                return False

        # Check if the number already exists in the column
        for i in range(9):
            if sudoku[i][col] == num:
                return False

        # Check if the number already exists in the 3x3 sub-grid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if sudoku[start_row + i][start_col + j] == num:
                    return False

        return True

    def find_empty_cell():
        # Find an empty cell in the Sudoku grid
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == 0:
                    return row, col
        return None

    def solve():
        # Find an empty cell to start with
        cell = find_empty_cell()
        if cell is None:
            return True

        row, col = cell

        # Try placing numbers from 1 to 9 in the cell
        for num in range(1, 10):
            if is_valid(row, col, num):
                sudoku[row][col] = num
                print(sudoku)

                # Recursively solve the Sudoku puzzle
                if solve():
                    # print(sudoku)
                    return True

                # If the current number doesn't lead to a solution, backtrack
                else:
                    # print('backtracking')
                    sudoku[row][col] = 0
                    
        return False

    # Make a copy of the original Sudoku grid to preserve it
    original_sudoku = [row[:] for row in sudoku]

    # Solve the Sudoku puzzle
    if solve():
        return sudoku
    else:
        # If the Sudoku puzzle cannot be solved, return the original grid
        return original_sudoku
