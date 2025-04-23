import unittest  # Import the unittest module
from typing import List  # Import List for type hinting


class Solution:
    """
    Implements the Dutch National Flag algorithm (3-way partitioning)
    to sort an array containing only 0s, 1s, and 2s in-place.
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the array nums containing 0s, 1s, and 2s in-place.

        Args:
            nums: A list of integers (0, 1, or 2).

        Returns:
            None. Modifies the input list `nums` directly.
        """
        # Pointer for the next position to place a 0
        left = 0
        # Pointer for the next position to place a 2 (starting from the end)
        right = len(nums) - 1
        # Current element pointer
        i = 0

        # Iterate while the current pointer is less than or equal to the right pointer
        # The loop terminates when i crosses right, meaning all elements
        # from right+1 onwards are 2s, and all elements before i are 0s or 1s.
        while i <= right:
            if nums[i] == 2:
                # If the current element is 2, swap it with the element at the right pointer
                nums[i], nums[right] = nums[right], nums[i]
                # Decrement the right pointer because we've placed a 2 in its correct section
                # We do NOT increment i here, because the element swapped from the right
                # could be a 0 or 1 and needs to be processed.
                right -= 1
            elif nums[i] == 0:
                # If the current element is 0, swap it with the element at the left pointer
                nums[i], nums[left] = nums[left], nums[i]
                # Increment the left pointer because we've placed a 0 in its correct section
                left += 1
                # Increment the current pointer because the element at nums[left]
                # was already processed (it must have been a 1, or it was the element at i itself
                # if left == i), and the element now at nums[i] (swapped from left) is guaranteed
                # not to be 2 (otherwise it would have been swapped right already).
                i += 1
            else:  # nums[i] == 1
                # If the current element is 1, it's already in its potential correct place
                # relative to 0s and 2s. Just move to the next element.
                i += 1


# --- Unit Tests ---
class TestSortColors(unittest.TestCase):

    def setUp(self):
        """Set up the Solution instance for each test."""
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        expected = [0, 0, 1, 1, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_example_2(self):
        nums = [2, 0, 1]
        expected = [0, 1, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_already_sorted(self):
        nums = [0, 0, 1, 1, 2, 2]
        expected = [0, 0, 1, 1, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_reverse_sorted(self):
        nums = [2, 2, 1, 1, 0, 0]
        expected = [0, 0, 1, 1, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        expected = [0, 0, 0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_all_ones(self):
        nums = [1, 1, 1, 1]
        expected = [1, 1, 1, 1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_all_twos(self):
        nums = [2, 2]
        expected = [2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_zeros_and_ones(self):
        nums = [1, 0, 1, 0, 0]
        expected = [0, 0, 0, 1, 1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_ones_and_twos(self):
        nums = [2, 1, 2, 1, 1]
        expected = [1, 1, 1, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_zeros_and_twos(self):
        nums = [0, 2, 0, 2, 2, 0]
        expected = [0, 0, 0, 2, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_single_element_zero(self):
        nums = [0]
        expected = [0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_single_element_one(self):
        nums = [1]
        expected = [1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_single_element_two(self):
        nums = [2]
        expected = [2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)

    def test_empty_list(self):
        nums = []
        expected = []
        self.solution.sortColors(nums)
        self.assertEqual(nums, expected)


# Standard boilerplate to run the tests when the script is executed
if __name__ == "__main__":
    unittest.main()
