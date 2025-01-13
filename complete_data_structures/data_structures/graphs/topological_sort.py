from collections import defaultdict


class Graph:
    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topological_sort_util(self, vertex, visited, stack):
        visited.append(vertex)

        for i in self.graph[vertex]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, vertex)

    def topological_sort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_util(k, visited, stack)

        print(stack)


customGraph = Graph(8)
customGraph.add_edge("A", "C")
customGraph.add_edge("C", "E")
customGraph.add_edge("E", "H")
customGraph.add_edge("E", "F")
customGraph.add_edge("F", "G")
customGraph.add_edge("B", "D")
customGraph.add_edge("B", "C")
customGraph.add_edge("D", "F")

customGraph.topological_sort()
