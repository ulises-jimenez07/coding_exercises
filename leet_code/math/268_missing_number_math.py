"""
Problem: Find the missing number in an array containing n distinct numbers from 0 to n

Approach:
- Use Gauss formula: sum of 0 to n = n * (n + 1) / 2
- Subtract actual sum from expected sum to find missing number
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        target_sum = n * (n + 1) / 2  # Gauss formula for sum
        actual_sum = sum(nums)
        return int(target_sum - actual_sum)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Test with a basic example."""
        nums = [3, 0, 1]
        expected = 2
        self.assertEqual(self.solution.missingNumber(nums), expected)

    def test_missing_number_at_beginning(self):
        """
        Test when the missing number is at the beginning (0).
        """
        nums = [1, 2, 3]
        expected = 0
        self.assertEqual(self.solution.missingNumber(nums), expected)

    def test_missing_number_at_end(self):
        """
        Test when the missing number is at the end (n).
        """
        nums = [0, 1, 2]
        expected = 3
        self.assertEqual(self.solution.missingNumber(nums), expected)

    def test_single_element_list(self):
        """Test with a single element list."""
        nums = [0]
        expected = 1
        self.assertEqual(self.solution.missingNumber(nums), expected)

    def test_empty_list(self):
        """Test with an empty list (edge case)."""
        nums = []
        expected = 0
        self.assertEqual(self.solution.missingNumber(nums), expected)


if __name__ == "__main__":
    unittest.main()
