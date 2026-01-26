"""
Problem: Given an array of meeting time intervals, find the minimum number of conference rooms required.

Approach:
- Separate start and end times and sort them individually
- Iterate through the start times
- If a meeting starts after the earliest ending meeting finishes, we can reuse that room
- Otherwise, we need a new room
- Time complexity: O(N log N) due to sorting
- Space complexity: O(N) for storing sorted start and end times
"""

import unittest
from typing import List


class Solution:
    """Solution for Meeting Rooms II."""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Calculates the minimum number of meeting rooms required."""
        if not intervals:
            return 0

        used_rooms = 0

        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])

        end_idx = 0

        for start_idx in range(len(intervals)):
            # If the current meeting starts after or when the previous one ends,
            # we can reuse the room.
            if start_timings[start_idx] >= end_timings[end_idx]:
                used_rooms -= 1
                end_idx += 1

            used_rooms += 1

        return used_rooms


class TestMinMeetingRooms(unittest.TestCase):
    """Unit tests for the MinMeetingRooms solution."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_overlap(self):
        """Meetings that overlap."""
        intervals = [[0, 30], [5, 10], [15, 20]]
        self.assertEqual(self.solution.minMeetingRooms(intervals), 2)

    def test_no_overlap(self):
        """Meetings that do not overlap."""
        intervals = [[7, 10], [2, 4]]
        self.assertEqual(self.solution.minMeetingRooms(intervals), 1)

    def test_nested_meetings(self):
        """One meeting completely inside another."""
        intervals = [[0, 30], [5, 10]]
        self.assertEqual(self.solution.minMeetingRooms(intervals), 2)

    def test_consecutive_meetings(self):
        """One meeting starts exactly when another ends."""
        intervals = [[0, 10], [10, 20]]
        self.assertEqual(self.solution.minMeetingRooms(intervals), 1)

    def test_empty_intervals(self):
        """Empty input."""
        self.assertEqual(self.solution.minMeetingRooms([]), 0)


if __name__ == "__main__":
    unittest.main()
