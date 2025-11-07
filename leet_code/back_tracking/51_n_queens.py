"""
Problem: Place N queens on NxN chessboard so no queens attack each other

Approach:
- Use backtracking to place queens row by row
- Check if position is safe from attacks (column, diagonals)
- Build solution string when all queens placed
- Time complexity: O(n!)
- Space complexity: O(n^2) for board storage
"""

import unittest
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [["." for i in range(n)] for j in range(n)]
        self.solutions: list[list[str]] = []
        self.back_track(0)
        return self.solutions

    def back_track(self, row: int):
        # Base case: placed all queens
        if row == len(self.board):
            solution = []
            for r in self.board:
                solution.append("".join(r))
            self.solutions.append(solution)
        else:
            # Try placing queen in each column
            for col in range(len(self.board[0])):
                if self.is_safe(row, col):
                    self.board[row][col] = "Q"
                    self.back_track(row + 1)
                    self.board[row][col] = "."  # Backtrack

    def is_safe(self, row: int, col: int) -> bool:
        # Check column above
        for i in range(row):
            if self.board[i][col] == "Q":
                return False

        # Check upper-left diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(self.board[0]):
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True


class TestNQueens(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.maxDiff = None

    def test_n_equals_4(self):
        expected_solutions = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        expected_set = set(tuple(sol) for sol in expected_solutions)
        actual_solutions = self.solution.solveNQueens(4)
        actual_set = set(tuple(sol) for sol in actual_solutions)
        self.assertEqual(len(actual_set), len(expected_set))
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
