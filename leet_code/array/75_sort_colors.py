"""
Problem: Sort array containing 0s, 1s, and 2s in-place (Dutch National Flag)

Approach:
- Use three pointers to partition array into three sections
- Move 0s to left, 2s to right, 1s stay in middle
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sorts array containing 0s, 1s, and 2s in-place using Dutch National Flag algorithm."""
        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            else:
                i += 1


class TestSortColors(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Example 1."""
        nums = [2, 0, 2, 1, 1, 0]
        expected = [0, 0, 1, 1, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_example_2(self):
        """Example 2."""
        nums = [2, 0, 1]
        expected = [0, 1, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_already_sorted(self):
        """Already sorted."""
        nums = [0, 0, 1, 1, 2, 2]
        expected = [0, 0, 1, 1, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_reverse_sorted(self):
        """Reverse sorted."""
        nums = [2, 2, 1, 1, 0, 0]
        expected = [0, 0, 1, 1, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_all_zeros(self):
        """All zeros."""
        nums = [0, 0, 0]
        expected = [0, 0, 0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_all_ones(self):
        """All ones."""
        nums = [1, 1, 1, 1]
        expected = [1, 1, 1, 1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_all_twos(self):
        """All twos."""
        nums = [2, 2]
        expected = [2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_zeros_and_ones(self):
        """Zeros and ones."""
        nums = [1, 0, 1, 0, 0]
        expected = [0, 0, 0, 1, 1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_ones_and_twos(self):
        """Ones and twos."""
        nums = [2, 1, 2, 1, 1]
        expected = [1, 1, 1, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_zeros_and_twos(self):
        """Zeros and twos."""
        nums = [0, 2, 0, 2, 2, 0]
        expected = [0, 0, 0, 2, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_single_element_zero(self):
        """Single zero."""
        nums = [0]
        expected = [0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_single_element_one(self):
        """Single one."""
        nums = [1]
        expected = [1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_single_element_two(self):
        """Single two."""
        nums = [2]
        expected = [2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_empty_list(self):
        """Empty list."""
        nums = []
        expected = []
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()
