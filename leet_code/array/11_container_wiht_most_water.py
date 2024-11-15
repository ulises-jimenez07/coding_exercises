class Solution(object):
    def maxArea(self, height):
        """
        Finds the largest area of a container formed by two lines from the given heights.

        The container's bottom is the x-axis, and the two lines are drawn vertically.
        The area is calculated as: area = min(height[left], height[right]) * (right - left).

        :type height: List[int]  # List of heights representing the vertical lines.
        :rtype: int             # The maximum area that can be formed.
        """
        left = 0  # Initialize left pointer to the start of the list.
        right = len(height) - 1  # Initialize right pointer to the end of the list.
        max_area = 0  # Initialize maximum area to 0.

        while (
            left < right
        ):  # Continue as long as the left pointer is less than the right pointer.
            length = min(
                height[left], height[right]
            )  # Find the shorter line, which determines the container's height.
            width = right - left  # Calculate the width of the container.
            area = length * width  # Calculate the current area.
            max_area = max(
                max_area, area
            )  # Update the maximum area if the current area is greater.

            # Move the pointer of the shorter line inward to potentially find a larger area.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area  # Return the calculated maximum area.


# Test cases
solution = Solution()

# Test case 1: Basic example
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
expected1 = 49
result1 = solution.maxArea(height1)
print(f"Test case 1: Expected {expected1}, got {result1}")
assert result1 == expected1

# Test case 2: All lines same height
height2 = [5, 5, 5, 5, 5]
expected2 = 20  # 5 * 4 (right - left)
result2 = solution.maxArea(height2)
print(f"Test case 2: Expected {expected2}, got {result2}")
assert result2 == expected2

# Test case 3: Descending heights
height3 = [5, 4, 3, 2, 1]
expected3 = 6
result3 = solution.maxArea(height3)
print(f"Test case 3: Expected {expected3}, got {result3}")
assert result3 == expected3


# Test case 4: Empty list
height4 = [list]
expected4 = 0
result4 = solution.maxArea(height4)
print(f"Test case 4: Expected {expected4}, got {result4}")
assert result4 == expected4

# Test case 5: Single element list
height5 = [5]
expected5 = 0
result5 = solution.maxArea(height5)
print(f"Test case 5: Expected {expected5}, got {result5}")
assert result5 == expected5

# Test case 6: Two lines of the same height
height6 = [5, 5]
expected6 = 5
result6 = solution.maxArea(height6)
print(f"Test case 6: Expected {expected6}, got {result6}")
assert result6 == expected6
