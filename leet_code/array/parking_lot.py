"""
Problem: Determine the maximum number of cars parked concurrently in a parking lot

Approach 1 (Sweep Line):
- Create entry/exit events for each interval
- Sort events by time and process them
- Time complexity: O(n log n)
- Space complexity: O(n)

Approach 2 (Difference Array):
- Use prefix sum with difference array
- Time complexity: O(n + k) where k is time range
- Space complexity: O(k)
"""

import unittest
from typing import List


class Solution:
    """Solution using sweep line algorithm."""

    def minParkingSpaces(self, intervals: List[List[int]]) -> int:
        """Finds minimum parking spaces using sweep line algorithm."""
        if not intervals:
            return 0

        events = []

        # Create entry and exit events
        for start, end in intervals:
            events.append((start, 1))  # Car enters at start
            events.append((end + 1, -1))  # Car exits after end (inclusive interval)

        # Sort events by time
        events.sort()

        max_cars = 0
        current_cars = 0

        # Process each event
        for _, delta in events:
            current_cars += delta
            max_cars = max(max_cars, current_cars)

        return max_cars


class SolutionDifferenceArray:
    """Solution using difference array and prefix sum."""

    def minParkingSpaces(self, intervals: List[List[int]]) -> int:
        """Finds minimum parking spaces using difference array and prefix sum."""
        if not intervals:
            return 0

        # Find the maximum time to determine array size
        max_time = max(end for start, end in intervals)

        # Create difference array with extra space
        diff = [0] * (max_time + 2)

        # Mark entry and exit points
        for start, end in intervals:
            diff[start] += 1  # Car enters
            diff[end + 1] -= 1  # Car exits (after inclusive end)

        # Compute prefix sum and find maximum
        max_cars = 0
        current_cars = 0

        for delta in diff:
            current_cars += delta
            max_cars = max(max_cars, current_cars)

        return max_cars


# Unit Tests


class TestParkingLotCapacity(unittest.TestCase):
    """Test cases for parking lot capacity problem."""

    def setUp(self):
        self.solution1 = Solution()
        self.solution2 = SolutionDifferenceArray()

    def test_example1(self):
        """Basic overlapping intervals."""
        intervals = [[1, 5], [2, 7], [8, 10]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 2)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 2)

    def test_example2(self):
        """Complete overlap of three intervals."""
        intervals = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 3)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 3)

    def test_example3(self):
        """Non-overlapping intervals."""
        intervals = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 1)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 1)

    def test_example4(self):
        """Single interval."""
        intervals = [[1, 10]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 1)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 1)

    def test_empty_input(self):
        """Empty intervals list."""
        intervals = []
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 0)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 0)

    def test_all_same_interval(self):
        """All cars park at the same time."""
        intervals = [[5, 10], [5, 10], [5, 10], [5, 10]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 4)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 4)

    def test_nested_intervals(self):
        """Nested intervals."""
        intervals = [[1, 10], [2, 9], [3, 8], [4, 7]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 4)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 4)

    def test_touching_intervals(self):
        """Intervals that touch at boundaries."""
        intervals = [[1, 3], [3, 5], [5, 7]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 2)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 2)

    def test_adjacent_intervals(self):
        """Adjacent but non-overlapping intervals."""
        intervals = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 1)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 1)

    def test_point_intervals(self):
        """Intervals where start equals end."""
        intervals = [[1, 1], [1, 1], [2, 2]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 2)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 2)

    def test_large_overlapping(self):
        """Many overlapping intervals."""
        intervals = [[1, 100], [2, 100], [3, 100], [4, 100], [5, 100]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 5)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 5)

    def test_staircase_pattern(self):
        """Staircase pattern of intervals."""
        intervals = [[1, 5], [3, 7], [5, 9], [7, 11]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 3)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 3)

    def test_zero_start_time(self):
        """Intervals starting at time zero."""
        intervals = [[0, 5], [0, 3], [1, 4]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 3)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 3)

    def test_max_time_boundary(self):
        """Intervals at maximum time boundary."""
        intervals = [[998, 1000], [999, 1000], [1000, 1000]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 3)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 3)

    def test_complex_overlap(self):
        """Complex overlapping pattern."""
        intervals = [[1, 4], [2, 6], [3, 5], [7, 9], [8, 10], [9, 11]]
        self.assertEqual(self.solution1.minParkingSpaces(intervals), 3)
        self.assertEqual(self.solution2.minParkingSpaces(intervals), 3)


if __name__ == "__main__":
    unittest.main()
