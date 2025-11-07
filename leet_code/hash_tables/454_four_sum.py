"""
Problem: Count tuples (i,j,k,l) where nums1[i]+nums2[j]+nums3[k]+nums4[l]==0

Approach:
- Store all sums of nums1[i]+nums2[j] in hash table
- For each sum of nums3[k]+nums4[l], check if negative exists
- Count matching pairs
- Time complexity: O(n²)
- Space complexity: O(n²)
"""

import unittest


class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = 0
        map = {}

        # Store all sums from first two arrays
        for a in nums1:
            for b in nums2:
                sum_ab = a + b
                map[sum_ab] = map.get(sum_ab, 0) + 1

        # Check complement from last two arrays
        for c in nums3:
            for d in nums4:
                sum_cd = c + d
                complement = -sum_cd
                if complement in map:
                    count += map[complement]

        return count


class TestFourSumCount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_lists(self):
        self.assertEqual(self.solution.fourSumCount([], [], [], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(self.solution.fourSumCount([1], [1], [-1], [-1]), 1)
        self.assertEqual(self.solution.fourSumCount([1], [2], [-2], [-1]), 1)
        self.assertEqual(self.solution.fourSumCount([1], [1], [-2], [-1]), 0)

    def test_multiple_elements(self):
        nums1 = [1, 2]
        nums2 = [-2, -1]
        nums3 = [-1, 2]
        nums4 = [0, 2]
        self.assertEqual(self.solution.fourSumCount(nums1, nums2, nums3, nums4), 2)

    def test_all_zeros(self):
        self.assertEqual(self.solution.fourSumCount([0], [0], [0], [0]), 1)
        self.assertEqual(self.solution.fourSumCount([0, 0], [0, 0], [0, 0], [0, 0]), 16)

    def test_large_input(self):
        nums1 = list(range(100))
        nums2 = list(range(100))
        nums3 = list(range(-100, 0))
        nums4 = list(range(-100, 0))
        self.assertGreaterEqual(self.solution.fourSumCount(nums1, nums2, nums3, nums4), 0)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
