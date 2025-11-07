"""
Problem: Increment an integer represented as a list of digits by one

Approach:
- Process digits right to left, handling carry propagation
- Insert new digit at front if final carry exists
- Time complexity: O(n)
- Space complexity: O(1) or O(n) if new digit needed
"""

import unittest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Increments the integer represented as a list of digits by one."""
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i], carry = (digits[i] + carry) % 10, (digits[i] + carry) // 10
            if carry == 0:
                break
        if carry:
            digits.insert(0, carry)
        return digits


class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_digit(self):
        self.assertEqual(self.solution.plusOne([0]), [1])
        self.assertEqual(self.solution.plusOne([5]), [6])
        self.assertEqual(self.solution.plusOne([9]), [1, 0])

    def test_multiple_digits_no_carry(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_multiple_digits_with_carry(self):
        self.assertEqual(self.solution.plusOne([1, 9, 9]), [2, 0, 0])
        self.assertEqual(self.solution.plusOne([9, 9, 9]), [1, 0, 0, 0])
        self.assertEqual(self.solution.plusOne([9, 8, 9]), [9, 9, 0])

    def test_leading_zeros(self):
        """Handle leading zeros."""
        self.assertEqual(self.solution.plusOne([0, 0, 1]), [0, 0, 2])


if __name__ == "__main__":
    unittest.main()
