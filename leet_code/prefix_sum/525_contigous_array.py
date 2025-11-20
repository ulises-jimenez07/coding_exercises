"""
Problem: Find the maximum length of a contiguous subarray with equal number of 0s and 1s

Approach:
- Convert 0s to -1s conceptually (by incrementing/decrementing a counter)
- Use prefix sum (running count) with hash map to track when the same count was seen
- If we see the same count twice, the subarray between those positions has equal 0s and 1s
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest
from typing import List


class Solution:
    """Solution class for contiguous array problem."""

    def findMaxLength(self, nums: List[int]) -> int:
        """
        Find the maximum length of contiguous subarray with equal 0s and 1s.
        Strategy:
        - Treat 0 as -1 and 1 as +1
        - Track running count (balance)
        - Store first occurrence of each count in hash map
        - If same count appears again, we found equal 0s and 1s between positions
        """
        hm = {}
        # Initialize with count 0 at index -1 (handles case when entire prefix is balanced)
        hm[0] = -1

        ans = 0
        count = 0  # Running balance: +1 for each 1, -1 for each 0

        for i, num in enumerate(nums):
            # Increment count for 1, decrement for 0
            if num == 1:
                count += 1
            else:
                count -= 1

            # If we've seen this count before, calculate length
            if count in hm:
                # Subarray from (hm[count] + 1) to i has equal 0s and 1s
                ans = max(ans, i - hm[count])
            else:
                # Store first occurrence of this count
                hm[count] = i

        return ans


class TestFindMaxLength(unittest.TestCase):
    """Test cases for contiguous array solution."""

    def test_simple_balanced_case(self):
        """Test simple two-element balanced array."""
        sol = Solution()
        nums = [0, 1]
        self.assertEqual(sol.findMaxLength(nums), 2)  # 0 and 1 are balanced

    def test_basic_three_elements(self):
        """Test basic case with 3 elements."""
        sol = Solution()
        nums = [0, 1, 0]
        self.assertEqual(sol.findMaxLength(nums), 2)  # [0, 1] or [1, 0]

    def test_complex_case(self):
        """Test complex case with multiple subarrays."""
        sol = Solution()
        nums = [0, 0, 1, 0, 0, 0, 1, 1]
        self.assertEqual(sol.findMaxLength(nums), 6)  # [0, 1, 0, 0, 0, 1] from index 1-6

    def test_multiple_balanced_subarrays(self):
        """Test array with multiple balanced subarrays."""
        sol = Solution()
        nums = [0, 1, 1, 0, 1, 1, 1, 0]
        self.assertEqual(sol.findMaxLength(nums), 4)  # [0, 1, 1, 0] from index 0-3

    def test_single_zero(self):
        """Test array with single zero - no balanced subarray."""
        sol = Solution()
        nums = [0]
        self.assertEqual(sol.findMaxLength(nums), 0)

    def test_single_one(self):
        """Test array with single one - no balanced subarray."""
        sol = Solution()
        nums = [1]
        self.assertEqual(sol.findMaxLength(nums), 0)

    def test_all_zeros(self):
        """Test array with all zeros - no balanced subarray."""
        sol = Solution()
        nums = [0, 0, 0]
        self.assertEqual(sol.findMaxLength(nums), 0)

    def test_all_ones(self):
        """Test array with all ones - no balanced subarray."""
        sol = Solution()
        nums = [1, 1, 1]
        self.assertEqual(sol.findMaxLength(nums), 0)

    def test_entire_array_balanced(self):
        """Test when entire array is balanced."""
        sol = Solution()
        nums = [1, 0, 1, 0]
        self.assertEqual(sol.findMaxLength(nums), 4)  # All 4 elements: 2 ones and 2 zeros

    def test_entire_array_balanced_complex(self):
        """Test when entire complex array is balanced."""
        sol = Solution()
        nums = [0, 0, 1, 1, 0, 1]
        self.assertEqual(sol.findMaxLength(nums), 6)  # All 6 elements: 3 ones and 3 zeros


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
