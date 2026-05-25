"""
Module to solve the Combination Sum problem using backtracking.

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen
numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
"""

import unittest
from typing import List


class Solution:
    """
    Backtracking solver for finding combination sums.
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates that sum to target.
        """
        ans = []
        n = len(candidates)

        def backtrack(curr, curr_sum, index):
            """
            Helper function to backtrack and find combinations.
            """
            # Base case: if current sum matches target, record combination
            if curr_sum == target:
                ans.append(curr[:])
            # If current sum is less than target, explore further candidates
            elif curr_sum < target:
                for i in range(index, n):
                    curr.append(candidates[i])
                    # Re-use candidate at index i
                    backtrack(curr, curr_sum + candidates[i], i)
                    curr.pop()  # Backtrack

        backtrack([], 0, 0)
        return ans


class TestSolution(unittest.TestCase):
    """
    Unit tests for combinationSum solution.
    """

    def setUp(self):
        self.solution = Solution()
        self.maxDiff = None

    def test_example_one(self):
        """Test with candidates [2, 3, 6, 7] and target 7."""
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        actual = self.solution.combinationSum(candidates, target)
        self.assertCountEqual(actual, expected)

    def test_example_two(self):
        """Test with candidates [2, 3, 5] and target 8."""
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        actual = self.solution.combinationSum(candidates, target)
        self.assertCountEqual(actual, expected)

    def test_empty_candidates(self):
        """Test with empty candidates list."""
        candidates = []
        target = 7
        expected = []
        actual = self.solution.combinationSum(candidates, target)
        self.assertEqual(actual, expected)

    def test_target_zero(self):
        """Test with target 0."""
        candidates = [2, 3, 5]
        target = 0
        expected = [[]]
        actual = self.solution.combinationSum(candidates, target)
        self.assertCountEqual(actual, expected)

    def test_single_element_match(self):
        """Test with a single element candidate matching target."""
        candidates = [2]
        target = 2
        expected = [[2]]
        actual = self.solution.combinationSum(candidates, target)
        self.assertCountEqual(actual, expected)

    def test_single_element_no_match(self):
        """Test with a single element candidate not matching target."""
        candidates = [3]
        target = 2
        expected = []
        actual = self.solution.combinationSum(candidates, target)
        self.assertCountEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
