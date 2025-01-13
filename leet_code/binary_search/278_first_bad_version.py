# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Mock isBadVersion function for local testing.  In a real LeetCode
# environment, this function would be provided and you would not
# need to implement it.  Adjust bad_version for different test scenarios.
bad_version = 0  # Example: first bad version


def isBadVersion(version: int) -> bool:
    return version >= bad_version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Finds the first bad version in a sequence of versions.

        Uses a binary search approach to efficiently find the first version that is considered "bad".
        The isBadVersion API is used to check if a given version is bad.

        Args:
            n: The total number of versions.

        Returns:
            The index of the first bad version.
        """
        left = 1  # Initialize left pointer to the first version.
        right = n  # Initialize right pointer to the last version.

        while left < right:  # Continue searching while left < right
            mid = (right + left) // 2  # Calculate midpoint using integer division

            if isBadVersion(
                mid
            ):  # If the middle version is bad, the first bad version could be mid or before.
                right = mid  # Narrow search to the left half, including mid.
            else:  # If the middle version is good, the first bad version is after mid.
                left = mid + 1  # Narrow search to the right half, excluding mid.

        return left  # Return the left pointer, which represents the first bad version.


# Test cases (using the mock isBadVersion)
solution = Solution()

# Test case 1: First version is bad
bad_version = 1
n1 = 5
expected1 = 1
result1 = solution.firstBadVersion(n1)
assert (
    result1 == expected1
), f"Test case 1 failed. Expected: {expected1}, Got: {result1}"


# Test case 2: Last version is bad
bad_version = 5
n2 = 5
expected2 = 5
result2 = solution.firstBadVersion(n2)
assert (
    result2 == expected2
), f"Test case 2 failed. Expected: {expected2}, Got: {result2}"

# Test case 3: Middle version is bad
bad_version = 3
n3 = 5
expected3 = 3
result3 = solution.firstBadVersion(n3)
assert (
    result3 == expected3
), f"Test case 3 failed. Expected: {expected3}, Got: {result3}"

# Test case 4: No bad versions
bad_version = 6  # Set a bad_version outside range 1-5
n4 = 5
expected4 = 5
result4 = solution.firstBadVersion(n4)
assert (
    result4 == expected4
), f"Test case 4 failed. Expected: {expected4}, Got: {result4}"


# Test case 5: Single version
bad_version = 1
n5 = 1
expected5 = 1
result5 = solution.firstBadVersion(n5)
assert (
    result5 == expected5
), f"Test case 5 failed. Expected: {expected5}, Got: {result5}"


print("All test cases passed!")
