"""
Problem: Minimum Size Subarray Sum

Approach:
- Use sliding window (flexible - shortest) pattern
- Expand window by adding elements until sum >= target
- Shrink window from left while condition is met to find minimum length
- Track minimum length seen across all valid windows
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Solution for finding minimum size subarray with sum >= target."""

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Finds minimum length of subarray with sum >= target."""
        min_sub = len(nums) + 1  # Use impossible length as sentinel
        left = 0
        current_sum = 0

        for right, num in enumerate(nums):
            # Expand window: add current element to sum
            current_sum += num

            # Shrink window: while sum is valid (>= target)
            while current_sum >= target:
                # Update minimum length
                min_sub = min(min_sub, right - left + 1)

                # Remove leftmost element and move left pointer
                current_sum -= nums[left]
                left += 1

        # Return 0 if no valid subarray found, otherwise return minimum length
        return min_sub if min_sub <= len(nums) else 0


class TestMinSubArrayLen(unittest.TestCase):
    """Test cases for minimum size subarray sum problem."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example with target 7."""
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 2)

    def test_single_element_sufficient(self):
        """Single element meets or exceeds target."""
        target = 4
        nums = [1, 4, 4]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

    def test_no_solution(self):
        """No subarray sum meets target."""
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 0)

    def test_entire_array_needed(self):
        """Entire array needed to meet target."""
        target = 15
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 5)

    def test_large_numbers(self):
        """Large numbers in array."""
        target = 11
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 3)

    def test_single_element_array(self):
        """Single element array that meets target."""
        target = 5
        nums = [5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

    def test_single_element_insufficient(self):
        """Single element array that doesn't meet target."""
        target = 10
        nums = [5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 0)

    def test_consecutive_elements(self):
        """Multiple consecutive elements needed."""
        target = 213
        nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 8)


if __name__ == "__main__":
    unittest.main()
