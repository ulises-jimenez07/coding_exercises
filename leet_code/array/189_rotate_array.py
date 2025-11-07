"""
Problem: Rotate an array to the right by k steps in-place

Approach:
- Reverse entire array, then reverse first k elements, then reverse remaining
- Uses three reversals to achieve rotation without extra space
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, start, end):
            i = start
            j = end
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k = k % n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)


class TestRotate(unittest.TestCase):
    def test_rotate_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_rotate_2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        expected = [3, 99, -1, -100]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_rotate_3(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 4
        expected = [3, 4, 5, 6, 1, 2]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_rotate_4(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 6
        expected = [1, 2, 3, 4, 5, 6]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_rotate_5(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 0
        expected = [1, 2, 3, 4, 5, 6]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_rotate_6(self):
        nums = [1]
        k = 0
        expected = [1]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_rotate_7(self):
        nums = [1]
        k = 1
        expected = [1]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_rotate_8(self):
        nums = [1, 2]
        k = 3
        expected = [2, 1]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()
