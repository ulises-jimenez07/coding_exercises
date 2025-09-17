class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        This function computes the length of the longest common subsequence (LCS)
        of two strings using a recursive approach with memoization.
        It initializes a dictionary for memoization and calls a helper function.

        Args:
            text1 (str): The first string.
            text2 (str): The second string.

        Returns:
            int: The length of the longest common subsequence.
        """
        self.dp = {}  # Dictionary to store results of subproblems (memoization)
        self.text1 = text1
        self.text2 = text2
        n = len(text1)
        m = len(text2)
        return self.lcs(n - 1, m - 1)

    def lcs(self, i, j):
        """
        A recursive helper function to find the length of the LCS.

        Args:
            i (int): The current index of the first string.
            j (int): The current index of the second string.

        Returns:
            int: The length of the LCS of substrings up to indices i and j.
        """
        # Base case: if either index goes below 0, there's no common subsequence
        if i == -1 or j == -1:
            return 0

        # Check if the result for the current subproblem is already computed
        if (i, j) in self.dp:
            return self.dp[(i, j)]

        # If the characters at the current indices match
        if self.text1[i] == self.text2[j]:
            # The LCS length is 1 plus the LCS of the remaining strings
            self.dp[(i, j)] = 1 + self.lcs(i - 1, j - 1)
        else:
            # If characters don't match, the LCS is the maximum of two possibilities:
            # 1. Excluding the last character of text1
            # 2. Excluding the last character of text2
            self.dp[(i, j)] = max(self.lcs(i - 1, j), self.lcs(i, j - 1))

        return self.dp[(i, j)]


# --- Unit Tests ---
import unittest


class TestSolution(unittest.TestCase):
    def test_longestCommonSubsequence(self):
        # Test case 1: Common subsequence exists
        sol = Solution()
        self.assertEqual(sol.longestCommonSubsequence("abcde", "ace"), 3)

        # Test case 2: No common subsequence
        sol = Solution()
        self.assertEqual(sol.longestCommonSubsequence("abc", "def"), 0)

        # Test case 3: One string is a subsequence of the other
        sol = Solution()
        self.assertEqual(sol.longestCommonSubsequence("ab", "acb"), 2)

        # Test case 4: Empty strings
        sol = Solution()
        self.assertEqual(sol.longestCommonSubsequence("", "abc"), 0)

        sol = Solution()
        self.assertEqual(sol.longestCommonSubsequence("abc", ""), 0)

        # Test case 5: Identical strings
        sol = Solution()
        self.assertEqual(sol.longestCommonSubsequence("abcde", "abcde"), 5)

        # Test case 6: Longer example
        sol = Solution()
        self.assertEqual(sol.longestCommonSubsequence("AGGTAB", "GXTXAYB"), 4)  # GTAB or GXTAB


if __name__ == "__main__":
    unittest.main()
