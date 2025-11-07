"""
Problem: Determine if any subset of numbers sums to target value.

Approach:
- Use 2D dynamic programming table
- dp[i][j] = can we make sum j using first i numbers
- Base case: sum 0 is always possible (empty subset)
- For each number, can include it or exclude it
- Time complexity: O(n * target_sum) fill entire table
- Space complexity: O(n * target_sum) for dp table

Example: [1,2,3], target=5 -> True (2+3=5)
"""

import unittest
from typing import List


class Solution:
    def isSubsetSum(self, nums: List[int], n: int, target_sum: int) -> bool:
        subset = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

        # Base case: sum of 0 is always achievable
        for i in range(n + 1):
            subset[i][0] = True

        # Base case: can't make positive sum with 0 elements
        for i in range(1, target_sum + 1):
            subset[0][i] = False

        # Fill dp table
        for i in range(1, n + 1):
            for j in range(1, target_sum + 1):
                if j < nums[i - 1]:
                    # Can't include current number (too large)
                    subset[i][j] = subset[i - 1][j]
                else:
                    # Try both including and excluding current number
                    subset[i][j] = subset[i - 1][j] or subset[i - 1][j - nums[i - 1]]

        return subset[n][target_sum]


class TestIsSubsetSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_set_zero_sum(self):
        """Test with an empty set and zero sum."""
        self.assertTrue(self.solution.isSubsetSum([], 0, 0))

    def test_empty_set_non_zero_sum(self):
        """Test with an empty set and non-zero sum."""
        self.assertFalse(self.solution.isSubsetSum([], 0, 5))

    def test_positive_elements_found(self):
        """Test with positive elements where subset sum is found."""
        self.assertTrue(self.solution.isSubsetSum([1, 2, 3], 3, 3))
        self.assertTrue(self.solution.isSubsetSum([1, 2, 3], 3, 5))

    def test_positive_elements_not_found(self):
        """Test with positive elements where subset sum is not found."""
        self.assertFalse(self.solution.isSubsetSum([1, 2, 3], 3, 7))

    def test_zero_target_sum(self):
        """Test with a zero target sum."""
        self.assertTrue(self.solution.isSubsetSum([1, 2, 3], 3, 0))

    def test_duplicate_elements(self):
        """Test with duplicate elements."""
        self.assertTrue(self.solution.isSubsetSum([2, 2, 3], 3, 4))

    def test_large_set_found(self):
        """Test with a large set where subset sum is found."""
        self.assertTrue(self.solution.isSubsetSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 55))

    def test_large_set_not_found(self):
        """Test with a large set where subset sum is not found."""
        self.assertFalse(self.solution.isSubsetSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 60))


if __name__ == "__main__":
    unittest.main()
