"""
Module to solve the 'Surrounded Regions' problem.
"""

import unittest
from typing import List


class Solution:
    """Class containing the solution for the Surrounded Regions problem."""

    def solve(self, board: List[List[str]]) -> List[List[str]]:
        """
        Captures all 'O' regions that are surrounded by 'X's in-place.
        """
        if not board:
            return board

        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            """Perform DFS to mark un-surrounded regions."""
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "U":
                board[r][c] = "O"
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        # Mark all 'O's as temporary 'U'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "U"

        # DFS from borders to restore safe 'O's
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)

        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)

        # Convert remaining 'U's to 'X'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "U":
                    board[i][j] = "X"

        return board


class TestSolution(unittest.TestCase):
    """Unit tests for the Solution class."""

    def test_example_case(self):
        """Test case from the common problem statement."""
        input_board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
        expected_board = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
        Solution().solve(input_board)
        self.assertEqual(input_board, expected_board)

    def test_empty_board(self):
        """Test case for an empty board."""
        input_board = []
        expected_board = []
        Solution().solve(input_board)
        self.assertEqual(input_board, expected_board)

    def test_no_capture(self):
        """Test case where all 'O's are connected to the border."""
        input_board = [["O", "O", "O"], ["O", "X", "O"], ["O", "O", "O"]]
        expected_board = [["O", "O", "O"], ["O", "X", "O"], ["O", "O", "O"]]
        Solution().solve(input_board)
        self.assertEqual(input_board, expected_board)

    def test_full_capture(self):
        """Test case where all 'O's are completely surrounded."""
        input_board = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]
        expected_board = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]
        Solution().solve(input_board)
        self.assertEqual(input_board, expected_board)

    def test_single_element(self):
        """Test case for a single element board."""
        input_board = [["O"]]
        expected_board = [["O"]]
        Solution().solve(input_board)
        self.assertEqual(input_board, expected_board)


if __name__ == "__main__":
    unittest.main()
