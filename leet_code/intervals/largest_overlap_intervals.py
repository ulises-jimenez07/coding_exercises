"""
Problem: Find the maximum number of overlapping intervals.

Approach 1: Sweep-line
- Decompose intervals into start and end points.
- Sort all points by time and type.
- Increment/decrement active count.

Approach 2: Two-pointer/Two-sorted-lists
- Sort start times and end times separately.
- Compare current start with current end to track concurrent intervals.

Both approaches have:
- Time complexity: O(n log n) for sorting.
- Space complexity: O(n) for points or sorted lists.
"""

import unittest
from typing import List


class Interval:
    """Represents an interval with a start and end time."""

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    """Solution for finding the largest overlap of intervals."""

    def largest_overlap_sweep_line(self, intervals: List[Interval]) -> int:
        """Finds max overlaps using a sweep-line algorithm."""
        if not intervals:
            return 0

        points: List[tuple[int, str]] = []
        for interval in intervals:
            points.append((interval.start, "S"))
            points.append((interval.end, "E"))

        # End (E) comes before Start (S) at the same time to handle non-overlap at points.
        points.sort(key=lambda x: (x[0], x[1]))

        active, max_overlaps = 0, 0
        for _, point_type in points:
            if point_type == "S":
                active += 1
            else:
                active -= 1
            max_overlaps = max(max_overlaps, active)

        return max_overlaps

    def largest_overlap_two_pointers(self, intervals: List[Interval]) -> int:
        """Finds max overlaps using two sorted lists and two pointers."""
        if not intervals:
            return 0

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        max_overlaps = 0
        current_overlaps = 0
        s_idx, e_idx = 0, 0

        # Process starts until we've check all intervals
        while s_idx < len(starts):
            if starts[s_idx] < ends[e_idx]:
                current_overlaps += 1
                s_idx += 1
            else:
                current_overlaps -= 1
                e_idx += 1

            max_overlaps = max(max_overlaps, current_overlaps)

        return max_overlaps


class TestSolution(unittest.TestCase):
    """Unit tests for the overlap solutions."""

    def setUp(self):
        self.solution = Solution()

    def _run_tests(self, intervals, expected):
        """Helper to test both implementations."""
        self.assertEqual(self.solution.largest_overlap_sweep_line(intervals), expected)
        self.assertEqual(self.solution.largest_overlap_two_pointers(intervals), expected)

    def test_empty_intervals(self):
        """Should return 0 for an empty list."""
        self._run_tests([], 0)

    def test_single_element(self):
        """Should return 1 for a single interval."""
        self._run_tests([Interval(1, 5)], 1)

    def test_no_overlap(self):
        """Should return 1 when intervals do not overlap."""
        intervals = [Interval(1, 2), Interval(3, 4), Interval(5, 6)]
        self._run_tests(intervals, 1)

    def test_complete_overlap(self):
        """Should return the count of all intervals when they all overlap."""
        intervals = [Interval(1, 10), Interval(2, 9), Interval(3, 8)]
        self._run_tests(intervals, 3)

    def test_partial_overlap(self):
        """Should return the maximum number of concurrent intervals."""
        intervals = [Interval(1, 5), Interval(2, 6), Interval(8, 10), Interval(4, 9)]
        self._run_tests(intervals, 3)

    def test_touching_endpoints(self):
        """Should return 1 if intervals touch at endpoints but don't overlap."""
        intervals = [Interval(1, 2), Interval(2, 3), Interval(3, 4)]
        self._run_tests(intervals, 1)

    def test_complex_cases(self):
        """Tests multiple scenarios using enumerate."""
        scenarios = [
            ([Interval(1, 4), Interval(2, 5), Interval(9, 12), Interval(5, 9)], 2),
            ([Interval(1, 10), Interval(2, 3), Interval(4, 5), Interval(6, 7)], 2),
            ([Interval(1, 2), Interval(1, 2), Interval(1, 2)], 3),
        ]
        for i, (intervals, expected) in enumerate(scenarios):
            with self.subTest(scenario=i):
                self._run_tests(intervals, expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
