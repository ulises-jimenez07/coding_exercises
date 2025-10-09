import unittest
from typing import List

class Solution:
    """
    Solution class to find the duplicate number in an array.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in a list of integers using binary search.
        The input list `nums` contains `n + 1` integers where each integer is between 1 and `n` (inclusive).
        This guarantees that at least one duplicate number must exist.

        Args:
            nums: A list of integers.

        Returns:
            The repeated number in the list.
        """
        start = 1
        end = len(nums) - 1

        # Binary search on the range of possible duplicate numbers [1, n]
        while start <= end:
            mid = (start + end) // 2
            
            # Count how many numbers in the array are less than or equal to `mid`
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            # If the count is less than or equal to `mid`, the duplicate is in the upper half
            # (i.e., the numbers from `mid + 1` to `end`). This is because if there were no
            # duplicates, the count would be exactly `mid` for the range [1, mid].
            if count <= mid:
                start = mid + 1
            # If the count is greater than `mid`, it implies a duplicate exists in the lower half
            # (i.e., the numbers from `start` to `mid`). We store `mid` as a potential answer
            # and continue searching the lower half.
            else:
                ans = mid
                end = mid - 1
        return ans

# --- Unit Tests ---

class TestFindDuplicate(unittest.TestCase):
    """
    Unit tests for the findDuplicate method in the Solution class.
    """
    def test_single_duplicate(self):
        """Tests a basic case with one duplicate number."""
        sol = Solution()
        self.assertEqual(sol.findDuplicate([1, 3, 4, 2, 2]), 2)
    
    def test_another_single_duplicate(self):
        """Tests a different case with a single duplicate number."""
        sol = Solution()
        self.assertEqual(sol.findDuplicate([3, 1, 3, 4, 2]), 3)

    def test_duplicate_at_boundaries(self):
        """Tests cases where the duplicate is at the beginning or end of the range."""
        sol = Solution()
        # Duplicate is the smallest possible number
        self.assertEqual(sol.findDuplicate([2, 1, 1]), 1)
        # Duplicate is the largest possible number
        self.assertEqual(sol.findDuplicate([1, 2, 3, 4, 5, 5]), 5)
    
    def test_larger_list(self):
        """Tests with a larger list of numbers."""
        sol = Solution()
        self.assertEqual(sol.findDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]), 9)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)