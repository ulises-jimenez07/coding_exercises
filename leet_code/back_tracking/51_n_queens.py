"""
Problem: Place N queens on NxN chessboard so no queens attack each other

Approach:
- Version 1: Backtracking with explicit board rendering (LeetCode 51 style).
- Version 2: Optimized backtracking using sets for O(1) conflict checks, returning the count of solutions (LeetCode 52 style).
- Time complexity: O(n!)
- Space complexity: O(n) for the sets and recursion stack.
"""

import unittest
from typing import List


class Solution:
    """
    Backtracking solution for N-Queens that returns all possible board configurations.
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [["." for i in range(n)] for j in range(n)]  # pylint: disable=attribute-defined-outside-init
        self.solutions: list[list[str]] = []  # pylint: disable=attribute-defined-outside-init
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


# Version 2: Optimized count-based backtracking using sets for O(1) lookups
res = 0


def n_queens(n: int) -> int:
    """
    Returns the total number of solutions for the N-Queens problem using sets.
    """
    global res  # pylint: disable=global-statement
    res = 0
    dfs(0, set(), set(), set(), n)
    return res


def dfs(r, diagonals_set, anti_diagonals_set, col_set, n):
    global res  # pylint: disable=global-statement
    if r == n:
        res += 1
        return

    for c in range(n):
        curr_diagonal = r - c
        curr_anti_diagonal = r + c

        if c in col_set or curr_diagonal in diagonals_set or curr_anti_diagonal in anti_diagonals_set:
            continue

        col_set.add(c)
        diagonals_set.add(curr_diagonal)
        anti_diagonals_set.add(curr_anti_diagonal)

        dfs(r + 1, diagonals_set, anti_diagonals_set, col_set, n)
        col_set.remove(c)
        diagonals_set.remove(curr_diagonal)
        anti_diagonals_set.remove(curr_anti_diagonal)


class TestNQueens(unittest.TestCase):
    """
    Unit tests for both N-Queens implementations.
    """

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

    def test_v2_counts(self):
        # Version 2 returns counts directly
        self.assertEqual(n_queens(1), 1)
        self.assertEqual(n_queens(2), 0)
        self.assertEqual(n_queens(3), 0)
        self.assertEqual(n_queens(4), 2)
        self.assertEqual(n_queens(8), 92)


if __name__ == "__main__":
    unittest.main()
