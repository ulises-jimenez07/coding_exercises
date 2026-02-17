"""
Problem: Find shortest paths from source to all nodes (non-negative weights only).

Approach:
- Use min-heap to greedily select closest unvisited node
- Relax edges to update shortest distances
- Time complexity: O((V + E) log V)
- Space complexity: O(V) for heap and distance tracking
"""

import heapq
import math
from collections import defaultdict
from typing import List


class Graph:
    """
    Represents a graph and implements Dijkstra's algorithm.
    """

    def __init__(self, n, directed):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.adj[u].append((w, v))
        if not self.directed:
            self.adj[v].append(u)

    def print_graph(self):
        print(self.adj)

    def dijsktra(self, source):
        heap = []
        distance = {i: math.inf for i in range(self.n)}

        heapq.heappush(heap, (0, source))

        while heap:
            top = heapq.heappop(heap)

            node = top[1]
            dis = top[0]

            if dis <= distance[node]:
                distance[node] = dis
                for nei in self.adj[node]:
                    nei_node = nei[1]
                    nei_weight = nei[0]
                    if distance[node] + nei_weight < distance[nei_node]:
                        distance[nei_node] = distance[node] + nei_weight
                        heapq.heappush(heap, (distance[nei_node], nei_node))

        return distance


def shortest_path(n: int, edges: List[List[int]], start: int) -> List[int]:
    """
    Alternative implementation of Dijkstra's algorithm.
    """
    graph = defaultdict(list)
    distances = [math.inf] * n
    distances[start] = 0

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    min_heap = [(0, start)]

    while min_heap:
        curr_dist, curr_node = heapq.heappop(min_heap)

        if curr_dist > distances[curr_node]:
            continue

        for neigbor, weight in graph[curr_node]:
            neigbor_dist = curr_dist + weight

            if neigbor_dist < distances[neigbor]:
                distances[neigbor] = neigbor_dist
                heapq.heappush(min_heap, (neigbor_dist, neigbor))

    return [-1 if dist == math.inf else int(dist) for dist in distances]


if __name__ == "__main__":
    # Test Graph class
    print("Testing Graph class (directed):")
    graph = Graph(5, True)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 3, 10)
    graph.add_edge(1, 2, 11)
    graph.add_edge(1, 4, 4)
    graph.add_edge(2, 4, 9)
    graph.add_edge(3, 2, 2)

    distance = graph.dijsktra(0)
    print(distance)

    # Test shortest_path function (undirected as per implementation)
    print("\nTesting shortest_path function (undirected):")
    edges = [[0, 1, 5], [0, 3, 10], [1, 2, 11], [1, 4, 4], [2, 4, 9], [3, 2, 2]]
    print(shortest_path(5, edges, 0))
