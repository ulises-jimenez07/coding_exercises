class Solution(object):
    def searchRange(self, nums, target):
        """
        Finds the starting and ending positions of a given target value in a sorted array.

        :type nums: List[int]  The sorted array of integers.
        :type target: int      The target value to search for.
        :rtype: List[int]     A list containing the starting and ending positions of the target.
        Returns [-1, -1] if the target is not found.
        """
        left = self.getLeftPosition(
            nums, target
        )  # Find the leftmost occurrence of the target
        right = self.getRightPosition(
            nums, target
        )  # Find the rightmost occurrence of the target
        return [left, right]

    def getLeftPosition(self, nums, target):
        """
        Finds the leftmost (starting) position of the target in the sorted array.

        :type nums: List[int]  The sorted array of integers.
        :type target: int      The target value to search for.
        :rtype: int           The index of the leftmost occurrence of the target, or -1 if not found.
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (
                left + (right - left) // 2
            )  # Calculate the middle index to avoid potential overflow
            if nums[mid] == target:
                # Check if mid is the leftmost occurrence: either mid is 0 or the element to its left is different
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1  # Search in the left half
            elif nums[mid] > target:
                right = mid - 1  # Search in the left half
            else:
                left = mid + 1  # Search in the right half

        return -1  # Target not found

    def getRightPosition(self, nums, target):
        """
        Finds the rightmost (ending) position of the target in the sorted array.

        :type nums: List[int]  The sorted array of integers.
        :type target: int      The target value to search for.
        :rtype: int           The index of the rightmost occurrence of the target, or -1 if not found.
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # Check if mid is the rightmost occurrence: either mid is the last element or the element to its right is different
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1  # Search in the right half
            elif nums[mid] > target:
                right = mid - 1  # Search in the left half
            else:
                left = mid + 1  # Search in the right half

        return -1  # Target not found


# Test cases
solution = Solution()

# Test case 1: Target present multiple times
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
expected1 = [3, 4]
result1 = solution.searchRange(nums1, target1)
assert (
    result1 == expected1
), f"Test case 1 failed. Expected: {expected1}, Got: {result1}"

# Test case 2: Target present once
nums2 = [5, 7, 7, 8, 8, 10]
target2 = 10
expected2 = [5, 5]
result2 = solution.searchRange(nums2, target2)
assert (
    result2 == expected2
), f"Test case 2 failed. Expected: {expected2}, Got: {result2}"

# Test case 3: Target not present
nums3 = [5, 7, 7, 8, 8, 10]
target3 = 6
expected3 = [-1, -1]
result3 = solution.searchRange(nums3, target3)
assert (
    result3 == expected3
), f"Test case 3 failed. Expected: {expected3}, Got: {result3}"


# Test case 4: Empty array
nums4 = []
target4 = 0
expected4 = [-1, -1]
result4 = solution.searchRange(nums4, target4)
assert (
    result4 == expected4
), f"Test case 4 failed. Expected: {expected4}, Got: {result4}"

# Test case 5: Array with one element - target present
nums5 = [1]
target5 = 1
expected5 = [0, 0]
result5 = solution.searchRange(nums5, target5)
assert (
    result5 == expected5
), f"Test case 5 failed. Expected: {expected5}, Got: {result5}"


# Test case 6: Array with one element - target not present
nums6 = [1]
target6 = 2
expected6 = [-1, -1]
result6 = solution.searchRange(nums6, target6)
assert (
    result6 == expected6
), f"Test case 6 failed. Expected: {expected6}, Got: {result6}"

print("All test cases passed!")  # This will only print if all assertions pass
