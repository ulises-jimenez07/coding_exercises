"""
Problem: Find minimum time for signal to reach all nodes in a network (shortest path).

Approach:
- Use Dijkstra's algorithm with min-heap for shortest paths
- Track shortest distances and return max distance if all nodes are reached
- Time complexity: O((V + E) log V)
- Space complexity: O(V + E) for graph and heap
"""

import collections
import heapq
import unittest


class Solution:
    """
    Solves the Network Delay Time problem using Dijkstra's algorithm.
    """

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Calculates the minimum time for all nodes to receive the signal.
        """
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((w, v))

        distances = {i: float("inf") for i in range(1, n + 1)}
        distances[k] = 0
        heap = [(0, k)]

        while heap:
            curr_dist, curr_node = heapq.heappop(heap)

            # Skip processing if a shorter path to this node has already been processed
            if curr_dist > distances[curr_node]:
                continue

            for direct_distance, neighbor in graph[curr_node]:
                new_dist = curr_dist + direct_distance

                # If a shorter path to the neighbor is found, update distance and push to heap
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        # Check if all nodes were reached
        max_dist = max(distances.values())
        return int(max_dist) if max_dist != float("inf") else -1


class TestNetworkDelayTime(unittest.TestCase):
    """
    Unit tests for the Solution.networkDelayTime method.
    """

    def setUp(self):
        self.sol = Solution()

    def test_network_delay_time_1(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        expected = 2
        self.assertEqual(self.sol.networkDelayTime(times, n, k), expected)

    def test_network_delay_time_2(self):
        times = [[1, 2, 1]]
        n = 2
        k = 1
        expected = 1
        self.assertEqual(self.sol.networkDelayTime(times, n, k), expected)

    def test_network_delay_time_3(self):
        times = [[1, 2, 1]]
        n = 2
        k = 2
        expected = -1
        self.assertEqual(self.sol.networkDelayTime(times, n, k), expected)

    def test_network_delay_time_4(self):
        times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
        n = 3
        k = 1
        expected = 3
        self.assertEqual(self.sol.networkDelayTime(times, n, k), expected)


if __name__ == "__main__":
    unittest.main()
