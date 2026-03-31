"""
Problem: 427. Construct Quad Tree (Medium)

Given a `n * n` matrix `grid` of `0's` and `1's` only. We want to represent the `grid` with a Quad-Tree.
A Quad-Tree is a tree data structure in which each internal node has exactly four children.
Besides, each node has two attributes:
- `val`: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
- `isLeaf`: True if the node is leaf node on the tree or False if the node has the four children.

We can construct a Quad-Tree from a two-dimensional area using the following steps:
1. If the current grid has the same value (all 1's or all 0's), set `isLeaf` True and set `val` to the value of the grid and set the four children to Null and stop.
2. If the current grid has different values, set `isLeaf` False and set `val` to any value and divide the current grid into four sub-grids.
3. Recurse for each of the four sub-grids with the appropriate coordinates.

Approach:
- Recursive subdivision.
- Check if all values in the current grid are the same.
- If they are, it's a leaf.
- If they are not, it's an internal node with 4 children.
- Time complexity: O(N^2 log N) or O(N^2) depending on how we check for uniform value.
- Let's use O(N^2) by checking each subgrid value.
- Space complexity: O(log N) stack space.
"""

import unittest
from typing import (
    List,
    Optional,
)


# Definition for a QuadTree node.
class Node:
    """
    Represents a node in a QuadTree.
    """

    # pylint: disable=too-many-arguments,too-many-positional-arguments
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    """
    Solution for Construct Quad Tree problem.
    """

    def construct(self, grid: List[List[int]]) -> Optional[Node]:
        def build(r, c, length):
            if length == 1:
                return Node(grid[r][c] == 1, True)

            half = length // 2
            top_left = build(r, c, half)
            top_right = build(r, c + half, half)
            bottom_left = build(r + half, c, half)
            bottom_right = build(r + half, c + half, half)

            # Check if all four children are leaves and have the same value
            if (
                top_left.isLeaf
                and top_right.isLeaf
                and bottom_left.isLeaf
                and bottom_right.isLeaf
                and top_left.val == top_right.val == bottom_left.val == bottom_right.val
            ):
                return Node(top_left.val, True)

            return Node(True, False, top_left, top_right, bottom_left, bottom_right)

        return build(0, 0, len(grid))


class TestConstructQuadTree(unittest.TestCase):
    """
    Unit tests for Construct Quad Tree.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[0, 1], [1, 0]]
        root = self.solution.construct(grid)
        self.assertFalse(root.isLeaf)
        self.assertTrue(root.topLeft.isLeaf)
        self.assertFalse(root.topLeft.val)
        self.assertTrue(root.topRight.isLeaf)
        self.assertTrue(root.topRight.val)

    def test_example_2(self):
        grid = [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
        ]
        root = self.solution.construct(grid)
        self.assertFalse(root.isLeaf)
        # Check some property
        self.assertTrue(root.topLeft.isLeaf)
        self.assertTrue(root.topLeft.val)


if __name__ == "__main__":
    unittest.main()
