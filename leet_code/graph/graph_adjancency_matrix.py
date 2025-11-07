"""
Problem: Represent a graph using adjacency matrix data structure.

Approach:
- Store graph as 2D matrix where matrix[i][j] represents edge weight
- 0 indicates no edge between nodes
- Time complexity: O(1) for add_edge and edge lookup
- Space complexity: O(V^2)
"""


class Graph:
    """
    Represents a graph using an adjacency matrix.
    """

    def __init__(self, n, directed):
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.directed = directed

    def add_edge(self, u, v, w):
        self.matrix[u][v] = w
        if not self.directed:
            self.matrix[v][u] = w

    def print_graph(self):
        print(self.matrix)


if __name__ == "__main__":
    graph = Graph(4, False)
    graph.add_edge(0, 1, 10)
    graph.add_edge(1, 3, 40)
    graph.add_edge(2, 3, 30)
    graph.print_graph()
