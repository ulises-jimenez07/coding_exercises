"""
Problem: Next Largest Number to the Right - find the first larger element to the right

Approach:
- Use a monotonic stack to maintain candidates for the next greater element
- Iterate backwards through the array
- Time complexity: O(n) where n is the length of the list
- Space complexity: O(n) for the stack and result list
"""

import unittest
from typing import List


class Solution:
    """
    Class to solve the Next Largest Number to the Right problem.
    """

    def next_largest_number_to_the_right(self, nums: List[int]) -> List[int]:
        """
        Returns a list where each element is replaced by the first larger
        element to its right. If no such element exists, -1 is used.
        """
        res = [0] * len(nums)
        stack: List[int] = []

        # Process elements from right to left
        for i, num in reversed(list(enumerate(nums))):
            # Remove elements from stack that are not greater than current
            while stack and stack[-1] <= num:
                stack.pop()

            # The top of the stack is the next greater element
            res[i] = stack[-1] if stack else -1
            stack.append(num)

        return res


class TestNextLargestNumber(unittest.TestCase):
    """
    Unit tests for the Next Largest Number to the Right solution.
    """

    def setUp(self):
        """Initialize the solution instance before each test."""
        self.solution = Solution()

    def test_leetcode_example(self):
        """Test with a standard sequence including varying values."""
        nums = [1, 3, 2, 4]
        expected = [3, 4, 4, -1]
        self.assertEqual(self.solution.next_largest_number_to_the_right(nums), expected)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(self.solution.next_largest_number_to_the_right([]), [])

    def test_single_element(self):
        """Test with a single element list."""
        self.assertEqual(self.solution.next_largest_number_to_the_right([5]), [-1])

    def test_all_decreasing(self):
        """Test with elements in strictly decreasing order."""
        self.assertEqual(self.solution.next_largest_number_to_the_right([4, 3, 2, 1]), [-1, -1, -1, -1])

    def test_all_increasing(self):
        """Test with elements in strictly increasing order."""
        self.assertEqual(self.solution.next_largest_number_to_the_right([1, 2, 3, 4]), [2, 3, 4, -1])

    def test_duplicate_elements(self):
        """Test with multiple identical elements."""
        nums = [2, 2, 2, 2]
        expected = [-1, -1, -1, -1]
        self.assertEqual(self.solution.next_largest_number_to_the_right(nums), expected)


if __name__ == "__main__":
    unittest.main()
