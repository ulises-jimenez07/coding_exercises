"""
Problem: Find the single number in an array where every element appears twice except one

Approach:
- Use XOR bitwise operation: a ^ a = 0, a ^ 0 = a
- XORing all numbers cancels out duplicates, leaving the single number
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num  # XOR cancels duplicate pairs
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Test with a basic example."""
        nums = [2, 2, 1]
        expected = 1
        self.assertEqual(self.solution.singleNumber(nums), expected)

    def test_single_number_at_beginning(self):
        """Test when the single number is at the beginning."""
        nums = [1, 2, 2]
        expected = 1
        self.assertEqual(self.solution.singleNumber(nums), expected)

    def test_single_number_at_end(self):
        """Test when the single number is at the end."""
        nums = [2, 1, 2]
        expected = 1
        self.assertEqual(self.solution.singleNumber(nums), expected)

    def test_longer_list(self):
        """Test with a longer list."""
        nums = [4, 1, 2, 1, 2]
        expected = 4
        self.assertEqual(self.solution.singleNumber(nums), expected)

    def test_single_element_list(self):
        """Test with a list containing only one element."""
        nums = [5]
        expected = 5
        self.assertEqual(self.solution.singleNumber(nums), expected)


if __name__ == "__main__":
    unittest.main()
