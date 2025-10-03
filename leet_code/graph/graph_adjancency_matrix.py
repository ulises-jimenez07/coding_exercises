class Graph:
    def __init__(self, n, directed):
        self.n = n
        self.matrix = [ [0 for _ in range(n)] for _ in range(n)]
        self.directed = directed
        
    def add_edge(self,u,v,w):
        self.matrix[u][v] = w
        if not self.directed:
            self.matrix[v][u] = w

    # def add_edge(self, u,v):
    #     self.add_edge(u,v,1)

    def print_graph(self):
        print(self.matrix)

graph = Graph(4, False)
graph.add_edge(0,1,10)
graph.add_edge(1,3,40)
graph.add_edge(2,3,30)
graph.print_graph()