"""
Problem: Sorted Squares
Given a sorted integer array, return the squares of each number in sorted order.

Approach:
- The largest square must come from one of the two ends
- Use two pointers and fill the result from right to left
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest


class Solution:
    """Two-pointer solution for LeetCode 977."""

    def sortedSquares(self, nums):
        """Return sorted squares for a non-decreasing sorted array."""
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for index in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] ** 2
                left += 1
            else:
                result[index] = nums[right] ** 2
                right -= 1

        return result


class TestSortedSquares(unittest.TestCase):
    """Unit tests for Solution.sortedSquares."""

    def setUp(self):
        self.solution = Solution()

    def test_mixed_numbers(self):
        nums = [-4, -1, 0, 3, 10]

        self.assertEqual(self.solution.sortedSquares(nums), [0, 1, 9, 16, 100])

    def test_duplicate_negative_numbers(self):
        nums = [-7, -3, 2, 3, 11]

        self.assertEqual(self.solution.sortedSquares(nums), [4, 9, 9, 49, 121])

    def test_all_negative(self):
        nums = [-5, -3, -2]

        self.assertEqual(self.solution.sortedSquares(nums), [4, 9, 25])

    def test_all_positive(self):
        nums = [1, 2, 3]

        self.assertEqual(self.solution.sortedSquares(nums), [1, 4, 9])

    def test_empty_array(self):
        self.assertEqual(self.solution.sortedSquares([]), [])

    def test_single_element(self):
        self.assertEqual(self.solution.sortedSquares([-4]), [16])


if __name__ == "__main__":
    unittest.main()
