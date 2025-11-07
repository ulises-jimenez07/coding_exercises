"""
Problem: Count distinct ways to climb n stairs (1 or 2 steps at a time).

Approach:
- Use top-down recursion with memoization
- From position i, can move to i+1 or i+2
- Base cases: reached n (1 way), exceeded n (0 ways)
- Cache results to avoid recomputation
- Time complexity: O(n) with memoization
- Space complexity: O(n) for cache and recursion stack

Example: n=5 -> 8 ways
"""

import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        self.num_ways: dict[int, int] = {}
        return self.num_ways_to_n(0, n)

    def num_ways_to_n(self, i: int, n: int) -> int:
        # Base cases
        if i > n:
            return 0
        if i == n:
            return 1

        # Return cached result
        if i in self.num_ways:
            return self.num_ways[i]
        else:
            # Try both 1-step and 2-step moves
            self.num_ways[i] = self.num_ways_to_n(i + 1, n) + self.num_ways_to_n(i + 2, n)
            return self.num_ways[i]


class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_equals_1(self):
        """Test case for n = 1."""
        self.assertEqual(self.solution.climbStairs(1), 1)

    def test_n_equals_2(self):
        """Test case for n = 2."""
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_n_equals_3(self):
        """Test case for n = 3."""
        self.assertEqual(self.solution.climbStairs(3), 3)

    def test_n_equals_4(self):
        """Test case for n = 4."""
        self.assertEqual(self.solution.climbStairs(4), 5)

    def test_n_equals_5(self):
        """Test case for n = 5."""
        self.assertEqual(self.solution.climbStairs(5), 8)

    def test_n_equals_30(self):
        """Test case for a larger number, n = 30."""
        self.assertEqual(self.solution.climbStairs(30), 1346269)


if __name__ == "__main__":
    unittest.main()
