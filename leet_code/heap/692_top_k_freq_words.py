"""
Problem: Top K Frequent Words
Return the k most frequent words, sorted by frequency and then lexicographical order.

Approach:
- Use a min-heap to keep track of the k most frequent words.
- Define a custom comparison for words with equal frequency using a Pair class.
- Maintain heap size at k by removing the "smallest" element.
- Time complexity: O(n log k)
- Space complexity: O(n)
"""

import heapq
import unittest
from collections import Counter
from typing import List


class Pair:
    """Helper class for custom heap comparison logic."""

    def __init__(self, word: str, freq: int):
        self.word = word
        self.freq = freq

    def __lt__(self, other: "Pair") -> bool:
        """
        Custom comparison for min-heap.
        Lower frequency has higher priority for popping.
        If frequencies are equal, lexicographically larger word has higher priority.
        """
        if self.freq == other.freq:
            # Lexicographical comparison: higher string is considered "smaller" in min-heap
            # so it gets popped first, leaving the smaller strings in the heap.
            return self.word > other.word
        return self.freq < other.freq


class Solution:
    """Class to find the top k frequent words in a list."""

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Finds the top k frequent words.

        Args:
            words: List of strings.
            k: Number of top elements to return.

        Returns:
            List of top k frequent words sorted by frequency and lexicographical order.
        """
        if not words or k <= 0:
            return []

        # Count frequencies of each word
        freqs = Counter(words)
        min_heap: List[Pair] = []

        # Maintain a min-heap of size k
        for word, freq in freqs.items():
            heapq.heappush(min_heap, Pair(word, freq))

            # Keep only top k elements
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Build results by popping from min-heap
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap).word)

        # Reverse to get results in descending order of frequency
        res.reverse()

        return res


class TestTopKFrequent(unittest.TestCase):
    """Unit tests for topKFrequent implementation."""

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """LeetCode Example 1."""
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2
        expected = ["i", "love"]
        self.assertEqual(self.solution.topKFrequent(words, k), expected)

    def test_example_2(self):
        """LeetCode Example 2."""
        words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
        k = 4
        expected = ["the", "is", "sunny", "day"]
        self.assertEqual(self.solution.topKFrequent(words, k), expected)

    def test_empty_list(self):
        """Edge case: empty list of words."""
        self.assertEqual(self.solution.topKFrequent([], 0), [])

    def test_single_element(self):
        """Edge case: single word."""
        self.assertEqual(self.solution.topKFrequent(["apple"], 1), ["apple"])

    def test_multiple_k_values(self):
        """Test with different k values using enumerate for cleaner logic."""
        words = ["a", "a", "b", "b", "c"]
        possible_ks = [1, 2, 3]
        expected_results = [["a"], ["a", "b"], ["a", "b", "c"]]

        for i, k in enumerate(possible_ks):
            self.assertEqual(self.solution.topKFrequent(words, k), expected_results[i])


if __name__ == "__main__":
    unittest.main()
