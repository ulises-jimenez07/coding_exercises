"""
Problem: Find minimum operations to reduce x to zero by removing elements from array ends

Approach:
- Instead of tracking what to remove, find the longest subarray with sum = total - x
- Use sliding window to find this maximum length subarray
- Answer is n - max_subarray_length
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Solution for minimum operations to reduce x to zero."""

    def minOperations(self, nums: List[int], x: int) -> int:
        # We want to find the longest subarray with sum = total - x
        # Then we remove everything else from the ends
        current = sum(nums)
        n = len(nums)
        min_op = n + 1  # Track minimum operations needed
        left = 0

        # Expand window with right pointer
        for right, num in enumerate(nums):
            current -= num

            # Shrink window if current sum is less than target
            while current < x and left <= right:
                current += nums[left]
                left += 1

            # Found a valid subarray, calculate operations needed
            if current == x:
                min_op = min(min_op, (n - 1 - right) + left)

        return min_op if min_op != n + 1 else -1


class TestMinOperations(unittest.TestCase):
    """Test cases for minimum operations to reduce x to zero solution."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example with operations from both ends."""
        self.assertEqual(self.solution.minOperations([1, 1, 4, 2, 3], 5), 2)

    def test_remove_all_elements(self):
        """Need to remove all elements."""
        self.assertEqual(self.solution.minOperations([5, 6, 7, 8, 9], 4), -1)

    def test_exact_match(self):
        """Sum equals x, remove all elements."""
        self.assertEqual(self.solution.minOperations([3, 2, 20, 1, 1, 3], 10), 5)

    def test_single_element_match(self):
        """Single element equals x."""
        self.assertEqual(self.solution.minOperations([5], 5), 1)

    def test_impossible(self):
        """Cannot reduce to zero."""
        self.assertEqual(self.solution.minOperations([1, 1, 1, 1], 10), -1)

    def test_remove_from_left_only(self):
        """Only remove from left side."""
        self.assertEqual(self.solution.minOperations([1, 1, 1, 1, 1], 3), 3)

    def test_large_array(self):
        """Larger array test."""
        self.assertEqual(self.solution.minOperations([8, 1, 1, 1, 1, 8], 10), 3)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
