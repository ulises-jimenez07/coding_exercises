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

    def dijsktra(self,source):
        heap = []
        distance = {i:math.inf for i in range(self.n)}

        heapq.heappush(heap, (0,source))

        while heap:
            top = heapq.heappop(heap)

            node = top[1]
            dis = top[0]

            if dis <= distance[node]:
                distance[node] = dis
                for nei in self.adj[node]:
                    nei_node = nei[1]
                    nei_weight = nei[0]
                    if distance[node] + nei_weight < distance[nei_node]:
                        distance[nei_node] = distance[node] + nei_weight
                        heapq.heappush(heap, (distance[nei_node], nei_node))

        return distance


graph = Graph(5, True)
graph.add_edge(0,1, 5)
graph.add_edge(0,3, 10)
graph.add_edge(1,2, 11)
graph.add_edge(1,4,4)
graph.add_edge(2,4, 9)
graph.add_edge(3,2, 2)

distance = graph.dijsktra(0)
print(distance)