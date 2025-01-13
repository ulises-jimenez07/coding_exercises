class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two indices in a list of integers such that the values at those indices sum up to the target value.

        Args:
            nums: A list of integers.
            target: The target sum.

        Returns:
            A list containing the indices of the two numbers that add up to the target, or None if no such pair exists.
        """
        seen = {}  # Hash map to store numbers encountered so far and their indices

        for i, num in enumerate(nums):
            complement = (
                target - num
            )  # Calculate the complement needed to reach the target
            if complement in seen:
                return [
                    seen[complement],
                    i,
                ]  # Return the indices if the complement is found
            else:
                seen[num] = i  # Store the current number and its index

        return None  # Added this for clarity. If no two numbers sum up to the target after check all numbers.


# Test cases
import unittest


class TestTwoSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Solution().twoSum([], 0), None)

    def test_single_element_list(self):
        self.assertEqual(Solution().twoSum([5], 10), None)

    def test_two_elements_sum_found(self):
        self.assertEqual(Solution().twoSum([2, 7], 9), [0, 1])

    def test_no_sum_found(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 10), None)

    def test_duplicate_numbers(self):
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])
        self.assertEqual(Solution().twoSum([3, 2, 3], 6), [0, 2])

    def test_negative_numbers(self):
        self.assertEqual(Solution().twoSum([-1, -2, 7], 5), [2, 0])

    def test_zero_target(self):
        self.assertEqual(Solution().twoSum([0, 4, -4], 0), [1, 2])

    def test_large_list(self):  # Test case for scalability
        nums = list(range(10000))
        target = 19997
        expected_output = [9998, 9999]
        self.assertEqual(Solution().twoSum(nums, target), expected_output)


if __name__ == "__main__":
    unittest.main()
