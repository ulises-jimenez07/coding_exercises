from typing import List
import unittest

class Solution:
    """
    This class implements a search algorithm to find a target value in a rotated sorted array.
    """
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        This algorithm uses a modified binary search approach to handle the rotation.
        It divides the array into two parts: a left sorted part and a right sorted part.
        By comparing the middle element with the first element of the array, it determines
        which part is sorted and narrows down the search space accordingly.

        Args:
            nums: A list of integers representing the rotated sorted array.
            target: The integer value to search for.

        Returns:
            The index of the target value if found, otherwise -1.
        """
        start = 0
        end = len(nums) - 1
        ans = -1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            # Determine which half of the array the mid element belongs to.
            # If nums[mid] is in the left sorted part and target is in the right unsorted part.
            if nums[mid] >= nums[0] and target < nums[0]:
                start = mid + 1
            # If nums[mid] is in the right sorted part and target is in the left unsorted part.
            elif nums[mid] < nums[0] and target >= nums[0]:
                end = mid - 1
            # Regular binary search on the determined part of the array.
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:  # nums[mid] > target
                    end = mid - 1
        return ans

# --- Unit Tests ---

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def setUp(self):
        """
        Set up a new instance of the Solution class before each test.
        """
        self.solution = Solution()

    def test_target_found_in_rotated_array(self):
        """
        Test case where the target is present in a rotated array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_target_found_in_unrotated_array(self):
        """
        Test case where the target is present in a non-rotated array.
        """
        nums = [1, 2, 3, 4, 5, 6, 7]
        target = 3
        self.assertEqual(self.solution.search(nums, target), 2)

    def test_target_not_found(self):
        """
        Test case where the target is not present in the array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_target_is_first_element(self):
        """
        Test case where the target is the first element of the array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 4
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_target_is_last_element(self):
        """
        Test case where the target is the last element of the array.
        """
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 2
        self.assertEqual(self.solution.search(nums, target), 6)

    def test_empty_array(self):
        """
        Test case with an empty array.
        """
        nums = []
        target = 5
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_single_element_array_found(self):
        """
        Test case with a single-element array where the target is found.
        """
        nums = [1]
        target = 1
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_single_element_array_not_found(self):
        """
        Test case with a single-element array where the target is not found.
        """
        nums = [1]
        target = 0
        self.assertEqual(self.solution.search(nums, target), -1)

# To run the tests, you can use:
# unittest.main()

if __name__ == '__main__':
    unittest.main()