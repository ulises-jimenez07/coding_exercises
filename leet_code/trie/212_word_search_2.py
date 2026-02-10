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


class TrieNode:
    """A node in a Trie."""

    def __init__(self):
        self.childrens = {}
        self.word = None


def find_all_words_on_a_board(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Finds all words from the list on the board using a TrieNode-based approach.
    """
    root = TrieNode()

    for word in words:
        node = root
        for char in word:
            if char not in node.childrens:
                node.childrens[char] = TrieNode()
            node = node.childrens[char]
        node.word = word

    res: List[str] = []

    for r, _ in enumerate(board):
        for c, _ in enumerate(board[0]):
            if board[r][c] in root.childrens:
                dfs(board, r, c, root.childrens[board[r][c]], res)

    return res


def dfs(board: List[List[str]], r: int, c: int, node: TrieNode, res: List[str]):
    """Deep-first search to find words in the board."""
    if node.word:
        res.append(node.word)
        node.word = None

    temp = board[r][c]
    board[r][c] = "#"

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if is_within_bounds(nr, nc, board) and board[nr][nc] in node.childrens:
            dfs(board, nr, nc, node.childrens[board[nr][nc]], res)

    board[r][c] = temp


def is_within_bounds(r, c, board):
    """Checks if coordinates are within the board bounds."""
    return 0 <= r < len(board) and 0 <= c < len(board[0])


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

    def test_find_all_words_version_2(self):
        """Test the second version of findWords."""
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain"]
        expected = ["oath", "eat"]
        result = find_all_words_on_a_board(board, words)
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
