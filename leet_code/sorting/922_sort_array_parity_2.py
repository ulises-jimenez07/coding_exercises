"""
Problem: Sort an array such that nums[i] has the same parity as i.
The array contains an equal number of even and odd integers.

Approach:
- Iterate through even indices using range(0, len(nums), 2).
- When an odd number is found at an even index, find the next even number at an odd index.
- Swap the elements to correct their positions.
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Namespace for the solution to LeetCode 922: Sort Array By Parity II."""

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """Moves even integers to even indices and odd integers to odd indices."""
        swap = 1

        # Iterate through the even indices
        for i in range(0, len(nums), 2):
            # If current even index holds an odd number, swap it
            if nums[i] % 2:
                # Find the next even number at an odd position
                while nums[swap] % 2:
                    swap += 2
                nums[swap], nums[i] = nums[i], nums[swap]

        return nums


class TestSortParityII(unittest.TestCase):
    """Unit tests for the Sort Array By Parity II solution."""

    def setUp(self):
        self.solution = Solution()

    def _validate_parity(self, result: List[int]):
        """Helper to verify that every element matches its index parity."""
        for i, num in enumerate(result):
            self.assertEqual(i % 2, num % 2, f"Mismatch at index {i}: {num}")

    def test_example_1(self):
        """LeetCode example 1: [4, 2, 5, 7]."""
        nums = [4, 2, 5, 7]
        result = self.solution.sortArrayByParityII(nums.copy())
        self._validate_parity(result)

    def test_example_2(self):
        """LeetCode example 2: [2, 3]."""
        nums = [2, 3]
        result = self.solution.sortArrayByParityII(nums.copy())
        self._validate_parity(result)

    def test_already_sorted(self):
        """Array already satisfying the parity condition."""
        nums = [2, 1, 4, 3, 6, 5]
        result = self.solution.sortArrayByParityII(nums.copy())
        self.assertEqual(result, [2, 1, 4, 3, 6, 5])

    def test_reverse_sorted(self):
        """Array where every element starts at the wrong parity."""
        nums = [1, 2, 3, 4]
        result = self.solution.sortArrayByParityII(nums.copy())
        self._validate_parity(result)

    def test_empty_list(self):
        """Edge case: empty input list."""
        nums = []
        result = self.solution.sortArrayByParityII(nums)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
