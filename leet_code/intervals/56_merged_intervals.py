"""
Problem: Merge all overlapping intervals

Approach:
- Sort intervals by start time
- Merge consecutive intervals if they overlap
- Time complexity: O(n log n)
- Space complexity: O(n) for output
"""

import unittest
from typing import List


class Solution:
    """Solution for Merge Intervals."""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merges overlapping intervals."""
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged: list[list[int]] = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


class TestSolution(unittest.TestCase):
    """Unit tests for the Merge Intervals solution."""

    def setUp(self):
        self.solution = Solution()

    def test_empty_intervals(self):
        """Empty intervals."""
        self.assertEqual(self.solution.merge([]), [])

    def test_single_interval(self):
        """Single interval."""
        self.assertEqual(self.solution.merge([[1, 4]]), [[1, 4]])

    def test_no_overlap(self):
        """No overlap."""
        self.assertEqual(self.solution.merge([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
        self.assertEqual(self.solution.merge([[1, 2], [3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]])

    def test_complete_overlap(self):
        """Complete overlap."""
        self.assertEqual(self.solution.merge([[1, 5], [2, 3]]), [[1, 5]])
        self.assertEqual(self.solution.merge([[2, 3], [1, 5]]), [[1, 5]])

    def test_partial_overlap(self):
        """Partial overlap."""
        self.assertEqual(self.solution.merge([[1, 3], [2, 6]]), [[1, 6]])
        self.assertEqual(self.solution.merge([[1, 4], [3, 5]]), [[1, 5]])

    def test_multiple_overlaps(self):
        """Multiple overlaps."""
        self.assertEqual(self.solution.merge([[1, 4], [0, 4]]), [[0, 4]])
        self.assertEqual(self.solution.merge([[0, 0], [0, 0]]), [[0, 0]])
        self.assertEqual(self.solution.merge([[1, 4], [0, 1]]), [[0, 4]])
        self.assertEqual(self.solution.merge([[1, 4], [2, 3], [4, 5]]), [[1, 5]])

    def test_example_from_leetcode_1(self):
        """LeetCode example 1."""
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_example_from_leetcode_2(self):
        """LeetCode example 2."""
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_complex_intervals(self):
        """Complex intervals."""
        intervals = [[1, 4], [0, 0], [2, 3], [5, 7], [8, 9]]
        expected = [[0, 0], [1, 4], [5, 7], [8, 9]]
        self.assertEqual(self.solution.merge(intervals), expected)

        intervals = [[1, 4], [0, 4], [0, 1]]
        expected = [[0, 4]]
        self.assertEqual(self.solution.merge(intervals), expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
