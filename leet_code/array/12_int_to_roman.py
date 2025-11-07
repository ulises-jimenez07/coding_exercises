"""
Problem: Convert an integer to a Roman numeral string

Approach:
- Use greedy approach with value-symbol pairs from largest to smallest
- Apply each symbol as many times as possible before moving to next
- Time complexity: O(1) - fixed number of symbols
- Space complexity: O(1)
"""

import unittest


class Solution:
    def intToRoman(self, num: int) -> str:
        """Converts an integer to a Roman numeral string."""
        digits = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman_digits = []

        for value, symbol in digits:
            if num == 0:
                break
            count, num = divmod(num, value)
            roman_digits.append(symbol * count)
        return "".join(roman_digits)


class TestIntToRoman(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_numbers(self):
        self.assertEqual(self.solution.intToRoman(1), "I")
        self.assertEqual(self.solution.intToRoman(5), "V")
        self.assertEqual(self.solution.intToRoman(10), "X")
        self.assertEqual(self.solution.intToRoman(50), "L")
        self.assertEqual(self.solution.intToRoman(100), "C")
        self.assertEqual(self.solution.intToRoman(500), "D")
        self.assertEqual(self.solution.intToRoman(1000), "M")

    def test_additive_numbers(self):
        self.assertEqual(self.solution.intToRoman(2), "II")
        self.assertEqual(self.solution.intToRoman(3), "III")
        self.assertEqual(self.solution.intToRoman(6), "VI")
        self.assertEqual(self.solution.intToRoman(7), "VII")
        self.assertEqual(self.solution.intToRoman(8), "VIII")
        self.assertEqual(self.solution.intToRoman(11), "XI")
        self.assertEqual(self.solution.intToRoman(12), "XII")
        self.assertEqual(self.solution.intToRoman(13), "XIII")

    def test_subtractive_numbers(self):
        self.assertEqual(self.solution.intToRoman(4), "IV")
        self.assertEqual(self.solution.intToRoman(9), "IX")
        self.assertEqual(self.solution.intToRoman(40), "XL")
        self.assertEqual(self.solution.intToRoman(90), "XC")
        self.assertEqual(self.solution.intToRoman(400), "CD")
        self.assertEqual(self.solution.intToRoman(900), "CM")

    def test_complex_numbers(self):
        self.assertEqual(self.solution.intToRoman(1994), "MCMXCIV")
        self.assertEqual(self.solution.intToRoman(3999), "MMMCMXCIX")
        self.assertEqual(self.solution.intToRoman(1666), "MDCLXVI")
        self.assertEqual(self.solution.intToRoman(14), "XIV")
        self.assertEqual(self.solution.intToRoman(19), "XIX")
        self.assertEqual(self.solution.intToRoman(99), "XCIX")
        self.assertEqual(self.solution.intToRoman(999), "CMXCIX")


if __name__ == "__main__":
    unittest.main()
