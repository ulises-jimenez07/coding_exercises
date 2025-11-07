"""
Problem: Determine if a 9x9 Sudoku board is valid

Approach:
- Use sets to track seen numbers in each row, column, and 3x3 box
- Check for duplicates while iterating through board once
- Time complexity: O(1) - fixed 9x9 board
- Space complexity: O(1) - fixed size sets
"""

import unittest
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Determines if a 9x9 Sudoku board is valid."""
        N = 9
        rows: list[set[str]] = [set() for _ in range(N)]
        cols: list[set[str]] = [set() for _ in range(N)]
        boxes: list[set[str]] = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]

                if val == ".":
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                idx = (r // 3) * 3 + (c // 3)
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True


class TestIsValidSudoku(unittest.TestCase):
    def setUp(self):
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
            ["5", "3", "5", ".", "7", ".", ".", ".", "."],
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
            ["5", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.invalid_box_board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", "5", ".", "1", "9", "5", ".", ".", "."],
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
        """Valid Sudoku board."""
        self.assertTrue(self.solution.isValidSudoku(self.valid_board))

    def test_invalid_row(self):
        """Board with duplicate in row."""
        self.assertFalse(self.solution.isValidSudoku(self.invalid_row_board))

    def test_invalid_column(self):
        """Board with duplicate in column."""
        self.assertFalse(self.solution.isValidSudoku(self.invalid_col_board))

    def test_invalid_box(self):
        """Board with duplicate in 3x3 box."""
        self.assertFalse(self.solution.isValidSudoku(self.invalid_box_board))

    def test_empty_board(self):
        """Empty board."""
        self.assertTrue(self.solution.isValidSudoku(self.empty_board))

    def test_partially_filled_valid(self):
        """Partially filled valid board."""
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
