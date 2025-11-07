"""
Problem: Find all unique combinations that sum to target, allowing reuse of numbers

Approach:
- Use backtracking to explore combinations
- Allow reusing same number by passing current index to recursive call
- Prune branches where sum exceeds target
- Time complexity: O(2^t) where t is target value
- Space complexity: O(t) for recursion stack
"""


class Solution:
    def combinationSum(self, candidates, target):
        return self.solution(candidates, [], [], target, 0, 0)

    def solution(self, candidates, ans, curr, target, index, current_sum):
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


import unittest


class TestSolution(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
