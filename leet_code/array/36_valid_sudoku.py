import unittest
from typing import List


class Solution:
    """
    Contains the method to validate a Sudoku board.
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determines if a 9x9 Sudoku board is valid.

        A Sudoku board is valid if:
        1. Each row contains the digits 1-9 without repetition.
        2. Each column contains the digits 1-9 without repetition.
        3. Each of the nine 3x3 sub-boxes of the grid contains the digits 1-9 without repetition.

        Note:
        - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        - Only the filled cells need to be validated according to the mentioned rules.
        - The board contains digits '1'-'9' and the character '.'.

        Args:
            board: A 9x9 list of lists of strings representing the Sudoku board.

        Returns:
            True if the board is valid according to the rules, False otherwise.
        """
        N = 9  # Size of the Sudoku grid

        # Use sets to keep track of seen numbers in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        # Iterate through each cell of the board
        for r in range(N):
            for c in range(N):
                val = board[r][c]

                # Skip empty cells represented by '.'
                if val == ".":
                    continue

                # Check row validity
                if val in rows[r]:
                    return False  # Duplicate found in the current row
                rows[r].add(val)

                # Check column validity
                if val in cols[c]:
                    return False  # Duplicate found in the current column
                cols[c].add(val)

                # Check 3x3 box validity
                # Calculate the index of the 3x3 box (0-8)
                # Integer division maps rows 0,1,2 to box row 0; 3,4,5 to 1; 6,7,8 to 2
                # Integer division maps cols 0,1,2 to box col 0; 3,4,5 to 1; 6,7,8 to 2
                # Box index = (row // 3) * 3 + (col // 3)
                idx = (r // 3) * 3 + (c // 3)
                if val in boxes[idx]:
                    return False  # Duplicate found in the current 3x3 box
                boxes[idx].add(val)

        # If no duplicates were found in any row, column, or box, the board is valid
        return True


# --- Unit Tests ---
class TestIsValidSudoku(unittest.TestCase):
    def setUp(self):
        """Set up the test fixture."""
        self.solution = Solution()
        self.valid_board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.invalid_row_board = [
            ["5", "3", "5", ".", "7", ".", ".", ".", "."],  # Duplicate '5' in row 0
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.invalid_col_board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            ["5", ".", ".", ".", "8", ".", ".", "7", "9"],  # Duplicate '5' in col 0
        ]
        self.invalid_box_board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            [
                "6",
                "5",
                ".",
                "1",
                "9",
                "5",
                ".",
                ".",
                ".",
            ],  # Duplicate '5' in top-left box
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.empty_board = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]

    def test_valid_board(self):
        """Test a valid Sudoku board."""
        self.assertTrue(self.solution.isValidSudoku(self.valid_board))

    def test_invalid_row(self):
        """Test a board with a duplicate in a row."""
        self.assertFalse(self.solution.isValidSudoku(self.invalid_row_board))

    def test_invalid_column(self):
        """Test a board with a duplicate in a column."""
        self.assertFalse(self.solution.isValidSudoku(self.invalid_col_board))

    def test_invalid_box(self):
        """Test a board with a duplicate in a 3x3 box."""
        self.assertFalse(self.solution.isValidSudoku(self.invalid_box_board))

    def test_empty_board(self):
        """Test an empty board (should be valid as there are no conflicts)."""
        self.assertTrue(self.solution.isValidSudoku(self.empty_board))

    def test_partially_filled_valid(self):
        """Test another partially filled but valid board."""
        board = [
            ["1", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "2", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "3", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "4", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "5", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "6", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "7", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "8", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "9"],
        ]
        self.assertTrue(self.solution.isValidSudoku(board))


if __name__ == "__main__":
    unittest.main()
