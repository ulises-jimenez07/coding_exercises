"""
Problem: Insert Interval (LeetCode 57)

Insert a new interval into a sorted list of non-overlapping intervals and merge if necessary.

Approach:
- Use binary search to find insertion position for new interval
- Insert at correct position to maintain sorted order
- Merge overlapping intervals in one pass
- Time complexity: O(n) for merging, O(log n) for binary search
- Space complexity: O(n) for result array
"""

import unittest
from typing import List


class Solution:
    """Solution class for insert interval problem."""

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert new interval and merge overlapping intervals.

        Strategy: Binary search for insertion point, then merge overlapping intervals.
        """
        if not intervals:
            return [newInterval]

        target = newInterval[0]
        left = 0
        right = len(intervals) - 1

        # Binary search for correct insertion position
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Insert at 'left' position (not 'mid') because 'left' points to where
        # the new interval should go to maintain sorted order by start time
        intervals.insert(left, newInterval)

        # Merge overlapping intervals
        res: List[List[int]] = []
        for interval in intervals:
            # No overlap: current interval starts after last merged interval ends
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # Overlap: extend the last interval's end time
                res[-1][1] = max(res[-1][1], interval[1])

        return res


class TestInsertInterval(unittest.TestCase):
    """Test cases for insert interval solution."""

    def setUp(self):
        self.sol = Solution()

    def test_insert_middle_no_merge(self):
        """Test inserting interval in middle without merging."""
        intervals = [[1, 3], [6, 9]]
        newInterval = [4, 5]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, [[1, 3], [4, 5], [6, 9]])

    def test_insert_with_merge(self):
        """Test inserting interval that overlaps with existing ones."""
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, [[1, 2], [3, 10], [12, 16]])

    def test_empty_intervals(self):
        """Test inserting into empty list."""
        intervals = []
        newInterval = [5, 7]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, [[5, 7]])

    def test_insert_at_beginning(self):
        """Test inserting interval at the beginning."""
        intervals = [[3, 5], [6, 9]]
        newInterval = [1, 2]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, [[1, 2], [3, 5], [6, 9]])

    def test_insert_at_end(self):
        """Test inserting interval at the end."""
        intervals = [[1, 3], [6, 9]]
        newInterval = [10, 12]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, [[1, 3], [6, 9], [10, 12]])

    def test_merge_all_intervals(self):
        """Test new interval overlaps with all existing intervals."""
        intervals = [[1, 2], [3, 4], [5, 6]]
        newInterval = [0, 7]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, [[0, 7]])

    def test_new_interval_inside_existing(self):
        """Test new interval completely inside existing interval."""
        intervals = [[1, 5]]
        newInterval = [2, 3]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, [[1, 5]])

    def test_existing_inside_new_interval(self):
        """Test existing intervals inside new interval."""
        intervals = [[2, 3], [5, 6]]
        newInterval = [1, 7]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, [[1, 7]])

    def test_adjacent_intervals(self):
        """Test merging adjacent intervals."""
        intervals = [[1, 5]]
        newInterval = [6, 8]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, [[1, 5], [6, 8]])

    def test_single_existing_interval_merge(self):
        """Test merging with single existing interval."""
        intervals = [[1, 3]]
        newInterval = [2, 5]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, [[1, 5]])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
