"""
Problem: Remove duplicates from sorted array in-place and return new length

Approach:
- Use two pointers: one for reading, one for writing unique elements
- Write unique elements to front of array, overwriting duplicates
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Removes duplicates from sorted array in-place and returns new length."""
        if not nums:
            return 0

        swap = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[swap] = nums[i]
                swap += 1

        return swap


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example with duplicates."""
        nums = [1, 1, 2]
        result_len = self.solution.removeDuplicates(nums)
        self.assertEqual(result_len, 2)
        self.assertEqual(nums[:result_len], [1, 2])

    def test_more_duplicates(self):
        """Multiple duplicates."""
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        result_len = self.solution.removeDuplicates(nums)
        self.assertEqual(result_len, 5)
        self.assertEqual(nums[:result_len], [0, 1, 2, 3, 4])

    def test_no_duplicates(self):
        """No duplicates."""
        nums = [1, 2, 3, 4]
        result_len = self.solution.removeDuplicates(nums)
        self.assertEqual(result_len, 4)
        self.assertEqual(nums[:result_len], [1, 2, 3, 4])

    def test_all_same(self):
        """All same elements."""
        nums = [1, 1, 1, 1]
        result_len = self.solution.removeDuplicates(nums)
        self.assertEqual(result_len, 1)
        self.assertEqual(nums[:result_len], [1])

    def test_empty_array(self):
        """Empty array."""
        nums = []
        result_len = self.solution.removeDuplicates(nums)
        self.assertEqual(result_len, 0)
        self.assertEqual(nums[:result_len], [])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
