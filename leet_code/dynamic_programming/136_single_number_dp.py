"""
Problem: Find the element that appears only once while all others appear twice.

Approach:
- Use XOR bit manipulation property: a ^ a = 0 and a ^ 0 = a
- XOR all numbers together, duplicates cancel out
- Only the single number remains
- Time complexity: O(n) single pass
- Space complexity: O(1) constant space

Example: [2,2,1] -> 2^2^1 = 0^1 = 1
"""

import unittest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        # XOR all numbers: duplicates cancel out
        for num in nums:
            ans ^= num
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_single_number(self):
        """Tests with a positive single number."""
        self.assertEqual(self.solution.singleNumber([2, 2, 1]), 1)

    def test_negative_single_number(self):
        """Tests with a negative single number."""
        self.assertEqual(self.solution.singleNumber([-1, -1, -2]), -2)

    def test_zero_as_duplicate(self):
        """Tests with zero as the duplicate number."""
        self.assertEqual(self.solution.singleNumber([0, 1, 0]), 1)

    def test_long_list(self):
        """Tests with a longer list of numbers."""
        self.assertEqual(self.solution.singleNumber([4, 1, 2, 1, 2]), 4)

    def test_single_element_list(self):
        """Tests with a list containing only one element."""
        self.assertEqual(self.solution.singleNumber([7]), 7)


if __name__ == "__main__":
    unittest.main()
