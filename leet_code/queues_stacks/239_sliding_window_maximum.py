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
from typing import List


class Solution:
    """
    Class containing different implementations for the Sliding Window Maximum problem.
    """

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

    def maximums_of_sliding_window(self, nums: List[int], k: int) -> List[int]:
        """
        Alternative implementation using a unified while loop and left/right pointers.
        This approach maintains a deque of indices where the values are in
        decreasing order.
        """
        if not nums or k == 0:
            return []
        if k > len(nums):
            return [max(nums)]

        res = []
        dq: collections.deque[int] = collections.deque()
        left = right = 0

        while right < len(nums):
            # Maintain decreasing order in deque:
            # Remove elements from back that are smaller than current element
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            # Check if the window has reached size k
            if right - left + 1 == k:
                # Check if the leftmost element in deque is outside the window
                if dq and dq[0] < left:
                    dq.popleft()

                # The first element in deque is the maximum for the current window
                res.append(nums[dq[0]])

                # Slide the window
                left += 1

            right += 1

        return res


class TestMaxSlidingWindow(unittest.TestCase):
    """
    Unit tests for the Sliding Window Maximum implementations.
    """

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

    def test_against_alternative_version(self):
        """Test that the alternative implementation produces the same results."""
        test_cases = [
            ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
            ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
            ([1, 3, -1, -3, 5], 5, [5]),
            ([-1, -3, -5, -2, -4], 3, [-1, -2, -2]),
            ([10, 5, 2, 8, 15, 3], 4, [10, 15, 15]),
            ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
            ([], 3, []),
            ([1, 2, 3], 0, []),
            ([1, 2, 3], 5, [3]),
            ([9, 8, 7, 6, 5, 4], 3, [9, 8, 7, 6]),
            ([1, 2, 3, 4, 5, 6], 3, [3, 4, 5, 6]),
        ]
        for nums, k, expected in test_cases:
            with self.subTest(nums=nums, k=k):
                self.assertEqual(self.solution.maximums_of_sliding_window(nums, k), expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
