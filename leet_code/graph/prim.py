import heapq

class Graph:
    def __init__(self, n, directed):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.adj[u].append((w, v))
        if not self.directed:
            self.adj[v].append((w, u)) # Corrected: u is the other node

    def print_graph(self): # Corrected: pring -> print
        print(self.adj)

    def prim(self, source):
        heap = []
        visited = {i: False for i in range(self.n)}
        mst_cost = 0
        nodes_in_mst = 0
        
        # Push the first edge into the heap. Since it's the start, cost is 0.
        heapq.heappush(heap, (0, source))

        while heap and nodes_in_mst < self.n:
            cost, node = heapq.heappop(heap)

            if visited[node]:
                continue
            
            mst_cost += cost
            visited[node] = True
            nodes_in_mst += 1

            for neighbor_cost, neighbor_node in self.adj[node]:
                if not visited[neighbor_node]:
                    heapq.heappush(heap, (neighbor_cost, neighbor_node))
        
        # Check if the graph is connected. If not, the MST won't include all nodes.
        if nodes_in_mst == self.n:
            return mst_cost
        else:
            return float('inf') # Or handle as an error, e.g., print a message
            
graph = Graph(5, False)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 3, 10)
graph.add_edge(1, 2, 11)
graph.add_edge(1, 4, 4)
graph.add_edge(2, 4, 9)
graph.add_edge(3, 2, 2)

mst = graph.prim(0)
print(mst) # Output will be 20