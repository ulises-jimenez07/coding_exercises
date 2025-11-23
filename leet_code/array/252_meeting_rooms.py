"""
Problem: Given an array of meeting time intervals, determine if a person can attend all meetings

Approach:
- Sort intervals by start time
- Check for any overlapping meetings (end time > next start time)
- Time complexity: O(n log n) for sorting
- Space complexity: O(1) excluding sort space
"""

import unittest
from typing import List


class Solution:
    """Solution for LeetCode 252: Meeting Rooms."""

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """Determines if a person can attend all meetings without overlap."""
        if not intervals:
            return True

        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


class TestCanAttendMeetings(unittest.TestCase):
    """Unit tests for the Meeting Rooms solution."""

    def setUp(self):
        self.solution = Solution()

    def test_overlapping_meetings(self):
        """Meetings that overlap."""
        self.assertEqual(self.solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]]), False)

    def test_non_overlapping_meetings(self):
        """Meetings that don't overlap."""
        self.assertEqual(self.solution.canAttendMeetings([[7, 10], [2, 4]]), True)

    def test_empty_list(self):
        """Empty meeting list."""
        self.assertEqual(self.solution.canAttendMeetings([]), True)

    def test_single_meeting(self):
        """Single meeting."""
        self.assertEqual(self.solution.canAttendMeetings([[1, 5]]), True)

    def test_adjacent_meetings(self):
        """Meetings that end exactly when next starts."""
        self.assertEqual(self.solution.canAttendMeetings([[1, 5], [5, 10]]), True)

    def test_same_start_time(self):
        """Meetings with same start time."""
        self.assertEqual(self.solution.canAttendMeetings([[1, 5], [1, 10]]), False)


if __name__ == "__main__":
    unittest.main()
