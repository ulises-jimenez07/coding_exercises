"""This module implements Dijkstra's algorithm."""

import heapq


class Edge:
    """Represents an edge in a graph with a weight and connected vertices."""

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:
    """Represents a node (vertex) in a graph for Dijkstra's algorithm."""

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

    def add_edge(self, weight, destination_vertex):
        """Adds an edge from this node to a destination node."""
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)


class Dijkstra:
    """Implements Dijkstra's algorithm for finding the shortest paths in a graph."""

    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        """Calculates the shortest paths from a starting vertex to all other vertices."""
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.predecessor = start
                    target.min_distance = new_distance
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True

    def get_shortest_path(self, vertex):
        """Prints the shortest path to a given vertex."""
        print(f"The shortest path to the vertex is: {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor


node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")
node_h = Node("H")

node_a.add_edge(6, node_b)
node_a.add_edge(10, node_c)
node_a.add_edge(69, node_d)

node_b.add_edge(5, node_d)
node_b.add_edge(16, node_e)
node_b.add_edge(13, node_f)

node_c.add_edge(6, node_d)
node_c.add_edge(5, node_h)
node_c.add_edge(21, node_g)

node_d.add_edge(8, node_f)
node_d.add_edge(7, node_h)

node_e.add_edge(10, node_g)

node_f.add_edge(4, node_e)
node_f.add_edge(12, node_g)

node_h.add_edge(2, node_f)
node_h.add_edge(14, node_g)

algorithm = Dijkstra()
algorithm.calculate(node_a)
algorithm.get_shortest_path(node_g)
