from typing import List
import unittest

# Define the class for the N-Queens problem solver
class Solution:
    """
    Solves the N-Queens problem using backtracking.
    The N-Queens problem is to place N non-attacking queens on an N×N chessboard.
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Main function to initiate the solving process.

        :param n: The size of the chessboard (N x N).
        :return: A list of all distinct solutions, where each solution is a list of strings
                 representing the board configuration. 'Q' denotes a queen, '.' denotes an empty spot.
        """
        # Initialize the N x N board with all empty spots ('.')
        self.board = [['.' for i in range(n)] for j in range(n)]
        # Initialize a list to store all valid solutions
        self.solutions = []
        # Start the backtracking process from the first row (row 0)
        self.back_track(0)
        return self.solutions

    def back_track(self, row: int):
        """
        Recursive helper function to place queens row by row.

        :param row: The current row being considered for placing a queen.
        """
        # Base case: If all rows have been successfully filled with queens
        if row == len(self.board):
            # A valid solution is found. Convert the board state to the required format (list of strings)
            solution = []
            for r in self.board:
                solution.append(''.join(r))
            # Store the solution
            self.solutions.append(solution)
        else:
            # Iterate through all columns in the current row
            for col in range(len(self.board[0])):
                # Check if placing a queen at (row, col) is safe
                if self.is_safe(row, col):
                    # Place a queen ('Q') at (row, col)
                    self.board[row][col] = 'Q'
                    # Recurse to the next row (row + 1)
                    self.back_track( row + 1)
                    # Backtrack: Remove the queen (reset the spot to '.') to explore other possibilities
                    self.board[row][col] = '.'

    def is_safe(self, row: int, col: int) -> bool:
        """
        Checks if placing a queen at (row, col) is safe (i.e., not attacked by any existing queens).
        We only need to check columns and diagonals *above* the current row
        since queens are placed row by row, from top to bottom.

        :param row: The row index of the potential queen.
        :param col: The column index of the potential queen.
        :return: True if safe, False otherwise.
        """
        # 1. Check for conflicts in the same column (above the current row)
        # Iterate through rows above the current one (from 0 up to row - 1)
        for i in range(row): # Note: This range goes from 0 to row - 1, checking rows above.
            if self.board[i][col] == 'Q':
                return False

        # 2. Check for conflicts in the upper-left diagonal
        i = row - 1  # Start checking from the row immediately above
        j = col - 1  # Start checking from the column immediately to the left

        # Continue checking as long as the indices are within the board boundaries
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i -= 1 # Move one step up
            j -= 1 # Move one step left

        # 3. Check for conflicts in the upper-right diagonal
        i = row - 1  # Start checking from the row immediately above
        j = col + 1  # Start checking from the column immediately to the right

        # Continue checking as long as the indices are within the board boundaries
        while i >= 0 and j < len(self.board[0]):
            if self.board[i][j] == 'Q':
                return False
            i -= 1 # Move one step up
            j += 1 # Move one step right

        # If no conflicts found, the position is safe
        return True

# --- Unit Tests ---

class TestNQueens(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def test_n_equals_4(self):
        """
        Tests the case for N=4, which has 2 distinct solutions.
        """
        s = Solution()
        expected_solutions = [
            [".Q..",
             "...Q",
             "Q...",
             "..Q."],

            ["..Q.",
             "Q...",
             "...Q",
             ".Q.."]
        ]
        # The order of solutions can vary, so we convert them to sets of tuples for comparison
        expected_set = set(tuple(sol) for sol in expected_solutions)
        actual_solutions = s.solveNQueens(4)
        actual_set = set(tuple(sol) for sol in actual_solutions)
        self.assertEqual(len(actual_set), len(expected_set), "Should find the correct number of solutions for N=4")
        self.assertEqual(actual_set, expected_set, "Solutions for N=4 should match the expected set")

    def test_n_equals_1(self):
        """
        Tests the case for N=1, which has 1 solution.
        """
        s = Solution()
        expected_solutions = [["Q"]]
        self.assertEqual(s.solveNQueens(1), expected_solutions, "Should find the single solution for N=1")

    def test_n_equals_2_and_3(self):
        """
        Tests the cases for N=2 and N=3, which have 0 solutions.
        """
        s2 = Solution()
        self.assertEqual(s2.solveNQueens(2), [], "Should find 0 solutions for N=2")
        s3 = Solution()
        self.assertEqual(s3.solveNQueens(3), [], "Should find 0 solutions for N=3")

    def test_n_equals_8(self):
        """
        Tests the case for N=8, which has 92 solutions.
        This test checks only the total count for efficiency.
        """
        s = Solution()
        # N=8 is known to have 92 solutions
        self.assertEqual(len(s.solveNQueens(8)), 92, "Should find 92 solutions for N=8")

# Standard boilerplate to run the tests when the script is executed
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)