class Solution(object):
    def combinationSum(self, candidates, target):
        """
        Finds all unique combinations of candidates where the candidate numbers sum to target.

        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        The same repeated number may be chosen from candidates unlimited number of times.
        Two combinations are considered unique if the frequency of at least one of the chosen numbers is different.
        """
        return self.solution(candidates, [], [], target, 0, 0)

    def solution(self, candidates, ans, curr, target, index, sum):
        """
        Recursive helper function to explore combinations.

        :param candidates: List of candidate numbers.
        :param ans: List to store the resulting combinations.
        :param curr: Current combination being built.
        :param target: Target sum.
        :param index: Index of the current candidate being considered.
        :param sum: Current sum of the combination being built.
        :return: List of combinations that sum to the target.
        """

        # Base case: If the current sum equals the target, add a copy of the current combination to the result.
        if sum == target:
            ans.append(curr[:])  # Append a copy to avoid modification later

        # Recursive case: If the current sum is less than the target, explore further combinations.
        elif sum < target:
            n = len(candidates)
            # Iterate through candidates starting from the given index.
            for i in range(index, n):
                # Add the current candidate to the combination.
                curr.append(candidates[i])
                # Recursively call the function with the updated sum and index.
                self.solution(candidates, ans, curr, target, i, sum + candidates[i])
                # Backtrack: Remove the last added candidate to explore other combinations.
                curr.pop()

        # Return the list of combinations.
        return ans


# Test cases
solution = Solution()

# Test case 1:
candidates1 = [2, 3, 6, 7]
target1 = 7
expected1 = [[2, 2, 3], [7]]
result1 = solution.combinationSum(candidates1, target1)
print(
    f"Test case 1: Expected {expected1}, got {result1}"
)  # Add print statements for easy verification
assert sorted(result1) == sorted(expected1)  # Use assertions for automated testing


# Test case 2:
candidates2 = [2, 3, 5]
target2 = 8
expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
result2 = solution.combinationSum(candidates2, target2)
print(f"Test case 2: Expected {expected2}, got {result2}")
assert sorted(result2) == sorted(expected2)

# Test case 3: Empty candidates list
candidates3 = []
target3 = 7
expected3 = []
result3 = solution.combinationSum(candidates3, target3)
print(f"Test case 3: Expected {expected3}, got {result3}")
assert sorted(result3) == sorted(expected3)


# Test case 4: Target is 0
candidates4 = [2, 3, 5]
target4 = 0
expected4 = [[]]
result4 = solution.combinationSum(candidates4, target4)
print(f"Test case 4: Expected {expected4}, got {result4}")
assert sorted(result4) == sorted(expected4)
