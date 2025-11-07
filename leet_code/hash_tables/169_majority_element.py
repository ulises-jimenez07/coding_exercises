"""
Problem: Find element that appears more than n/2 times in array

Approach:
- Use hash table to count frequency of each element
- Return element when count exceeds n/2
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = len(nums) // 2
        counter: dict[int, int] = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > majority:
                return num
        return -1  # Should never reach here as problem guarantees majority element exists


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element_list(self):
        self.assertEqual(self.solution.majorityElement([5]), 5)

    def test_simple_majority(self):
        self.assertEqual(self.solution.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_another_simple_majority(self):
        self.assertEqual(self.solution.majorityElement([3, 2, 3]), 3)

    def test_all_same_element(self):
        self.assertEqual(self.solution.majorityElement([5, 5, 5, 5, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.majorityElement([-1, -1, 2, -1, -1]), -1)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
