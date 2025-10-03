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

graph = Graph(4, False)
graph.add_edge(0,1)
graph.add_edge(1,3)
graph.add_edge(2,3)

graph.pring_graph()