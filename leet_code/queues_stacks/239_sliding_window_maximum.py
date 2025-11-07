"""
Problem: Sliding Window Maximum - find max in each window of size k

Approach:
- Use a deque to maintain indices of potential maximums
- Remove elements outside window and smaller than current
- Time complexity: O(n) where n is array length
- Space complexity: O(k) for the deque
"""

import collections
import unittest


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Finds the maximum value in each sliding window of size `k`.
        Uses a deque to efficiently track potential maximums.
        """
        if not nums or k == 0:
            return []
        if k > len(nums):
            return [max(nums)]

        ans = []
        n = len(nums)
        de: collections.deque[int] = collections.deque()

        # Initialize the deque for the first window
        for i in range(k):
            while de and nums[de[-1]] < nums[i]:
                de.pop()
            de.append(i)

        ans.append(nums[de[0]])

        # Slide the window
        for j in range(k, n):
            starting_point = j - k + 1

            while de and de[0] < starting_point:
                de.popleft()

            while de and nums[de[-1]] < nums[j]:
                de.pop()

            de.append(j)
            ans.append(nums[de[0]])

        return ans


class TestMaxSlidingWindow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Test with a standard array and window size."""
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_single_element_window(self):
        """Test with window size k=1."""
        nums = [1, 2, 3, 4, 5]
        k = 1
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_window_equals_array_length(self):
        """Test with window size k equal to the array length."""
        nums = [1, 3, -1, -3, 5]
        k = 5
        expected = [5]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_all_negative_numbers(self):
        """Test with an array containing only negative numbers."""
        nums = [-1, -3, -5, -2, -4]
        k = 3
        expected = [-1, -2, -2]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_all_positive_numbers(self):
        """Test with an array containing only positive numbers."""
        nums = [10, 5, 2, 8, 15, 3]
        k = 4
        expected = [10, 15, 15]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_duplicate_numbers(self):
        """Test with an array containing duplicate numbers."""
        nums = [1, 3, 1, 2, 0, 5]
        k = 3
        expected = [3, 3, 2, 5]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_empty_nums(self):
        """Test with an empty input array."""
        nums = []
        k = 3
        expected = []
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_k_is_zero(self):
        """Test with k = 0."""
        nums = [1, 2, 3]
        k = 0
        expected = []
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_k_greater_than_nums_length(self):
        """Test with k greater than the length of nums."""
        nums = [1, 2, 3]
        k = 5
        expected = [3]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_decreasing_numbers(self):
        """Test with a strictly decreasing sequence."""
        nums = [9, 8, 7, 6, 5, 4]
        k = 3
        expected = [9, 8, 7, 6]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_increasing_numbers(self):
        """Test with a strictly increasing sequence."""
        nums = [1, 2, 3, 4, 5, 6]
        k = 3
        expected = [3, 4, 5, 6]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
