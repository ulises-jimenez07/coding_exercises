"""
Problem: Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

Approach:
- Use a hash table to store the value of each element and its corresponding index.
- For each element, calculate the complement (target - current value).
- If the complement exists in the hash table, return the indices.
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest
from typing import List


class Solution:
    """Solution for the Two Sum problem."""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Find indices of two numbers that sum to the target."""
        # Mapping of value to its index
        num_to_index: dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement was already seen
            if complement in num_to_index:
                return [num_to_index[complement], i]

            # Store current number's index for future lookups
            num_to_index[num] = i

        return []


class TestTwoSum(unittest.TestCase):
    """Unit tests for the twoSum solution."""

    def setUp(self):
        """Set up the Solution instance."""
        self.solution = Solution()

    def test_example_1(self):
        """Test example 1 from LeetCode."""
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_example_2(self):
        """Test example 2 from LeetCode."""
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

    def test_example_3(self):
        """Test example 3 from LeetCode."""
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_no_solution(self):
        """Test case where no solution exists."""
        nums = [1, 2, 3]
        target = 7
        self.assertEqual(self.solution.twoSum(nums, target), [])

    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        self.assertEqual(self.solution.twoSum(nums, target), [2, 4])

    def test_large_target(self):
        """Test with a large target value."""
        nums = [10, 20, 30]
        target = 50
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])


if __name__ == "__main__":
    unittest.main()
