"""
Problem: Find the missing number in array containing n distinct numbers from 0 to n

Approach:
- Use XOR property: a ^ a = 0, so XOR all indices with all values
- Missing number won't have a pair to cancel out
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for i in range(len(nums) + 1):
            x ^= i  # XOR with all expected numbers

        y = 0
        for num in nums:
            y ^= num  # XOR with all actual numbers

        return x ^ y  # Result is the missing number


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_small_array_middle_missing(self):
        """Test with a small array where the missing number is in the middle: [3, 0, 1] -> 2."""
        self.assertEqual(self.solution.missingNumber([3, 0, 1]), 2)

    def test_missing_at_end(self):
        """Test with the missing number at the end of the range: [0, 1] -> 2."""
        self.assertEqual(self.solution.missingNumber([0, 1]), 2)

    def test_larger_array_beginning_missing(self):
        """Test with a larger array and the missing number at the beginning: [9, 6, 4, 2, 3, 5, 7, 0, 1] -> 8."""
        self.assertEqual(self.solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_empty_array(self):
        """Test with an empty array: [] -> 0."""
        self.assertEqual(self.solution.missingNumber([]), 0)


if __name__ == "__main__":
    unittest.main()
