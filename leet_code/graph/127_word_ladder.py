"""
Problem: Given two words (beginWord and endWord) and a dictionary's word list, find the length of shortest
         transformation sequence from beginWord to endWord, such that:
         1. Only one letter can be changed at a time.
         2. Each transformed word must exist in the word list.

Approach:
- Treat words as nodes in a graph. An edge exists if words differ by exactly one letter.
- Use BFS to find the shortest path from beginWord to endWord.
- To optimize finding neighbors, we preprocess the wordList. For each word, we generate all generic forms
  by replacing one letter with a wildcard '*'. E.g. "hot" -> "*ot", "h*t", "ho*".
- Map these generic forms to the list of words that match. This allows O(L) lookup for neighbors.

- Time Complexity: O(M^2 * N), where M is the length of each word and N is the total number of words.
- Space Complexity: O(M^2 * N) to store the dictionary of intermediate words.
"""

import unittest
from collections import (
    defaultdict,
    deque,
)
from typing import List


class Solution:
    """Solves the Word Ladder problem using BFS."""

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Returns the number of steps in the shortest transformation sequence.
        Returns 0 if no such sequence exists.
        """
        if endWord not in wordList or not beginWord or not wordList:
            return 0

        L = len(beginWord)

        # 1. Preprocess wordList to find all generic combinations
        # Key is the generic word (e.g. "h*t"), Value is a list of words sharing that pattern.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Replace the i-th character with '*'
                generic_word = word[:i] + "*" + word[i + 1 :]
                all_combo_dict[generic_word].append(word)

        # 2. BFS Initialization
        # Queue stores (current_word, level)
        queue = deque([(beginWord, 1)])
        # Keep track of visited words to avoid cycles
        visited = set([beginWord])

        # 3. Process the queue
        while queue:
            current_word, level = queue.popleft()

            # Find valid next words by trying all possible generic forms of current_word
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1 :]

                # Look up words that match this pattern
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))

                # Optimization: Clear the list for this pattern as we've visited all its neighbors
                # This prevents reprocessing the same edges if we encounter this pattern again
                all_combo_dict[intermediate_word] = []

        return 0


class TestWordLadder(unittest.TestCase):
    """Test cases for Word Ladder."""

    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        """Test the standard example case."""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        # Path: hit -> hot -> dot -> dog -> cog (5 steps)
        # OR: hit -> hot -> lot -> log -> cog (5 steps)
        expected = 5
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

    def test_no_path(self):
        """Test when endWord is not reachable."""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        # 'cog' is not in wordList (or unreachable). Even if 'cog' was target,
        # in this specific input list provided in LeetCode examples, if endWord isn't in list, return 0.
        expected = 0
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

    def test_end_word_not_in_list(self):
        """Test simple case where endWord is missing from list."""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot"]
        expected = 0
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

    def test_direct_match(self):
        """Test case where start and end are 1 step apart."""
        beginWord = "hit"
        endWord = "hot"
        wordList = ["hot", "dot"]
        expected = 2  # hit -> hot
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)


if __name__ == "__main__":
    unittest.main()
