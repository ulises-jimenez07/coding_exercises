"""
Problem: Find minimum operations to reduce a number to 1.

Approach:
- Use top-down DP with memoization
- If even: divide by 2
- If odd: choose to add 1 or subtract 1
- Recursively find minimum operations
- Time complexity: O(log n) with memoization
- Space complexity: O(log n) for cache and recursion

Example: 8 -> 8/2=4, 4/2=2, 2/2=1 (3 operations)
"""

import unittest


class Solution:
    def integerReplacement(self, n: int) -> int:
        self.dp: dict[int, int] = {}
        return self.min_no_op_i_to_1(n)

    def min_no_op_i_to_1(self, i: int) -> int:
        # Base case
        if i <= 1:
            return 0

        if i not in self.dp:
            ans = 0
            if i % 2 == 0:
                # Even: divide by 2
                ans = 1 + self.min_no_op_i_to_1(i // 2)
            else:
                # Odd: try both increment and decrement
                ans = 1 + min(self.min_no_op_i_to_1(i - 1), self.min_no_op_i_to_1(i + 1))
            self.dp[i] = ans

        return self.dp[i]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_even_number(self):
        """Test with an even number: 8 -> 3."""
        self.assertEqual(self.solution.integerReplacement(8), 3)

    def test_odd_number(self):
        """Test with an odd number: 7 -> 4."""
        self.assertEqual(self.solution.integerReplacement(7), 4)

    def test_one(self):
        """Test with the number 1: 1 -> 0."""
        self.assertEqual(self.solution.integerReplacement(1), 0)

    def test_path_through_increment(self):
        """Test with a number that results in a path through incrementation: 3 -> 2."""
        self.assertEqual(self.solution.integerReplacement(3), 2)

    def test_path_through_decrement(self):
        """Test with a number that results in a path through decrementation: 65535 -> 17."""
        self.assertEqual(self.solution.integerReplacement(65535), 17)


if __name__ == "__main__":
    unittest.main()
