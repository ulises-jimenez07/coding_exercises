"""
Problem: Find minimum cost to reach top of stairs with given step costs.

Approach:
- Use dynamic programming array
- dp[i] = minimum cost to reach step i
- Can start from step 0 or 1 (cost 0)
- At each step, choose min of coming from i-1 or i-2
- Time complexity: O(n) single pass
- Space complexity: O(n) for dp array

Example: [10,15,20] -> start at 1, pay 15, reach top = 15
"""

import unittest
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        # Can start from step 0 or 1
        for i in range(2, n + 1):
            # Choose min: step from i-1 or i-2
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Tests example from problem description: [10, 15, 20] -> 15."""
        self.assertEqual(self.solution.minCostClimbingStairs([10, 15, 20]), 15)

    def test_example_2(self):
        """Tests example from problem description: [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] -> 6."""
        self.assertEqual(self.solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    def test_empty_cost_list(self):
        """Tests with an empty cost list -> 0."""
        self.assertEqual(self.solution.minCostClimbingStairs([]), 0)

    def test_two_steps(self):
        """Tests with two steps: [1, 2] -> 1."""
        self.assertEqual(self.solution.minCostClimbingStairs([1, 2]), 1)

    def test_single_step(self):
        """Tests with a single step: [5] -> 0."""
        self.assertEqual(self.solution.minCostClimbingStairs([5]), 0)

    def test_more_complex_case(self):
        """Tests a more complex case: [10, 1, 1, 1, 1] -> 2."""
        self.assertEqual(self.solution.minCostClimbingStairs([10, 1, 1, 1, 1]), 2)


if __name__ == "__main__":
    unittest.main()
