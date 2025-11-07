"""
Problem: Find the minimum number of coins needed to make a target amount.

Approach:
- Use bottom-up dynamic programming
- dp[i] = minimum coins needed to make amount i
- For each amount, try all coins and take minimum
- Build up from 0 to target amount
- Time complexity: O(amount * coins) nested loops
- Space complexity: O(amount) for dp array

Example: coins=[1,2,5], amount=11 -> use 5+5+1 for 3 coins
"""

import unittest
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                # Try using this coin if it fits
                if coin <= i and dp[i - coin] != float("inf"):
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return int(dp[amount]) if dp[amount] != float("inf") else -1


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_amount_zero(self):
        """Test with amount zero."""
        self.assertEqual(self.solution.coinChange([1, 2, 5], 0), 0)

    def test_amount_less_than_zero(self):
        """Test with amount less than zero."""
        self.assertEqual(self.solution.coinChange([1, 2, 5], -5), 0)

    def test_cannot_make_amount(self):
        """Test case where the amount cannot be made."""
        self.assertEqual(self.solution.coinChange([2], 3), -1)

    def test_single_coin(self):
        """Test with a single coin denomination."""
        self.assertEqual(self.solution.coinChange([1], 5), 5)

    def test_multiple_coins(self):
        """Test with multiple coin denominations."""
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)

    def test_large_amount(self):
        """Test with a large amount."""
        self.assertEqual(self.solution.coinChange([1, 2, 5], 100), 20)

    def test_duplicate_coins(self):
        """Test with duplicate coin denominations."""
        self.assertEqual(self.solution.coinChange([1, 2, 2, 5], 11), 3)

    def test_empty_coins(self):
        """Test with an empty list of coins."""
        self.assertEqual(self.solution.coinChange([], 5), -1)

    def test_leetcode_example_1(self):
        """Test case from LeetCode example 1."""
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)

    def test_leetcode_example_2(self):
        """Test case from LeetCode example 2."""
        self.assertEqual(self.solution.coinChange([2], 3), -1)

    def test_leetcode_example_3(self):
        """Test case from LeetCode example 3."""
        self.assertEqual(self.solution.coinChange([1], 0), 0)


if __name__ == "__main__":
    unittest.main()
