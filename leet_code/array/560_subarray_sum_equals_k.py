from typing import List
import unittest

class Solution:
    """
    Contains two methods for solving the Subarray Sum Equals K problem:
    1. subarraySum (Efficient O(n) using Prefix Sum and Hash Map)
    2. subarraySum_bruteforce (Correct but less efficient O(n^2))
    """

    def subarraySum_bruteforce(self, nums: List[int], k: int) -> int:
        """
        Brute-force approach with O(n^2) time complexity.
        Checks every contiguous subarray sum.
        """
        ans = 0
        # Outer loop fixes the starting index 'i' of the subarray.
        for i in range(len(nums)):
            partial_sum = 0
            # Inner loop iterates from the starting index 'i' to the end, 
            # calculating the sum of the subarray nums[i:j+1].
            for j in range(i, len(nums)):
                partial_sum += nums[j]
                if partial_sum == k:
                    ans += 1
        return ans

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Efficient approach using Prefix Sum and Hash Map with O(n) time complexity.
        This is the preferred solution for performance.
        """
        # 'ans' stores the count of subarrays that sum up to 'k'.
        ans = 0
        # 'current_sum' tracks the running prefix sum.
        current_sum = 0

        # 'cum_hashmap' stores the frequency of each prefix sum. {sum: frequency}
        # {0: 1} handles subarrays starting from index 0.
        cum_hashmap = {0: 1}

        # Iterate through each number.
        for num in nums:
            # 1. Update the current prefix sum.
            current_sum += num
            
            # 2. Calculate the required preceding prefix sum (S_previous).
            # We are looking for S_previous such that S_current - S_previous = k.
            required_sum = current_sum - k

            # 3. Check how many times that required sum has occurred before.
            if required_sum in cum_hashmap:
                # Add the frequency; each occurrence represents a valid subarray ending here.
                ans += cum_hashmap[required_sum]

            # 4. Update the map with the current prefix sum's frequency.
            # (Note: This must happen *after* checking for the required_sum 
            # to avoid counting the current index as both start and end point).
            cum_hashmap[current_sum] = cum_hashmap.get(current_sum, 0) + 1
            
        return ans

# --- Unit Tests ---
class TestSubarraySum(unittest.TestCase):
    
    def setUp(self):
        """Set up the Solution object for each test."""
        self.sol = Solution()
        # Define common test cases
        self.tests = [
            ([1, 1, 1], 2, 2, "Basic positive numbers"),
            ([0, 0, 0, 0, 0], 0, 15, "Zeros case (n*(n+1)/2)"),
            ([1, -1, 0], 0, 3, "Negatives and zero"),
            ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4, "Complex case"),
            ([1, 2, 3], 7, 0, "No match"),
            ([5], 5, 1, "Single element match"),
        ]

    def test_efficient_solution(self):
        """Test the O(n) prefix sum solution."""
        print("\nTesting O(n) solution...")
        for nums, k, expected, desc in self.tests:
            with self.subTest(msg=desc, nums=nums, k=k):
                result = self.sol.subarraySum(nums, k)
                self.assertEqual(result, expected, f"Failed for {nums}, k={k}. Expected {expected}, got {result}")

    def test_bruteforce_solution(self):
        """Test the O(n^2) brute-force solution."""
        print("Testing O(n^2) brute-force solution...")
        for nums, k, expected, desc in self.tests:
            with self.subTest(msg=desc, nums=nums, k=k):
                result = self.sol.subarraySum_bruteforce(nums, k)
                self.assertEqual(result, expected, f"Failed for {nums}, k={k}. Expected {expected}, got {result}")

if __name__ == '__main__':
    # Run the tests when the script is executed directly
    unittest.main(argv=['first-arg-is-ignored'], exit=False)