"""
Problem: Replace words in a sentence with the shortest 'root' word from a given dictionary
         if the sentence word starts with that root.

Approach:
- This problem is efficiently solved using a **Trie (Prefix Tree)** data structure.
- **Trie Construction:** All words in the `dictionary` are inserted into the Trie.
  This allows for quick prefix checking.
- **Shortest Root Search:** The `shortest_root` method is the core logic.
  When checking a word from the sentence:
    1. Traverse the word character-by-character along the Trie paths.
    2. The moment a node is encountered that is marked as the end of a valid dictionary root (`end_of_string = True`),
       that prefix is guaranteed to be the *shortest* possible root for the current word, so we immediately return it.
    3. If the path breaks (a character is not found), no root exists, and the original word is returned.
- **Sentence Replacement:** The sentence is split, each word is checked against the Trie, and the resulting words are joined back.

- Time Complexity: O(L_dict + L_sentence), where L_dict is the total length of all words in the dictionary,
  and L_sentence is the total length of all words in the sentence. This is very efficient as it avoids repeated string comparisons.
- Space Complexity: O(L_dict * D), for storing the Trie, where D is the alphabet size.
"""

import unittest
from typing import (
    Dict,
    List,
)

# --- TrieNode Class ---


class TrieNode:
    """Represents a single node in the Trie (Prefix Tree)."""

    def __init__(self):
        # Dictionary to hold child nodes, mapped by the character they represent.
        # Key: character (str), Value: TrieNode
        self.childrens: Dict[str, "TrieNode"] = {}
        # Flag to indicate if this node marks the end of a valid 'root' word from the dictionary.
        self.end_of_string: bool = False


# --- Trie Class ---


class Trie:
    """The main Trie (Prefix Tree) class for dictionary management."""

    def __init__(self):
        """Initializes the Trie with a root node."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a 'root' word from the dictionary into the Trie.
        """
        curr = self.root
        # Traverse and build the tree character by character
        for c in word:
            if c not in curr.childrens:
                # Create a new node if the path does not exist
                curr.childrens[c] = TrieNode()
            curr = curr.childrens[c]
        # Mark the end of the full word
        curr.end_of_string = True

    def shortest_root(self, word: str) -> str:
        """
        Finds the shortest prefix of 'word' that is a root in the dictionary.
        If no prefix is a root, returns the original word.
        """
        curr = self.root
        # Iterate through the word, keeping track of the index (for slicing)
        for i, c in enumerate(word):
            if c not in curr.childrens:
                # Path is broken, so no root exists as a prefix
                return word

            curr = curr.childrens[c]

            # This is the crucial step: if we hit the end of a dictionary word,
            # it must be the shortest possible root because we are traversing
            # the word from the start.
            if curr.end_of_string:
                # The root is word[0] up to and including the current character (i+1)
                return word[: i + 1]

        # If the whole word is traversed without finding a root marked by 'end_of_string',
        # the original word is returned (e.g., if the word itself is in the dictionary or no prefix is a root).
        return word


# --- Solution Class ---


class Solution:
    """
    Implements the logic to replace words in a sentence with their shortest root
    from a given dictionary, using a Trie for efficient lookups.
    """

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        Replaces words in the 'sentence' with the shortest 'root' found in the
        'dictionary' (if the word starts with a root).

        Args:
            dictionary: A list of root words.
            sentence: A string containing words to be replaced.

        Returns:
            The sentence with words replaced by their shortest root.
        """
        # 1. Build the Trie with all dictionary root words.
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        # 2. Split the sentence into individual words.
        word_array = sentence.split()

        # 3. Iterate over the words and replace them with the shortest root.
        for i, word in enumerate(word_array):
            # Find the shortest root for the current word
            word_array[i] = trie.shortest_root(word)

        # 4. Join the words back into a sentence.
        return " ".join(word_array)


# --- Unit Tests ---


class TestReplaceWords(unittest.TestCase):
    """Test cases for the Solution class's replaceWords method."""

    def setUp(self):
        """Set up the Solution object before each test."""
        self.solution = Solution()

    def test_basic_replacement(self):
        """Test a simple case with a single replacement."""
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        expected = "the cat was rat by the bat"
        self.assertEqual(self.solution.replaceWords(dictionary, sentence), expected)

    def test_shortest_root_precedence(self):
        """Test that the shortest root is chosen over longer roots."""
        dictionary = ["a", "at", "ate"]
        sentence = "the atom in the universe"
        # 'atom' starts with 'a', 'at', and potentially 'ato' etc. 'a' is the shortest root found first.
        expected = "the a in the universe"
        self.assertEqual(self.solution.replaceWords(dictionary, sentence), expected)

    def test_no_replacement(self):
        """Test a case where no word needs to be replaced."""
        dictionary = ["zoo", "car"]
        sentence = "the cow jumped over the moon"
        expected = "the cow jumped over the moon"
        self.assertEqual(self.solution.replaceWords(dictionary, sentence), expected)

    def test_empty_dictionary_and_sentence(self):
        """Test with an empty dictionary and an empty sentence."""
        self.assertEqual(self.solution.replaceWords([], ""), "")

    def test_long_word_with_root(self):
        """Test a long word that is replaced."""
        dictionary = ["hello"]
        sentence = "greetings helloworld people"
        expected = "greetings hello people"
        self.assertEqual(self.solution.replaceWords(dictionary, sentence), expected)


if __name__ == "__main__":
    # Using specific argv to avoid errors when running in environments like Jupyter/colab
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
