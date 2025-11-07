"""
Problem: Find the length of the longest strictly increasing subsequence.

Approach:
- Use dynamic programming with O(n²) approach
- dp[i] = length of LIS ending at index i
- For each position, check all previous smaller elements
- Build up length by extending previous subsequences
- Time complexity: O(n²) nested loops
- Space complexity: O(n) for dp array

Example: [10,9,2,5,3,7,101,18] -> [2,3,7,101] with length 4
"""

import unittest
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        ans = 1

        for i in range(1, len(nums)):
            current_val = 1
            # Check all previous elements
            for j in range(i):
                if nums[j] < nums[i]:
                    # Extend subsequence ending at j
                    current_val = max(current_val, dp[j] + 1)
            dp[i] = current_val
            ans = max(ans, dp[i])

        return ans


class TestLengthOfLIS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_increasing_subsequence(self):
        """Test case with a standard increasing subsequence."""
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_all_increasing_order(self):
        """Test case with all numbers in increasing order."""
        nums = [0, 1, 2, 3, 4, 5]
        expected = 6
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_all_decreasing_order(self):
        """Test case with all numbers in decreasing order."""
        nums = [7, 6, 5, 4, 3, 2, 1]
        expected = 1
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_empty_list(self):
        """Test case with an empty list."""
        nums = []
        expected = 0
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_single_element_list(self):
        """Test case with a single-element list."""
        nums = [5]
        expected = 1
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_duplicate_numbers(self):
        """Test case with duplicate numbers."""
        nums = [1, 3, 2, 4, 5, 2, 3, 4]
        expected = 4
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)


if __name__ == "__main__":
    unittest.main()
