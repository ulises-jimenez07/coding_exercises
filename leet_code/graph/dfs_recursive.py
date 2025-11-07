"""
Problem: Implement recursive Depth-First Search (DFS) graph traversal.

Approach:
- Use recursion to visit nodes deeply before backtracking
- Track visited nodes to avoid cycles
- Time complexity: O(V + E)
- Space complexity: O(V) for recursion stack and visited set
"""


class Graph:
    """
    Represents a graph and implements recursive Depth-First Search (DFS).
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

    def dfs_core(self, source, visited):
        if not visited[source]:
            visited[source] = True
            print(source)
            for nei in self.adj[source]:
                if not visited[nei]:
                    self.dfs_core(nei, visited)

    def dfs(self):
        visited = {i: False for i in range(self.n)}
        for i in range(self.n):
            if not visited[i]:
                self.dfs_core(i, visited)


if __name__ == "__main__":
    graph = Graph(6, False)

    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)
    graph.add_edge(0, 4)

    graph.dfs()
