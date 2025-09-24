import unittest
from typing import List

class Solution:
    """
    Solution for the Min Cost Climbing Stairs problem.
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Calculates the minimum cost to climb to the top of a staircase.

        You can either climb one or two steps at a time. The cost of
        a step is given by `cost[i]`. After paying the cost, you can
        either step one or two steps.

        Args:
            cost: A list of integers where `cost[i]` is the cost of the i-th step.

        Returns:
            The minimum cost to reach the top of the stairs.
        """
        n = len(cost)
        
        # `dp[i]` represents the minimum cost to reach the i-th step.
        # We need a size of n+1 to account for the "top" of the stairs.
        dp = [0] * (n + 1)
        
        # Base cases: The cost to reach step 0 and 1 is 0, since you can start there for free.
        # This is implicitly handled by initializing `dp` with zeros.

        # Iterate from the third step up to the top of the stairs (n).
        for i in range(2, n + 1):
            # The minimum cost to reach step `i` is the minimum of two options:
            # 1. Coming from step `i-1`: The cost is `dp[i-1]` + the cost of step `i-1`.
            # 2. Coming from step `i-2`: The cost is `dp[i-2]` + the cost of step `i-2`.
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        # The result is the minimum cost to reach the top of the stairs, which is at `dp[-1]`.
        return dp[-1]

# -----------------------------------------------------------------------------

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """
    def test_minCostClimbingStairs(self):
        """
        Tests the minCostClimbingStairs method with various test cases.
        """
        sol = Solution()

        # Test case 1: Example from the problem description
        self.assertEqual(sol.minCostClimbingStairs([10, 15, 20]), 15)

        # Test case 2: Example from the problem description
        self.assertEqual(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
        
        # Test case 3: Empty cost list
        self.assertEqual(sol.minCostClimbingStairs([]), 0)
        
        # Test case 4: Two steps
        self.assertEqual(sol.minCostClimbingStairs([1, 2]), 1)
        
        # Test case 5: Single step
        # The code will handle this gracefully because the loop range(2, 2) is empty.
        # The result `dp[-1]` will be `dp[1]`, which is 0. This is a valid interpretation
        # as you can "step off" the one stair for free.
        self.assertEqual(sol.minCostClimbingStairs([5]), 0)

        # Test case 6: More complex case
        self.assertEqual(sol.minCostClimbingStairs([10, 1, 1, 1, 1]), 2)

if __name__ == '__main__':
    unittest.main()