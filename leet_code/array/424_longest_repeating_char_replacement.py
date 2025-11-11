"""
Problem: Longest Repeating Character Replacement

Given a string s and an integer k, you can choose any character of the string
and change it to any other uppercase English character. You can perform this
operation at most k times. Return the length of the longest substring containing
the same letter you can get after performing the above operations.

Approach 1 (Brute Force with Sliding Window):
- For each unique character in the string, treat it as the target character
- Use sliding window to find the longest substring where we can replace
  at most k characters to make all characters equal to the target
- Time complexity: O(26 * n) = O(n) where n is the length of string
- Space complexity: O(1) since we only track 26 unique letters at most

Approach 2 (Optimized Sliding Window with Frequency Map):
- Use sliding window with a frequency map to track character counts
- Keep track of the maximum frequency of any character in current window
- Window is valid if: window_length - max_frequency <= k
  (we can replace the non-max-frequency characters)
- Time complexity: O(n)
- Space complexity: O(26) = O(1) for the frequency map
"""

import unittest
from collections import defaultdict


class Solution:
    """Solution using character-by-character approach with sliding window."""

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring with at most k replacements.
        Uses the approach of iterating through each unique character.
        """
        all_letters = set(s)
        max_length = 0

        # Try each unique character as the target character
        for letter in all_letters:
            left = 0
            updates = 0  # Count of characters that need to be replaced

            for right, ch in enumerate(s):
                # If current character is not the target, we need to replace it
                if ch != letter:
                    updates += 1

                # Shrink window if we've exceeded k replacements
                while updates > k:
                    if s[left] != letter:
                        updates -= 1
                    left += 1

                # Update max length with current valid window
                max_length = max(right - left + 1, max_length)

        return max_length


class SolutionOptimized:
    """Optimized solution using frequency map and maximum frequency tracking."""

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Optimized approach using frequency map and max frequency tracking.
        More efficient as it only makes one pass through the string.
        """
        freq_map: defaultdict[str, int] = defaultdict(int)
        left = 0
        max_freq = 0  # Maximum frequency of any character in current window
        longest_sub_length = 0

        for right, char in enumerate(s):
            # Add current character to window
            freq_map[char] += 1
            # Update max frequency seen in current window
            max_freq = max(max_freq, freq_map[char])

            # Check if current window is valid
            # Valid if: (window_length - max_freq) <= k
            # This means we can replace the remaining characters
            is_valid = (right - left + 1 - max_freq) <= k

            if not is_valid:
                # Shrink window from left
                freq_map[s[left]] -= 1
                left += 1

            # Update longest substring length
            longest_sub_length = right - left + 1

        return longest_sub_length


class TestCharacterReplacement(unittest.TestCase):
    """Unit tests for the Longest Repeating Character Replacement problem."""

    def setUp(self):
        self.solution = Solution()
        self.solution_optimized = SolutionOptimized()

    def test_example_1(self):
        """Test case: ABAB with k=2"""
        s = "ABAB"
        k = 2
        expected = 4  # Can replace both B's to get "AAAA"
        self.assertEqual(self.solution.characterReplacement(s, k), expected)
        self.assertEqual(self.solution_optimized.characterReplacement(s, k), expected)

    def test_example_2(self):
        """Test case: AABABBA with k=1"""
        s = "AABABBA"
        k = 1
        expected = 4  # Can get "AAAA" or "BBBB"
        self.assertEqual(self.solution.characterReplacement(s, k), expected)
        self.assertEqual(self.solution_optimized.characterReplacement(s, k), expected)

    def test_all_same_characters(self):
        """Test case: All characters are the same"""
        s = "AAAA"
        k = 2
        expected = 4  # Already all the same
        self.assertEqual(self.solution.characterReplacement(s, k), expected)
        self.assertEqual(self.solution_optimized.characterReplacement(s, k), expected)

    def test_k_zero(self):
        """Test case: k=0, no replacements allowed"""
        s = "ABCDE"
        k = 0
        expected = 1  # Can only take single character
        self.assertEqual(self.solution.characterReplacement(s, k), expected)
        self.assertEqual(self.solution_optimized.characterReplacement(s, k), expected)

    def test_single_character(self):
        """Test case: Single character string"""
        s = "A"
        k = 1
        expected = 1
        self.assertEqual(self.solution.characterReplacement(s, k), expected)
        self.assertEqual(self.solution_optimized.characterReplacement(s, k), expected)

    def test_replace_all(self):
        """Test case: Can replace entire string"""
        s = "ABCD"
        k = 3
        expected = 4  # Can replace 3 characters to make all same
        self.assertEqual(self.solution.characterReplacement(s, k), expected)
        self.assertEqual(self.solution_optimized.characterReplacement(s, k), expected)


if __name__ == "__main__":
    unittest.main()
