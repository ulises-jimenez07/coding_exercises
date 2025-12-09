"""
Problem: Implement a Trie (Prefix Tree) for efficient insertion, searching of words,
         and checking for prefixes.

Approach:
- The Trie structure consists of nodes (`TrieNode`).
- Each node stores a dictionary/hash map (`self.children`) where keys are characters
  and values are references to the next `TrieNode`.
- Each node also has a flag (`self.end_of_string`) to mark if the node represents
  the end of a complete word.
- **Insert:** Traverse the tree based on characters in the word, creating new nodes
  if a character path does not exist. Mark the final node as `end_of_string = True`.
- **Search:** Traverse the tree. If any character path is missing, the word does not
  exist. If the traversal is complete, check the final node's `end_of_string` flag.
- **StartsWith:** Similar to search, but only checks if the prefix path exists,
  ignoring the `end_of_string` flag of the final node.

- Time complexity (Insert/Search/StartsWith): O(L), where L is the length of the string/prefix.
- Space complexity: O(N * L * D), where N is the number of words, L is the average
  length of words, and D is the alphabet size (worst case, if no prefixes are shared).
  In practice, it is often much better due to shared prefixes.
"""

import unittest
from typing import (
    Dict,
)


class TrieNode:
    """Represents a single node in the Trie (Prefix Tree)."""

    def __init__(self):
        """Initializes a node with an empty dictionary of children and a word-end marker."""
        # Dictionary to hold child nodes, mapped by the character they represent.
        # Key: character (str), Value: TrieNode
        self.children: Dict[str, "TrieNode"] = {}
        # Flag to indicate if this node marks the end of a word.
        self.end_of_string: bool = False


class Trie:
    """The main Trie (Prefix Tree) class."""

    def __init__(self):
        """Initializes the Trie with a root node."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        """
        curr = self.root
        # Traverse the word character by character
        for ch in word:
            # Check if the path (character) already exists
            node = curr.children.get(ch)
            if not node:
                # If not, create a new node and add it to the children map
                node = TrieNode()
                curr.children[ch] = node
            # Move the pointer to the next node
            curr = node

        # After processing the last character, mark the node as the end of a word
        curr.end_of_string = True

    def search(self, word: str) -> bool:
        """
        Checks if a word is fully present in the Trie.
        """
        curr = self.root
        # Traverse the word character by character
        for ch in word:
            node = curr.children.get(ch)
            # If the path for any character is missing, the word is not in the Trie
            if not node:
                return False
            curr = node

        # The path exists, now check if the final node marks the end of a valid word
        return curr.end_of_string

    def startsWith(self, prefix: str) -> bool:
        """
        Checks if any word in the Trie starts with the given prefix.
        """
        curr = self.root
        # Traverse the prefix character by character
        for ch in prefix:
            node = curr.children.get(ch)
            # If the path for any character is missing, the prefix does not exist
            if not node:
                return False
            curr = node

        # If we successfully traversed the entire prefix, it exists in the Trie
        return True


# -----------------------------------------------------------------------------


class TestTrie(unittest.TestCase):
    """Test cases for the Trie data structure implementation."""

    def setUp(self):
        """Set up a new Trie object before each test."""
        self.trie = Trie()

    def test_insert_and_search_word(self):
        """Test basic insertion and successful search of a word."""
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))

    def test_search_non_existent_word(self):
        """Test search for a word that was not inserted."""
        self.trie.insert("apple")
        self.assertFalse(self.trie.search("app"))  # "app" is a prefix, but not a full word

    def test_search_non_existent_prefix(self):
        """Test search for a word with a prefix that was not inserted."""
        self.trie.insert("apple")
        self.assertFalse(self.trie.search("banana"))

    def test_starts_with_full_word(self):
        """Test startsWith where the prefix is a full word."""
        self.trie.insert("apple")
        self.assertTrue(self.trie.startsWith("apple"))

    def test_starts_with_prefix(self):
        """Test startsWith for a common prefix of an inserted word."""
        self.trie.insert("apple")
        self.assertTrue(self.trie.startsWith("app"))

    def test_starts_with_non_existent_prefix(self):
        """Test startsWith for a prefix that does not exist."""
        self.trie.insert("apple")
        self.assertFalse(self.trie.startsWith("ban"))

    def test_multiple_words_shared_prefix(self):
        """Test insertion and search with shared prefixes."""
        self.trie.insert("apple")
        self.trie.insert("apply")
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("apply"))
        self.assertTrue(self.trie.startsWith("app"))
        self.assertTrue(self.trie.startsWith("appl"))
        self.assertFalse(self.trie.search("appl"))  # Not marked as a word end

    def test_word_as_prefix_of_another(self):
        """Test a shorter word that is a prefix of a longer word."""
        self.trie.insert("app")
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.startsWith("app"))
        self.assertTrue(self.trie.search("apple"))


if __name__ == "__main__":
    unittest.main()
