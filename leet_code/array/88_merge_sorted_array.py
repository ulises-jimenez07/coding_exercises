"""
Problem: Merge two sorted arrays in-place into the first array

Approach:
- Start from end of both arrays, place larger element at end of nums1
- Work backwards to avoid overwriting unprocessed elements
- Time complexity: O(m+n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Merges two sorted arrays in-place into nums1."""
        num2_idx = n - 1
        num1_idx = m - 1

        for i in range(m + n - 1, -1, -1):
            if num2_idx < 0:
                break
            if num1_idx < 0 or nums2[num2_idx] >= nums1[num1_idx]:
                nums1[i] = nums2[num2_idx]
                num2_idx -= 1
            else:
                nums1[i] = nums1[num1_idx]
                num1_idx -= 1


class TestMerge(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example."""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_empty_nums2(self):
        """Empty nums2."""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = []
        n = 0
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 0, 0, 0])

    def test_empty_nums1(self):
        """Empty nums1."""
        nums1 = [0, 0, 0]
        m = 0
        nums2 = [1, 2, 3]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])

    def test_nums1_larger_than_nums2(self):
        """Nums1 larger than nums2."""
        nums1 = [1, 2, 5, 0, 0, 0]
        m = 3
        nums2 = [3, 4]
        n = 2
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 0])

    def test_nums2_larger_than_nums1(self):
        """Nums2 larger than nums1."""
        nums1 = [1, 3, 0, 0, 0]
        m = 2
        nums2 = [2, 4, 5]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
