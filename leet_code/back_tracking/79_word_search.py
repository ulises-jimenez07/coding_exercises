"""
Problem: Search for a word in a 2D grid using adjacent cells

Approach:
- Use backtracking with DFS to explore all paths
- Mark visited cells temporarily to avoid reuse in the same path
- Try all 4 directions (up, down, left, right) from each cell
- Time complexity: O(m*n*4^L) where m,n are grid dimensions, L is word length
- Space complexity: O(L) for recursion stack
"""

import unittest
from typing import List


class Solution:
    """
    Solution class to check if a word exists in a 2D board of characters.
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Determine if the target word exists in the 2D board.
        """
        if not board or not board[0]:
            return not word
        if not word:
            return True

        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(r: int, c: int, index: int) -> bool:
            """
            Perform backtracking to match the remaining characters of the word.
            """
            # Found the complete word
            if len(word) == index:
                return True

            # Check boundaries and if the current character matches
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[index]:
                # Mark as visited temporarily
                temp = board[r][c]
                board[r][c] = "#"

                # Try all four directions
                for dr, dc in directions:
                    if backtrack(r + dr, c + dc, index + 1):
                        return True

                # Backtrack: restore original character
                board[r][c] = temp
                return False

            return False

        # Search for starting characters using enumerate
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == word[0]:
                    if backtrack(r, c, 0):
                        return True
        return False


class TestWordSearch(unittest.TestCase):
    """
    Unit tests for the Word Search solution.
    """

    def setUp(self) -> None:
        """Set up the Solution instance before each test."""
        self.solution = Solution()
        self.maxDiff = None

    def test_word_exists(self) -> None:
        """Test when the word does not exist due to a dead end."""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCEFSADEESE"
        self.assertFalse(self.solution.exist(board, word))

    def test_word_does_not_exist(self) -> None:
        """Test search for a word with cyclic paths that does not exist."""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        self.assertFalse(self.solution.exist(board, word))

    def test_empty_word(self) -> None:
        """Test search with an empty word."""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = ""
        self.assertTrue(self.solution.exist(board, word))

    def test_word_exists_see(self) -> None:
        """Test search for the word 'SEE' which exists."""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word))

    def test_word_exists_abcced(self) -> None:
        """Test search for the word 'ABCCED' which exists."""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        self.assertTrue(self.solution.exist(board, word))

    def test_single_element_match(self) -> None:
        """Test a single-element board that matches the word."""
        board = [["A"]]
        word = "A"
        self.assertTrue(self.solution.exist(board, word))

    def test_single_element_no_match(self) -> None:
        """Test a single-element board that does not match the word."""
        board = [["A"]]
        word = "B"
        self.assertFalse(self.solution.exist(board, word))

    def test_empty_board(self) -> None:
        """Test an empty board."""
        board: List[List[str]] = []
        word = "A"
        self.assertFalse(self.solution.exist(board, word))


if __name__ == "__main__":
    unittest.main()
