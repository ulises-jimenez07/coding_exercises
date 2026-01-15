"""Module to solve the Median of Two Sorted Arrays problem."""

import math
import unittest
from typing import List


class Solution:
    """Provides a method to find the median of two sorted arrays."""

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Finds the median of two combined sorted arrays in O(log(m+n)) time."""
        n1, n2 = len(nums1), len(nums2)
        total_len = n1 + n2

        def find_kth(k, a_start, a_end, b_start, b_end):
            """Recursive helper to find the kth element in the union of two arrays."""
            if a_start > a_end:
                return nums2[k - a_start]
            if b_start > b_end:
                return nums1[k - b_start]

            # Compare middle elements to narrow search space
            a_mid, b_mid = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_val, b_val = nums1[a_mid], nums2[b_mid]

            if a_mid + b_mid < k:
                # Targeted k is in the right half of the combined space
                if a_val > b_val:
                    return find_kth(k, a_start, a_end, b_mid + 1, b_end)
                return find_kth(k, a_mid + 1, a_end, b_start, b_end)

            # Targeted k is in the left half of the combined space
            if a_val > b_val:
                return find_kth(k, a_start, a_mid - 1, b_start, b_end)
            return find_kth(k, a_start, a_end, b_start, b_mid - 1)

        if total_len % 2:
            return float(find_kth(total_len // 2, 0, n1 - 1, 0, n2 - 1))

        left = find_kth(total_len // 2 - 1, 0, n1 - 1, 0, n2 - 1)
        right = find_kth(total_len // 2, 0, n1 - 1, 0, n2 - 1)
        return (left + right) / 2.0

    def find_the_median_from_two_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Another version using partition logic, which is often considered more intuitive.
        Time: O(log(min(m, n)))
        Space: O(1)
        """
        # Ensure nums1 is the shorter array to minimize binary search range
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        # Targeted size for the left partition
        half_total_len = (m + n) // 2
        left, right = 0, m - 1

        while True:
            # Binary search for partition point in the smaller array
            l1_index = (left + right) // 2
            # Corresponding partition point in the larger array
            l2_index = half_total_len - (l1_index + 1) - 1

            # Get values at the borders of the partition, using infinity for out-of-bounds
            # l1, r1 are from nums1; l2, r2 are from nums2
            l1 = -math.inf if l1_index < 0 else nums1[l1_index]
            r1 = math.inf if l1_index >= m - 1 else nums1[l1_index + 1]
            l2 = -math.inf if l2_index < 0 else nums2[l2_index]
            r2 = math.inf if l2_index >= n - 1 else nums2[l2_index + 1]

            # Validate if the current partition is correct
            if l1 > r2:
                # nums1's left side is too large, move search left
                right = l1_index - 1
            elif l2 > r1:
                # nums1's left side is too small, move search right
                left = l1_index + 1
            else:
                # Partition found!
                if (m + n) % 2 == 0:
                    # Even total elements: average of the max of lefts and min of rights
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                # Odd total elements: the median is the smallest of the right partition elements
                return min(r1, r2)


class TestMedianSortedArrays(unittest.TestCase):
    """Unit tests for finding the median of two sorted arrays."""

    def setUp(self):
        """Sets up the solution instance for testing."""
        self.solution = Solution()

    def test_example_1(self):
        """Standard case 1."""
        for method in [self.solution.findMedianSortedArrays, self.solution.find_the_median_from_two_sorted_arrays]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method([1, 3], [2]), 2.0)

    def test_example_2(self):
        """Standard case 2 (even length)."""
        for method in [self.solution.findMedianSortedArrays, self.solution.find_the_median_from_two_sorted_arrays]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method([1, 2], [3, 4]), 2.5)

    def test_one_empty(self):
        """One array is empty."""
        for method in [self.solution.findMedianSortedArrays, self.solution.find_the_median_from_two_sorted_arrays]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method([], [1]), 1.0)
                self.assertEqual(method([2], []), 2.0)

    def test_both_single_element(self):
        """Both arrays have one element."""
        for method in [self.solution.findMedianSortedArrays, self.solution.find_the_median_from_two_sorted_arrays]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method([1], [3]), 2.0)

    def test_large_disjoints(self):
        """Arrays with large difference in values."""
        for method in [self.solution.findMedianSortedArrays, self.solution.find_the_median_from_two_sorted_arrays]:
            with self.subTest(method=method.__name__):
                self.assertEqual(method([1, 2], [10, 11]), 6.0)


if __name__ == "__main__":
    unittest.main()
