"""
Problem: Find all unique triplets in array that sum to zero

Approach:
- Use hash set to track seen numbers and avoid duplicate triplets
- For each number, find pairs that complement to zero using two-sum logic
- Time complexity: O(n^2)
- Space complexity: O(n)
"""

import unittest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans: set[tuple[int, ...]] = set()
        dups: set[int] = set()
        seen: dict[int, int] = {}

        for i, target in enumerate(nums):
            if target not in dups:
                dups.add(target)

                for num in nums[i + 1 :]:
                    complement = -target - num
                    # Check if complement was seen in current target's context
                    if complement in seen and seen[complement] == i:
                        ans.add(tuple(sorted([target, complement, num])))
                    else:
                        seen[num] = i

        return [list(t) for t in ans]


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def assertListOfListsEqual(self, list1: List[List[int]], list2: List[List[int]]):
        """Compare two lists of lists, ignoring order."""
        self.assertEqual(len(list1), len(list2))
        set1 = set(tuple(sorted(sublist)) for sublist in list1)
        set2 = set(tuple(sorted(sublist)) for sublist in list2)
        self.assertEqual(set1, set2)

    def test_empty_list(self):
        self.assertListOfListsEqual(self.solver.threeSum([]), [])

    def test_no_triplets(self):
        self.assertListOfListsEqual(self.solver.threeSum([1, 2, 3]), [])
        self.assertListOfListsEqual(self.solver.threeSum([0, 1, 2]), [])

    def test_simple_case(self):
        self.assertListOfListsEqual(self.solver.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_with_zeros(self):
        self.assertListOfListsEqual(self.solver.threeSum([0, 0, 0]), [[0, 0, 0]])
        self.assertListOfListsEqual(self.solver.threeSum([0, 0, 0, 0]), [[0, 0, 0]])

    def test_duplicates_in_input(self):
        self.assertListOfListsEqual(self.solver.threeSum([-1, 0, 1, 2, -1, -4, -1]), [[-1, -1, 2], [-1, 0, 1]])

    def test_more_complex_case(self):
        self.assertListOfListsEqual(self.solver.threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])

    def test_all_negative(self):
        self.assertListOfListsEqual(self.solver.threeSum([-1, -2, -3]), [])

    def test_all_positive(self):
        self.assertListOfListsEqual(self.solver.threeSum([1, 2, 3]), [])


if __name__ == "__main__":
    unittest.main()
