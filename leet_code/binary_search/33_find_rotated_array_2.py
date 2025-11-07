"""
Problem: Search for a target value in a rotated sorted array (cleaner approach)

Approach:
- Single pass binary search identifying which half is sorted
- Compare target with sorted half boundaries to decide which side to search
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        ans = -1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            # Determine which half to search based on pivot
            if nums[mid] >= nums[0] and target < nums[0]:
                start = mid + 1
            elif nums[mid] < nums[0] and target >= nums[0]:
                end = mid - 1
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return ans


# --- Unit Tests ---


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def setUp(self):
        """
        Set up a new instance of the Solution class before each test.
        """
        self.solution = Solution()

    def test_target_found_in_rotated_array(self):
        """
        Test case where the target is present in a rotated array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_target_found_in_unrotated_array(self):
        """
        Test case where the target is present in a non-rotated array.
        """
        nums = [1, 2, 3, 4, 5, 6, 7]
        target = 3
        self.assertEqual(self.solution.search(nums, target), 2)

    def test_target_not_found(self):
        """
        Test case where the target is not present in the array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_target_is_first_element(self):
        """
        Test case where the target is the first element of the array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 4
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_target_is_last_element(self):
        """
        Test case where the target is the last element of the array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 2
        self.assertEqual(self.solution.search(nums, target), 6)

    def test_empty_array(self):
        """
        Test case with an empty array.
        """
        nums = []
        target = 5
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_single_element_array_found(self):
        """
        Test case with a single-element array where the target is found.
        """
        nums = [1]
        target = 1
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_single_element_array_not_found(self):
        """
        Test case with a single-element array where the target is not found.
        """
        nums = [1]
        target = 0
        self.assertEqual(self.solution.search(nums, target), -1)


# To run the tests, you can use:
# unittest.main()

if __name__ == "__main__":
    unittest.main()
