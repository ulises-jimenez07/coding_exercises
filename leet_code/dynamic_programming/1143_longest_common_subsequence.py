"""
Problem: Find the length of the longest common subsequence between two strings.

Approach:
- Approach 1: Top-down dynamic programming with memoization (O(m*n) time/space)
- Approach 2: Bottom-up iterative dynamic programming (O(m*n) time/space)

Example: "abcde" and "ace" -> LCS is "ace" with length 3
"""

import unittest


class SolutionV1:
    """Longest Common Subsequence using top-down recursion with memoization."""

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo: dict[tuple[int, int], int] = {}
        return self._lcs(text1, text2, len(text1) - 1, len(text2) - 1, memo)

    # pylint: disable=too-many-arguments,too-many-positional-arguments
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


class SolutionV2:
    """Longest Common Subsequence using bottom-up iterative dynamic programming."""

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        # dp[i][j] stores the LCS length for substrings s1[i:] and s2[j:]
        # Extra row and column (all zeros) handle base cases where either string is exhausted
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        # Iterate through both strings backwards
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                # If characters match, LCS length is 1 + LCS length of remaining substrings
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # If characters don't match, take the maximum of skipping a character from s1 or s2
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # Result is stored at the beginning of the table
        return dp[0][0]


class TestSolutions(unittest.TestCase):
    """Unit tests for Longest Common Subsequence implementations."""

    def setUp(self):
        self.solutions = [SolutionV1(), SolutionV2()]

    def test_common_subsequence(self):
        """Tests a case where a common subsequence exists."""
        for sol in self.solutions:
            with self.subTest(solver=type(sol).__name__):
                self.assertEqual(sol.longestCommonSubsequence("abcde", "ace"), 3)

    def test_no_common_subsequence(self):
        """Tests a case with no common subsequence."""
        for sol in self.solutions:
            with self.subTest(solver=type(sol).__name__):
                self.assertEqual(sol.longestCommonSubsequence("abc", "def"), 0)

    def test_one_string_is_subsequence(self):
        """Tests a case where one string is a subsequence of the other."""
        for sol in self.solutions:
            with self.subTest(solver=type(sol).__name__):
                self.assertEqual(sol.longestCommonSubsequence("ab", "acb"), 2)

    def test_empty_strings(self):
        """Tests cases with empty strings."""
        for sol in self.solutions:
            with self.subTest(solver=type(sol).__name__):
                self.assertEqual(sol.longestCommonSubsequence("", "abc"), 0)
                self.assertEqual(sol.longestCommonSubsequence("abc", ""), 0)

    def test_identical_strings(self):
        """Tests a case with identical strings."""
        for sol in self.solutions:
            with self.subTest(solver=type(sol).__name__):
                self.assertEqual(sol.longestCommonSubsequence("abcde", "abcde"), 5)

    def test_longer_example(self):
        """Tests a longer example."""
        for sol in self.solutions:
            with self.subTest(solver=type(sol).__name__):
                self.assertEqual(sol.longestCommonSubsequence("AGGTAB", "GXTXAYB"), 4)


if __name__ == "__main__":
    unittest.main()
