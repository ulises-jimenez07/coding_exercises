"""Module to find the cheapest flight within K stops."""

import heapq
import unittest
from collections import defaultdict
from typing import (
    Dict,
    List,
    Tuple,
)


class Solution:
    """Solves the cheapest flights with K stops problem using Dijkstra's algorithm."""

    # pylint: disable=too-many-arguments,too-many-positional-arguments,unused-argument
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Finds the cheapest flight price from src to dst with at most k stops."""
        # Build adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))

        # Priority queue stores tuples of (cost, current_city, stops_made)
        heap = [(0, src, 0)]
        # Track the minimum cost found to reach a city with a specific number of stops
        best: Dict[Tuple[int, int], int] = {}

        while heap:
            cost, city, stops = heapq.heappop(heap)

            # Since we use a min-heap, the first time we reach dst, it's the cheapest valid price
            if city == dst:
                return cost

            # Skip if we exceed the allowed number of stops
            if stops > k:
                continue

            # Skip if we already reached this city with the same or fewer stops at a cheaper cost
            if (city, stops) in best and best[(city, stops)] <= cost:
                continue

            best[(city, stops)] = cost

            # Explore neighbors and push to the min-heap
            for neighbor, price in graph[city]:
                new_cost = cost + price
                heapq.heappush(heap, (new_cost, neighbor, stops + 1))

        return -1


class TestSolution(unittest.TestCase):
    """Unit tests for the cheapest flights with K stops solution."""

    def setUp(self) -> None:
        self.solution = Solution()

    def test_leetcode_example_1(self) -> None:
        """Test with first LeetCode example case."""
        n = 4
        flights = [
            [0, 1, 100],
            [1, 2, 100],
            [2, 0, 500],
            [1, 3, 600],
            [2, 3, 200],
        ]
        src = 0
        dst = 3
        k = 1
        # Cheapest path is 0 -> 1 -> 3 with cost 100 + 600 = 700 (1 stop)
        self.assertEqual(self.solution.findCheapestPrice(n, flights, src, dst, k), 700)

    def test_leetcode_example_2(self) -> None:
        """Test with second LeetCode example case."""
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        # Cheapest path is 0 -> 1 -> 2 with cost 100 + 100 = 200 (1 stop)
        self.assertEqual(self.solution.findCheapestPrice(n, flights, src, dst, k), 200)

    def test_leetcode_example_3(self) -> None:
        """Test with third LeetCode example case (0 stops allowed)."""
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        # With 0 stops, we must take the direct flight 0 -> 2 with cost 500
        self.assertEqual(self.solution.findCheapestPrice(n, flights, src, dst, k), 500)

    def test_unreachable_destination(self) -> None:
        """Test when the destination is completely unreachable."""
        n = 3
        flights = [[0, 1, 100]]
        src = 0
        dst = 2
        k = 1
        self.assertEqual(self.solution.findCheapestPrice(n, flights, src, dst, k), -1)

    def test_empty_flights(self) -> None:
        """Test with no flights available."""
        n = 2
        flights: List[List[int]] = []
        src = 0
        dst = 1
        k = 0
        self.assertEqual(self.solution.findCheapestPrice(n, flights, src, dst, k), -1)

    def test_source_is_destination(self) -> None:
        """Test when source is the same as the destination."""
        n = 2
        flights = [[0, 1, 100]]
        src = 0
        dst = 0
        k = 0
        self.assertEqual(self.solution.findCheapestPrice(n, flights, src, dst, k), 0)


if __name__ == "__main__":
    unittest.main()
