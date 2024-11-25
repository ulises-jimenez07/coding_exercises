import unittest  # Import the unittest module for writing test cases


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Finds the majority element in a list of integers.

        The majority element is the element that appears more than n // 2 times, where n is the length of the list.

        Args:
            nums: A list of integers.

        Returns:
            The majority element.
        """
        majority = (
            len(nums) // 2
        )  # Calculate the threshold for majority (more than n//2)
        counter = {}  # Initialize a dictionary to store element counts

        for num in nums:
            counter[num] = (
                counter.get(num, 0) + 1
            )  # Increment the count for the current number
            if (
                counter[num] > majority
            ):  # Check if the count exceeds the majority threshold
                return num  # Return the number if it's the majority element


# Test cases using the unittest module
class TestMajorityElement(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(
            Solution().majorityElement([5]), 5
        )  # Single element is the majority element

    def test_simple_majority(self):
        self.assertEqual(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_another_simple_majority(self):
        self.assertEqual(Solution().majorityElement([3, 2, 3]), 3)

    def test_all_same_element(self):
        self.assertEqual(
            Solution().majorityElement([5, 5, 5, 5, 5]), 5
        )  # All elements are the same

    def test_negative_numbers(self):
        self.assertEqual(
            Solution().majorityElement([-1, -1, 2, -1, -1]), -1
        )  # Test with negative numbers


if __name__ == "__main__":
    unittest.main()
