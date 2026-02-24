"""
Problem: Solve the 0/1 Knapsack problem.

Approach:
- Use dynamic programming with a 2D table.
- dp[i][w] represents the maximum value possible using the first i items with weight capacity w.
- For each item, decide whether to include it (if capacity allows) or exclude it.
- Time complexity: O(n * k) where n is number of items and k is capacity.
- Space complexity: O(n * k) for the DP table.
"""

import unittest
from typing import List


class Solution:
    """Solution for the 0/1 Knapsack problem."""

    def knapsack(self, k: int, weights: List[int], values: List[int]) -> int:
        """
        Calculate the maximum value that can be fit into a knapsack of capacity k.
        """
        n = len(values)
        # Initialize DP table with zeros
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Fill the DP table using enumerate for items
        for i, (w, v) in enumerate(zip(weights, values), 1):
            for c in range(1, k + 1):
                if w <= c:
                    # Decide to include item i or not
                    dp[i][c] = max(v + dp[i - 1][c - w], dp[i - 1][c])
                else:
                    # Item is too heavy, skip it
                    dp[i][c] = dp[i - 1][c]

        return dp[n][k]


class TestKnapsack(unittest.TestCase):
    """Unit tests for the knapsack implementation."""

    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example(self):
        """Test with a standard example."""
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        k = 7
        # Optimal: items with weight 3 and 4 (total value 4+5=9)
        self.assertEqual(self.solution.knapsack(k, weights, values), 9)

    def test_empty_lists(self):
        """Test with empty weights and values."""
        self.assertEqual(self.solution.knapsack(10, [], []), 0)

    def test_zero_capacity(self):
        """Test with zero capacity."""
        self.assertEqual(self.solution.knapsack(0, [1, 2, 3], [10, 20, 30]), 0)

    def test_single_element_fits(self):
        """Test with a single item that fits."""
        self.assertEqual(self.solution.knapsack(5, [3], [10]), 10)

    def test_single_element_too_heavy(self):
        """Test with a single item that is too heavy."""
        self.assertEqual(self.solution.knapsack(2, [3], [10]), 0)

    def test_all_elements_too_heavy(self):
        """Test where all items exceed the capacity."""
        self.assertEqual(self.solution.knapsack(2, [5, 10, 15], [100, 200, 300]), 0)

    def test_all_elements_fit(self):
        """Test where all items can fit."""
        self.assertEqual(self.solution.knapsack(50, [5, 10, 15], [100, 200, 300]), 600)


if __name__ == "__main__":
    unittest.main()
