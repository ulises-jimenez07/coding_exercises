from typing import List
import unittest


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Finds the maximum number of consecutive 1s in a binary array.

        Args:
            nums: A list of integers (0s and 1s).

        Returns:
            The maximum number of consecutive 1s in the array.
        """
        count = max_count = 0  # Initialize current count and max count to 0

        # Iterate through the array
        for num in nums:
            if num == 1:  # If the current number is 1
                count += 1  # Increment the current count
            else:  # If the current number is 0
                max_count = max(
                    count, max_count
                )  # Update max_count if current count is greater
                count = 0  # Reset the current count
        return max(
            max_count, count
        )  # Return the maximum of max_count and count (in case the array ends with 1s)


class TestFindMaxConsecutiveOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)

    def test_all_zeros(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0, 0, 0, 0]), 0)

    def test_all_ones(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1, 1, 1]), 4)

    def test_empty_list(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([]), 0)

    def test_single_one(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1]), 1)


if __name__ == "__main__":
    unittest.main()
