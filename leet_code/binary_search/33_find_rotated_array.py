"""
Problem: Search for a target value in a rotated sorted array

Approach:
- Find the rotation pivot using binary search
- Determine which half contains the target
- Perform standard binary search on the appropriate half
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Solution class for search in rotated sorted array problem."""

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Find pivot if array is rotated
        if right > 0 and nums[left] >= nums[right]:
            middle = (right + left) // 2
            while nums[middle] <= nums[middle + 1]:
                if nums[left] <= nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
                middle = (right + left) // 2
                if left > right:
                    break

            # Choose the appropriate half to search
            if nums[0] <= target <= nums[middle]:
                left = 0
                right = middle
            else:
                left = middle + 1
                right = len(nums) - 1

        # Standard binary search
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1


class TestSearch(unittest.TestCase):
    """Unit tests for the search in rotated sorted array implementation."""

    def setUp(self):
        self.sol = Solution()

    def test_search_rotated_array(self):
        self.assertEqual(self.sol.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(self.sol.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(self.sol.search([1], 0), -1)
        self.assertEqual(self.sol.search([1, 3], 3), 1)
        self.assertEqual(self.sol.search([3, 1], 1), 1)
        self.assertEqual(self.sol.search([5, 1, 3], 5), 0)
        self.assertEqual(self.sol.search([4, 5, 6, 7, 8, 1, 2, 3], 8), 4)


if __name__ == "__main__":
    unittest.main()
