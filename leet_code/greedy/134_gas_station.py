"""
Problem: Find the starting gas station index to complete a circular circuit.

Approach:
- Greedy algorithm: if total gas >= total cost, a solution exists
- Track cumulative tank (gas - cost) as we traverse stations
- When tank goes negative, reset start to next station and tank to 0
- The last valid start after full pass is the answer
- Time complexity: O(n) single pass
- Space complexity: O(1) constant space

Example: gas=[1,2,3,4,5], cost=[3,4,5,1,2] -> start at index 3
"""

import unittest
from typing import List


class Solution:
    """
    Greedy approach: One pass with tank tracking.
    If total gas < total cost, return -1. Otherwise, track tank and reset start when tank < 0.
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # No solution if total gas cannot cover total cost
        if sum(gas) < sum(cost):
            return -1

        start = tank = 0

        for i, _ in enumerate(gas):
            tank += gas[i] - cost[i]

            # Tank went negative: cannot start from any index in [start, i]
            if tank < 0:
                start, tank = i + 1, 0

        return start


class TestCanCompleteCircuit(unittest.TestCase):
    """Unit tests for Gas Station implementations."""

    def setUp(self):
        self.solution = Solution()

    def test_can_complete_circuit(self):
        """Tests a case where the circuit can be completed from index 3."""
        self.assertEqual(
            self.solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
            3,
        )

    def test_cannot_complete_circuit(self):
        """Tests a case where total gas < total cost, no solution."""
        self.assertEqual(
            self.solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]),
            -1,
        )

    def test_single_station(self):
        """Tests a single station with enough gas."""
        self.assertEqual(self.solution.canCompleteCircuit([5], [4]), 0)

    def test_single_station_insufficient(self):
        """Tests a single station with insufficient gas."""
        self.assertEqual(self.solution.canCompleteCircuit([3], [4]), -1)

    def test_start_at_last_index(self):
        """Tests a case where the valid start is the last index."""
        self.assertEqual(
            self.solution.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]),
            4,
        )

    def test_equal_gas_cost(self):
        """Tests a case where gas equals cost at each station."""
        self.assertEqual(
            self.solution.canCompleteCircuit([1, 1, 1], [1, 1, 1]),
            0,
        )


if __name__ == "__main__":
    unittest.main()
