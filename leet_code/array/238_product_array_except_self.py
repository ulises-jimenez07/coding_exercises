"""
Problem: Return array where each element is the product of all elements except itself

Approach:
- Build left and right product arrays for products before and after each index
- Multiply corresponding left and right products for final result
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        output = []
        for i in range(0, n):
            output.append(left[i] * right[i])

        return output


class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Tests basic case."""
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_zeros(self):
        """Tests with zero."""
        self.assertEqual(self.solution.productExceptSelf([1, 0, 3, 4]), [0, 12, 0, 0])

    def test_all_zeros(self):
        """Tests all zeros."""
        self.assertEqual(self.solution.productExceptSelf([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_negative_numbers(self):
        """Tests negative numbers."""
        self.assertEqual(self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_single_element(self):
        """Tests single element."""
        self.assertEqual(self.solution.productExceptSelf([5]), [1])


if __name__ == "__main__":
    unittest.main()
