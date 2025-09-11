import unittest
from typing import List


class Solution:
    """
    A class to solve the "Jump Game" problem.
    """

    def canJump(self, nums: List[int]) -> bool:
        """
        Determines if the last index can be reached from the first index
        by performing jumps.

        Args:
            nums: A list of non-negative integers where each element represents
                  the maximum jump length from that position.

        Returns:
            True if the last index can be reached, False otherwise.
        """
        # max_reachable tracks the maximum index that can be reached
        # from the current position.
        max_reachable = nums[0]
        i = 1

        # Iterate through the array as long as the current index 'i' is within
        # the array bounds and is reachable.
        while i < len(nums) and max_reachable >= i:
            # Update max_reachable if a further jump is possible from the current position.
            if (i + nums[i]) > max_reachable:
                max_reachable = i + nums[i]
            i += 1

        # Check if the maximum reachable index is at or beyond the last index.
        if max_reachable >= len(nums) - 1:
            return True
        return False


# -----------------------------------------------------------------------------
## Unit Tests


class TestCanJump(unittest.TestCase):
    """
    Unit tests for the canJump method of the Solution class.
    """

    def test_can_reach_end(self):
        """
        Tests a case where the end is reachable.
        """
        self.assertTrue(Solution().canJump([2, 3, 1, 1, 4]))

    def test_cannot_reach_end(self):
        """
        Tests a case where the end is not reachable.
        """
        self.assertFalse(Solution().canJump([3, 2, 1, 0, 4]))

    def test_single_element_array(self):
        """
        Tests a single-element array, which should always be reachable.
        """
        self.assertTrue(Solution().canJump([0]))

    def test_large_jumps(self):
        """
        Tests a case with large jumps.
        """
        self.assertTrue(Solution().canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))

    def test_zero_in_middle_blocking(self):
        """
        Tests a case where a zero blocks the path.
        """
        self.assertTrue(Solution().canJump([1, 2, 0, 1]))

    def test_zero_at_start(self):
        """
        Tests a case where the starting position is 0.
        """
        self.assertFalse(Solution().canJump([0, 1]))


if __name__ == "__main__":
    unittest.main()
