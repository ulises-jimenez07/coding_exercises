"""
Problem: Find the contiguous subarray with the maximum product

Approach:
- Track both max and min products (negatives can become max when multiplied)
- Update both at each position, swap when encountering negative numbers
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = nums[0]
        max_product = nums[0]
        min_product = nums[0]

        for num in nums[1:]:
            if num >= 0:
                max_product = max(max_product * num, num)
                min_product = min(min_product * num, num)
            else:
                temp = max_product
                max_product = max(min_product * num, num)
                min_product = min(temp * num, num)

            result = max(result, max_product)

        return result


class TestMaxProduct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        """Tests empty array."""
        self.assertEqual(self.solution.maxProduct([]), 0)

    def test_single_element_array(self):
        """Tests single element."""
        self.assertEqual(self.solution.maxProduct([5]), 5)
        self.assertEqual(self.solution.maxProduct([-3]), -3)

    def test_positive_numbers(self):
        """Tests positive numbers."""
        self.assertEqual(self.solution.maxProduct([2, 3, -2, 4]), 6)
        self.assertEqual(self.solution.maxProduct([1, 2, 3, 4]), 24)

    def test_negative_numbers(self):
        """Tests negative numbers."""
        self.assertEqual(self.solution.maxProduct([-2, 0, -1]), 0)
        self.assertEqual(self.solution.maxProduct([-2, -3, -4]), 12)  # -3 * -4 = 12, not 24
        self.assertEqual(self.solution.maxProduct([-1, -2, -3, 0]), 6)

    def test_mixed_numbers(self):
        """Arrays with mixed positive and negative numbers."""
        self.assertEqual(self.solution.maxProduct([-2, 3, -4]), 24)
        self.assertEqual(self.solution.maxProduct([0, 2]), 2)
        self.assertEqual(self.solution.maxProduct([-4, -3, -2]), 12)  # -3 * -4 = 12
        self.assertEqual(self.solution.maxProduct([2, -5, -2, -4, 3]), 24)  # -2 * -4 * 3 = 24

    def test_array_with_zeros(self):
        """Arrays containing zeros."""
        self.assertEqual(self.solution.maxProduct([0, 0, 0]), 0)
        self.assertEqual(self.solution.maxProduct([1, -2, 0, 3]), 3)
        self.assertEqual(self.solution.maxProduct([-1, -2, -3, 0, -4, -5]), 20)  # -4 * -5 = 20


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
