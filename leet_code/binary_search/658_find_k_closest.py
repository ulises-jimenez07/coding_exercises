"""
Problem: Find K Closest Elements

Approach:
- Use binary search to find the left bound of the closest k elements.
- The search range is [0, len(arr) - k].
- Compare the distance of x from mid and mid + k to adjust the search range.
- Time complexity: O(log(n-k) + k)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Provides a method to find the k closest elements to a target value."""

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Finds the k closest integers to x in the array.
        """
        left = 0
        right = len(arr) - k

        # Binary search for the starting index of the k closest elements
        while left < right:
            mid = (left + right) // 2

            # If x is closer to arr[mid] than arr[mid + k], move right boundary
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]


class TestFindClosestElements(unittest.TestCase):
    """Unit tests for the findClosestElements method."""

    def setUp(self):
        """Initializes the Solution object."""
        self.solution = Solution()

    def test_example_1(self):
        """Tests with a standard example from LeetCode."""
        self.assertEqual(self.solution.findClosestElements([1, 2, 3, 4, 5], 4, 3), [1, 2, 3, 4])

    def test_example_2(self):
        """Tests with a target outside the array's range."""
        self.assertEqual(self.solution.findClosestElements([1, 2, 3, 4, 5], 4, -1), [1, 2, 3, 4])

    def test_target_larger_than_all(self):
        """Tests when the target is larger than all elements in the array."""
        self.assertEqual(self.solution.findClosestElements([1, 2, 3, 4, 5], 4, 10), [2, 3, 4, 5])

    def test_single_element_array(self):
        """Tests with a single element array."""
        self.assertEqual(self.solution.findClosestElements([1], 1, 1), [1])

    def test_all_elements(self):
        """Tests when k equals the length of the array."""
        self.assertEqual(self.solution.findClosestElements([1, 2, 3, 4, 5], 5, 3), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        """Tests with an array containing negative numbers."""
        self.assertEqual(self.solution.findClosestElements([-5, -2, 0, 1, 3, 8], 3, -1), [-2, 0, 1])


if __name__ == "__main__":
    unittest.main()
