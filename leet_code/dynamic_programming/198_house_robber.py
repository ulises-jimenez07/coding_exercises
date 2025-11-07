"""
Problem: Find maximum money that can be robbed without robbing adjacent houses.

Approach:
- Use dynamic programming with O(1) space
- For each house, choose max of: rob it (+ prev non-adjacent) or skip it
- Track two variables: max from two houses ago and one house ago
- Time complexity: O(n) single pass
- Space complexity: O(1) constant space

Example: [1,2,3,1] -> rob houses 0 and 2 for total 4
"""

import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # For each house, decide to rob it or skip
        for n in nums:
            # Either rob current + two houses ago, or keep previous max
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Tests a common example."""
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_example_2(self):
        """Tests another common example."""
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12)

    def test_single_house(self):
        """Tests with a single house."""
        self.assertEqual(self.solution.rob([10]), 10)

    def test_empty_list(self):
        """Tests with an empty list of houses."""
        self.assertEqual(self.solution.rob([]), 0)

    def test_two_houses(self):
        """Tests with two houses."""
        self.assertEqual(self.solution.rob([5, 6]), 6)


if __name__ == "__main__":
    unittest.main()
