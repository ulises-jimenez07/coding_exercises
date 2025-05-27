import collections
import unittest


class Solution:
    """
    A class to find the maximum value in each sliding window of a given array.
    """

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Finds the maximum value in each sliding window of size `k`.

        This method uses a deque (double-ended queue) to efficiently keep track
        of potential maximums in the current window. The deque stores indices
        of elements from `nums` in decreasing order of their corresponding values.
        This ensures that the front of the deque always holds the index of the
        maximum element in the current window.

        Args:
            nums: The input list of integers.
            k: The size of the sliding window.

        Returns:
            A list of integers, where each element is the maximum value
            of the corresponding sliding window.
        """
        # Handle edge cases where the input list is empty or k is invalid.
        # If nums is empty or k is 0, there are no windows.
        if not nums or k == 0:
            return []
        # If k is greater than the length of nums, the window covers the whole array.
        # In this case, the maximum is simply the maximum of the entire array.
        if k > len(nums):
            return [max(nums)]

        ans = []  # This list will store the maximums for each window.
        n = len(nums)  # Total number of elements in the input array.

        # Deque will store indices of elements.
        # Elements in the deque are maintained in decreasing order of their values.
        # The front of the deque (de[0]) will always be the index of the current maximum.
        de = collections.deque()

        # --- Phase 1: Initialize the deque and find the maximum for the first window (0 to k-1) ---
        # Iterate through the first 'k' elements to populate the initial deque.
        for i in range(k):
            # Remove elements from the back of the deque that are smaller than the current element.
            # This ensures that the deque maintains elements in decreasing order of value.
            # If nums[de[-1]] < nums[i], then de[-1] cannot be the maximum of any future window
            # that includes 'i', because 'i' is larger and appears later.
            while de and nums[de[-1]] < nums[i]:
                de.pop()
            # Add the current element's index to the back of the deque.
            de.append(i)

        # After processing the first 'k' elements, the front of the deque (de[0])
        # holds the index of the maximum element in the first window.
        ans.append(nums[de[0]])

        # --- Phase 2: Slide the window from k to n-1 ---
        # Iterate through the remaining elements, starting from index 'k'.
        for j in range(k, n):
            # Calculate the starting index of the current window.
            # For a window ending at 'j' with size 'k', it starts at 'j - k + 1'.
            starting_point = j - k + 1

            # Remove elements from the front of the deque that are outside the current window.
            # If de[0] (the current maximum's index) is less than the window's starting_point,
            # it means the maximum is no longer in the current window, so remove it.
            while de and de[0] < starting_point:
                de.popleft()

            # Remove elements from the back of the deque that are smaller than the current element.
            # This is similar to Phase 1, maintaining the decreasing order property.
            while de and nums[de[-1]] < nums[j]:
                de.pop()

            # Add the current element's index to the back of the deque.
            de.append(j)

            # The element at the front of the deque (de[0]) is now the maximum
            # for the current window (ending at 'j').
            ans.append(nums[de[0]])

        return ans


class TestMaxSlidingWindow(unittest.TestCase):
    """
    Unit tests for the Solution.maxSlidingWindow method.
    """

    def setUp(self):
        """Set up a Solution instance before each test."""
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


# This block allows running the tests directly when the script is executed.
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
