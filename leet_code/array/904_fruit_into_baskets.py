"""
Problem: Find maximum fruits that can be picked with two baskets (max subarray with 2 types)

Approach:
- Use sliding window with hash map to track fruit types
- Expand window, contract when more than 2 types present
- Time complexity: O(n)
- Space complexity: O(1) - max 3 types in map
"""

import unittest
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """Finds maximum fruits that can be picked with two baskets using sliding window."""
        basket: dict[int, int] = {}
        left = 0
        max_fruits = 0

        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits


class TestTotalFruit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Example 1."""
        self.assertEqual(self.solution.totalFruit([1, 2, 1]), 3)

    def test_example_2(self):
        """Example 2."""
        self.assertEqual(self.solution.totalFruit([0, 1, 2, 2]), 3)

    def test_example_3(self):
        """Example 3."""
        self.assertEqual(self.solution.totalFruit([1, 2, 3, 2, 2]), 4)

    def test_example_4(self):
        """Mixed fruit types."""
        self.assertEqual(self.solution.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)

    def test_empty_list(self):
        """Empty list."""
        self.assertEqual(self.solution.totalFruit([]), 0)

    def test_one_fruit_type(self):
        """One fruit type."""
        self.assertEqual(self.solution.totalFruit([1, 1, 1, 1, 1]), 5)

    def test_two_fruit_types(self):
        """Two fruit types."""
        self.assertEqual(self.solution.totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]), 5)


if __name__ == "__main__":
    unittest.main()
