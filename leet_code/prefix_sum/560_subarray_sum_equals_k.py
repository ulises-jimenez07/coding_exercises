"""
Problem: Count number of continuous subarrays that sum to k

Approach:
- Use prefix sum with hash map to track cumulative sums
- Check if (current_sum - k) exists to find valid subarrays
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest
from typing import List


class Solution:
    """Solution class for subarray sum equals k problem."""

    def subarraySum_bruteforce(self, nums: List[int], k: int) -> int:
        """Brute-force approach with O(n^2) time complexity."""
        ans = 0
        for i in range(len(nums)):
            partial_sum = 0
            for j in range(i, len(nums)):
                partial_sum += nums[j]
                if partial_sum == k:
                    ans += 1
        return ans

    def subarraySum(self, nums: List[int], k: int) -> int:
        """Efficient approach using prefix sum and hash map with O(n) time complexity."""
        ans = 0
        current_sum = 0
        cum_hashmap = {0: 1}

        for num in nums:
            current_sum += num
            required_sum = current_sum - k

            if required_sum in cum_hashmap:
                ans += cum_hashmap[required_sum]

            cum_hashmap[current_sum] = cum_hashmap.get(current_sum, 0) + 1

        return ans


class TestSubarraySum(unittest.TestCase):
    """Test cases for subarray sum solution."""

    def setUp(self):
        self.sol = Solution()
        self.tests = [
            ([1, 1, 1], 2, 2, "Basic positive numbers"),
            ([0, 0, 0, 0, 0], 0, 15, "Zeros case"),
            ([1, -1, 0], 0, 3, "Negatives and zero"),
            ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4, "Complex case"),
            ([1, 2, 3], 7, 0, "No match"),
            ([5], 5, 1, "Single element match"),
        ]

    def test_efficient_solution(self):
        """O(n) prefix sum solution."""
        for nums, k, expected, desc in self.tests:
            with self.subTest(msg=desc, nums=nums, k=k):
                result = self.sol.subarraySum(nums, k)
                self.assertEqual(result, expected)

    def test_bruteforce_solution(self):
        """O(n^2) brute-force solution."""
        for nums, k, expected, desc in self.tests:
            with self.subTest(msg=desc, nums=nums, k=k):
                result = self.sol.subarraySum_bruteforce(nums, k)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
