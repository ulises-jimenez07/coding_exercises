"""
Problem: Remove duplicates from sorted array II (at most two occurrences)

Approach:
- Use two pointers: one for reading, one for writing
- Track occurrences of the current number with a counter
- Only copy element if it's the first or second occurrence
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Namespace for the solution to LeetCode 80: Remove Duplicates from Sorted Array II."""

    def removeDuplicates(self, nums: List[int]) -> int:
        """Removes duplicates in-place, allowing each element at most twice."""
        if not nums:
            return 0

        # swap tracks the write position, pointer tracks the read position
        pointer = 1
        swap = 1
        count = 1

        while pointer < len(nums):
            if nums[pointer] == nums[pointer - 1]:
                count += 1
                # Skip if we already have two of the current number
                if count > 2:
                    pointer += 1
                    continue
            else:
                count = 1

            # Move valid element to the swap position
            nums[swap] = nums[pointer]
            swap += 1
            pointer += 1

        return swap


class TestRemoveDuplicates(unittest.TestCase):
    """Unit tests for the Remove Duplicates II solution."""

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        """Standard example from LeetCode."""
        nums = [1, 1, 1, 2, 2, 3]
        length = self.solution.removeDuplicates(nums)
        self.assertEqual(length, 5)
        self.assertEqual(nums[:length], [1, 1, 2, 2, 3])

    def test_example_two(self):
        """Longer example with multiple duplicate stretches."""
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        length = self.solution.removeDuplicates(nums)
        self.assertEqual(length, 7)
        self.assertEqual(nums[:length], [0, 0, 1, 1, 2, 3, 3])

    def test_all_duplicates(self):
        """Array with only one value repeated many times."""
        nums = [1, 1, 1, 1, 1]
        length = self.solution.removeDuplicates(nums)
        self.assertEqual(length, 2)
        self.assertEqual(nums[:length], [1, 1])

    def test_no_duplicates(self):
        """Array with no duplicates at all."""
        nums = [1, 2, 3, 4]
        length = self.solution.removeDuplicates(nums)
        self.assertEqual(length, 4)
        self.assertEqual(nums[:length], [1, 2, 3, 4])

    def test_empty_list(self):
        """Edge case: empty input list."""
        nums = []
        length = self.solution.removeDuplicates(nums)
        self.assertEqual(length, 0)
        self.assertEqual(nums, [])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
