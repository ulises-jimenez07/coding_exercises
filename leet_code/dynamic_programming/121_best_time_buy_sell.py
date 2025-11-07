"""
Problem: Find the maximum profit from buying and selling a stock once.

Approach:
- Track the minimum buy price seen so far
- For each price, calculate profit if selling today
- Keep track of maximum profit found
- Time complexity: O(n) single pass through prices
- Space complexity: O(1) only storing two variables

Example: [7,1,5,3,6,4] -> buy at 1, sell at 6 for profit of 5
"""

import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = 10**9
        profit = 0

        for price in prices:
            # Update minimum buy price
            if price < buy_price:
                buy_price = price
            else:
                # Calculate profit if selling today
                profit = max(profit, price - buy_price)

        return profit


class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_prices(self):
        """Tests with an empty prices array."""
        self.assertEqual(self.solution.maxProfit([]), 0)

    def test_single_price(self):
        """Tests with a single price."""
        self.assertEqual(self.solution.maxProfit([5]), 0)

    def test_decreasing_prices(self):
        """Tests with decreasing prices."""
        self.assertEqual(self.solution.maxProfit([5, 4, 3, 2, 1]), 0)

    def test_increasing_prices(self):
        """Tests with increasing prices."""
        self.assertEqual(self.solution.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_mixed_prices(self):
        """Tests with mixed prices."""
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit(self):
        """Tests a case where no profit can be made."""
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
