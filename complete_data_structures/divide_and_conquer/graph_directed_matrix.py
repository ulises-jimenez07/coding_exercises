class Graph:
    def __init__(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes
        self.graph = [[0 for x in range(number_of_nodes)] for y in range(number_of_nodes)]

    def with_in_bounds(self, v1, v2):
        return v1 >= 0 and v1 < self.number_of_nodes and v2 >= 0 and v2 < self.number_of_nodes

    def print_graph(self):
        for i in range(self.number_of_nodes):
            for j in range(self.number_of_nodes):
                if self.graph[i][j]:
                    print(i, "->", j)

    def add_edge(self, v1, v2):
        if self.with_in_bounds(v1, v2):
            self.graph[v1][v2] = 1


g = Graph(5)

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(4, 5)

g.print_graph()
