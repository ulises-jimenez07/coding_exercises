def lps(input_str):
    """
    Finds the length of the longest palindromic subsequence (LPS) in a given string.

    A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
    A palindrome is a string that reads the same forwards and backward.

    Args:
        input_str: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(input_str)  # Get the length of the input string

    # Create a 2D table to store lengths of LPS of substrings
    # L[i][j] stores the length of LPS of substring input_str[i..j]
    L = [[0 for _ in range(n)] for _ in range(n)]

    # Strings of length 1 are palindromes of length 1
    for i in range(n):
        L[i][i] = 1

    # Iterate through substrings of length cl (from 2 to n)
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1  # Ending index of the substring
            if input_str[i] == input_str[j] and cl == 2:
                # If the substring is of length 2 and the characters match, it's a palindrome of length 2
                L[i][j] = 2
            elif input_str[i] == input_str[j]:
                # If the characters match, the LPS is 2 + LPS of the inner substring
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                # If the characters don't match, the LPS is the maximum of LPS of substrings excluding either the first or last character
                L[i][j] = max(L[i][j - 1], L[i + 1][j])

    # L[0][n-1] contains the length of LPS of the entire string
    return L[0][n - 1]


import unittest


class TestLPS(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(lps(""), 0)

    def test_single_char_string(self):
        self.assertEqual(lps("a"), 1)

    def test_palindrome_string(self):
        self.assertEqual(lps("madam"), 5)

    def test_non_palindrome_string(self):
        self.assertEqual(lps("bananas"), 5)

    def test_another_non_palindrome_string(self):
        self.assertEqual(lps("agbdba"), 5)

    def test_long_string(self):
        self.assertEqual(lps("character"), 5)


if __name__ == "__main__":
    unittest.main()
