"""
Problem: Capture all regions that are surrounded by 'X' on a 2D board.

Approach:
- Mark all 'O's as temporary 'U', then DFS from borders to restore safe 'O's
- Convert remaining 'U's to 'X' (captured regions)
- Time complexity: O(m * n)
- Space complexity: O(m * n) for recursion stack
"""

import unittest
from typing import List


class Solution:
    """
    This class contains a method to solve the 'Surrounded Regions' problem.
    The goal is to capture all 'O's that are entirely surrounded by 'X's.
    An 'O' is *not* captured if it is on the border or can reach the border.
    The board is modified in-place.
    """

    def solve(self, board: List[List[str]]) -> None:
        """
        Captures all 'O' regions that are surrounded by 'X's.
        The strategy is to:
        1. Mark all 'O's as 'U' (Unvisited/Unsure).
        2. Use DFS starting from 'U's on the border to mark them back to 'O' (Safe/Uncaptured).
        3. Convert all remaining 'U's (which are surrounded) to 'X' (Captured).

        Do not return anything, modify board in-place instead.
        """
        # Get dimensions of the board
        self.n = len(board)
        if self.n == 0:
            return
        self.m = len(board[0])
        if self.m == 0:
            return

        # Step 1: Mark all 'O's as 'U' (Unsure/Unvisited)
        # This is a temporary marker. Only 'O's can be potentially captured.
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "O":
                    board[i][j] = "U"

        # Step 2: Traverse the border and run DFS on any 'U' found,
        # changing it back to 'O'. These 'O's and all connected 'O's
        # will not be captured.

        # Traverse left and right borders
        for i in range(self.n):
            # Left border (col = 0)
            self.dfs_core(i, 0, board)
            # Right border (col = self.m-1)
            self.dfs_core(i, self.m - 1, board)

        # Traverse top and bottom borders
        for j in range(self.m):
            # Top border (row = 0)
            self.dfs_core(0, j, board)
            # Bottom border (row = self.n -1)
            self.dfs_core(self.n - 1, j, board)

        # Step 3: Final conversion
        # All remaining 'U's are surrounded 'O's, so they are captured and converted to 'X'.
        # All 'O's are safe (connected to the border).
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "U":
                    board[i][j] = "X"

    def dfs_core(self, row, col, board):
        """
        Depth First Search core logic.
        Marks a connected region of 'U's as 'O's, indicating they are safe (connected to the border).
        """
        # Check boundary conditions and if the current cell is the temporary marker 'U'
        if row >= 0 and row < self.n and col >= 0 and col < self.m and board[row][col] == "U":
            # Mark the cell as 'O' (Safe/Uncaptured)
            board[row][col] = "O"

            # Recursively call DFS on all four neighbors
            self.dfs_core(row - 1, col, board)  # Up
            self.dfs_core(row + 1, col, board)  # Down
            self.dfs_core(row, col - 1, board)  # Left
            self.dfs_core(row, col + 1, board)  # Right


# -----------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def test_example_case(self):
        """
        Test case from the common problem statement.
        The 'O's in the center $3\times3$ area should be flipped.
        The 'O's on the border should remain.
        """
        input_board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

        expected_board = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

        Solution().solve(input_board)

        self.assertEqual(input_board, expected_board, "The surrounded regions were not correctly captured.")

    def test_empty_board(self):
        """
        Test case for an empty board (0 rows).
        """
        input_board = []
        expected_board = []
        Solution().solve(input_board)
        self.assertEqual(input_board, expected_board, "Empty board handling failed.")

    def test_no_capture(self):
        """
        Test case where all 'O's are connected to the border, so none are captured.
        """
        input_board = [["O", "O", "O"], ["O", "X", "O"], ["O", "O", "O"]]

        expected_board = [["O", "O", "O"], ["O", "X", "O"], ["O", "O", "O"]]

        Solution().solve(input_board)
        self.assertEqual(input_board, expected_board, "Board where all 'O's are safe was incorrectly modified.")

    def test_full_capture(self):
        """
        Test case where all 'O's are completely surrounded and should be captured.
        """
        input_board = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]

        expected_board = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]

        Solution().solve(input_board)
        self.assertEqual(input_board, expected_board, "Full capture of surrounded 'O' failed.")


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # boilerplate code to run the tests when the script is executed
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
