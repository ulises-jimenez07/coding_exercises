"""
Problem: Subarray Sums Divisible by K (LeetCode 974)

Given an integer array nums and an integer k, return the number of non-empty
subarrays that have a sum divisible by k.

Approach:
- Use prefix sum with modulo arithmetic and hash map
- Key insight: if (prefix[j] - prefix[i]) % k == 0, then prefix[j] % k == prefix[i] % k
- Track frequency of each remainder (prefix_sum % k)
- Handle negative remainders by converting to positive: (remainder % k + k) % k
- Time complexity: O(n)
- Space complexity: O(k) - at most k different remainders
"""

import unittest
from typing import List


class Solution:
    """Solution class for subarray sums divisible by k problem."""

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        Find number of subarrays with sum divisible by k.

        Strategy: Use prefix sum modulo k. If two prefix sums have same remainder,
        the subarray between them is divisible by k. Track remainder frequencies.
        """
        count = 0
        prefix_sum = 0
        remainder_freq = {0: 1}  # Initialize for subarrays starting at index 0

        for num in nums:
            prefix_sum += num

            # Normalize remainder to handle negative numbers
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k

            # Count valid subarrays ending at current position
            if remainder in remainder_freq:
                count += remainder_freq[remainder]

            remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1

        return count


class TestSubarraysDivByK(unittest.TestCase):
    """Test cases for subarray sums divisible by k solution."""

    def setUp(self):
        self.sol = Solution()

    def test_basic_case(self):
        """Test basic case with multiple valid subarrays."""
        nums = [4, 5, 0, -2, -3, 1]
        k = 5
        result = self.sol.subarraysDivByK(nums, k)
        self.assertEqual(result, 7)

    def test_single_element_divisible(self):
        """Test single element divisible by k."""
        nums = [5]
        k = 5
        result = self.sol.subarraysDivByK(nums, k)
        self.assertEqual(result, 1)

    def test_single_element_not_divisible(self):
        """Test single element not divisible by k."""
        nums = [3]
        k = 5
        result = self.sol.subarraysDivByK(nums, k)
        self.assertEqual(result, 0)

    def test_all_zeros(self):
        """Test array with all zeros."""
        nums = [0, 0, 0]
        k = 5
        result = self.sol.subarraysDivByK(nums, k)
        self.assertEqual(result, 6)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, 2, 9]
        k = 2
        result = self.sol.subarraysDivByK(nums, k)
        self.assertEqual(result, 2)

    def test_entire_array_divisible(self):
        """Test where entire array sum is divisible by k."""
        nums = [2, 3, 5]
        k = 10
        result = self.sol.subarraysDivByK(nums, k)
        self.assertEqual(result, 1)

    def test_no_valid_subarrays(self):
        """Test case with no valid subarrays."""
        nums = [1, 2]
        k = 5
        result = self.sol.subarraysDivByK(nums, k)
        self.assertEqual(result, 0)

    def test_multiple_subarrays_same_remainder(self):
        """Test with multiple subarrays having same remainder."""
        nums = [3, 3, 3]
        k = 3
        result = self.sol.subarraysDivByK(nums, k)
        self.assertEqual(result, 6)

    def test_large_k(self):
        """Test with k larger than any element."""
        nums = [1, 2, 3]
        k = 100
        result = self.sol.subarraysDivByK(nums, k)
        self.assertEqual(result, 0)

    def test_consecutive_elements(self):
        """Test consecutive elements forming valid subarrays."""
        nums = [5, -5, 5, -5]
        k = 5
        result = self.sol.subarraysDivByK(nums, k)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
