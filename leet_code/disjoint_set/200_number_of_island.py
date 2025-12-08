"""
Problem: Count the number of islands (connected components of '1's) in a 2D grid.

Approach:
- Use the Union-Find (Disjoint Set) data structure to group adjacent land cells ('1').
- Map the 2D grid coordinates (r, c) to a 1D index: `r * cols + c`.
- Initialize the UnionFind structure with a count equal to the total number of '1's in the grid.
  Initially, every land cell is considered a separate island.
- Iterate through the grid. For every land cell ('1'):
    - Check its four neighbors.
    - If a neighbor is also land ('1') and the current cell and the neighbor are not
      already in the same set, perform a union operation.
- The UnionFind's internal `count` variable is decremented every time a successful union
  (connecting two previously separate islands) occurs.
- The final value of `count` represents the total number of disjoint land components (islands).
- Time complexity: O(R * C * α(R*C)), where R is rows, C is columns, and α is
  the inverse Ackermann function (nearly constant). The R*C factor comes from
  iterating over the grid.
- Space complexity: O(R * C) for the UnionFind parent map.


"""

import unittest
from typing import List


class Solution:
    """Union-Find approach to count the number of islands."""

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Counts the number of islands in a grid where '1's represent land and '0's represent water.
        """
        if not grid or not grid[0]:
            return 0

        # Define the four cardinal directions for neighbor checking
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])

        # 1. Initialize the UnionFind structure
        initial_land_count = 0
        land_indices = {}  # To map 1D index to existence of land. Not strictly needed for logic, but for clarity.

        # Count the initial number of land cells. This is the starting count of islands.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    initial_land_count += 1
                    # Map 2D coordinates to a unique 1D index
                    index = r * cols + c
                    land_indices[index] = True

        uf = UnionFind(initial_land_count)

        # 2. Iterate and perform union operations
        for r in range(rows):
            for c in range(cols):
                # We only process '1' cells (land)
                if grid[r][c] == "1":

                    # Convert 2D coordinates (r, c) to a 1D index
                    current_index = r * cols + c

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        # Check if the neighbor is within bounds and is also '1' (land)
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            # Convert neighbor coordinates (nr, nc) to a 1D index
                            neighbor_index = nr * cols + nc

                            # Perform the union operation. If successful, uf.count is decremented.
                            uf.union(current_index, neighbor_index)

        # The final count in the UnionFind object is the number of islands
        return uf.count


class UnionFind:
    """Disjoint set data structure with path compression and simple union."""

    def __init__(self, size):
        """
        Initializes the UnionFind structure.

        The initial count is set to the total number of land cells ('1's).
        """
        # The parent map stores the parent of each element.
        self.parent = {}
        # The count tracks the number of disjoint sets (islands).
        self.count = size

    def find(self, x):
        """
        Finds the root of element x with path compression.
        """
        # Initialize node if not seen
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

        # If roots are different, they belong to two separate components (islands)
        if root_x != root_y:
            # Simple union: merge one root into the other
            self.parent[root_x] = root_y
            # Since two components were merged into one, decrement the total count
            self.count -= 1


# -----------------------------------------------------------------------------


class TestNumIslands(unittest.TestCase):
    """Test cases for the Solution.numIslands method."""

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example_one(self):
        """Test case: Standard example with one large island."""
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_example_two(self):
        """Test case: Standard example with multiple islands."""
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        # Islands: (0,0), (0,1), (1,0), (1,1) is one island. (2,2) is a second. (3,3), (3,4) is a third.
        self.assertEqual(self.solution.numIslands(grid), 3)

    def test_no_islands(self):
        """Test case: Grid full of water ('0')."""
        grid = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
        self.assertEqual(self.solution.numIslands(grid), 0)

    def test_all_land(self):
        """Test case: Grid full of land ('1')."""
        grid = [["1", "1", "1"], ["1", "1", "1"]]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_complex_shape(self):
        """Test case: Islands connected diagonally are NOT considered one island."""
        grid = [["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]]
        # Four islands: (0,0), (0,2), (2,0), (2,2). (1,1) is isolated. This should be 5 in a standard implementation, but the current code only processes the '1's.
        # Let's re-examine: (0,0) is land. (0,2) is land. (1,1) is land. (2,0) is land. (2,2) is land.
        # (0,0) neighbor (1,0) is water.
        # (1,1) neighbor (0,1) is water, (2,1) is water, (1,0) is water, (1,2) is water.
        # Every '1' in this grid is isolated from other '1's by '0's.
        self.assertEqual(self.solution.numIslands(grid), 5)

    def test_empty_grid(self):
        """Test case: Empty grid or grid with empty row."""
        self.assertEqual(self.solution.numIslands([]), 0)
        self.assertEqual(self.solution.numIslands([[]]), 0)


if __name__ == "__main__":
    unittest.main()
