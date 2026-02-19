"""
Problem: Find all unique combinations that sum to target, allowing reuse of numbers

Approach:
- Version 1: Backtracking using a current_sum accumulator.
- Version 2: Simplified backtracking using target reduction (provided by user).
- Time complexity: O(N^(T/M)) where N is candidates length, T is target, M is minimum candidate.
- Space complexity: O(T/M) for recursion stack.
"""

import unittest
from typing import List


class Solution:
    """
    Backtracking solution for the combination sum problem.
    """

    def combinationSum(self, candidates, target):
        return self.solution(candidates, [], [], target, 0, 0)

    def solution(
        self, candidates, ans, curr, target, index, current_sum
    ):  # pylint: disable=too-many-arguments,too-many-positional-arguments
        # Found valid combination
        if current_sum == target:
            ans.append(curr[:])
        elif current_sum < target:
            n = len(candidates)
            # Try each candidate from current index
            for i in range(index, n):
                curr.append(candidates[i])
                # Can reuse same element (index i)
                self.solution(candidates, ans, curr, target, i, current_sum + candidates[i])
                curr.pop()  # Backtrack
        return ans


# Version 2: Simplified backtracking using target reduction
def combinations_of_sum_k(nums: List[int], target: int) -> List[List[int]]:
    """
    Finds all unique combinations that sum to target using recursion.
    """
    res: List[List[int]] = []
    dfs([], 0, nums, target, res)
    return res


def dfs(combination, start_index, nums, target, res):
    """
    Helper function for recursion.
    """
    if target == 0:
        res.append(combination[:])
        return
    if target < 0:
        return

    for i in range(start_index, len(nums)):
        combination.append(nums[i])
        dfs(combination, i, nums, target - nums[i], res)
        combination.pop()


class TestSolution(unittest.TestCase):
    """
    Unit tests for combination sum implementations.
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
        """
        Test with candidates [2, 3, 5] and target 8.
        Expected combinations: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        """
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        actual = self.solution.combinationSum(candidates, target)
        self.assertCountEqual(actual, expected)

    def test_empty_candidates(self):
        """Test with an empty candidates list."""
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

    def test_v2_combinations(self):
        """Test Version 2: combinations_of_sum_k."""
        # Test Case 1
        nums1 = [2, 3, 6, 7]
        target1 = 7
        expected1 = [[2, 2, 3], [7]]
        self.assertCountEqual(combinations_of_sum_k(nums1, target1), expected1)

        # Test Case 2
        nums2 = [2, 3, 5]
        target2 = 8
        expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertCountEqual(combinations_of_sum_k(nums2, target2), expected2)


if __name__ == "__main__":
    unittest.main()
