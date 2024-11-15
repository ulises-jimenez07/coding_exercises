from typing import List


class Solution:
    def valid_mountain_arrar(self, A: List[int]) -> bool:
        """
        Checks if an array is a valid mountain array.

        A valid mountain array has the following properties:
        - A.length >= 3
        - There exists some i with 0 < i < A.length - 1 such that:
            - A[0] < A[1] < ... A[i-1] < A[i]
            - A[i] > A[i+1] > ... > A[A.length - 1]

        Args:
            A: The input array of integers.

        Returns:
            True if A is a valid mountain array, False otherwise.
        """

        n = len(A)
        if n < 3:  # Mountain array must have at least 3 elements
            return False

        i = 1
        # Walk up the mountain
        while i < n and A[i] > A[i - 1]:
            i += 1

        # Peak can't be the first or last element
        if i == 1 or i == n:
            return False

        # Walk down the mountain
        while i < n and A[i] < A[i - 1]:
            i += 1

        # If we traversed the entire array, it's a valid mountain
        return i == n


# Test cases
solution = Solution()

# Test case 1: Valid mountain
arr1 = [0, 3, 2, 1]
print(
    f"Test case 1: {arr1}, Expected: True, Result: {solution.valid_mountain_arrar(arr1)}"
)
assert solution.valid_mountain_arrar(arr1) == True

# Test case 2: Not a mountain (increasing)
arr2 = [0, 1, 2, 3, 4]
print(
    f"Test case 2: {arr2}, Expected: False, Result: {solution.valid_mountain_arrar(arr2)}"
)
assert solution.valid_mountain_arrar(arr2) == False

# Test case 3: Not a mountain (decreasing)
arr3 = [4, 3, 2, 1, 0]
print(
    f"Test case 3: {arr3}, Expected: False, Result: {solution.valid_mountain_arrar(arr3)}"
)
assert solution.valid_mountain_arrar(arr3) == False

# Test case 4: Valid mountain (longer)
arr4 = [0, 1, 2, 3, 4, 3, 2, 1]
print(
    f"Test case 4: {arr4}, Expected: True, Result: {solution.valid_mountain_arrar(arr4)}"
)
assert solution.valid_mountain_arrar(arr4) == True

# Test case 5: Not a mountain (plateau)
arr5 = [0, 1, 2, 3, 3, 2, 1]
print(
    f"Test case 5: {arr5}, Expected: False, Result: {solution.valid_mountain_arrar(arr5)}"
)
assert solution.valid_mountain_arrar(arr5) == False

# Test case 6: Too short
arr6 = [0, 1]
print(
    f"Test case 6: {arr6}, Expected: False, Result: {solution.valid_mountain_arrar(arr6)}"
)
assert solution.valid_mountain_arrar(arr6) == False

# Test case 7: Single element
arr7 = [1]
print(
    f"Test case 7: {arr7}, Expected: False, Result: {solution.valid_mountain_arrar(arr7)}"
)
assert solution.valid_mountain_arrar(arr7) == False
