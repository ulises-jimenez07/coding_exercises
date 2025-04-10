from typing import List
import unittest


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Finds the maximum product of a contiguous subarray in a given list of integers.

        Args:
            nums: A list of integers.

        Returns:
            The maximum product of a contiguous subarray.
        """
        # Initialize the result with the first element of the array.
        # This handles the case where the array has only one element.
        result = nums[0]

        # Initialize max_product and min_product to keep track of the maximum and minimum
        # product ending at the current position. We need to track both because a negative
        # number multiplied by another negative number can become positive and potentially
        # the new maximum.
        max_product = nums[0]
        min_product = nums[0]

        # Iterate through the array starting from the second element.
        for num in nums[1:]:
            # If the current number is non-negative:
            # - The new maximum product ending at the current position is the maximum of
            #   the current number itself or the previous maximum product multiplied by the
            #   current number.
            # - The new minimum product ending at the current position is the minimum of
            #   the current number itself or the previous minimum product multiplied by the
            #   current number.
            if num >= 0:
                max_product = max(max_product * num, num)
                min_product = min(min_product * num, num)
            # If the current number is negative:
            # - Multiplying a negative number with the previous maximum product can result
            #   in a new minimum product.
            # - Multiplying a negative number with the previous minimum product can result
            #   in a new maximum product.
            else:
                # Temporarily store the previous maximum product.
                temp = max_product
                # The new maximum product is the maximum of the current number itself or the
                # previous minimum product multiplied by the current number.
                max_product = max(min_product * num, num)
                # The new minimum product is the minimum of the current number itself or the
                # previous maximum product (stored in temp) multiplied by the current number.
                min_product = min(temp * num, num)

            # Update the overall result if the current maximum product is greater.
            result = max(result, max_product)

        return result


class TestMaxProduct(unittest.TestCase):
    def test_empty_array(self):
        solution = Solution()
        self.assertEqual(
            solution.maxProduct([]), 0
        )  # Or raise an error, depending on desired behavior

    def test_single_element_array(self):
        solution = Solution()
        self.assertEqual(solution.maxProduct([5]), 5)
        self.assertEqual(solution.maxProduct([-3]), -3)

    def test_positive_numbers(self):
        solution = Solution()
        self.assertEqual(solution.maxProduct([2, 3, -2, 4]), 6)
        self.assertEqual(solution.maxProduct([1, 2, 3, 4]), 24)

    def test_negative_numbers(self):
        solution = Solution()
        self.assertEqual(solution.maxProduct([-2, 0, -1]), 0)
        self.assertEqual(solution.maxProduct([-2, -3, -4]), 24)
        self.assertEqual(solution.maxProduct([-1, -2, -3, 0]), 6)

    def test_mixed_numbers(self):
        solution = Solution()
        self.assertEqual(solution.maxProduct([-2, 3, -4]), 24)
        self.assertEqual(solution.maxProduct([0, 2]), 2)
        self.assertEqual(solution.maxProduct([-4, -3, -2]), 24)
        self.assertEqual(solution.maxProduct([2, -5, -2, -4, 3]), 20)

    def test_array_with_zeros(self):
        solution = Solution()
        self.assertEqual(solution.maxProduct([0, 0, 0]), 0)
        self.assertEqual(solution.maxProduct([1, -2, 0, 3]), 3)
        self.assertEqual(solution.maxProduct([-1, -2, -3, 0, -4, -5]), 6)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
