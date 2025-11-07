"""
Problem: Move all zeros to the end while maintaining relative order of non-zeros

Approach:
- Use two-pass approach: first copy non-zeros to front, then fill rest with zeros
- Maintains relative order of non-zero elements
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Moves all zeros to the end while maintaining relative order of non-zero elements."""
        j = 0

        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1

        for x in range(j, len(nums)):
            nums[x] = 0


class TestMoveZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example with zeros mixed in."""
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_all_zeros(self):
        """All zeros."""
        nums = [0, 0, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0, 0, 0])

    def test_no_zeros(self):
        """No zeros."""
        nums = [1, 2, 3, 4, 5]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_single_zero(self):
        """Single zero."""
        nums = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0])

    def test_empty_list(self):
        """Empty list."""
        nums = []
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [])

    def test_zeros_at_beginning(self):
        """Zeros at the beginning."""
        nums = [0, 0, 1]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 0, 0])

    def test_zeros_at_end(self):
        """Zeros at the end."""
        nums = [1, 2, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 0, 0])


if __name__ == "__main__":
    unittest.main()
