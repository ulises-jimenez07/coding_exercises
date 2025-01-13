import unittest


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        Formats a license key string by grouping characters into segments of length k.

        The characters in the license key string are alphanumeric, and the key contains hyphens '-'.
        The function removes all hyphens, converts characters to uppercase, and groups the characters into segments of length k.
        The segments are separated by hyphens. The first segment may have fewer than k characters.

        Args:
            s: The license key string.
            k: The length of each segment.

        Returns:
            The formatted license key string.
        """

        res = []  # Initialize a list to store the formatted characters
        i = 0  # Counter for characters within a segment
        # Iterate through the input string in reverse order
        for c in reversed(s):
            if c != "-":  # Ignore hyphens
                res.append(c.upper())  # Add the uppercase character to the result
                i += 1  # Increment the character counter
                if i == k:  # If a segment is complete
                    i = 0  # Reset the character counter
                    res.append("-")  # Add a hyphen separator

        # Remove the trailing hyphen if present
        if len(res) > 0 and res[-1] == "-":
            res = res[:-1]

        res = res[::-1]  # reverse string
        return "".join(res)  # Return the formatted string


class TestLicenseKeyFormatting(unittest.TestCase):
    def test_example_1(self):
        s = "5F3Z-2e-9-w"
        k = 4
        expected = "5F3Z-2E9W"
        self.assertEqual(Solution().licenseKeyFormatting(s, k), expected)

    def test_example_2(self):
        s = "2-5g-3-J"
        k = 2
        expected = "2-5G-3J"
        self.assertEqual(Solution().licenseKeyFormatting(s, k), expected)

    def test_empty_string(self):
        s = ""
        k = 2
        expected = ""
        self.assertEqual(Solution().licenseKeyFormatting(s, k), expected)

    def test_all_hyphens(self):
        s = "----"
        k = 2
        expected = ""
        self.assertEqual(Solution().licenseKeyFormatting(s, k), expected)

    def test_single_character(self):
        s = "a"
        k = 1
        expected = "A"
        self.assertEqual(Solution().licenseKeyFormatting(s, k), expected)

    def test_no_hyphens(self):
        s = "abcdef"
        k = 2
        expected = "AB-CD-EF"
        self.assertEqual(Solution().licenseKeyFormatting(s, k), expected)

    def test_leading_hyphens(self):
        s = "--a-b-c"
        k = 2
        expected = "A-BC"
        self.assertEqual(Solution().licenseKeyFormatting(s, k), expected)


if __name__ == "__main__":
    unittest.main()
