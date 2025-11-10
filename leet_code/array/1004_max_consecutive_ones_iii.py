"""
Problem: Find the longest subarray of 1's after flipping at most k zeros

Approach:
- Use sliding window to track zeros in current window
- Expand window right, contract left when zeros exceed k
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Solution for finding longest subarray of 1's after flipping at most k zeros."""

    def longestOnes(self, nums: List[int], k: int) -> int:
        """Finds the length of longest subarray of 1's after flipping at most k zeros."""
        zeros = 0
        left = 0
        max_length = 0

        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_length = max(right - left + 1, max_length)

        return max_length


class TestLongestOnes(unittest.TestCase):
    """Test cases for the longestOnes solution."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example with k flips."""
        self.assertEqual(self.solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)

    def test_all_zeros(self):
        """Array with all zeros."""
        self.assertEqual(self.solution.longestOnes([0, 0, 0, 0], 2), 2)

    def test_all_ones(self):
        """Array with all ones."""
        self.assertEqual(self.solution.longestOnes([1, 1, 1, 1], 0), 4)

    def test_no_flips_allowed(self):
        """No flips allowed."""
        self.assertEqual(self.solution.longestOnes([1, 0, 1, 1, 0, 1], 0), 2)

    def test_single_element(self):
        """Single element array."""
        self.assertEqual(self.solution.longestOnes([0], 1), 1)

    def test_k_larger_than_zeros(self):
        """k larger than number of zeros."""
        self.assertEqual(self.solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10)


if __name__ == "__main__":
    unittest.main()
