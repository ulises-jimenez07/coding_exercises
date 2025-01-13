class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Checks if a list of integers contains any duplicate elements.

        Args:
            nums: A list of integers.

        Returns:
            True if the list contains duplicates, False otherwise.
        """
        seen = set()  # Use a set to store seen numbers efficiently
        for num in nums:
            if num in seen:  # Check if the current number has already been encountered
                return True  # Return True immediately if a duplicate is found
            seen.add(num)  # Add the current number to the set of seen numbers
        return (
            False  # Return False if no duplicates are found after checking all numbers
        )


# Test cases
import unittest


class TestContainsDuplicate(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(Solution().containsDuplicate([]))

    def test_single_element_list(self):
        self.assertFalse(Solution().containsDuplicate([5]))

    def test_duplicates_present(self):
        self.assertTrue(Solution().containsDuplicate([1, 2, 3, 1]))

    def test_no_duplicates(self):
        self.assertFalse(Solution().containsDuplicate([1, 2, 3, 4]))

    def test_all_duplicates(self):
        self.assertTrue(Solution().containsDuplicate([2, 2, 2, 2]))

    def test_negative_numbers(self):
        self.assertTrue(Solution().containsDuplicate([-1, 2, -1, 3]))

    def test_mixed_positive_and_negative(self):
        self.assertFalse(Solution().containsDuplicate([-1, 2, 3, 4]))
        self.assertTrue(Solution().containsDuplicate([-1, 2, -1, 4]))


if __name__ == "__main__":
    unittest.main()
