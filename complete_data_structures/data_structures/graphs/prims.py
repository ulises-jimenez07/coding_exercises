"""This module implements Prim's algorithm for finding the Minimum Spanning Tree."""

import sys


class Graph:
    """Represents a graph for Prim's algorithm."""

    def __init__(self, num_vertices, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.num_vertices = num_vertices
        self.mst = []

    def print_solution(self):
        """Prints the Minimum Spanning Tree (MST) edges and their weights."""
        print("Edge : Weight")
        for s, d, w in self.mst:
            print("%s -> %s: %s" % (s, d, w))

    def _find_min_edge(self, visited):
        min_weight = sys.maxsize
        s, d = 0, 0
        for i in range(self.num_vertices):
            if visited[i]:
                for j in range(self.num_vertices):
                    if (not visited[j]) and self.edges[i][j]:
                        if min_weight > self.edges[i][j]:
                            min_weight = self.edges[i][j]
                            s = i
                            d = j
        return s, d, min_weight

    def prims_algo(self):
        """Implements Prim's algorithm to find the Minimum Spanning Tree."""
        visited = [0] * self.num_vertices
        edge_count = 0
        visited[0] = True
        while edge_count < self.num_vertices - 1:
            s, d, _min_weight = self._find_min_edge(visited)
            self.mst.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edge_count += 1
        self.print_solution()


edges = [
    [0, 10, 20, 0, 0],
    [10, 0, 30, 5, 0],
    [20, 30, 0, 15, 6],
    [0, 5, 15, 0, 8],
    [0, 0, 6, 8, 0],
]
nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.prims_algo()
