import unittest
from typing import List


class Solution:
    """
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.
    """

    def rob(self, nums: List[int]) -> int:
        """
        Dynamic programming approach to solve the house robber problem.
        """
        n = len(nums)
        if n == 0:  # Handle empty input
            return 0

        dp = [0] * n  # Initialize DP table
        dp[0] = nums[0]  # Base case: robbing the first house

        for i in range(1, n):
            if i == 1:  # Special case: second house
                dp[i] = max(nums[0], nums[1])
            else:  # General case: consider robbing current house or skipping it
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]  # Return the maximum amount that can be robbed


class TestRob(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_input(self):
        self.assertEqual(self.solution.rob([]), 0)

    def test_single_house(self):
        self.assertEqual(self.solution.rob([5]), 5)

    def test_two_houses(self):
        self.assertEqual(self.solution.rob([1, 2]), 2)

    def test_example_1(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12)

    def test_all_same_value(self):
        self.assertEqual(self.solution.rob([5, 5, 5, 5, 5]), 15)

    def test_descending_values(self):
        self.assertEqual(self.solution.rob([5, 4, 3, 2, 1]), 9)


if __name__ == "__main__":
    unittest.main()
