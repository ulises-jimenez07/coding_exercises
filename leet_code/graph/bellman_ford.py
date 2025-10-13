import heapq
import math
class Graph:
    def __init__(self, n, directed):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]
        
    def add_edge(self, u, v, w):
        self.adj[u].append((w,v))
        if not self.directed:
            self.adj[v].append(u)

    def pring_graph(self):
        print(self.adj)

    def bellman_ford(self, source):
        distance = {i:math.inf for i in range(self.n)}
        distance[source] = 0

        negative_cycle = False
        for i in range(self.n):
            for u in range(self.n):
                for nei in self.adj[u]:
                    w = nei[0]
                    v = nei[1]
                    if distance[v] > (distance[u] + w):
                        if i == self.n -1:
                            negative_cycle = True
                        distance[v] = distance[u] + w
        return (distance, negative_cycle)

graph = Graph(5, True)
graph.add_edge(0,1, 5)
graph.add_edge(0,3, 10)
graph.add_edge(1,2, 11)
graph.add_edge(1,4,4)
graph.add_edge(2,4, 9)
graph.add_edge(3,2, 2)

(distance, negative_cycle) = graph.bellman_ford(0)

print(distance)
print(negative_cycle)