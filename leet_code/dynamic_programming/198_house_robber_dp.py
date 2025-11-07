"""
Problem: Find maximum money that can be robbed without robbing adjacent houses.

Approach:
- Use dynamic programming with O(n) space array
- Build up solution: dp[i] = max money robbing houses 0 to i
- For each house: either rob it (+ dp[i-2]) or skip it (keep dp[i-1])
- Time complexity: O(n) single pass
- Space complexity: O(n) for dp array

Example: [2,7,9,3,1] -> rob houses 1 and 3 for total 12
"""

import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            if i == 1:
                # Choose max of first two houses
                dp[i] = max(nums[0], nums[1])
            else:
                # Rob current + i-2, or skip current
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


class TestRob(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_input(self):
        """Test with an empty list of houses."""
        self.assertEqual(self.solution.rob([]), 0)

    def test_single_house(self):
        """Test with a single house."""
        self.assertEqual(self.solution.rob([5]), 5)

    def test_two_houses(self):
        """Test with two houses."""
        self.assertEqual(self.solution.rob([1, 2]), 2)

    def test_example_1(self):
        """Test case from problem description: [1, 2, 3, 1] -> 4."""
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_example_2(self):
        """Test case from problem description: [2, 7, 9, 3, 1] -> 12."""
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12)

    def test_all_same_value(self):
        """Test with all houses having the same value."""
        self.assertEqual(self.solution.rob([5, 5, 5, 5, 5]), 15)

    def test_descending_values(self):
        """Test with houses having descending values."""
        self.assertEqual(self.solution.rob([5, 4, 3, 2, 1]), 9)


if __name__ == "__main__":
    unittest.main()
