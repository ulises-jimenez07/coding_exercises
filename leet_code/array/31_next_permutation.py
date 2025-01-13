from typing import List
import unittest


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Finds the next lexicographically greater permutation of a list of integers in-place.

        Args:
            nums: A list of integers.

        Do not return anything, modify nums in-place instead.
        """

        def _reverse(nums, start):
            """Reverses a portion of the list nums in-place."""
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        i = n - 2
        # Find the first decreasing element from right to left.
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            # Find the smallest element to the right of nums[i] that is greater than nums[i].
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j].
            nums[i], nums[j] = nums[j], nums[i]
        # Reverse the portion of the list to the right of i.
        _reverse(nums, i + 1)


class TestNextPermutation(unittest.TestCase):
    def test_next_permutation_1(self):
        nums = [1, 2, 3]
        expected = [1, 3, 2]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_next_permutation_2(self):
        nums = [3, 2, 1]
        expected = [1, 2, 3]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_next_permutation_3(self):
        nums = [1, 1, 5]
        expected = [1, 5, 1]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_next_permutation_4(self):
        nums = [1]
        expected = [1]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_next_permutation_5(self):
        nums = [1, 2]
        expected = [2, 1]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_next_permutation_6(self):
        nums = [2, 3, 1]
        expected = [3, 1, 2]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()
