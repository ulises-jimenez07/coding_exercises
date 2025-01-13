import collections
import heapq
import unittest


class Solution:
    # Dijkstra's algorithm to find the shortest path from a source node to all other nodes in a weighted graph.
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build the graph as an adjacency list: {u: [(cost, v), ...]}
        g = collections.defaultdict(list)

        for u, v, cost in times:
            g[u].append((cost, v))

        # Initialize min-heap with starting node and its distance (0)
        min_heap = [(0, k)]

        # Keep track of visited nodes
        visited = set()

        # Initialize distances to infinity for all nodes
        distance = {i: float("inf") for i in range(1, n + 1)}
        distance[k] = 0

        # Iterate while the heap is not empty
        while min_heap:
            # Get the node with the smallest distance from the heap
            cur_dist, u = heapq.heappop(min_heap)

            # If node is already visited, skip
            if u in visited:
                continue

            # Mark current node as visited
            visited.add(u)

            # If all nodes are visited, return the current distance (max distance)
            if len(visited) == n:
                return cur_dist

            # Iterate over neighbors of current node
            for direct_distance, v in g[u]:
                # Relax the edge: update the distance to neighbor if a shorter path is found
                if cur_dist + direct_distance < distance[v] and v not in visited:
                    distance[v] = cur_dist + direct_distance

                    # Add the neighbor to the heap with updated distance
                    heapq.heappush(min_heap, (cur_dist + direct_distance, v))

        # If not all nodes are reachable, return -1
        return -1


class TestNetworkDelayTime(unittest.TestCase):
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
