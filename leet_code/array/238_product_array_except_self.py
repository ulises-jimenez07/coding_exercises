from typing import List
import unittest


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates the product of all elements in the array except for the element at the current index.

        Args:
            nums: A list of integers.

        Returns:
            A list of integers where each element is the product of all elements in nums except itself.
        """
        n = len(nums)
        left = [1] * n  # Initialize the left array with 1s
        right = [1] * n  # Initialize the right array with 1s

        # Calculate the product of all elements to the left of each element
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        # Calculate the product of all elements to the right of each element
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        output = []  # Initialize the output array

        # Calculate the product of all elements except self by multiplying left and right products
        for i in range(0, n):
            output.append(left[i] * right[i])

        return output  # Return the output array


class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)

    def test_zeros(self):
        nums = [1, 0, 3, 4]
        expected = [0, 12, 0, 0]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)

    def test_negative_numbers(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)

    def test_single_element(self):
        nums = [5]
        expected = [1]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)


if __name__ == "__main__":
    unittest.main()
