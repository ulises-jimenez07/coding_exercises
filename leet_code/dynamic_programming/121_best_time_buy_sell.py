import unittest


class Solution(object):
    def maxProfit(self, prices):
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        :type prices: List[int]
        :rtype: int
        """
        buy_price = float("inf")  # Initialize buy price to infinity
        profit = 0  # Initialize profit to 0

        for price in prices:  # Iterate through the prices
            if (
                price < buy_price
            ):  # If current price is lower than buy price, update buy price
                buy_price = price
            else:  # If current price is higher than buy price, calculate potential profit
                profit = max(
                    profit, price - buy_price
                )  # Update profit if potential profit is higher

        return profit  # Return the maximum profit


class TestMaxProfit(unittest.TestCase):  # Test cases using unittest
    def setUp(self):
        self.solution = Solution()

    def test_empty_prices(self):  # Test with empty prices array
        self.assertEqual(self.solution.maxProfit([]), 0)

    def test_single_price(self):  # Test with single price
        self.assertEqual(self.solution.maxProfit([5]), 0)

    def test_decreasing_prices(self):  # Test with decreasing prices
        self.assertEqual(self.solution.maxProfit([5, 4, 3, 2, 1]), 0)

    def test_increasing_prices(self):  # Test with increasing prices
        self.assertEqual(self.solution.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_mixed_prices(self):  # Test with mixed prices
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_example_1(self):  # Example 1 from LeetCode
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
