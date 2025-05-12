import unittest
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence in an unsorted list of integers.

        The algorithm works by first converting the input list into a set for O(1) average time complexity
        for checking the existence of an element. Then, it iterates through each number in the set.
        If a number `num` is the start of a sequence (i.e., `num - 1` is not in the set),
        it then counts the length of the consecutive sequence starting from `num`.
        The maximum length found is updated and returned.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest consecutive elements sequence.
        """
        # Convert the list of numbers into a set to allow for O(1) average time complexity
        # for checking the existence of elements. This also handles duplicate numbers automatically.
        n_set = set(nums)

        # Initialize the variable to store the length of the longest consecutive sequence found so far.
        ans = 0

        # Iterate through each unique number in the input list.
        for num in n_set:
            # Check if the current number is the start of a new consecutive sequence.
            # A number is the start of a sequence if its predecessor (num - 1) is not present in the set.
            # This check is crucial for optimizing the algorithm to avoid redundant counting.
            # If we only start counting from the beginning of a sequence, each number will be part of
            # the "while" loop's check at most once.
            if (num - 1) not in n_set:
                # Initialize the current number being checked in the potential sequence.
                current = num
                # Initialize the length of the current consecutive sequence.
                current_streak = 1

                # While the next consecutive number (current + 1) is present in the set,
                # extend the current streak.
                while current + 1 in n_set:
                    current_streak += 1
                    current += 1

                # Update the longest consecutive sequence found so far if the current streak is longer.
                ans = max(current_streak, ans)

        # Return the length of the longest consecutive sequence found.
        return ans


class TestLongestConsecutive(unittest.TestCase):
    def setUp(self):
        """Set up the Solution instance for testing."""
        self.solution = Solution()

    def test_empty_list(self):
        """Test an empty list, expecting 0."""
        self.assertEqual(self.solution.longestConsecutive([]), 0)

    def test_no_consecutive_elements(self):
        """Test a list with no consecutive elements, expecting 1 (each element is a sequence of 1)."""
        self.assertEqual(self.solution.longestConsecutive([10, 20, 30, 40]), 1)

    def test_simple_consecutive_sequence(self):
        """Test a list with a simple consecutive sequence."""
        self.assertEqual(self.solution.longestConsecutive([1, 2, 3, 4, 5]), 5)

    def test_example_from_problem_statement_1(self):
        """Test the first example from common problem statements."""
        self.assertEqual(self.solution.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_example_from_problem_statement_2(self):
        """Test the second example from common problem statements."""
        self.assertEqual(self.solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_with_duplicates(self):
        """Test a list containing duplicate numbers."""
        self.assertEqual(self.solution.longestConsecutive([1, 2, 0, 1, 1, 2, 3]), 4)  # 0, 1, 2, 3

    def test_with_negative_numbers(self):
        """Test a list containing negative numbers and a consecutive sequence."""
        self.assertEqual(self.solution.longestConsecutive([-1, -2, -3, 0, 1, -4]), 6)

    def test_single_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(self.solution.longestConsecutive([5]), 1)

    def test_all_same_elements(self):
        """Test a list where all elements are the same."""
        self.assertEqual(self.solution.longestConsecutive([7, 7, 7, 7]), 1)

    def test_non_sequential_but_overlapping_potential_starts(self):
        """Test a case where numbers might seem like starts but are part of other sequences."""
        self.assertEqual(
            self.solution.longestConsecutive([9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7]), 4
        )  # -4, -3, -2, -1 or 1, 2, 3, 4

    def test_sequence_at_the_end(self):
        """Test when the longest sequence is at the end of processing order."""
        self.assertEqual(self.solution.longestConsecutive([50, 40, 30, 1, 2, 3]), 3)

    def test_sequence_at_the_beginning(self):
        """Test when the longest sequence is at the beginning of processing order."""
        self.assertEqual(self.solution.longestConsecutive([1, 2, 3, 50, 40, 30]), 3)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
