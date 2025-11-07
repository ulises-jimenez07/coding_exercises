"""This module implements Single Source Shortest Path (SSSP) using BFS."""


class Graph:
    """Represents a graph for Single Source Shortest Path (SSSP) problems."""

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        """Performs a Breadth-First Search (BFS) to find the shortest path between two nodes."""
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return None


custom_dict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"],
}

g = Graph(custom_dict)
print(g.bfs("a", "e"))
