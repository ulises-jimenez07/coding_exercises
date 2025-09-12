from typing import List
import unittest


class Solution:
    """
    Solves the Coin Change problem using a top-down dynamic programming (memoization) approach.
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Calculates the minimum number of coins to make a given amount.

        Args:
            coins: A list of coin denominations.
            amount: The target amount.

        Returns:
            The minimum number of coins, or -1 if the amount cannot be made.
        """
        # Memoization dictionary to store results for subproblems
        self.dp = {}
        # Store the list of coins for easy access in the recursive helper
        self.coins = coins
        # Start the recursive calculation from the target amount
        return self.how_many_to_i(amount)

    def how_many_to_i(self, i: int) -> int:
        """
        A recursive helper function to find the minimum number of coins for amount `i`.

        Args:
            i: The current amount to calculate.

        Returns:
            The minimum number of coins, or -1 if the amount cannot be made.
        """
        # Base case: if the amount is 0 or less, no coins are needed
        if i == 0:
            return 0
        # If the amount is negative, it's an invalid path, so return -1
        if i < 0:
            return -1
        # Check if the result for amount `i` is already memoized
        if i in self.dp:
            return self.dp[i]

        # Initialize the answer to a value indicating it's not yet found
        ans = float("inf")

        # Iterate through each coin to find the best possible solution
        for coin in self.coins:
            # Recursive call to find the number of coins for the remaining amount
            result = self.how_many_to_i(i - coin)

            # If a valid solution exists for the subproblem, update the answer
            if result != -1:
                ans = min(ans, result + 1)

        # Memoize the result. If `ans` is still infinity, it means no solution was found.
        self.dp[i] = ans if ans != float("inf") else -1
        return self.dp[i]


# Unit tests for the Solution class
class TestCoinChange(unittest.TestCase):
    """
    Unit tests for the coinChange method.
    """

    def test_example_1(self):
        """
        Test case from the problem description: coins = [1, 2, 5], amount = 11.
        Expected output: 3 (5 + 5 + 1)
        """
        sol = Solution()
        self.assertEqual(sol.coinChange([1, 2, 5], 11), 3)

    def test_example_2(self):
        """
        Test case where the amount cannot be made: coins = [2], amount = 3.
        Expected output: -1
        """
        sol = Solution()
        self.assertEqual(sol.coinChange([2], 3), -1)

    def test_example_3(self):
        """
        Test case with amount 0: coins = [1], amount = 0.
        Expected output: 0
        """
        sol = Solution()
        self.assertEqual(sol.coinChange([1], 0), 0)

    def test_large_amount_and_coins(self):
        """
        Test case with a large amount and different coins.
        Expected output: 20 (186 + 186 + 186 + 186 + 186 = 930)
        """
        sol = Solution()
        self.assertEqual(sol.coinChange([186, 419, 83, 408], 6249), 20)

    def test_single_coin(self):
        """
        Test case with a single coin that perfectly divides the amount.
        Expected output: 3
        """
        sol = Solution()
        self.assertEqual(sol.coinChange([3], 9), 3)

    def test_no_solution_with_large_coins(self):
        """
        Test case where no solution exists because all coins are larger than the amount.
        Expected output: -1
        """
        sol = Solution()
        self.assertEqual(sol.coinChange([10, 20, 30], 5), -1)

    def test_recursive_logic_with_mismatch(self):
        """
        This test case exposes the flaw in the original logic. The recursive call
        `self.how_many_to_i(i - coin)` needs to check for a valid return value
        before proceeding. The original code has an error where it doesn't correctly
        handle invalid subproblem results. My corrected code addresses this.
        """
        sol = Solution()
        self.assertEqual(sol.coinChange([4, 5], 7), -1)


if __name__ == "__main__":
    unittest.main()
