"""
Problem: Check if array contains any duplicate values

Approach:
- Use set to track seen numbers
- Return true if number already seen
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertFalse(self.solution.containsDuplicate([]))

    def test_single_element_list(self):
        self.assertFalse(self.solution.containsDuplicate([5]))

    def test_duplicates_present(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))

    def test_no_duplicates(self):
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]))

    def test_all_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate([2, 2, 2, 2]))

    def test_negative_numbers(self):
        self.assertTrue(self.solution.containsDuplicate([-1, 2, -1, 3]))

    def test_mixed_positive_and_negative(self):
        self.assertFalse(self.solution.containsDuplicate([-1, 2, 3, 4]))
        self.assertTrue(self.solution.containsDuplicate([-1, 2, -1, 4]))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
