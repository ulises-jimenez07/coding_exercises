import unittest  # Import the unittest module
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()  # Use a set to store unique triplets
        dups = (
            set()
        )  # Use a set to keep track of processed 'target' values to avoid redundant computations
        seen = (
            {}
        )  # A dictionary to store numbers encountered in the inner loop and their 'target's index

        # Iterate through each number in the list, considering it as a potential 'target'
        for i, target in enumerate(nums):
            # If this 'target' has not been processed yet (to avoid duplicate triplets originating from the same target value)
            if target not in dups:
                dups.add(target)  # Mark this 'target' as processed

                # For each 'target', iterate through the rest of the list to find two other numbers
                # nums[i+1:] ensures we don't reuse the same element for 'target' and 'num' in the same triplet iteration
                # and also helps in finding unique combinations.
                # The original j was an index relative to nums[i+1:], which is not directly used.
                # We only care about the 'num' itself from the subarray.
                for num in nums[i + 1 :]:
                    # Calculate the complement needed to make the sum zero
                    complement = -target - num
                    # Check if this complement has been 'seen' before for the *current* 'target'
                    # 'seen[complement] == i' ensures that the complement was found
                    # in the context of the current 'target' (from a previous iteration of the inner loop for this 'target').
                    # This is crucial because 'seen' is not cleared for each 'target'.
                    if complement in seen and seen[complement] == i:
                        # If found, a triplet is formed. Sort it to ensure uniqueness regardless of order.
                        # Add the sorted tuple to the 'ans' set.
                        ans.add(tuple(sorted([target, complement, num])))
                    else:
                        # Store the current 'num' and the index 'i' of its 'target'.
                        # This means 'num' was encountered while processing 'nums[i]' (the current 'target').
                        seen[num] = i

        # Convert the set of tuples back to a list of lists
        return list(ans)


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def assertListOfListsEqual(self, list1: List[List[int]], list2: List[List[int]]):
        """Helper method to compare two lists of lists, ignoring order of inner lists and outer list."""
        self.assertEqual(len(list1), len(list2))
        # Sort each inner list, then convert to tuple to make them hashable for set comparison
        set1 = set(tuple(sorted(sublist)) for sublist in list1)
        set2 = set(tuple(sorted(sublist)) for sublist in list2)
        self.assertEqual(set1, set2)

    def test_empty_list(self):
        self.assertListOfListsEqual(self.solver.threeSum([]), [])

    def test_no_triplets(self):
        self.assertListOfListsEqual(self.solver.threeSum([1, 2, 3]), [])
        self.assertListOfListsEqual(self.solver.threeSum([0, 1, 2]), [])

    def test_simple_case(self):
        self.assertListOfListsEqual(
            self.solver.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]
        )

    def test_with_zeros(self):
        self.assertListOfListsEqual(self.solver.threeSum([0, 0, 0]), [[0, 0, 0]])
        self.assertListOfListsEqual(self.solver.threeSum([0, 0, 0, 0]), [[0, 0, 0]])

    def test_duplicates_in_input(self):
        self.assertListOfListsEqual(
            self.solver.threeSum([-1, 0, 1, 2, -1, -4, -1]), [[-1, -1, 2], [-1, 0, 1]]
        )

    def test_more_complex_case(self):
        self.assertListOfListsEqual(
            self.solver.threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]]
        )

    def test_all_negative(self):
        self.assertListOfListsEqual(self.solver.threeSum([-1, -2, -3]), [])

    def test_all_positive(self):
        self.assertListOfListsEqual(self.solver.threeSum([1, 2, 3]), [])


if __name__ == "__main__":
    unittest.main()
