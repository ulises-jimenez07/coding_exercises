"""
Problem: Find the minimum number of coins needed to make a target amount.

Approach:
- Use top-down dynamic programming with memoization
- Recursively try each coin and take minimum
- Cache results to avoid recomputation
- Base cases: amount 0 needs 0 coins, negative is invalid
- Time complexity: O(amount * coins) with memoization
- Space complexity: O(amount) for cache and recursion stack

Example: coins=[1,2,5], amount=11 -> use 5+5+1 for 3 coins
"""

import unittest
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp: dict[int, int] = {}
        self.coins = coins
        return self.how_many_to_i(amount)

    def how_many_to_i(self, i: int) -> int:
        # Base cases
        if i == 0:
            return 0
        if i < 0:
            return -1

        # Return cached result
        if i in self.dp:
            return self.dp[i]

        ans = float("inf")

        # Try each coin
        for coin in self.coins:
            result = self.how_many_to_i(i - coin)

            if result != -1:
                ans = min(ans, result + 1)

        self.dp[i] = int(ans) if ans != float("inf") else -1
        return self.dp[i]


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case from the problem description: coins = [1, 2, 5], amount = 11 -> 3."""
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)

    def test_amount_cannot_be_made(self):
        """Test case where the amount cannot be made: coins = [2], amount = 3 -> -1."""
        self.assertEqual(self.solution.coinChange([2], 3), -1)

    def test_amount_zero(self):
        """Test case with amount 0: coins = [1], amount = 0 -> 0."""
        self.assertEqual(self.solution.coinChange([1], 0), 0)

    def test_large_amount_and_coins(self):
        """Test case with a large amount and different coins: 6249 -> 20."""
        self.assertEqual(self.solution.coinChange([186, 419, 83, 408], 6249), 20)

    def test_single_coin_perfect_division(self):
        """Test case with a single coin that perfectly divides the amount: [3], 9 -> 3."""
        self.assertEqual(self.solution.coinChange([3], 9), 3)

    def test_no_solution_with_large_coins(self):
        """Test case where no solution exists because all coins are larger than the amount: [10, 20, 30], 5 -> -1."""
        self.assertEqual(self.solution.coinChange([10, 20, 30], 5), -1)

    def test_recursive_logic_with_mismatch(self):
        """Test case for recursive logic with a mismatch: [4, 5], 7 -> -1."""
        self.assertEqual(self.solution.coinChange([4, 5], 7), -1)


if __name__ == "__main__":
    unittest.main()
