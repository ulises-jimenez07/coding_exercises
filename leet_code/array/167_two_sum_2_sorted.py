"""
Problem: Find two numbers in a sorted array that add up to a target

Approach:
- Use two pointers from start and end of array
- Move pointers based on sum comparison with target
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            current_sum = numbers[start] + numbers[end]

            if current_sum < target:
                start += 1
            elif current_sum > target:
                end -= 1
            else:
                return [start + 1, end + 1]

        return []


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        """Tests basic example."""
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_no_solution(self):
        """Tests no solution case."""
        numbers = [1, 2, 3, 4]
        target = 10
        self.assertEqual(self.solution.twoSum(numbers, target), [])

    def test_large_numbers(self):
        """Tests larger numbers."""
        numbers = [10, 20, 30, 40, 50]
        target = 70
        self.assertEqual(self.solution.twoSum(numbers, target), [2, 5])

    def test_negative_numbers(self):
        """Tests negative numbers."""
        numbers = [-5, -2, 0, 1, 3, 6]
        target = -2
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 5])

    def test_duplicate_numbers(self):
        """Tests duplicate numbers."""
        numbers = [1, 2, 3, 3, 4, 5]
        target = 6
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 6])

    def test_target_at_ends(self):
        """Tests target from first and last elements."""
        numbers = [1, 5, 8, 10]
        target = 11
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 4])

    def test_minimum_length_array(self):
        """Tests two element array."""
        numbers = [1, 2]
        target = 3
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_empty_array(self):
        """Tests empty array."""
        numbers = []
        target = 5
        self.assertEqual(self.solution.twoSum(numbers, target), [])

    def test_single_element_array(self):
        """Tests single element array."""
        numbers = [5]
        target = 5
        self.assertEqual(self.solution.twoSum(numbers, target), [])


if __name__ == "__main__":
    unittest.main()
