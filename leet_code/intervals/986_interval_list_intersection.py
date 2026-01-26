"""
Problem: Interval List Intersections

Approach:
- Use two pointers to iterate through both lists
- Find the intersection of the current two intervals by comparing start and end times
- Move the pointer of the interval that ends first to find the next possible intersection
- Time complexity: O(n + m) where n and m are lengths of the lists
- Space complexity: O(min(n, m)) for the output list
"""

import unittest
from typing import List


class Solution:
    """Solution for Interval List Intersections."""

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """Finds the intersection of two sorted interval lists."""
        overlaps = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            # Identify which interval starts first to simplify intersection logic
            if firstList[i][0] <= secondList[j][0]:
                first, second = firstList[i], secondList[j]
            else:
                first, second = secondList[j], firstList[i]

            # If they overlap, add the intersection range
            if first[1] >= second[0]:
                overlaps.append([second[0], min(first[1], second[1])])

            # Move pointer for the interval that ends earlier
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return overlaps


class TestSolution(unittest.TestCase):
    """Unit tests for the Interval List Intersections solution."""

    def setUp(self):
        self.solution = Solution()

    def test_empty_lists(self):
        """Test with empty lists."""
        self.assertEqual(self.solution.intervalIntersection([], []), [])
        self.assertEqual(self.solution.intervalIntersection([[1, 2]], []), [])
        self.assertEqual(self.solution.intervalIntersection([], [[1, 2]]), [])

    def test_single_elements_overlap(self):
        """Test with single elements that overlap."""
        self.assertEqual(self.solution.intervalIntersection([[1, 5]], [[2, 3]]), [[2, 3]])

    def test_single_elements_no_overlap(self):
        """Test with single elements that do not overlap."""
        self.assertEqual(self.solution.intervalIntersection([[1, 2]], [[3, 4]]), [])

    def test_leetcode_example_1(self):
        """LeetCode example 1."""
        first_list = [[0, 2], [5, 10], [13, 23], [24, 25]]
        second_list = [[1, 5], [8, 12], [15, 24], [25, 26]]
        expected = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
        self.assertEqual(self.solution.intervalIntersection(first_list, second_list), expected)

    def test_leetcode_example_2(self):
        """LeetCode example 2."""
        first_list = [[1, 3], [5, 9]]
        second_list = []
        expected = []
        self.assertEqual(self.solution.intervalIntersection(first_list, second_list), expected)

    def test_edge_overlap(self):
        """Test intervals overlapping only at the edge."""
        self.assertEqual(self.solution.intervalIntersection([[1, 2]], [[2, 3]]), [[2, 2]])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
