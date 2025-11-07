"""
Problem: Detect cycles in a directed graph.

Approach:
- Use DFS with 3-state tracking (Unvisited, Visiting, Processed)
- Cycle detected when visiting node encounters another visiting node
- Time complexity: O(V + E)
- Space complexity: O(V) for state tracking and recursion stack
"""


class Graph:
    """
    Represents a graph and implements cycle detection using DFS.
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

    def dfs_core(self, source, state):
        if state[source] == "U":
            state[source] = "V"
            print(source)
            for nei in self.adj[source]:
                self.dfs_core(nei, state)
            state[source] = "P"
        elif state[source] == "V":
            print(f"Cycle detected at {source}")

    def detect_cycle(self):
        state = {i: "U" for i in range(self.n)}
        for i in range(self.n):
            if state[i] == "U":
                self.dfs_core(i, state)


if __name__ == "__main__":
    graph = Graph(4, True)

    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(0, 2)
    graph.add_edge(3, 1)
    graph.add_edge(2, 3)

    graph.detect_cycle()
