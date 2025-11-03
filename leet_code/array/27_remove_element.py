from typing import List
import unittest

class Solution:
    """
    Implements a method to remove all occurrences of a specific value 'val' 
    from a list of integers 'nums' in-place.
    The order of elements that are not equal to 'val' can be changed.
    The function returns the number of elements in 'nums' which are not equal to 'val'.
    The elements beyond the returned length do not matter.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of 'val' in-place.

        Args:
            nums (List[int]): The input list of integers.
            val (int): The value to be removed from the list.

        Returns:
            int: The new length of the array after removal (count of elements not equal to 'val').
        """
        # 'swap' acts as a pointer for the next position to insert a non-'val' element.
        # It also tracks the count of elements that are NOT equal to 'val'.
        swap = 0

        # Iterate through the entire list with pointer 'i'.
        for i in range(len(nums)):
            # If the current element is not the value we want to remove...
            if nums[i] != val:
                # ...then move this element to the 'swap' position. 
                # This effectively pushes non-'val' elements to the front of the list.
                nums[swap] = nums[i]
                # Increment 'swap' to point to the next available position for a non-'val' element.
                swap += 1

        # 'swap' now holds the count of elements not equal to 'val', 
        # which is the required new length.
        return swap

# --- Unit Tests ---

class TestRemoveElement(unittest.TestCase):
    """
    Unit tests for the removeElement method in the Solution class.
    """

    def test_example_one(self):
        """Test with a standard example where 'val' appears multiple times."""
        # Arrange
        solution = Solution()
        nums = [3, 2, 2, 3]
        val = 3
        expected_len = 2
        
        # Act
        result_len = solution.removeElement(nums, val)
        
        # Assert
        self.assertEqual(result_len, expected_len, "The returned length should be 2")
        # Check that the first 'expected_len' elements are correct (2s in any order)
        self.assertEqual(sorted(nums[:result_len]), [2, 2], "The first 2 elements should be [2, 2]")

    def test_example_two(self):
        """Test with an example where 'val' appears less frequently and other numbers are present."""
        # Arrange
        solution = Solution()
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_len = 5
        
        # Act
        result_len = solution.removeElement(nums, val)
        
        # Assert
        self.assertEqual(result_len, expected_len, "The returned length should be 5")
        # The expected non-'val' elements are [0, 1, 3, 0, 4]. Check the first 'expected_len' elements.
        self.assertEqual(sorted(nums[:result_len]), [0, 0, 1, 3, 4], "The first 5 elements should contain [0, 1, 3, 0, 4] in some order")

    def test_no_match(self):
        """Test case where 'val' is not present in the list."""
        # Arrange
        solution = Solution()
        nums = [1, 2, 3, 4]
        val = 5
        expected_len = 4
        
        # Act
        result_len = solution.removeElement(nums, val)
        
        # Assert
        self.assertEqual(result_len, expected_len, "The returned length should be 4")
        self.assertEqual(nums[:result_len], [1, 2, 3, 4], "The list should remain unchanged")

    def test_all_match(self):
        """Test case where all elements match 'val'."""
        # Arrange
        solution = Solution()
        nums = [7, 7, 7]
        val = 7
        expected_len = 0
        
        # Act
        result_len = solution.removeElement(nums, val)
        
        # Assert
        self.assertEqual(result_len, expected_len, "The returned length should be 0")
        self.assertEqual(nums[:result_len], [], "The list should effectively be empty")

    def test_empty_list(self):
        """Test case with an empty input list."""
        # Arrange
        solution = Solution()
        nums = []
        val = 1
        expected_len = 0
        
        # Act
        result_len = solution.removeElement(nums, val)
        
        # Assert
        self.assertEqual(result_len, expected_len, "The returned length should be 0 for an empty list")
        self.assertEqual(nums[:result_len], [], "The list should remain empty")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)