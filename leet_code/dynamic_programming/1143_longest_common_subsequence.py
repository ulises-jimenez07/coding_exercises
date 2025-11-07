"""
Problem: Find the length of the longest common subsequence between two strings.

Approach:
- Use top-down dynamic programming with memoization
- Compare characters from the end of both strings
- If characters match, add 1 and move both pointers back
- If not, take max of moving either pointer back
- Time complexity: O(m * n) where m, n are string lengths
- Space complexity: O(m * n) for memoization dictionary

Example: "abcde" and "ace" -> LCS is "ace" with length 3
"""

import unittest


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo: dict[tuple[int, int], int] = {}
        return self._lcs(text1, text2, len(text1) - 1, len(text2) - 1, memo)

    def _lcs(self, text1, text2, i, j, memo):
        # Base case: exhausted one string
        if i < 0 or j < 0:
            return 0

        # Return cached result if available
        if (i, j) in memo:
            return memo[(i, j)]

        # Characters match: include and move both pointers
        if text1[i] == text2[j]:
            memo[(i, j)] = 1 + self._lcs(text1, text2, i - 1, j - 1, memo)
        else:
            # Characters differ: try skipping from either string
            memo[(i, j)] = max(self._lcs(text1, text2, i - 1, j, memo), self._lcs(text1, text2, i, j - 1, memo))

        return memo[(i, j)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_common_subsequence(self):
        """Tests a case where a common subsequence exists."""
        self.assertEqual(self.solution.longestCommonSubsequence("abcde", "ace"), 3)

    def test_no_common_subsequence(self):
        """Tests a case with no common subsequence."""
        self.assertEqual(self.solution.longestCommonSubsequence("abc", "def"), 0)

    def test_one_string_is_subsequence(self):
        """Tests a case where one string is a subsequence of the other."""
        self.assertEqual(self.solution.longestCommonSubsequence("ab", "acb"), 2)

    def test_empty_strings(self):
        """Tests cases with empty strings."""
        self.assertEqual(self.solution.longestCommonSubsequence("", "abc"), 0)
        self.assertEqual(self.solution.longestCommonSubsequence("abc", ""), 0)

    def test_identical_strings(self):
        """Tests a case with identical strings."""
        self.assertEqual(self.solution.longestCommonSubsequence("abcde", "abcde"), 5)

    def test_longer_example(self):
        """Tests a longer example."""
        self.assertEqual(self.solution.longestCommonSubsequence("AGGTAB", "GXTXAYB"), 4)


if __name__ == "__main__":
    unittest.main()
