import unittest
from typing import List

class Solution:
    """
    A class to solve the "Search Insert Position" problem.
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, this method
        returns the index if the target is found. If not, it returns the index where
        it would be if it were inserted in order.

        Args:
            nums: A sorted list of distinct integers.
            target: The integer to search for or insert.

        Returns:
            The index of the target if found, or the insertion index if not found.
        
        This method uses a binary search algorithm. It maintains a `start` and `end`
        pointer to narrow down the search space. The `ans` variable is initialized
        to the length of the array, which is the default insertion point if the
        target is greater than all elements.
        
        The loop continues as long as `start` is less than or equal to `end`. In
        each iteration, it calculates the middle index `mid`.
        
        - If `nums[mid]` is less than the `target`, it means the target must be
          in the right half, so `start` is moved to `mid + 1`.
        - Otherwise, `nums[mid]` is greater than or equal to the `target`. This
          means `mid` is a potential answer. We store it in `ans` and try to find
          a smaller index by moving `end` to `mid - 1`.
        
        The loop terminates when `start` becomes greater than `end`, and the
        final `ans` holds the correct index.
        """
        start = 0
        end = len(nums) - 1
        ans = len(nums)

        while start <= end:
            mid = (start + end) // 2
            
            # If the middle element is less than the target,
            # the target must be in the right half.
            if nums[mid] < target:
                start = mid + 1
            # If the middle element is >= the target, it could be our answer.
            # We store it and check the left half for a better (smaller) index.
            else:
                ans = mid
                end = mid - 1
        return ans

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """
    def setUp(self):
        """
        Set up a Solution instance for each test.
        """
        self.solution = Solution()

    def test_target_is_found(self):
        """
        Test cases where the target is present in the array.
        """
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 1), 0)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 6), 3)

    def test_target_is_not_found(self):
        """
        Test cases where the target is not present in the array,
        and we need to find the correct insertion position.
        """
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 0), 0)

    def test_empty_array(self):
        """
        Test case for an empty input array.
        The target should be inserted at index 0.
        """
        self.assertEqual(self.solution.searchInsert([], 5), 0)

    def test_single_element_array(self):
        """
        Test cases for an array with a single element.
        """
        self.assertEqual(self.solution.searchInsert([5], 5), 0)
        self.assertEqual(self.solution.searchInsert([5], 6), 1)
        self.assertEqual(self.solution.searchInsert([5], 4), 0)

if __name__ == '__main__':
    unittest.main()