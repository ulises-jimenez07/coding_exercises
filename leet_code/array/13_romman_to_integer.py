"""
Problem: Convert a Roman numeral string to an integer

Approach:
- Process characters left to right, handling subtractive notation
- If current symbol is less than next, subtract it; otherwise add it
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        """Converts a Roman numeral string to an integer."""
        if len(s) < 1:
            return 0

        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0
        i = 0
        while i < len(s):
            # Handle subtractive combinations (IV, IX, XL, XC, CD, CM)
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                res += roman_map[s[i + 1]] - roman_map[s[i]]
                i += 2
            else:
                res += roman_map[s[i]]
                i += 1

        return res


class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertEqual(self.solution.romanToInt(""), 0)

    def test_single_characters(self):
        self.assertEqual(self.solution.romanToInt("I"), 1)
        self.assertEqual(self.solution.romanToInt("V"), 5)
        self.assertEqual(self.solution.romanToInt("X"), 10)
        self.assertEqual(self.solution.romanToInt("L"), 50)
        self.assertEqual(self.solution.romanToInt("C"), 100)
        self.assertEqual(self.solution.romanToInt("D"), 500)
        self.assertEqual(self.solution.romanToInt("M"), 1000)

    def test_additive_combinations(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)
        self.assertEqual(self.solution.romanToInt("VIII"), 8)
        self.assertEqual(self.solution.romanToInt("XXI"), 21)
        self.assertEqual(self.solution.romanToInt("LXXX"), 80)

    def test_subtractive_combinations(self):
        self.assertEqual(self.solution.romanToInt("IV"), 4)
        self.assertEqual(self.solution.romanToInt("IX"), 9)
        self.assertEqual(self.solution.romanToInt("XIV"), 14)
        self.assertEqual(self.solution.romanToInt("XIX"), 19)
        self.assertEqual(self.solution.romanToInt("XCIX"), 99)
        self.assertEqual(self.solution.romanToInt("CMXCIX"), 999)

    def test_complex_examples(self):
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)
        self.assertEqual(self.solution.romanToInt("MDCLXVI"), 1666)
        self.assertEqual(self.solution.romanToInt("MMMCMXCIX"), 3999)


if __name__ == "__main__":
    unittest.main()
