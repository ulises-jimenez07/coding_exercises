"""
Problem: Find two numbers in array that sum to target value

Approach:
- Use hash table to store seen numbers and indices
- For each number, check if complement exists in hash table
- Time complexity: O(n)
- Space complexity: O(n)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


import unittest


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

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
        self.assertEqual(Solution().twoSum([-1, -2, 7], 5), [1, 2])

    def test_zero_target(self):
        self.assertEqual(Solution().twoSum([0, 4, -4], 0), [1, 2])

    def test_large_list(self):  # Test case for scalability
        nums = list(range(10000))
        target = 19997
        expected_output = [9998, 9999]
        self.assertEqual(Solution().twoSum(nums, target), expected_output)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
