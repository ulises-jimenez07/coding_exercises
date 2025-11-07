"""
Problem: Generate all possible subsets (power set) of an array

Approach:
- Use backtracking to build subsets incrementally
- Add current subset at each recursion level
- For each element, choose to include or exclude it
- Time complexity: O(2^n) as there are 2^n subsets
- Space complexity: O(n) for recursion stack
"""


def subsets(nums):
    def _subsets(nums, ans, curr, index):
        if index > len(nums):
            return

        # Add current subset
        ans.append(curr[:])

        # Try adding each remaining element
        for i in range(index, len(nums)):
            curr.append(nums[i])
            _subsets(nums, ans, curr, i + 1)
            curr.pop()  # Backtrack
        return

    ans = []
    curr = []
    _subsets(nums, ans, curr, 0)
    return ans


import unittest


class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_example_one(self):
        nums = [1, 2, 3]
        expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        actual = subsets(nums)
        self.assertCountEqual(actual, expected)

    def test_empty_list(self):
        nums = []
        expected = [[]]
        actual = subsets(nums)
        self.assertCountEqual(actual, expected)

    def test_single_element(self):
        nums = [1]
        expected = [[], [1]]
        actual = subsets(nums)
        self.assertCountEqual(actual, expected)

    def test_two_elements(self):
        nums = [1, 2]
        expected = [[], [1], [1, 2], [2]]
        actual = subsets(nums)
        self.assertCountEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
