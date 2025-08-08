from typing import List
import unittest

class Solution:
    """
    Finds the minimum element in a rotated sorted array.
    """
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array using binary search.

        A rotated sorted array is an array that was originally sorted
        and then rotated at some pivot point. For example, [0, 1, 2, 4, 5, 6, 7]
        might become [4, 5, 6, 7, 0, 1, 2].

        The algorithm uses a modified binary search approach to efficiently find the
        minimum element. The key idea is to compare the middle element with the last
        element of the array to determine which side of the array is sorted.

        Args:
            nums: A list of integers representing the rotated sorted array.

        Returns:
            The minimum element in the array.
        """
        start = 0
        end = len(nums) - 1
        ans = nums[0]  # Initialize the answer with the first element

        while start <= end:
            mid = (start + end) // 2

            # Check if the middle element is less than or equal to the last element.
            # This indicates that the right half of the array is sorted, and the
            # minimum element is either nums[mid] or in the left half.
            if nums[mid] <= nums[-1]:
                ans = nums[mid]  # Update the answer
                end = mid - 1  # Search in the left half
            else:
                # The right half is not sorted, which means the minimum element is
                # in the right half of the array.
                start = mid + 1  # Search in the right half

        return ans

# --- Unit Tests ---
class TestFindMin(unittest.TestCase):
    """
    Unit tests for the Solution.findMin method.
    """
    def test_rotated_array(self):
        """
        Test case with a standard rotated sorted array.
        """
        solution = Solution()
        self.assertEqual(solution.findMin([3, 4, 5, 1, 2]), 1)

    def test_no_rotation(self):
        """
        Test case with an array that is not rotated.
        """
        solution = Solution()
        self.assertEqual(solution.findMin([1, 2, 3, 4, 5]), 1)

    def test_single_element(self):
        """
        Test case with a single-element array.
        """
        solution = Solution()
        self.assertEqual(solution.findMin([1]), 1)

    def test_fully_rotated_array(self):
        """
        Test case where the array is rotated at the very beginning.
        """
        solution = Solution()
        self.assertEqual(solution.findMin([4, 5, 6, 7, 0, 1, 2]), 0)
    
    def test_two_elements(self):
        """
        Test case with a two-element array.
        """
        solution = Solution()
        self.assertEqual(solution.findMin([2, 1]), 1)

if __name__ == '__main__':
    unittest.main()