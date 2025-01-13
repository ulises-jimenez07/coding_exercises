from collections import Counter
import unittest
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all unique permutations of a list of numbers (may contain duplicates).

        Args:
            nums: A list of integers.

        Returns:
            A list of lists, where each inner list represents a unique permutation of nums.
        """

        def _permute_unique(curr, counter):
            """
            Recursive helper function to generate unique permutations.

            Args:
                curr: The current permutation being built.
                counter: A Counter object tracking the remaining counts of each number.
            """
            if len(curr) == len(
                nums
            ):  # Base case: If the current permutation is complete
                ans.append(curr[:])  # Add a copy to avoid modification later
                return

            for num in counter:  # Iterate through the numbers in the counter
                if counter[num] > 0:  # If the number is still available
                    curr.append(num)  # Add it to the current permutation
                    counter[num] -= 1  # Decrement its count
                    _permute_unique(
                        curr, counter
                    )  # Recursively call for the next position
                    counter[num] += 1  # Backtrack: Restore the count
                    curr.pop()  # Backtrack: Remove the number from the current permutation

        ans = []  # Initialize the result list
        _permute_unique(
            [], Counter(nums)
        )  # Start the recursion with an empty permutation and the initial counts
        return ans


class TestPermuteUnique(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Solution().permuteUnique([]), [[]])

    def test_single_element(self):
        self.assertEqual(Solution().permuteUnique([1]), [[1]])

    def test_distinct_elements(self):
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(sorted(Solution().permuteUnique([1, 2, 3])), sorted(expected))

    def test_duplicate_elements(self):
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertEqual(sorted(Solution().permuteUnique([1, 1, 2])), sorted(expected))

    def test_another_duplicate_set(self):
        expected = [
            [1, 1, 2, 2],
            [1, 2, 1, 2],
            [1, 2, 2, 1],
            [2, 1, 1, 2],
            [2, 1, 2, 1],
            [2, 2, 1, 1],
        ]
        self.assertEqual(
            sorted(Solution().permuteUnique([1, 1, 2, 2])), sorted(expected)
        )


if __name__ == "__main__":
    unittest.main()
