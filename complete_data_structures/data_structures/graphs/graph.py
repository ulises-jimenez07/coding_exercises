"""This module implements a Graph data structure using an adjacency list."""

from collections import deque


class Graph:
    """Represents an undirected graph using an adjacency list."""

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Adds a new vertex to the graph."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        """Prints the adjacency list representation of the graph."""
        for vertex, neighbors in self.adjacency_list.items():
            print(vertex, ":", neighbors)

    def add_edge(self, vertex1, vertex2):
        """Adds an undirected edge between two vertices."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        """Removes an edge between two vertices."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        """Removes a vertex and all its incident edges from the graph."""
        if vertex in self.adjacency_list:
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    # time complexity O(V+E)
    # Space complexity O(v)
    def bfs(self, vertex):
        """Performs a Breadth-First Search (BFS) starting from a given vertex."""
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

    # time complexity O(V+E)
    # Space complexity O(v)
    def dfs(self, vertex):
        """Performs a Depth-First Search (DFS) starting from a given vertex (iterative)."""
        visited = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)

    def dfs_recursive(self, vertex, visited):
        """Performs a Depth-First Search (DFS) starting from a given vertex (recursive)."""
        visited.add(vertex)
        print(vertex, end=" ")

        for adjacent_vertex in self.adjacency_list[vertex]:
            if adjacent_vertex not in visited:
                self.dfs_recursive(adjacent_vertex, visited)


custom_graph = Graph()

custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_vertex("D")
custom_graph.add_vertex("E")
custom_graph.add_edge("A", "B")
custom_graph.add_edge("A", "C")
custom_graph.add_edge("B", "E")
custom_graph.add_edge("C", "D")
custom_graph.add_edge("D", "E")

custom_graph.print_graph()

custom_graph.dfs("A")
