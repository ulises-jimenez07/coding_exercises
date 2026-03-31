"""
Problem: 815. Bus Routes (Hard)

You are given an array `routes` representing bus routes where `routes[i]` is a bus route that the i-th bus repeats forever.
For example, if `routes[0] = [1, 5, 7]`, this means that the 0-th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop `source` (you are not on any bus initially), and you want to go to the bus stop `target`.
You can travel between bus stops by buses only.
Return the least number of buses you must take to travel from `source` to `target`. If it is not possible to take any bus to go from `source` to `target`, return -1.

Approach:
- This is a BFS problem.
- Instead of BFS on stops, we do BFS on bus routes.
- A "node" in our BFS is a bus route.
- Two routes are connected if they share at least one stop.
- Time complexity: O(Sum of routes[i].length + N^2) where N is number of routes.
- Space complexity: O(Sum of routes[i].length + N^2).
"""

import unittest
from collections import (
    defaultdict,
    deque,
)
from typing import List


class Solution:
    """
    Solution for Bus Routes problem.
    """

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Map each stop to the list of bus routes that pass through it
        stop_to_routes = defaultdict(list)
        for route_idx, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(route_idx)

        if source not in stop_to_routes or target not in stop_to_routes:
            return -1

        # BFS
        # Queue stores (bus_route_idx, number_of_buses_taken)
        queue: deque[tuple[int, int]] = deque()
        visited_routes = set()
        visited_stops = {source}

        # Initialize BFS with all routes that pass through the source stop
        for route_idx in stop_to_routes[source]:
            queue.append((route_idx, 1))
            visited_routes.add(route_idx)

        while queue:
            route_idx, num_buses = queue.popleft()

            # Check all stops in the current route
            for stop in routes[route_idx]:
                if stop == target:
                    return num_buses

                if stop not in visited_stops:
                    visited_stops.add(stop)
                    # For each unvisited stop, check other bus routes passing through it
                    for next_route_idx in stop_to_routes[stop]:
                        if next_route_idx not in visited_routes:
                            visited_routes.add(next_route_idx)
                            queue.append((next_route_idx, num_buses + 1))

        return -1


class TestBusRoutes(unittest.TestCase):
    """
    Unit tests for Bus Routes.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        routes = [[1, 2, 7], [3, 6, 7]]
        source = 1
        target = 6
        self.assertEqual(self.solution.numBusesToDestination(routes, source, target), 2)

    def test_example_2(self):
        routes = [[7, 12], [4, 5, 15], [6, 1], [15, 19], [9, 12, 13]]
        source = 15
        target = 12
        self.assertEqual(self.solution.numBusesToDestination(routes, source, target), -1)

    def test_same_source_target(self):
        routes = [[1, 2, 7], [3, 6, 7]]
        source = 1
        target = 1
        self.assertEqual(self.solution.numBusesToDestination(routes, source, target), 0)


if __name__ == "__main__":
    unittest.main()
