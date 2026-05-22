"""
Solution to 815. Bus Routes (Hard).

Approach:
- BFS is used where each state in the queue represents a bus route (bus index)
  and the number of buses taken to reach it.
- To optimize transitions, we map each bus stop to all bus routes that pass
  through it.
- We initialize the BFS queue with all buses passing through the source stop.
- For each bus route, we check all its stops. If the target stop is found, we
  return the count of buses taken.
- Otherwise, we look at all connected buses sharing those stops and queue them if
  they haven't been visited yet.
"""

import unittest
from collections import (
    defaultdict,
    deque,
)
from typing import List


class Solution:
    """
    Solves the Bus Routes problem by finding the minimum number of buses needed.
    """

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        Calculates the minimum number of buses to travel from source to target.
        """
        # If source and target are the same, no bus rides are needed
        if target == source:
            return 0

        # Build an adjacency list mapping each stop to all bus routes passing through it
        bus_stops = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                bus_stops[stop].append(i)

        # Track visited bus routes to avoid processing the same route multiple times
        visited: set[int] = set()
        queue: deque[tuple[int, int]] = deque()

        # Start BFS with all buses that pass through the source stop
        for bus in bus_stops[source]:
            queue.append((bus, 1))
            visited.add(bus)

        # Standard BFS traversal
        while queue:
            curr_bus, num_changes = queue.popleft()

            # Inspect all stops along the current bus route
            for stop in routes[curr_bus]:
                if stop == target:
                    return num_changes

                # Find all other buses passing through the current stop
                for connected_bus in bus_stops[stop]:
                    if connected_bus not in visited:
                        queue.append((connected_bus, num_changes + 1))
                        visited.add(connected_bus)

        # Return -1 if target is unreachable
        return -1


class TestBusRoutes(unittest.TestCase):
    """
    Unit tests for checking the correctness of Solution.numBusesToDestination.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test with a simple route layout where a destination is reachable."""
        routes = [[1, 2, 7], [3, 6, 7]]
        source = 1
        target = 6
        self.assertEqual(self.solution.numBusesToDestination(routes, source, target), 2)

    def test_example_2(self):
        """Test with disconnected route layout where a destination is unreachable."""
        routes = [[7, 12], [4, 5, 15], [6, 1], [15, 19], [9, 12, 13]]
        source = 15
        target = 12
        self.assertEqual(self.solution.numBusesToDestination(routes, source, target), -1)

    def test_same_source_target(self):
        """Test when source and target are the same, should return 0."""
        routes = [[1, 2, 7], [3, 6, 7]]
        source = 1
        target = 1
        self.assertEqual(self.solution.numBusesToDestination(routes, source, target), 0)


if __name__ == "__main__":
    unittest.main()
