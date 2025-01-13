import unittest


class Solution(object):
    def coinChange(self, coins, amount):
        """
        You are given an integer array coins representing a list of coin denominations and an integer amount representing a total amount of money.

        Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

        You may assume that you have an infinite number of each kind of coin.

        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # If amount is less than or equal to 0, return 0
        if amount <= 0:
            return 0

        # Initialize dp table with infinity for all amounts from 1 to amount
        dp = [float("inf")] * (amount + 1)
        # Base case: 0 coins needed to make amount 0
        dp[0] = 0

        # Iterate through amounts from 1 to amount
        for i in range(1, amount + 1):
            # Iterate through each coin denomination
            for coin in coins:
                # If current coin is less than or equal to current amount
                # and the number of coins needed to make up (amount - coin) is not infinity
                if coin <= i and dp[i - coin] != float("inf"):
                    # Update dp[i] with the minimum of current value and (number of coins to make (i-coin) + 1)
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # Return dp[amount] if it's not infinity, otherwise return -1
        return dp[amount] if dp[amount] != float("inf") else -1


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_amount_zero(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 0), 0)

    def test_amount_less_than_zero(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], -5), 0)

    def test_cannot_make_amount(self):
        self.assertEqual(self.solution.coinChange([2], 3), -1)

    def test_single_coin(self):
        self.assertEqual(self.solution.coinChange([1], 5), 5)

    def test_multiple_coins(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)

    def test_large_amount(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 100), 20)

    def test_duplicate_coins(self):
        self.assertEqual(self.solution.coinChange([1, 2, 2, 5], 11), 3)

    # Additional test cases
    def test_empty_coins(self):
        self.assertEqual(self.solution.coinChange([], 5), -1)

    def test_example_leetcode_1(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)

    def test_example_leetcode_2(self):
        self.assertEqual(self.solution.coinChange([2], 3), -1)

    def test_example_leetcode_3(self):
        self.assertEqual(self.solution.coinChange([1], 0), 0)


if __name__ == "__main__":
    unittest.main()
