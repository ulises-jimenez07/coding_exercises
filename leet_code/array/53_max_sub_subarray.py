"""
Problem: Find the contiguous subarray with the largest sum (Kadane's algorithm)

Approach:
- Track current sum, reset to 0 if negative, update max at each step
- Single pass through array keeping running sum
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Finds the contiguous subarray with the largest sum."""
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum = max(0, curr_sum) + num
            max_sum = max(max_sum, curr_sum)

        return max_sum


class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        self.assertEqual(self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_all_negative(self):
        self.assertEqual(self.solution.maxSubArray([-2, -1, -3, -4, -1]), -1)

    def test_all_positive(self):
        self.assertEqual(self.solution.maxSubArray([1, 2, 3, 4, 5]), 15)

    def test_single_element(self):
        self.assertEqual(self.solution.maxSubArray([1]), 1)

    def test_single_negative_element(self):
        self.assertEqual(self.solution.maxSubArray([-1]), -1)

    def test_empty_list(self):
        # Edge case: empty list
        with self.assertRaises(IndexError):
            self.solution.maxSubArray([])

    def test_mixed_numbers(self):
        self.assertEqual(self.solution.maxSubArray([-1, 2, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_start_with_negative(self):
        self.assertEqual(self.solution.maxSubArray([-2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
