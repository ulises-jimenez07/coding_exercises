"""
Problem: Next Greater Element II - find next greater element in circular array

Approach:
- Use a stack to track indices waiting for greater elements
- Iterate twice to handle circular nature
- Time complexity: O(n) where n is array length
- Space complexity: O(n) for the stack
"""

import unittest
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Finds the next greater element for each element in the input list,
        considering the list as circular.
        """
        stack: list[int] = []
        n = len(nums)
        ans = [-1] * n

        # Iterate through the array twice to handle circularity
        for i in range(2 * n):
            current_num = nums[i % n]
            while stack and nums[stack[-1]] < current_num:
                ans[stack.pop()] = current_num
            if i < n:  # Only push indices for the first pass
                stack.append(i)

        return ans


class TestNextGreaterElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(self.solution.nextGreaterElements([]), [])

    def test_single_element_list(self):
        """Test with a single element list."""
        self.assertEqual(self.solution.nextGreaterElements([1]), [-1])

    def test_example_1(self):
        """Test with example [1, 2, 1]."""
        self.assertEqual(self.solution.nextGreaterElements([1, 2, 1]), [2, -1, 2])

    def test_example_2(self):
        """Test with example [1, 2, 3, 4, 3]."""
        self.assertEqual(self.solution.nextGreaterElements([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4])

    def test_decreasing_list(self):
        """Test with a decreasing list."""
        self.assertEqual(self.solution.nextGreaterElements([4, 3, 2, 1]), [-1, 4, 4, 4])

    def test_increasing_list(self):
        """Test with an increasing list."""
        self.assertEqual(self.solution.nextGreaterElements([1, 2, 3, 4]), [2, 3, 4, -1])

    def test_circular_example_1(self):
        """Test with circular example [5,4,3,2,1]."""
        self.assertEqual(self.solution.nextGreaterElements([5, 4, 3, 2, 1]), [-1, 5, 5, 5, 5])

    def test_circular_example_2(self):
        """Test with circular example [1,5,3,6,8]."""
        self.assertEqual(self.solution.nextGreaterElements([1, 5, 3, 6, 8]), [5, 6, 6, 8, -1])


if __name__ == "__main__":
    unittest.main()
