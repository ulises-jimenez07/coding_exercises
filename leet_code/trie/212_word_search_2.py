"""
Problem: Given an m x n board of characters and a list of strings words, return all words on the board.
         Word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
         The same letter cell may not be used more than once in a word.

Approach:
- Build a Trie from the list of words to efficiently search for prefixes.
- Use Backtracking (DFS) to traverse the board.
- For each cell, check if it starts a word in the Trie.
- If a word is found, add it to the result and remove it from the Trie (pruning) to avoid duplicates and improve performance.
- Mark visited cells to avoid reusing them in the current path.

- Time complexity: O(M * N * 4^L), where M*N is the board size and L is the average length of words (or max length).
  Trie construction is O(K * L), where K is number of words.
- Space complexity: O(K * L) for Trie storage.
"""

import unittest
from typing import (
    Any,
    Dict,
    List,
)


class Solution:
    """Solves the Word Search II problem using Trie and Backtracking."""

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Finds all words from the given list that exist in the board.
        """
        WORD_KEY = "$"

        # 1. Build Trie
        trie: Dict[str, Any] = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            # Mark the end of a word
            node[WORD_KEY] = word

        rows = len(board)
        cols = len(board[0])
        ans = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtracking(row, col, parent):
            letter = board[row][col]
            curr_node = parent[letter]

            # Check if we found a word
            # Pop to ensure we don't add the same word twice if found via another path
            word_match = curr_node.pop(WORD_KEY, False)
            if word_match:
                ans.append(word_match)

            # Mark path as visited
            board[row][col] = "#"

            # Explore neighbors
            for rd, cd in directions:
                nr, nc = row + rd, col + cd
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node:
                    backtracking(nr, nc, curr_node)

            # Backtrack: restore board state
            board[row][col] = letter

            # Optimization: prune leaf nodes to reduce future search space
            # If curr_node is empty, it means all words in this branch have been found
            if not curr_node:
                parent.pop(letter)

        for row in range(rows):
            for col in range(cols):
                # Start DFS if the character matches a start of a word in Trie
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return ans


class TestWordSearchII(unittest.TestCase):
    """Test cases for Word Search II."""

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test the standard example case."""
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain"]
        expected = ["oath", "eat"]
        # Result order might vary, so we compare as sets or sorted lists
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, expected)

    def test_example_2(self):
        """Test valid word not in board."""
        board = [["a", "b"], ["c", "d"]]
        words = ["abcb"]
        expected = []
        result = self.solution.findWords(board, words)
        self.assertEqual(result, expected)

    def test_small_board_found(self):
        """Test small board with a found word."""
        board = [["a"]]
        words = ["a"]
        expected = ["a"]
        result = self.solution.findWords(board, words)
        self.assertEqual(result, expected)

    def test_pruning_optimization(self):
        """Test that multiple words are found correctly."""
        board = [["a", "b"], ["c", "d"]]
        words = ["ab", "abd", "abc"]  # "abd" not possible, "abc" not possible
        # Actually in 2x2: a->b, b->d (abd)
        # a (0,0) -> b (0,1) -> d (1,1) is valid
        # a (0,0) -> b (0,1) -> c (1,0) - wait c is at (1,0) which is adjacent to b(0,1)? No.
        # (0,1) neighbors: (0,0)='a', (1,1)='d'. (1,0)='c' is diagonal to (0,1).
        # So "abc" is not possible. "abd" is possible.

        # Grid:
        # a b
        # c d
        # neighbors of b(0,1) are a(0,0) and d(1,1).

        expected = ["ab", "abd"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
