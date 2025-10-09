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

    def dfs_core(self, source, state):
        if state[source] == 'U':
            state[source] = 'V'
            print(source)
            for nei in self.adj[source]:
                self.dfs_core(nei, state)
            state[source] = 'P'
        elif state[source] == 'V':
            print(f"Cycle detected at {source}")

    def detect_cycle(self):
        state = { i:'U' for i in range(self.n) }
        for i in range(self.n):
            if state[i] == 'U':
                self.dfs_core(i, state)
            


graph = Graph(4, True)

graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(0,2)
graph.add_edge(3,1)
graph.add_edge(2,3)

graph.detect_cycle()