"""
Problem: Find the element that appears once while all others appear twice

Approach:
- Use XOR operation: a ^ a = 0, a ^ 0 = a
- XOR all numbers; duplicates cancel out leaving the single number
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num  # XOR cancels duplicates
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Test with a basic example: [2, 2, 1] -> 1."""
        self.assertEqual(self.solution.singleNumber([2, 2, 1]), 1)

    def test_single_number_at_beginning(self):
        """Test with single number at the beginning: [1, 2, 2] -> 1."""
        self.assertEqual(self.solution.singleNumber([1, 2, 2]), 1)

    def test_single_number_at_end(self):
        """Test with single number at the end: [2, 1, 2] -> 1."""
        self.assertEqual(self.solution.singleNumber([2, 1, 2]), 1)

    def test_longer_list(self):
        """Test with a longer list: [4, 1, 2, 1, 2] -> 4."""
        self.assertEqual(self.solution.singleNumber([4, 1, 2, 1, 2]), 4)

    def test_single_element_list(self):
        """Test with a list containing a single element: [5] -> 5."""
        self.assertEqual(self.solution.singleNumber([5]), 5)


if __name__ == "__main__":
    unittest.main()
