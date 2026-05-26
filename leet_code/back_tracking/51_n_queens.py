"""
Problem: Place N queens on an NxN chessboard so that no two queens attack each other.
"""

import unittest
from typing import List


class Solution:
    """
    Backtracking solution for N-Queens that returns all possible board configurations.
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Finds all valid configurations of N queens on an NxN board.
        """

        def is_valid(row: int, col: int) -> bool:
            """
            Checks if placing a queen at (row, col) is valid.
            """
            # Check column for conflicts
            for i, r in enumerate(board):
                if r[col] == "Q":
                    return False

            # Check upper-left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < len(board[0]):
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row: int) -> None:
            """
            Recursively places queens row by row.
            """
            # Base case: all rows filled, record the configuration
            if row == len(board):
                result.append(["".join(r) for r in board])
                return

            # Try placing a queen in each column of the current row
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        result: List[List[str]] = []
        board = [["."] * n for _ in range(n)]
        backtrack(0)
        return result


class TestNQueens(unittest.TestCase):
    """
    Unit tests for the N-Queens solution.
    """

    def setUp(self):
        self.solution = Solution()

    def test_n_equals_4(self):
        expected_solutions = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        expected_set = set(tuple(sol) for sol in expected_solutions)
        actual_solutions = self.solution.solveNQueens(4)
        actual_set = set(tuple(sol) for sol in actual_solutions)
        self.assertEqual(actual_set, expected_set)

    def test_n_equals_1(self):
        expected_solutions = [["Q"]]
        self.assertEqual(self.solution.solveNQueens(1), expected_solutions)

    def test_n_equals_2_and_3(self):
        self.assertEqual(self.solution.solveNQueens(2), [])
        self.assertEqual(self.solution.solveNQueens(3), [])

    def test_n_equals_8(self):
        self.assertEqual(len(self.solution.solveNQueens(8)), 92)


if __name__ == "__main__":
    unittest.main()
