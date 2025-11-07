"""
Problem: Maximize the minimum magnetic force between m balls placed in given positions

Approach:
- Binary search on the minimum distance between balls
- For each distance, check if we can place m balls greedily
- Time complexity: O(n log n + n log(max_dist))
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        start = 1
        end = position[-1] - position[0]
        ans = 1

        while start <= end:
            mid = (start + end) // 2
            if self.is_distance_possible(position, m, mid):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans

    def is_distance_possible(self, position: List[int], m: int, dist: int) -> bool:
        # Greedily place balls with minimum distance constraint
        no_of_balls_placed = 1
        last_position = position[0]

        for i in range(1, len(position)):
            if position[i] >= last_position + dist:
                no_of_balls_placed += 1
                last_position = position[i]

        return no_of_balls_placed >= m


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Test case from the problem description:
        positions = [1, 2, 3, 4, 7], m = 3
        Expected output: 3
        Explanation: The optimal way is to place the balls at positions [1, 4, 7].
        The minimum distance is min(4-1, 7-4) = min(3, 3) = 3.
        """
        self.assertEqual(self.solution.maxDistance([1, 2, 3, 4, 7], 3), 3)

    def test_example_2(self):
        """
        Test case from the problem description:
        positions = [5, 4, 3, 2, 1, 1000000000], m = 2
        Expected output: 999999999
        Explanation: The optimal way is to place the balls at positions 1 and 1000000000.
        The minimum distance is 1000000000 - 1 = 999999999.
        """
        self.assertEqual(self.solution.maxDistance([5, 4, 3, 2, 1, 1000000000], 2), 999999999)

    def test_two_balls(self):
        """
        Test case with only two balls.
        The maximum distance should be the difference between the first and last positions.
        """
        self.assertEqual(self.solution.maxDistance([10, 20], 2), 10)

    def test_single_position(self):
        """
        Test case with only one position.
        This case is not possible to place more than 1 ball, so the problem constraints m>=2 make it non-existent.
        However, if we assume a case where m=1 is possible, the function should return 0 or 1 depending on constraints.
        Let's assume the provided code handles this correctly within its logic.
        """
        self.assertEqual(self.solution.maxDistance([10], 1), 1)

    def test_large_number_of_positions_and_balls(self):
        """
        Test with a larger number of positions and balls to ensure efficiency.
        """
        positions = [i * 2 for i in range(100)]
        self.assertEqual(
            self.solution.maxDistance(positions, 5), 48
        )  # Placed at 0, 48, 96, 144, 192. Min distance 48.


if __name__ == "__main__":
    unittest.main()
