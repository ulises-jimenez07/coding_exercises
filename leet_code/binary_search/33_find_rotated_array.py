from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        Args:
            nums: The rotated sorted array.
            target: The value to search for.

        Returns:
            The index of the target value if found, otherwise -1.
        """
        left = 0
        right = len(nums) - 1

        # Find the pivot point (where the rotation occurs) if the array is rotated
        if right > 0 and nums[left] >= nums[right]:  # Check if array is rotated
            middle = (right + left) // 2
            while nums[middle] <= nums[middle + 1]:  # Binary search to find the pivot
                if nums[left] <= nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
                middle = (right + left) // 2
                if (
                    middle + 1 > len(nums) - 1
                ):  # Handle edge case where middle+1 is out of bounds
                    break

            # Determine which subarray to search based on the target and pivot
            if target >= nums[0] and target <= nums[middle]:
                left = 0
                right = middle
            else:
                left = middle + 1
                right = len(nums) - 1

        # Perform binary search on the chosen subarray
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1

        return -1


class TestSearch(unittest.TestCase):

    def test_search_rotated_array(self):
        sol = Solution()
        self.assertEqual(sol.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(sol.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(sol.search([1], 0), -1)
        self.assertEqual(sol.search([1, 3], 3), 1)
        self.assertEqual(sol.search([3, 1], 1), 1)
        self.assertEqual(sol.search([5, 1, 3], 5), 0)
        self.assertEqual(sol.search([4, 5, 6, 7, 8, 1, 2, 3], 8), 4)


if __name__ == "__main__":
    unittest.main()
