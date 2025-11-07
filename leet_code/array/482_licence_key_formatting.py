"""
Problem: Format license key by grouping characters into segments of length k

Approach:
- Process from right to left to handle variable first group size
- Build groups of k characters, converting to uppercase
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """Formats license key by grouping characters into segments of length k."""
        res = []
        i = 0

        for c in reversed(s):
            if c != "-":
                res.append(c.upper())
                i += 1
                if i == k:
                    i = 0
                    res.append("-")

        if len(res) > 0 and res[-1] == "-":
            res = res[:-1]

        return "".join(reversed(res))


class TestLicenseKeyFormatting(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Basic example."""
        self.assertEqual(self.solution.licenseKeyFormatting("5F3Z-2e-9-w", 4), "5F3Z-2E9W")

    def test_example_2(self):
        """Another basic example."""
        self.assertEqual(self.solution.licenseKeyFormatting("2-5g-3-J", 2), "2-5G-3J")

    def test_empty_string(self):
        """Empty string."""
        self.assertEqual(self.solution.licenseKeyFormatting("", 2), "")

    def test_all_hyphens(self):
        """All hyphens."""
        self.assertEqual(self.solution.licenseKeyFormatting("----", 2), "")

    def test_single_character(self):
        """Single character."""
        self.assertEqual(self.solution.licenseKeyFormatting("a", 1), "A")

    def test_no_hyphens(self):
        """No hyphens."""
        self.assertEqual(self.solution.licenseKeyFormatting("abcdef", 2), "AB-CD-EF")

    def test_leading_hyphens(self):
        """Leading hyphens."""
        self.assertEqual(self.solution.licenseKeyFormatting("--a-b-c", 2), "A-BC")


if __name__ == "__main__":
    unittest.main()
