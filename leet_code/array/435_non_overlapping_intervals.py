"""
Problem: Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Approach:
- Greedy strategy: Sort intervals by their end times.
- Iterate through the sorted intervals.
- Keep track of the end time of the last added interval (`last_end`).
- If the current interval starts after or when the `last_end` finishes, it doesn't overlap. We keep it and update `last_end`.
- If it starts before `last_end`, it overlaps. We "remove" it (increment counter) because keeping the one with the earlier end time (which is `last_end`) leaves more room for future intervals.
- Time complexity: O(N log N) due to sorting.
- Space complexity: O(1) or O(N) depending on sort implementation.
"""

import unittest
from typing import List


class Solution:
    """Solution for Non-overlapping Intervals."""

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Calculates the minimum number of intervals to remove."""
        if not intervals:
            return 0

        # Sort by end time to maximize space for future intervals
        intervals.sort(key=lambda x: x[1])

        removed_count = 0
        last_end = float("-inf")

        for start, end in intervals:
            if start >= last_end:
                # No overlap, we can keep this interval
                last_end = end
            else:
                # Overlap detected, remove this interval
                removed_count += 1

        return removed_count


class TestNonOverlappingIntervals(unittest.TestCase):
    """Unit tests for the Non-overlapping Intervals solution."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_overlap(self):
        """Standard case with overlaps."""
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        # [1,3] overlaps with [1,2] and [2,3]. Removing [1,3] leaves [1,2], [2,3], [3,4].
        self.assertEqual(self.solution.eraseOverlapIntervals(intervals), 1)

    def test_chained_overlap(self):
        """Case where multiple removals are needed."""
        intervals = [[1, 2], [1, 2], [1, 2]]
        self.assertEqual(self.solution.eraseOverlapIntervals(intervals), 2)

    def test_no_overlap(self):
        """No overlaps at all."""
        intervals = [[1, 2], [2, 3]]
        self.assertEqual(self.solution.eraseOverlapIntervals(intervals), 0)

    def test_long_interval(self):
        """One long interval overlapping multiple short ones."""
        # [[1,4], [1,2], [2,3], [3,4]] -> Remove [1,4] to keep 3.
        intervals = [[1, 4], [1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.solution.eraseOverlapIntervals(intervals), 1)

    def test_empty(self):
        """Empty input."""
        self.assertEqual(self.solution.eraseOverlapIntervals([]), 0)


if __name__ == "__main__":
    unittest.main()
