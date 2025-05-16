import unittest
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges a list of overlapping intervals.

        The algorithm first sorts the intervals by their start times.
        Then, it iterates through the sorted intervals, merging them if they overlap.

        Args:
            intervals: A list of intervals, where each interval is represented as
                       a list of two integers [start, end].

        Returns:
            A new list of non-overlapping intervals that cover all the
            intervals in the input.
        """
        if not intervals:
            return []

        # Sort intervals based on their start times. This is crucial for
        # the merging logic to work correctly.
        intervals.sort(key=lambda x: x[0])

        merged = []  # This list will store the merged intervals.

        for interval in intervals:
            # If the merged list is empty, or if the current interval does not
            # overlap with the last interval in 'merged' (i.e., its start time
            # is greater than the end time of the last merged interval),
            # then simply add the current interval to 'merged'.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # If the current interval overlaps with the last interval in 'merged',
                # extend the end time of the last merged interval to be the maximum
                # of its current end time and the current interval's end time.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


class TestSolution(unittest.TestCase):
    def setUp(self):
        """Set up for test cases."""
        self.solution = Solution()

    def test_empty_intervals(self):
        """Test with an empty list of intervals."""
        self.assertEqual(self.solution.merge([]), [])

    def test_single_interval(self):
        """Test with a single interval."""
        self.assertEqual(self.solution.merge([[1, 4]]), [[1, 4]])

    def test_no_overlap(self):
        """Test with intervals that do not overlap."""
        self.assertEqual(self.solution.merge([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
        self.assertEqual(
            self.solution.merge([[1, 2], [3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]]
        )

    def test_complete_overlap(self):
        """Test with intervals where one completely contains another."""
        self.assertEqual(self.solution.merge([[1, 5], [2, 3]]), [[1, 5]])
        self.assertEqual(
            self.solution.merge([[2, 3], [1, 5]]), [[1, 5]]
        )  # Test with unsorted input

    def test_partial_overlap(self):
        """Test with intervals that partially overlap."""
        self.assertEqual(self.solution.merge([[1, 3], [2, 6]]), [[1, 6]])
        self.assertEqual(self.solution.merge([[1, 4], [3, 5]]), [[1, 5]])

    def test_multiple_overlaps(self):
        """Test with multiple overlapping intervals that merge into one."""
        self.assertEqual(self.solution.merge([[1, 4], [0, 4]]), [[0, 4]])
        self.assertEqual(self.solution.merge([[0, 0], [0, 0]]), [[0, 0]])
        self.assertEqual(self.solution.merge([[1, 4], [0, 1]]), [[0, 4]])
        self.assertEqual(self.solution.merge([[1, 4], [2, 3], [4, 5]]), [[1, 5]])

    def test_example_from_leetcode_1(self):
        """Test a common example from LeetCode: [[1,3],[2,6],[8,10],[15,18]]"""
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_example_from_leetcode_2(self):
        """Test another common example from LeetCode: [[1,4],[4,5]]"""
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_complex_intervals(self):
        """Test a more complex scenario with various overlaps and non-overlaps."""
        intervals = [[1, 4], [0, 0], [2, 3], [5, 7], [8, 9]]
        expected = [[0, 0], [1, 4], [5, 7], [8, 9]]
        self.assertEqual(self.solution.merge(intervals), expected)

        intervals = [[1, 4], [0, 4], [0, 1]]
        expected = [[0, 4]]
        self.assertEqual(self.solution.merge(intervals), expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
