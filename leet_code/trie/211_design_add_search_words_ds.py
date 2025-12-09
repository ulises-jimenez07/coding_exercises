"""
Problem: Design a data structure that supports adding words and searching for words
         that can contain the wildcard character '.' (dot), which matches any single letter.

Approach:
- A standard Trie is used for word storage.
- The `addWord` function is a regular Trie insertion.
- The `search` function initiates a recursive Depth-First Search (DFS) function, `_dfs_search`.
- The DFS handles the wildcard:
    - If the current character is a normal letter, it proceeds down that specific path.
    - If the current character is '.', it recursively attempts the search on *all* child nodes
      from the current node. If any path succeeds, the search returns True.

- Time Complexity:
    - addWord: O(L), where L is the length of the word.
    - search (no wildcard): O(L).
    - search (with wildcard): O(26^M) in the worst case, where M is the number of wildcards
      in the word (if the wildcard is at the start, it searches through 26 branches, and so on).
- Space Complexity: O(N * L) for storing all words in the Trie.
"""

import unittest
from typing import Dict


class TrieNode:
    """Represents a single node in the Trie."""

    def __init__(self):
        # Maps a character to its next TrieNode.
        self.children: Dict[str, "TrieNode"] = {}
        # True if this node marks the end of a complete word.
        self.end_of_string: bool = False


class WordDictionary:
    """Trie structure optimized for wildcard search."""

    def __init__(self):
        """Initialize the data structure with a root Trie node."""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word to the data structure (standard Trie insertion).
        """
        curr = self.root
        for ch in word:
            node = curr.children.get(ch)
            # Create a new node if the path doesn't exist.
            if not node:
                node = TrieNode()
                curr.children[ch] = node
            curr = node
        # Mark the last node as the end of a word.
        curr.end_of_string = True

    def search(self, word: str) -> bool:
        """
        Searches for a word, supporting the '.' wildcard character.
        """
        # Start the recursive DFS search from the root.
        return self._dfs_search(word, 0, self.root)

    def _dfs_search(self, word, index, node):
        """
        Recursive helper function to perform Depth-First Search.
        """
        # Base case: If we've processed all characters in the word
        if index == len(word):
            # Success only if the final node marks the end of a word
            return node.end_of_string

        ch = word[index]

        # Case 1: Current character is a normal letter
        if ch != ".":
            # Proceed only if the exact child path exists
            if ch in node.children:
                return self._dfs_search(word, index + 1, node.children[ch])
            # Path missing, so the word doesn't exist
            return False

        # Case 2: Current character is a wildcard '.'
        # Recursively try the search on ALL possible child paths
        for child_node in node.children.values():
            # If any path succeeds, return True immediately
            if self._dfs_search(word, index + 1, child_node):
                return True
        # No path matched the rest of the word
        return False


# -----------------------------------------------------------------------------


class TestWordDictionary(unittest.TestCase):
    """Test cases for the WordDictionary class."""

    def setUp(self):
        """Set up a new WordDictionary before each test."""
        self.wd = WordDictionary()
        self.wd.addWord("bad")
        self.wd.addWord("dad")
        self.wd.addWord("mad")

    def test_search_normal_word(self):
        """Test search for an existing word without a wildcard."""
        self.assertTrue(self.wd.search("dad"))
        self.assertFalse(self.wd.search("pad"))

    def test_search_with_wildcard_at_start(self):
        """Test wildcard matching at the beginning of the word."""
        self.assertTrue(self.wd.search(".ad"))
        self.assertTrue(self.wd.search("..d"))

    def test_search_with_wildcard_in_middle(self):
        """Test wildcard matching in the middle of the word."""
        self.assertTrue(self.wd.search("b.d"))
        self.assertTrue(self.wd.search("d.d"))
        self.assertTrue(self.wd.search("b.."))  # Requires a 4-letter word.

    def test_search_with_wildcard_at_end(self):
        """Test wildcard matching at the end of the word."""
        self.assertTrue(self.wd.search("da."))
        self.assertFalse(self.wd.search("a.d"))

    def test_search_with_multiple_wildcards(self):
        """Test search with more than one wildcard."""
        self.assertTrue(self.wd.search("..."))  # Matches 'bad', 'dad', 'mad'
        self.assertFalse(self.wd.search("...."))  # No 4-letter words exist

    def test_search_non_existent_length(self):
        """Test search for a word length not present."""
        self.assertFalse(self.wd.search("b"))
        self.wd.addWord("a")
        self.assertTrue(self.wd.search("a"))
        self.assertTrue(self.wd.search("."))


if __name__ == "__main__":
    unittest.main()
