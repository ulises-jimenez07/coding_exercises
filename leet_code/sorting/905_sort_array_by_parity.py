"""
Problem: Sort an array such that even numbers come before odd numbers

Approach:
- Use two pointers: one for the next available even position, one for scanning
- Swap even numbers to the front as they are encountered
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Namespace for the solution to LeetCode 905: Sort Array By Parity."""

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """Moves all even integers to the beginning of the array."""
        swap = 0

        for i, num in enumerate(nums):
            # If current number is even, swap it to the front
            if num % 2 == 0:
                nums[swap], nums[i] = nums[i], nums[swap]
                swap += 1

        return nums


class TestSortByParity(unittest.TestCase):
    """Unit tests for the Sort Array By Parity solution."""

    def setUp(self):
        self.solution = Solution()

    def test_mixed_numbers(self):
        """Mixed even and odd numbers."""
        nums = [3, 1, 2, 4]
        result = self.solution.sortArrayByParity(nums)
        # Check if all even numbers are before odd numbers
        evens = [x for x in result if x % 2 == 0]
        odds = [x for x in result if x % 2 != 0]
        self.assertEqual(result[: len(evens)], evens)
        self.assertEqual(result[len(evens) :], odds)

    def test_already_sorted(self):
        """Array already sorted by parity."""
        nums = [2, 4, 1, 3]
        result = self.solution.sortArrayByParity(nums.copy())
        self.assertEqual(result, [2, 4, 1, 3])

    def test_all_even(self):
        """Array with only even numbers."""
        nums = [2, 4, 6]
        result = self.solution.sortArrayByParity(nums.copy())
        self.assertEqual(result, [2, 4, 6])

    def test_all_odd(self):
        """Array with only odd numbers."""
        nums = [1, 3, 5]
        result = self.solution.sortArrayByParity(nums.copy())
        self.assertEqual(result, [1, 3, 5])

    def test_empty_list(self):
        """Empty input list."""
        nums = []
        result = self.solution.sortArrayByParity(nums)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
