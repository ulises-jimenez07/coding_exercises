from typing import List
import unittest


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of a list of distinct numbers.

        Args:
            nums: A list of distinct integers.

        Returns:
            A list of lists, where each inner list represents a permutation of nums.
        """

        def _permute(curr):
            """
            Recursive helper function to generate permutations.

            Args:
                curr: The current permutation being built.
            """
            if len(curr) == len(nums):  # Base case: Permutation is complete
                ans.append(curr[:])  # Add a copy to avoid modification
                return

            for num in nums:
                if num not in curr:  # Check if the number is already used
                    curr.append(num)  # Add the number to the permutation
                    _permute(curr)  # Recursively call for the next position
                    curr.pop()  # Backtrack: Remove the number for other permutations

        ans = []  # Initialize the result list
        _permute([])  # Start the recursion with an empty list
        return ans


class TestPermute(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Solution().permute([]), [[]])

    def test_single_element(self):
        self.assertEqual(Solution().permute([1]), [[1]])

    def test_multiple_elements(self):
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(sorted(Solution().permute([1, 2, 3])), sorted(expected))


if __name__ == "__main__":
    unittest.main()
