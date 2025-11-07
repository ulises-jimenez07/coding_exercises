"""
Problem: Find max money robbed from circular houses without robbing adjacent ones.

Approach:
- Houses form a circle: first and last are adjacent
- Split into two subproblems: rob houses [0..n-2] or [1..n-1]
- Use linear house robber logic on each subproblem
- Return the maximum of both scenarios
- Time complexity: O(n) process array twice
- Space complexity: O(1) constant space

Example: [2,3,2] -> can't rob both ends, so rob middle for 3
"""

import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Try both: skip last house or skip first house
        return max(self._rob_linear(nums[:-1]), self._rob_linear(nums[1:]))

    def _rob_linear(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            # Rob current + i-2, or skip current
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Tests a simple case with three houses."""
        self.assertEqual(self.solution.rob([2, 3, 2]), 3)

    def test_example_2(self):
        """Tests a case with four houses."""
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_single_house(self):
        """Tests with a single house."""
        self.assertEqual(self.solution.rob([1]), 1)

    def test_two_houses(self):
        """Tests with two houses."""
        self.assertEqual(self.solution.rob([1, 2]), 2)

    def test_empty_list(self):
        """Tests with an empty list of houses."""
        self.assertEqual(self.solution.rob([]), 0)

    def test_varied_values(self):
        """Tests with houses having varying values."""
        self.assertEqual(self.solution.rob([20, 10, 50, 40]), 70)

    def test_complex_case(self):
        """Tests a more complex case."""
        self.assertEqual(self.solution.rob([6, 7, 1, 3, 8, 2, 5]), 20)


if __name__ == "__main__":
    unittest.main()
