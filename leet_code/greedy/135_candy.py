"""
Problem: Distribute minimum candies so each child gets at least 1, and children with
higher ratings than neighbors get more candy.

Approach:
- Two-pass greedy: left-to-right for left-neighbor rule, right-to-left for right-neighbor
- Each child starts with 1 candy
- Left pass: if ratings[i] > ratings[i-1], give one more than left neighbor
- Right pass: if ratings[i] > ratings[i+1], take max of current and right_neighbor + 1
- Time complexity: O(n) two passes
- Space complexity: O(n) for candies array

Example: [1,0,2] -> 5 candies (2,1,2); [1,2,2] -> 4 candies (1,2,1)
"""

import unittest
from typing import List


class Solution:
    """
    Greedy approach: Two passes to satisfy both left and right neighbor constraints.
    """

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left-to-right: child with higher rating than left neighbor gets more
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right-to-left: child with higher rating than right neighbor gets more
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


class TestCandy(unittest.TestCase):
    """Unit tests for Candy distribution implementations."""

    def setUp(self):
        self.solution = Solution()

    def test_valley_in_middle(self):
        """Tests ratings with a valley: [1,0,2] -> 5."""
        self.assertEqual(self.solution.candy([1, 0, 2]), 5)

    def test_plateau(self):
        """Tests ratings with equal neighbors: [1,2,2] -> 4."""
        self.assertEqual(self.solution.candy([1, 2, 2]), 4)

    def test_single_child(self):
        """Tests a single child gets 1 candy."""
        self.assertEqual(self.solution.candy([1]), 1)

    def test_strictly_increasing(self):
        """Tests strictly increasing ratings: 1+2+3+4+5 = 15."""
        self.assertEqual(self.solution.candy([1, 2, 3, 4, 5]), 15)

    def test_strictly_decreasing(self):
        """Tests strictly decreasing ratings: 5+4+3+2+1 = 15."""
        self.assertEqual(self.solution.candy([5, 4, 3, 2, 1]), 15)

    def test_peak_in_middle(self):
        """Tests a peak in the middle: [1,2,3,2,1] -> 9."""
        self.assertEqual(self.solution.candy([1, 2, 3, 2, 1]), 9)

    def test_all_equal(self):
        """Tests all equal ratings: everyone gets 1."""
        self.assertEqual(self.solution.candy([3, 3, 3, 3]), 4)


if __name__ == "__main__":
    unittest.main()
