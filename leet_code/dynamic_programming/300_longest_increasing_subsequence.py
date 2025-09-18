import unittest
from typing import List


class Solution:
    """
    Class to solve the Longest Increasing Subsequence problem.
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Calculates the length of the longest increasing subsequence.

        This method uses dynamic programming to find the length of the longest increasing
        subsequence in a given array of integers.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest increasing subsequence.
        """
        if not nums:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at index i.
        dp = [1] * len(nums)
        ans = 1

        # Iterate through the array starting from the second element.
        for i in range(1, len(nums)):
            # Initialize the length for the current element to 1 (the element itself).
            current_val = 1
            # Iterate through the elements before the current one.
            for j in range(i):
                # If the previous element is smaller, it can potentially extend the LIS.
                if nums[j] < nums[i]:
                    # Update the current length by considering the LIS ending at j.
                    current_val = max(current_val, dp[j] + 1)
            # Store the calculated length in the dp array.
            dp[i] = current_val
            # Update the overall maximum length found so far.
            ans = max(ans, dp[i])

        return ans


class TestLengthOfLIS(unittest.TestCase):
    """
    Unit tests for the Solution.lengthOfLIS method.
    """

    def setUp(self):
        """
        Set up a new instance of the Solution class before each test.
        """
        self.solution = Solution()

    def test_example_1(self):
        """
        Test case with a standard increasing subsequence.
        """
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_example_2(self):
        """
        Test case with all numbers in increasing order.
        """
        nums = [0, 1, 2, 3, 4, 5]
        expected = 6
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_example_3(self):
        """
        Test case with all numbers in decreasing order.
        """
        nums = [7, 6, 5, 4, 3, 2, 1]
        expected = 1
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_example_4(self):
        """
        Test case with an empty list.
        """
        nums = []
        expected = 0
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_example_5(self):
        """
        Test case with a single-element list.
        """
        nums = [5]
        expected = 1
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_example_6(self):
        """
        Test case with duplicate numbers.
        """
        nums = [1, 3, 2, 4, 5, 2, 3, 4]
        expected = 4
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
