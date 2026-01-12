"""
Problem: Find all start indices of anagrams of string p in string s.

Approach:
- Use a sliding window with character frequency counters.
- Update the window as we iterate through s.
- Time complexity: O(ns) where ns is the length of s.
- Space complexity: O(1) as counters are capped by the alphabet size.
"""

import unittest
from collections import Counter
from typing import List


class Solution:
    """Provides methods to find anagram patterns within text strings."""

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Returns start indices of all p's anagrams found in s."""
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count: Counter[str] = Counter(p)
        s_count: Counter[str] = Counter()
        output = []

        for i, char in enumerate(s):
            # Include current character in window
            s_count[char] += 1

            # Maintain fixed window size by removing left-most character
            if i >= np:
                left_char = s[i - np]
                if s_count[left_char] == 1:
                    del s_count[left_char]
                else:
                    s_count[left_char] -= 1

            # Check if current window matches p's frequency
            if p_count == s_count:
                output.append(i - np + 1)

        return output


class TestFindAnagrams(unittest.TestCase):
    """Test suite for the findAnagrams implementation."""

    def setUp(self):
        self.solution = Solution()

    def test_leetcode_examples(self):
        """Verify standard LeetCode test cases."""
        self.assertEqual(self.solution.findAnagrams("cbaebabacd", "abc"), [0, 6])
        self.assertEqual(self.solution.findAnagrams("abab", "ab"), [0, 1, 2])

    def test_edge_cases(self):
        """Verify behavior with minimal or mismatched input sizes."""
        # Pattern longer than string
        self.assertEqual(self.solution.findAnagrams("a", "ab"), [])
        # Empty source string
        self.assertEqual(self.solution.findAnagrams("", "a"), [])
        # Single character match
        self.assertEqual(self.solution.findAnagrams("a", "a"), [0])

    def test_no_matches(self):
        """Verify behavior when no anagrams exist."""
        self.assertEqual(self.solution.findAnagrams("apple", "pie"), [])

    def test_repeated_characters(self):
        """Verify overlapping anagram matches."""
        self.assertEqual(self.solution.findAnagrams("aaaaa", "aa"), [0, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()
