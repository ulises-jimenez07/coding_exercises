"""
Problem: Count ways to assign +/- signs to numbers to reach target sum.

Approach:
- Use top-down DP with memoization
- At each position, try adding or subtracting the number
- Track (index, remaining_target) state
- Base case: at last element, check if target matches
- Time complexity: O(n * sum) possible states
- Space complexity: O(n * sum) for memoization

Example: [1,1,1,1,1], target=3 -> 5 ways like +1+1+1+1-1=3
"""

import unittest
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.ht: dict[tuple[int, int], int] = {}  # Memoization: (index, remaining_target) -> count
        return self.num_to_target(0, target)

    def num_to_target(self, i: int, ct: int) -> int:
        # Not at last element yet
        if i < len(self.nums) - 1:
            key = (i, ct)
            if key in self.ht:
                return self.ht[key]

            # Try subtracting and adding current number
            self.ht[key] = self.num_to_target(i + 1, ct - self.nums[i]) + self.num_to_target(i + 1, ct + self.nums[i])
            return self.ht[key]

        # Base case: at last element
        if ct == 0 and self.nums[i] == 0:
            return 2  # Can use +0 or -0

        if abs(ct) == abs(self.nums[i]):
            return 1  # Exactly one way to reach target

        return 0  # Cannot reach target


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case from problem description: [1,1,1,1,1], target = 3 -> 5."""
        self.assertEqual(self.solution.findTargetSumWays([1, 1, 1, 1, 1], 3), 5)

    def test_single_element_positive_target(self):
        """Test with a single element and a positive target: [1], target = 1 -> 1."""
        self.assertEqual(self.solution.findTargetSumWays([1], 1), 1)

    def test_single_element_negative_target(self):
        """Test with a single element and a negative target: [1], target = -1 -> 1."""
        self.assertEqual(self.solution.findTargetSumWays([1], -1), 1)

    def test_with_zero_element(self):
        """Test case involving a zero: [0], target = 0 -> 2."""
        self.assertEqual(self.solution.findTargetSumWays([0], 0), 2)

    def test_larger_set(self):
        """Test case with a larger set of numbers: [7,9,3,8,0,6,1,5,4,2], target = 1 -> 46."""
        self.assertEqual(self.solution.findTargetSumWays([7, 9, 3, 8, 0, 6, 1, 5, 4, 2], 1), 46)


if __name__ == "__main__":
    unittest.main()
