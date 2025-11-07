"""
Problem: Represent a graph using adjacency list data structure.

Approach:
- Store graph as array of lists where each index represents a node
- Each list contains neighboring nodes
- Time complexity: O(1) for add_edge, O(degree) for neighbor lookup
- Space complexity: O(V + E)
"""


class Graph:
    """
    Represents a graph using an adjacency list.
    """

    def __init__(self, n, directed):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def print_graph(self):
        print(self.adj)


if __name__ == "__main__":
    graph = Graph(4, False)
    graph.add_edge(0, 1)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)

    graph.print_graph()
