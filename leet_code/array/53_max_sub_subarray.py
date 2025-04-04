from typing import List
import unittest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray within a given array (containing at least one number) which has the largest sum.

        Args:
            nums: A list of integers.

        Returns:
            The maximum sum of a contiguous subarray.
        """
        max_sum = nums[0]  # Initialize max_sum with the first element
        curr_sum = 0  # Initialize current sum to 0

        for num in nums:  # Iterate through the numbers in the array
            curr_sum = (
                max(0, curr_sum) + num
            )  # If curr_sum is negative, reset it to 0, otherwise add the current number
            max_sum = max(max_sum, curr_sum)  # Update max_sum if curr_sum is greater

        return max_sum  # Return the maximum sum found


class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        self.assertEqual(self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_all_negative(self):
        self.assertEqual(self.solution.maxSubArray([-2, -1, -3, -4, -1]), -1)

    def test_all_positive(self):
        self.assertEqual(self.solution.maxSubArray([1, 2, 3, 4, 5]), 15)

    def test_single_element(self):
        self.assertEqual(self.solution.maxSubArray([1]), 1)

    def test_single_negative_element(self):
        self.assertEqual(self.solution.maxSubArray([-1]), -1)

    def test_empty_list(self):
        # Edge case: empty list
        with self.assertRaises(IndexError):
            self.solution.maxSubArray([])

    def test_mixed_numbers(self):
        self.assertEqual(self.solution.maxSubArray([-1, 2, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_start_with_negative(self):
        self.assertEqual(self.solution.maxSubArray([-2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
