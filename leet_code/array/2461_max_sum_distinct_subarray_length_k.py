"""
Problem: Find the maximum subarray sum of length k with distinct elements

Approach:
- Use a sliding window of size k
- Maintain a running sum and a frequency map of elements in the current window
- If the frequency map size equals k, all elements are distinct
- Time complexity: O(n) where n is the length of nums
- Space complexity: O(k) for the frequency map
"""

import unittest
from collections import defaultdict
from typing import List


class Solution:
    """Finds the maximum sum of a distinct subarray of length k."""

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """Calculates the max sum of a contiguous subarray of length k with all distinct elements."""
        seen: dict[int, int] = defaultdict(int)
        max_sum = 0
        curr_sum = 0

        for i, num in enumerate(nums):
            # Add current element to window
            curr_sum += num
            seen[num] += 1

            # Remove element that slides out of the window
            if i >= k:
                left_val = nums[i - k]
                curr_sum -= left_val
                seen[left_val] -= 1
                if seen[left_val] == 0:
                    del seen[left_val]

            # Update max sum if the window is valid (size k and all distinct)
            if len(seen) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum


class TestMaximumSubarraySum(unittest.TestCase):
    """Test suite for maximumSubarraySum method."""

    def setUp(self):
        """Initializes the Solution object before each test."""
        self.solution = Solution()

    def test_leetcode_example_1(self):
        """Tests the first LeetCode example."""
        self.assertEqual(self.solution.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3), 15)

    def test_leetcode_example_2(self):
        """Tests the second LeetCode example."""
        self.assertEqual(self.solution.maximumSubarraySum([4, 4, 4], 3), 0)

    def test_empty_list(self):
        """Tests an empty input list."""
        self.assertEqual(self.solution.maximumSubarraySum([], 3), 0)

    def test_single_element_list_valid_k(self):
        """Tests a single-element list where k=1."""
        self.assertEqual(self.solution.maximumSubarraySum([5], 1), 5)

    def test_single_element_list_invalid_k(self):
        """Tests a single-element list where k > length."""
        self.assertEqual(self.solution.maximumSubarraySum([5], 2), 0)

    def test_all_distinct_elements(self):
        """Tests a list where all elements are distinct."""
        self.assertEqual(self.solution.maximumSubarraySum([1, 2, 3, 4, 5], 3), 12)

    def test_no_valid_subarray(self):
        """Tests a list where no subarray of length k has all distinct elements."""
        self.assertEqual(self.solution.maximumSubarraySum([1, 1, 1, 1], 2), 0)


if __name__ == "__main__":
    unittest.main()
