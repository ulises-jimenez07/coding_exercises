"""This module implements a Disjoint Set (Union-Find) data structure."""

# disjoint


class DisjointSet:
    """Implements a Disjoint Set (Union-Find) data structure."""

    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        """Finds the representative (root) of the set containing the item."""
        if self.parent[item] == item:
            return item
        return self.find(self.parent[item])

    def union(self, x, y):
        """Unites the sets containing x and y."""
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
