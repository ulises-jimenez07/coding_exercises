import unittest


def isSubsetSum(set, n, sum):
    """
    Checks if there is a subset of the given set with sum equal to the given sum.

    Args:
        set: A list of integers representing the set.
        n: The number of elements in the set.
        sum: The target sum.

    Returns:
        True if there is a subset with the given sum, False otherwise.
    """

    # Create a 2D table to store results of subproblems
    # subset[i][j] will be True if there is a subset of set[0...i-1] with sum equal to j
    subset = [[False for _ in range(sum + 1)] for _ in range(n + 1)]

    # If sum is 0, then there is always an empty subset with sum 0
    for i in range(n + 1):
        subset[i][0] = True

    # If set is empty and sum is not 0, then there is no subset with the given sum
    for i in range(1, sum + 1):
        subset[0][i] = False

    # Fill the subset table in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            # If current element is greater than the current sum, exclude it
            if j < set[i - 1]:
                subset[i][j] = subset[i - 1][j]
            # Otherwise, include or exclude the current element
            else:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - set[i - 1]]

    # Return the result for the entire set and target sum
    return subset[n][sum]


class TestIsSubsetSum(unittest.TestCase):
    def test_empty_set(self):
        self.assertTrue(isSubsetSum([], 0, 0))
        self.assertFalse(isSubsetSum([], 0, 5))

    def test_positive_elements(self):
        self.assertTrue(isSubsetSum([1, 2, 3], 3, 3))
        self.assertTrue(isSubsetSum([1, 2, 3], 3, 5))
        self.assertFalse(isSubsetSum([1, 2, 3], 3, 7))

    def test_zero_sum(self):
        self.assertTrue(isSubsetSum([1, 2, 3], 3, 0))

    def test_duplicate_elements(self):
        self.assertTrue(isSubsetSum([2, 2, 3], 3, 4))

    def test_large_set(self):  # Added test case for a larger set and sum
        self.assertTrue(isSubsetSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 55))
        self.assertFalse(
            isSubsetSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 60)
        )  # Added test case for a slightly larger sum that cannot be reached


if __name__ == "__main__":
    unittest.main()
