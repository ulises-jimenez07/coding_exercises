from collections import deque

class Graph:
    def __init__(self, n, directed):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]
        
    def add_edge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def pring_graph(self):
        print(self.adj)

    def dfs_core(self, source, visited):
        stack = []
        stack.append(source)

        while stack:
            top = stack.pop()
            print(top)
            for nei in self.adj[top]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)
    def dfs(self):
        visited = { i:False for i in range(self.n) }
        for i in range(self.n):
            if not visited[i]:
                visited[i] = True
                self.dfs_core(i, visited)


graph = Graph(6, False)

graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(3,5)
graph.add_edge(4,5)
graph.add_edge(0,4)

graph.dfs()