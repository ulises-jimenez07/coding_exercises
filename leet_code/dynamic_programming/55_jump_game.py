"""
Problem: Determine if you can reach the last index by jumping.

Approach:
- Greedy algorithm tracking max reachable position
- For each position, update max reachable from that position
- Only visit positions that are reachable
- If max_reachable covers last index, return True
- Time complexity: O(n) single pass
- Space complexity: O(1) constant space

Example: [2,3,1,1,4] -> can jump to end, [3,2,1,0,4] -> blocked at index 3
"""

import unittest
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = nums[0]
        i = 1

        # Visit positions while they are reachable
        while i < len(nums) and max_reachable >= i:
            # Update max reachable from current position
            max_reachable = max(max_reachable, i + nums[i])
            i += 1

        return max_reachable >= len(nums) - 1


class TestCanJump(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_reach_end(self):
        """Tests a case where the end is reachable."""
        self.assertTrue(self.solution.canJump([2, 3, 1, 1, 4]))

    def test_cannot_reach_end(self):
        """Tests a case where the end is not reachable."""
        self.assertFalse(self.solution.canJump([3, 2, 1, 0, 4]))

    def test_single_element_array(self):
        """Tests a single-element array, which should always be reachable."""
        self.assertTrue(self.solution.canJump([0]))

    def test_large_jumps(self):
        """
        Tests a case with large jumps.
        """
        self.assertTrue(self.solution.canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))

    def test_zero_in_middle_blocking(self):
        """
        Tests a case where a zero blocks the path.
        """
        self.assertTrue(self.solution.canJump([1, 2, 0, 1]))

    def test_zero_at_start(self):
        """
        Tests a case where the starting position is 0.
        """
        self.assertFalse(self.solution.canJump([0, 1]))


if __name__ == "__main__":
    unittest.main()
