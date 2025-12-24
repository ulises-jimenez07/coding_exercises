"""Module to solve the Median of Two Sorted Arrays problem."""

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


class TestMedianSortedArrays(unittest.TestCase):
    """Unit tests for finding the median of two sorted arrays."""

    def setUp(self):
        """Sets up the solution instance for testing."""
        self.solution = Solution()

    def test_example_1(self):
        """Standard case 1."""
        self.assertEqual(self.solution.findMedianSortedArrays([1, 3], [2]), 2.0)

    def test_example_2(self):
        """Standard case 2 (even length)."""
        self.assertEqual(self.solution.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def test_one_empty(self):
        """One array is empty."""
        self.assertEqual(self.solution.findMedianSortedArrays([], [1]), 1.0)
        self.assertEqual(self.solution.findMedianSortedArrays([2], []), 2.0)

    def test_both_single_element(self):
        """Both arrays have one element."""
        self.assertEqual(self.solution.findMedianSortedArrays([1], [3]), 2.0)

    def test_large_disjoints(self):
        """Arrays with large difference in values."""
        self.assertEqual(self.solution.findMedianSortedArrays([1, 2], [10, 11]), 6.0)


if __name__ == "__main__":
    unittest.main()
