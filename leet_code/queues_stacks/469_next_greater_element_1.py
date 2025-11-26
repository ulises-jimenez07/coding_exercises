"""
Problem: Next Greater Element I - find next greater element for each number in subset

Approach:
- Use a monotonic decreasing stack to track elements without next greater element
- Build a hashmap of element -> next greater element for nums2
- For each element in nums2, pop smaller elements and map them to current element
- Time complexity: O(n + m) where n is len(nums2) and m is len(nums1)
- Space complexity: O(n) for the stack and hashmap
"""

import unittest
from typing import List


class Solution:
    """Solution for LeetCode 496: Next Greater Element I."""

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the next greater element for each element in nums1 within nums2.

        For each element x in nums1, find the next greater element in nums2.
        The next greater element is the first element to the right that is greater.
        """
        stack: list[int] = []  # Monotonic decreasing stack
        hashmap: dict[int, int] = {}  # Maps element -> next greater element

        # Process nums2 to build next greater element mapping
        for num in nums2:
            # Current num is greater than stack top - it's the next greater element
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num
            stack.append(num)

        # Build result array using the hashmap
        return [hashmap.get(i, -1) for i in nums1]


class TestNextGreaterElement(unittest.TestCase):
    """Test cases for Next Greater Element I solution."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Test with basic example where some elements have next greater."""
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        expected = [-1, 3, -1]
        self.assertEqual(self.solution.nextGreaterElement(nums1, nums2), expected)

    def test_all_elements_have_next_greater(self):
        """Test where all elements in nums1 have next greater element."""
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        expected = [3, -1]
        self.assertEqual(self.solution.nextGreaterElement(nums1, nums2), expected)

    def test_no_next_greater_elements(self):
        """Test where no elements have next greater element."""
        nums1 = [3, 2, 1]
        nums2 = [3, 2, 1]
        expected = [-1, -1, -1]
        self.assertEqual(self.solution.nextGreaterElement(nums1, nums2), expected)

    def test_single_element(self):
        """Test with single element in both arrays."""
        nums1 = [1]
        nums2 = [1]
        expected = [-1]
        self.assertEqual(self.solution.nextGreaterElement(nums1, nums2), expected)

    def test_increasing_sequence(self):
        """Test with strictly increasing sequence."""
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3, 4, 5]
        expected = [2, 3, 4]
        self.assertEqual(self.solution.nextGreaterElement(nums1, nums2), expected)

    def test_decreasing_sequence(self):
        """Test with strictly decreasing sequence."""
        nums1 = [5, 4, 3, 2, 1]
        nums2 = [5, 4, 3, 2, 1]
        expected = [-1, -1, -1, -1, -1]
        self.assertEqual(self.solution.nextGreaterElement(nums1, nums2), expected)

    def test_mixed_order(self):
        """Test with mixed order where nums1 elements appear in different order than nums2."""
        nums1 = [1, 3, 5, 2, 4]
        nums2 = [1, 2, 3, 4, 5, 6]
        expected = [2, 4, 6, 3, 5]
        self.assertEqual(self.solution.nextGreaterElement(nums1, nums2), expected)

    def test_nums1_single_element_from_larger_nums2(self):
        """Test with single element in nums1 from middle of nums2."""
        nums1 = [3]
        nums2 = [1, 2, 3, 4, 5]
        expected = [4]
        self.assertEqual(self.solution.nextGreaterElement(nums1, nums2), expected)

    def test_last_element_no_next_greater(self):
        """Test where element is last in nums2 so has no next greater."""
        nums1 = [5]
        nums2 = [1, 2, 3, 4, 5]
        expected = [-1]
        self.assertEqual(self.solution.nextGreaterElement(nums1, nums2), expected)


if __name__ == "__main__":
    unittest.main()
