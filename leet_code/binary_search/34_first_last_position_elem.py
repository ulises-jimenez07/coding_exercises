"""
Problem: Find first and last position of element in sorted array

Approach:
- Use two binary searches to find leftmost and rightmost occurrences
- Continue searching left/right even after finding target
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """
    Solution using boundary condition checks:
    - Use two binary searches to find leftmost and rightmost occurrences
    - Check boundary conditions immediately when target is found
    - Time complexity: O(log n)
    - Space complexity: O(1)
    """

    def searchRange(self, nums, target):
        left = self.getLeftPosition(nums, target)
        right = self.getRightPosition(nums, target)
        return [left, right]

    def getLeftPosition(self, nums, target):
        # Find leftmost occurrence
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def getRightPosition(self, nums, target):
        # Find rightmost occurrence
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


class Solution2:
    """
    Alternative approach using ans variable:
    - Update ans whenever target is found
    - Continue searching to find leftmost/rightmost occurrence
    - Time complexity: O(log n)
    - Space complexity: O(1)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.find_first(nums, target)
        last = self.find_last(nums, target)
        return [first, last]

    def find_first(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = -1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                ans = mid
                end = mid - 1
        return ans

    def find_last(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                ans = mid
                start = mid + 1
        return ans


class TestSearchRange(unittest.TestCase):
    """Test cases for searchRange method."""

    def setUp(self):
        self.solution = Solution()

    def test_target_present_multiple_times(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected = [3, 4]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_target_present_once(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 10
        expected = [5, 5]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_target_not_present(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected = [-1, -1]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_empty_array(self):
        nums = []
        target = 0
        expected = [-1, -1]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_single_element_array_target_present(self):
        nums = [1]
        target = 1
        expected = [0, 0]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_single_element_array_target_not_present(self):
        nums = [1]
        target = 2
        expected = [-1, -1]
        self.assertEqual(self.solution.searchRange(nums, target), expected)


if __name__ == "__main__":
    unittest.main()
