"""
Problem: Find the minimum element in a rotated sorted array

Approach:
- Use binary search to find the rotation pivot
- Compare mid element with last element to determine which half is sorted
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        ans = nums[0]

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] <= nums[-1]:
                ans = nums[mid]
                end = mid - 1
            else:
                start = mid + 1

        return ans


# --- Unit Tests ---
class TestFindMin(unittest.TestCase):
    """
    Unit tests for the Solution.findMin method.
    """

    def setUp(self):
        self.solution = Solution()

    def test_rotated_array(self):
        """
        Test case with a standard rotated sorted array.
        """
        self.assertEqual(self.solution.findMin([3, 4, 5, 1, 2]), 1)

    def test_no_rotation(self):
        """
        Test case with an array that is not rotated.
        """
        self.assertEqual(self.solution.findMin([1, 2, 3, 4, 5]), 1)

    def test_single_element(self):
        """
        Test case with a single-element array.
        """
        self.assertEqual(self.solution.findMin([1]), 1)

    def test_fully_rotated_array(self):
        """
        Test case where the array is rotated at the very beginning.
        """
        self.assertEqual(self.solution.findMin([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_two_elements(self):
        """
        Test case with a two-element array.
        """
        self.assertEqual(self.solution.findMin([2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
