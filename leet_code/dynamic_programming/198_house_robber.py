from typing import List
import unittest


# Solves the "House Robber" problem using dynamic programming with memoization.
class Solution:
    # Main method to start the robbery calculation.
    def rob(self, nums: List[int]) -> int:
        self.dp = {}  # Cache for memoization.
        self.nums = nums
        if len(nums) > 0:
            return self.max_rob(0, True)
        return 0

    # Recursive helper to find the maximum amount that can be robbed from index `i`.
    # `i`: Current house index.
    # `can_rob`: True if the current house can be robbed.
    def max_rob(self, i, can_rob):
        # Base case: last house.
        if i == len(self.nums) - 1:
            return self.nums[i] if can_rob else 0

        # Return cached result if available.
        if (i, can_rob) not in self.dp:
            if can_rob:
                # Max of robbing this house or skipping it.
                self.dp[(i, can_rob)] = max(
                    self.nums[i] + self.max_rob(i + 1, False), self.max_rob(i + 1, True)
                )
            else:
                # Must skip this house.
                self.dp[(i, can_rob)] = self.max_rob(i + 1, True)
        return self.dp[(i, can_rob)]


# Unit tests for the Solution class.
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # Test with a common example.
    def test_example_1(self):
        nums = [1, 2, 3, 1]
        expected_output = 4
        self.assertEqual(self.solution.rob(nums), expected_output)

    # Test with another example.
    def test_example_2(self):
        nums = [2, 7, 9, 3, 1]
        expected_output = 12
        self.assertEqual(self.solution.rob(nums), expected_output)

    # Test with a single house.
    def test_single_house(self):
        nums = [10]
        expected_output = 10
        self.assertEqual(self.solution.rob(nums), expected_output)

    # Test with an empty list.
    def test_empty_list(self):
        nums = []
        expected_output = 0
        self.assertEqual(self.solution.rob(nums), expected_output)

    # Test with two houses.
    def test_two_houses(self):
        nums = [5, 6]
        expected_output = 6
        self.assertEqual(self.solution.rob(nums), expected_output)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
