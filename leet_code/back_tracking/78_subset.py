def subsets(nums):
    """
    Generates all possible subsets (power set) of a given list of numbers.

    Args:
        nums: A list of integers.

    Returns:
        A list of lists, where each inner list represents a subset of nums.
    """

    def _subsets(nums, ans, curr, index):
        """
        Recursive helper function to generate subsets.

        Args:
            nums: The input list of numbers.
            ans: The list to store the generated subsets.
            curr: The current subset being built.
            index: The index of the next element to consider.
        """

        # Base case: If the index is beyond the bounds of nums, add the current subset
        # to the answer list.  We use a copy (curr[:]) to avoid modifications affecting
        # already added subsets.
        if index > len(nums):
            return

        # Add the current subset to the answer.
        ans.append(curr[:])

        # Iterate through the remaining elements from the current index.
        for i in range(index, len(nums)):
            # Include the current element in the subset.
            curr.append(nums[i])

            # Recursively call _subsets to generate subsets including the current element.
            _subsets(nums, ans, curr, i + 1)  # Increment index to avoid duplicates

            # Backtrack: Remove the current element to explore subsets without it. This is crucial
            # for generating all possible combinations.
            curr.pop()
        return

    # Initialize the answer list and the current subset.
    ans = []
    curr = []

    # Call the recursive helper function starting from index 0.
    _subsets(nums, ans, curr, 0)
    return ans


# Test cases
print(
    subsets([1, 2, 3])
)  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(subsets([]))  # Output: [[]]
print(subsets([1]))  # Output: [[], [1]]
print(subsets([1, 2]))  # Output: [[], [1], [1, 2], [2]]
