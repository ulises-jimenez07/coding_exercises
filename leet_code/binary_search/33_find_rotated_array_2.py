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
    """
    Solutions for searching in a rotated sorted array.
    """

    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for target in nums using a single-pass binary search.
        Logic: Determines if mid and target are in different sorted segments of the rotated array.
        """
        start = 0
        end = len(nums) - 1
        ans = -1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            # Logic: Check if mid and target are in different segments of the rotation
            # Segment 1: nums[i] >= nums[0] (left part of rotation)
            # Segment 2: nums[i] < nums[0] (right part of rotation)

            # If mid is in Segment 1 and target is in Segment 2
            if nums[mid] >= nums[0] and target < nums[0]:
                start = mid + 1  # Target must be to the right
            # If mid is in Segment 2 and target is in Segment 1
            elif nums[mid] < nums[0] and target >= nums[0]:
                end = mid - 1  # Target must be to the left
            else:
                # Both mid and target are in the same segment, perform standard binary search
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return ans

    def find_the_target_in_a_rotated_sorted_array(self, nums: List[int], target: int) -> int:
        """
        Alternative implementation using explicit side-of-pivot checks.
        """
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid  # Return immediately when found

            # Logic: Identify which side of the pivot (nums[0]) the mid and target are on.
            # (Both are >= nums[0] means they are on the left sorted portion,
            # both are < nums[0] means they are on the right sorted portion).
            mid_on_left = nums[mid] >= nums[0]
            target_on_left = target >= nums[0]

            if mid_on_left == target_on_left:
                # Logic: If both are on the same side, it's a standard sorted sequence relative to each other.
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # Logic: If they are on different sides, move towards the target's side.
                if target_on_left:
                    # Target is on the left side, mid is on the right side
                    right = mid - 1
                else:
                    # Target is on the right side, mid is on the left side
                    left = mid + 1

        return -1


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
        for method in [self.solution.search, self.solution.find_the_target_in_a_rotated_sorted_array]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(nums, target), 4)

    def test_target_found_in_unrotated_array(self):
        """
        Test case where the target is present in a non-rotated array.
        """
        nums = [1, 2, 3, 4, 5, 6, 7]
        target = 3
        for method in [self.solution.search, self.solution.find_the_target_in_a_rotated_sorted_array]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(nums, target), 2)

    def test_target_not_found(self):
        """
        Test case where the target is not present in the array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        for method in [self.solution.search, self.solution.find_the_target_in_a_rotated_sorted_array]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(nums, target), -1)

    def test_target_is_first_element(self):
        """
        Test case where the target is the first element of the array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 4
        for method in [self.solution.search, self.solution.find_the_target_in_a_rotated_sorted_array]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(nums, target), 0)

    def test_target_is_last_element(self):
        """
        Test case where the target is the last element of the array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 2
        for method in [self.solution.search, self.solution.find_the_target_in_a_rotated_sorted_array]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(nums, target), 6)

    def test_empty_array(self):
        """
        Test case with an empty array.
        """
        nums = []
        target = 5
        for method in [self.solution.search, self.solution.find_the_target_in_a_rotated_sorted_array]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(nums, target), -1)

    def test_single_element_array_found(self):
        """
        Test case with a single-element array where the target is found.
        """
        nums = [1]
        target = 1
        for method in [self.solution.search, self.solution.find_the_target_in_a_rotated_sorted_array]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(nums, target), 0)

    def test_single_element_array_not_found(self):
        """
        Test case with a single-element array where the target is not found.
        """
        nums = [1]
        target = 0
        for method in [self.solution.search, self.solution.find_the_target_in_a_rotated_sorted_array]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(nums, target), -1)


# To run the tests, you can use:
# unittest.main()

if __name__ == "__main__":
    unittest.main()
