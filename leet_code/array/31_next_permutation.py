"""
Problem: Find the next lexicographically greater permutation in-place

Approach:
- Find first decreasing element from right, swap with next larger element
- Reverse suffix to get smallest arrangement
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """Finds the next lexicographically greater permutation in-place."""

        def _reverse(nums, start):
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        i = n - 2
        # Find first decreasing element from right
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            # Find smallest element greater than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        _reverse(nums, i + 1)


class TestNextPermutation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        """Basic permutation."""
        nums = [1, 2, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])

    def test_reversed_order(self):
        """Largest permutation wraps to smallest."""
        nums = [3, 2, 1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_with_duplicates(self):
        """Permutation with duplicate values."""
        nums = [1, 1, 5]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 5, 1])

    def test_single_element(self):
        """Single element list."""
        nums = [1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1])

    def test_two_elements(self):
        """Two elements."""
        nums = [1, 2]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [2, 1])

    def test_complex(self):
        """Complex permutation."""
        nums = [2, 3, 1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
