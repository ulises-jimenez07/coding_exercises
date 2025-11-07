"""
Problem: Remove all occurrences of a value in-place and return new length

Approach:
- Use two pointers: one for reading, one for writing non-target elements
- Copy non-target elements to front, overwriting target values
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """Removes all occurrences of val in-place and returns new length."""
        swap = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[swap] = nums[i]
                swap += 1

        return swap


class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        """Standard example where val appears multiple times."""
        nums = [3, 2, 2, 3]
        result_len = self.solution.removeElement(nums, 3)
        self.assertEqual(result_len, 2)
        self.assertEqual(sorted(nums[:result_len]), [2, 2])

    def test_example_two(self):
        """Val appears less frequently with other numbers present."""
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        result_len = self.solution.removeElement(nums, 2)
        self.assertEqual(result_len, 5)
        self.assertEqual(sorted(nums[:result_len]), [0, 0, 1, 3, 4])

    def test_no_match(self):
        """Val is not present in the list."""
        nums = [1, 2, 3, 4]
        result_len = self.solution.removeElement(nums, 5)
        self.assertEqual(result_len, 4)
        self.assertEqual(nums[:result_len], [1, 2, 3, 4])

    def test_all_match(self):
        """All elements match val."""
        nums = [7, 7, 7]
        result_len = self.solution.removeElement(nums, 7)
        self.assertEqual(result_len, 0)
        self.assertEqual(nums[:result_len], [])

    def test_empty_list(self):
        """Empty input list."""
        nums = []
        result_len = self.solution.removeElement(nums, 1)
        self.assertEqual(result_len, 0)
        self.assertEqual(nums[:result_len], [])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
