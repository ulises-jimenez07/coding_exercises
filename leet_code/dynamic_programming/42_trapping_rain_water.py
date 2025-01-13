import unittest


class Solution(object):
    def trap(self, height):
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1,
        compute how much water it can trap after raining.

        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:  # Handle empty input
            return 0

        left = [0] * n  # Initialize left max array
        right = [0] * n  # Initialize right max array

        answer = 0  # Initialize trapped water

        left[0] = height[0]  # Initialize first element of left max array
        # Calculate left max for each bar
        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])

        right[n - 1] = height[n - 1]  # Initialize last element of right max array
        # Calculate right max for each bar
        for i in range(n - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])

        # Calculate trapped water for each bar
        for i in range(n):
            answer += min(right[i], left[i]) - height[i]

        return answer  # Return total trapped water


class TestTrap(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_input(self):
        self.assertEqual(self.solution.trap([]), 0)

    def test_single_bar(self):
        self.assertEqual(self.solution.trap([5]), 0)

    def test_two_bars(self):
        self.assertEqual(self.solution.trap([5, 2]), 0)

    def test_simple_case(self):
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_all_same_height(self):
        self.assertEqual(self.solution.trap([5, 5, 5, 5, 5]), 0)

    def test_increasing_height(self):
        self.assertEqual(self.solution.trap([1, 2, 3, 4, 5]), 0)

    def test_decreasing_height(self):
        self.assertEqual(self.solution.trap([5, 4, 3, 2, 1]), 0)

    def test_leetcode_example_1(self):
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_leetcode_example_2(self):
        self.assertEqual(self.solution.trap([4, 2, 0, 3, 2, 5]), 9)


if __name__ == "__main__":
    unittest.main()
