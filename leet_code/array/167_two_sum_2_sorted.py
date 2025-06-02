import unittest
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers in a sorted list that add up to a specific target.

        This function uses a two-pointer approach to efficiently find the indices
        (1-based) of the two numbers that sum up to the target. It assumes
        the input list 'numbers' is sorted in non-decreasing order.

        Args:
            numbers: A list of integers sorted in non-decreasing order.
            target: The integer target sum.

        Returns:
            A list containing the 1-based indices of the two numbers that sum to
            the target. If no such pair is found, an empty list is returned.
        """
        # Initialize two pointers: 'start' at the beginning of the list
        # and 'end' at the end of the list.
        start = 0
        end = len(numbers) - 1

        # Continue as long as the 'start' pointer is before the 'end' pointer.
        while start < end:
            # Calculate the sum of the numbers at the current 'start' and 'end' positions.
            current_sum = numbers[start] + numbers[end]

            # If the current sum is less than the target, it means we need a larger sum.
            # To achieve this, increment the 'start' pointer to consider a larger number
            # from the beginning of the list.
            if current_sum < target:
                start += 1
            # If the current sum is greater than the target, it means we need a smaller sum.
            # To achieve this, decrement the 'end' pointer to consider a smaller number
            # from the end of the list.
            elif current_sum > target:
                end -= 1
            # If the current sum is exactly equal to the target, we've found our pair.
            # Return their 1-based indices.
            else:
                return [start + 1, end + 1]

        # If the loop completes and no such pair is found, return an empty list.
        return []


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        """Set up for test cases."""
        self.solution = Solution()

    def test_example_case(self):
        """Test with a basic example where a solution exists."""
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_no_solution(self):
        """Test case where no two numbers sum up to the target."""
        numbers = [1, 2, 3, 4]
        target = 10
        self.assertEqual(self.solution.twoSum(numbers, target), [])

    def test_large_numbers(self):
        """Test with larger numbers and a larger target."""
        numbers = [10, 20, 30, 40, 50]
        target = 70
        self.assertEqual(self.solution.twoSum(numbers, target), [2, 5])

    def test_negative_numbers(self):
        """Test with negative numbers."""
        numbers = [-5, -2, 0, 1, 3, 6]
        target = -2
        # Original expectation: [2, 3] (-2 + 0)
        # Actual result from current code: [1, 5] (-5 + 3)
        # Both are valid. We update the test to match the code's valid output.
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 5])

    def test_duplicate_numbers(self):
        """Test with duplicate numbers in the input array."""
        numbers = [1, 2, 3, 3, 4, 5]
        target = 6
        # Original expectation: [2, 4] (2 + 3) - This was incorrect, 2+3=5
        # Actual result from current code: [1, 6] (1 + 5)
        # Both (1+5) and (2+4) and (3+3) can sum to 6.
        # Since the problem asks for any valid pair, [1, 6] is correct.
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 6])

    def test_target_at_ends(self):
        """Test case where the target sum is formed by the first and last elements."""
        numbers = [1, 5, 8, 10]
        target = 11
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 4])

    def test_minimum_length_array(self):
        """Test with the minimum possible array length (2 elements)."""
        numbers = [1, 2]
        target = 3
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_empty_array(self):
        """Test with an empty array (should return an empty list)."""
        numbers = []
        target = 5
        self.assertEqual(self.solution.twoSum(numbers, target), [])

    def test_single_element_array(self):
        """Test with a single element array (should return an empty list as two numbers are needed)."""
        numbers = [5]
        target = 5
        self.assertEqual(self.solution.twoSum(numbers, target), [])


# This allows running the tests directly when the script is executed.
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
