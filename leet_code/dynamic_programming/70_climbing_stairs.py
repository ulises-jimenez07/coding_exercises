"""
Problem: Count distinct ways to climb n stairs (1 or 2 steps at a time).

Approach:
- Use dynamic programming with O(1) space (Fibonacci pattern)
- ways[n] = ways[n-1] + ways[n-2]
- Only track last two values instead of full array
- Base cases: 1 step has 1 way, 2 steps have 2 ways
- Time complexity: O(n) iterate through steps
- Space complexity: O(1) constant space

Example: n=5 -> 8 ways (11111, 1112, 1121, 1211, 2111, 122, 212, 221)
"""

import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        one_step_before = 2
        two_steps_before = 1

        # Build up from step 3 to n
        for _ in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before


class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_one_step(self):
        """Test case for 1 step."""
        self.assertEqual(self.solution.climbStairs(1), 1)

    def test_two_steps(self):
        """Test case for 2 steps."""
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_three_steps(self):
        """Test case for 3 steps."""
        self.assertEqual(self.solution.climbStairs(3), 3)

    def test_four_steps(self):
        """Test case for 4 steps."""
        self.assertEqual(self.solution.climbStairs(4), 5)

    def test_five_steps(self):
        """Test case for 5 steps."""
        self.assertEqual(self.solution.climbStairs(5), 8)

    def test_large_number_of_steps(self):
        """Test case for a larger number of steps (10 steps)."""
        self.assertEqual(self.solution.climbStairs(10), 89)


if __name__ == "__main__":
    unittest.main()
