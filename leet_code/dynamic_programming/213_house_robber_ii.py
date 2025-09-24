import unittest
from typing import List

class Solution:
    """
    Solution for the House Robber II problem.
    """
    def rob(self, nums: List[int]) -> int:
        """
        Calculates the maximum amount of money that can be robbed from a circular row of houses.

        The problem is split into two subproblems: robbing houses from 0 to n-2 and robbing
        houses from 1 to n-1. This is because if the first house is robbed, the last one cannot be,
        and vice-versa, due to the circular arrangement. The maximum of these two
        subproblems is the final answer.

        Args:
            nums: A list of integers representing the amount of money in each house.

        Returns:
            The maximum amount of money that can be robbed.
        """
        n = len(nums)

        # Handle base cases for small number of houses.
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        # The problem is now reduced to finding the maximum of two non-circular subproblems.
        # Subproblem 1: Rob houses from index 0 to n-2.
        # Subproblem 2: Rob houses from index 1 to n-1.
        return max(self.house_rob(nums, 0, n - 2), self.house_rob(nums, 1, n - 1))

    def house_rob(self, nums: List[int], start: int, end: int) -> int:
        """
        Calculates the maximum amount of money that can be robbed from a linear
        row of houses using dynamic programming.

        This is a standard House Robber I solution. `dp[i]` represents the maximum
        money that can be robbed up to house `i`.

        Args:
            nums: A list of integers representing the amount of money in each house.
            start: The starting index of the houses to consider.
            end: The ending index of the houses to consider.

        Returns:
            The maximum amount of money that can be robbed in the specified range.
        """
        # Base case for a single house in the range.
        if start == end:
            return nums[start]

        # Initialize a DP array to store the maximum amount of money robbed up to each house.
        dp = [0] * len(nums)

        # `dp[start]` is the amount at the first house in the range.
        dp[start] = nums[start]
        # `dp[start + 1]` is the maximum of the first two houses in the range.
        dp[start + 1] = max(nums[start], nums[start + 1])

        # Iterate through the houses from the third one in the range.
        for i in range(start + 2, end + 1):
            # The maximum money at house `i` is the greater of two options:
            # 1. Robbing house `i` plus the maximum amount from `i-2`.
            # 2. Not robbing house `i` and taking the maximum from `i-1`.
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        # The result is the maximum amount at the last house in the range.
        return dp[end]

# -----------------------------------------------------------------------------

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """
    def test_rob(self):
        """
        Tests the rob method with various test cases.
        """
        sol = Solution()

        # Test case 1: Normal case, houses 1-2-3-1
        self.assertEqual(sol.rob([2, 3, 2]), 3)

        # Test case 2: Normal case, houses 2-7-9-3-1
        self.assertEqual(sol.rob([1, 2, 3, 1]), 4)
        
        # Test case 3: Single house
        self.assertEqual(sol.rob([1]), 1)
        
        # Test case 4: Two houses
        self.assertEqual(sol.rob([1, 2]), 2)
        
        # Test case 5: Empty list
        self.assertEqual(sol.rob([]), 0)
        
        # Test case 6: Houses with varying values
        self.assertEqual(sol.rob([20, 10, 50, 40]), 70)

        # Test case 7: A more complex case
        self.assertEqual(sol.rob([6, 7, 1, 3, 8, 2, 5]), 20)

if __name__ == '__main__':
    unittest.main()