"""
Problem: Find the smallest integer with the same digits that is greater than n.

Approach:
- Use the next permutation algorithm on the digits of n.
- Find the first digit that is smaller than the one to its right.
- Swap it with the smallest digit greater than it to its right.
- Reverse the suffix to get the smallest possible greater combination.
- Time complexity: O(L) where L is the number of digits.
- Space complexity: O(L) for the digit array.
"""

import unittest
from typing import List


class Solution:
    """Provides methods to find the next greater element with same digits."""

    def nextGreaterElement(self, n: int) -> int:
        """Finds the smallest integer with same digits greater than n."""

        def reverse(digits: List[str], start: int) -> None:
            """Reverses a portion of the list in-place."""
            left, right = start, len(digits) - 1
            while left < right:
                digits[left], digits[right] = digits[right], digits[left]
                left += 1
                right -= 1

        digits = list(str(n))
        size = len(digits)

        # Step 1: Find first decreasing digit from right
        i = size - 2
        while i >= 0 and digits[i + 1] <= digits[i]:
            i -= 1

        # If no such digit found, no greater element possible
        if i < 0:
            return -1

        pivot = i

        # Step 2: Find smallest digit greater than pivot from the right
        j = -1
        for idx, char in reversed(list(enumerate(digits))):
            if char > digits[pivot]:
                j = idx
                break

        # Step 3: Swap pivot with larger digit
        digits[pivot], digits[j] = digits[j], digits[pivot]

        # Step 4: Reverse suffix to get smallest arrangement
        reverse(digits, pivot + 1)

        result = int("".join(digits))

        # Ensure result fits in 32-bit signed integer
        return result if result <= 2**31 - 1 else -1


class TestNextGreaterElement(unittest.TestCase):
    """Unit tests for the nextGreaterElement function."""

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """LeetCode basic example 1."""
        self.assertEqual(self.solution.nextGreaterElement(12), 21)

    def test_example_2(self):
        """LeetCode basic example 2 (no greater possible)."""
        self.assertEqual(self.solution.nextGreaterElement(21), -1)

    def test_three_digits(self):
        """Test with three digits."""
        self.assertEqual(self.solution.nextGreaterElement(123), 132)

    def test_large_value(self):
        """Test with 32-bit overflow."""
        # Max 32-bit signed int is 2,147,483,647
        # 2147483476 next would be 2147483647 (fits)
        # 2147483647 next would be -1 (overflows if we could rearrange,
        # but actually all permutations are smaller or overflow)
        self.assertEqual(self.solution.nextGreaterElement(1999999999), -1)

    def test_single_element(self):
        """Single digit integer should return -1."""
        self.assertEqual(self.solution.nextGreaterElement(1), -1)

    def test_all_same_digits(self):
        """Integer with same digits should return -1."""
        self.assertEqual(self.solution.nextGreaterElement(111), -1)

    def test_complex_case(self):
        """A more complex rearrangement."""
        self.assertEqual(self.solution.nextGreaterElement(230241), 230412)


if __name__ == "__main__":
    unittest.main()
