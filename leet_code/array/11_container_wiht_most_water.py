"""
Problem: Find two lines that together with x-axis form a container with most water

Approach:
- Use two pointers at both ends of array
- Calculate area and move pointer pointing to shorter line inward
- Time complexity: O(n)
- Space complexity: O(1)
"""


class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            length = min(height[left], height[right])
            width = right - left
            area = length * width
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


import unittest


class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Tests varying heights."""
        self.assertEqual(self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_same_heights(self):
        """Tests same heights."""
        self.assertEqual(self.solution.maxArea([5, 5, 5, 5, 5]), 20)

    def test_descending_heights(self):
        """Tests descending heights."""
        self.assertEqual(self.solution.maxArea([5, 4, 3, 2, 1]), 6)

    def test_empty_list(self):
        """Tests empty list."""
        self.assertEqual(self.solution.maxArea([]), 0)

    def test_single_element(self):
        """Single element list."""
        self.assertEqual(self.solution.maxArea([5]), 0)

    def test_two_same_heights(self):
        """Two lines of the same height."""
        self.assertEqual(self.solution.maxArea([5, 5]), 5)


if __name__ == "__main__":
    unittest.main()
