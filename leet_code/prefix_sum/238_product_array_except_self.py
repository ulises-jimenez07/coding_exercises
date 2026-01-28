"""
Problem: Return array where each element is the product of all elements except itself

Approaches:
1. Prefix and Suffix Arrays:
   - Build left and right product arrays for products before and after each index
   - Multiply corresponding left and right products for final result
   - Time complexity: O(n)
   - Space complexity: O(n)

2. Space-Optimized (O(1) extra space):
   - Use the result array to store prefix products first
   - Iterate backwards to multiply by suffix products using a single variable
   - Time complexity: O(n)
   - Space complexity: O(1) (excluding the output array)
"""

import unittest
from typing import List


class Solution:
    """
    Solutions for the 'Product of Array Except Self' problem using different approaches.
    """

    def product_except_self_with_prefix_and_suffix_arrays(self, nums: List[int]) -> List[int]:
        """
        Original O(n) space version using separate prefix and suffix arrays.
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        output = []
        for i in range(0, n):
            output.append(left[i] * right[i])

        return output

    def product_except_self_space_optimized(self, nums: List[int]) -> List[int]:
        """
        Space-optimized version using a single result array and a running suffix product.
        Time: O(n), Space: O(1) (excluding result array).
        """
        n = len(nums)
        res = [1] * n

        # Pass 1: Build prefix products directly in the result array
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # Pass 2: Multiply by suffix products using a running variable
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res


class TestProductExceptSelf(unittest.TestCase):
    """
    Unit tests for both implementations of productExceptSelf.
    """

    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Tests basic case."""
        case = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(self.solution.product_except_self_with_prefix_and_suffix_arrays(case), expected)
        self.assertEqual(self.solution.product_except_self_space_optimized(case), expected)

    def test_zeros(self):
        """Tests with zero."""
        case = [1, 0, 3, 4]
        expected = [0, 12, 0, 0]
        self.assertEqual(self.solution.product_except_self_with_prefix_and_suffix_arrays(case), expected)
        self.assertEqual(self.solution.product_except_self_space_optimized(case), expected)

    def test_all_zeros(self):
        """Tests all zeros."""
        case = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        self.assertEqual(self.solution.product_except_self_with_prefix_and_suffix_arrays(case), expected)
        self.assertEqual(self.solution.product_except_self_space_optimized(case), expected)

    def test_negative_numbers(self):
        """Tests negative numbers."""
        case = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(self.solution.product_except_self_with_prefix_and_suffix_arrays(case), expected)
        self.assertEqual(self.solution.product_except_self_space_optimized(case), expected)

    def test_single_element(self):
        """Tests single element."""
        case = [5]
        expected = [1]
        self.assertEqual(self.solution.product_except_self_with_prefix_and_suffix_arrays(case), expected)
        self.assertEqual(self.solution.product_except_self_space_optimized(case), expected)


if __name__ == "__main__":
    unittest.main()
