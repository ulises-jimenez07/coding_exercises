"""
Problem: Find the minimum number of operations (moving cables) required to connect
         all 'n' computers in a network, given a list of existing connections.

Approach:
- Use the Union-Find (Disjoint Set) data structure to count the number of separate
  connected components (sub-networks).
- A network with 'k' separate components requires at least 'k - 1' additional
  connections (edges) to become fully connected.
- The total number of available cables (edges) in excess of what's needed to form
  the existing components is the pool of cables we can "move."
    - A successful union operation (merging two components) uses one cable to reduce
      the component count by one.
    - If a union operation attempts to connect two already connected computers, that
      cable is considered 'redundant' and available for moving.
- Logic:
    1. **Pre-check:** A fully connected network of 'n' nodes requires at least
       'n - 1' connections. If the total number of given connections is less than 'n - 1',
       it is impossible to connect the network, so return -1.
    2. **Count Components:** Iterate through all given connections, performing a
       `uf.union` operation for each. The final value of `uf.count` is the number
       of separate sub-networks ($k$).
    3. **Calculate Operations:** The minimum number of new connections needed is
       $k - 1$. Since any existing redundant cables can be used as these new connections,
       and the pre-check guarantees we have enough total cables (`len(connections) >= n - 1`),
       the answer is simply $k - 1$.
- Time complexity: O(E * α(N)) where E is the number of connections and N is the
  number of computers, and α is the inverse Ackermann function (nearly constant).
- Space complexity: O(N) for the UnionFind parent map.
"""

import unittest
from typing import List


class Solution:
    """Union-Find approach to find the minimum cable moves to connect a network."""

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        Calculates the minimum number of cables to move to connect all 'n' computers.
        """
        # 1. Pre-check: If total connections (edges) are fewer than the minimum
        # required for a fully connected graph (n - 1), it's impossible.
        if len(connections) < n - 1:
            return -1

        # 2. Initialize UnionFind with 'n' computers.
        uf = UnionFind(n)

        # 3. Process all connections to find the total number of components.
        for conn in connections:
            # Union the two connected computers.
            # The uf.union method updates uf.count only when a successful merge occurs.
            uf.union(conn[0], conn[1])

        # 4. Calculate operations.
        # If there are 'k' components, we need 'k - 1' additional connections to link them all.
        # Since we passed the initial length check, we are guaranteed to have enough
        # redundant cables to form these 'k - 1' connections.
        return uf.count - 1


class UnionFind:
    """Disjoint set data structure with path compression for component counting."""

    def __init__(self, initial_count):
        """
        Initializes the UnionFind structure.

        :param initial_count: The initial number of elements (computers), which
                              is also the starting number of components.
        """
        # The parent map stores the parent of each element.
        self.parent = {}
        # The count tracks the number of disjoint sets (sub-networks).
        self.count = initial_count

    def find(self, x):
        """
        Finds the root of element x with path compression.
        """
        # Initialize node if not seen (handles 0-based indexing for computers)
        if x not in self.parent:
            self.parent[x] = x

        # Path compression: recursively find the root and set x's parent directly to it
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        """
        Unites the components containing x and y, and decrements the component count if a union occurs.
        """
        root_x, root_y = self.find(x), self.find(y)

        # If roots are different, they belong to two separate components.
        if root_x != root_y:
            # Merge the two components.
            self.parent[root_x] = root_y
            # Decrement the total component count.
            self.count -= 1


# -----------------------------------------------------------------------------


class TestMakeConnected(unittest.TestCase):
    """Test cases for the Solution.makeConnected method."""

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example_one(self):
        """Test case: 4 computers, 3 connections. Already connected (1 component)."""
        n = 4
        connections = [[0, 1], [0, 2], [1, 2]]
        # Components: 1. Connections needed: 1 - 1 = 0.
        self.assertEqual(self.solution.makeConnected(n, connections), 1)

    def test_example_two(self):
        """Test case: 6 computers, 5 connections. 2 components."""
        n = 6
        connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
        # Components: {0,1,2,3}, {4}, {5}. uf.count = 3. Connections needed: 3 - 1 = 2.
        self.assertEqual(self.solution.makeConnected(n, connections), 2)

    def test_insufficient_cables(self):
        """Test case: Not enough cables to connect all computers (n-1 check)."""
        n = 6
        connections = [[0, 1], [0, 2], [4, 5]]
        # Total connections (3) < n - 1 (5). Impossible.
        self.assertEqual(self.solution.makeConnected(n, connections), -1)

    def test_already_fully_connected(self):
        """Test case: Network is already fully connected (1 component)."""
        n = 5
        connections = [[0, 1], [1, 2], [2, 3], [3, 4]]
        # Components: 1. Operations needed: 1 - 1 = 0.
        self.assertEqual(self.solution.makeConnected(n, connections), 0)

    def test_two_components_one_move(self):
        """Test case: Two separate components require one move."""
        n = 4
        connections = [[0, 1], [2, 3], [1, 0]]
        # Components: {0, 1}, {2, 3}. uf.count = 2. Operations needed: 2 - 1 = 1.
        self.assertEqual(self.solution.makeConnected(n, connections), 1)

    def test_single_computer(self):
        """Test case: Single computer, no connections needed."""
        n = 1
        connections = []
        self.assertEqual(self.solution.makeConnected(n, connections), 0)


if __name__ == "__main__":
    unittest.main()
