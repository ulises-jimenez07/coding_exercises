"""
Segment Tree implementation for range sum queries and point updates.

A segment tree is a binary tree data structure that allows efficient range queries
and updates on an array. This implementation supports:
- Range sum queries in O(log n) time
- Point updates in O(log n) time
- Space complexity: O(n)
"""


class SegmentTree:
    """
    Segment tree data structure for efficient range queries and updates.

    Attributes:
        tree: Array representation of the segment tree
        n: Size of the original data array
    """

    def __init__(self, data):
        """
        Initialize segment tree with given data.

        Args:
            data: List of integers to build the tree from
        """
        self.tree = [0] * 2 * len(data)
        self.build(data, 0, 0, len(data) - 1)
        self.n = len(data)
        print(f"Tree = {self.tree}")

    def build(self, data, node, start, end):
        """
        Recursively build the segment tree.

        Args:
            data: Original data array
            node: Current node index in tree
            start: Start index of current segment
            end: End index of current segment
        """
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    # pylint: disable=too-many-positional-arguments
    # pylint: disable=too-many-arguments
    def query(self, l, r, node, start, end):
        """
        Query the sum of elements in range [l, r].

        Args:
            l: Left bound of query range
            r: Right bound of query range
            node: Current node index in tree
            start: Start index of current segment
            end: End index of current segment

        Returns:
            Sum of elements in range [l, r]
        """
        if r < start or l > end:
            return 0
        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self.query(l, r, 2 * node + 1, start, mid)
        right_sum = self.query(l, r, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum

    def query_range(self, l, r):
        """
        Public method to query sum in range [l, r].

        Args:
            l: Left bound of query range
            r: Right bound of query range

        Returns:
            Sum of elements in range [l, r]
        """
        print(f"Finding answer for range {l} and {r}")
        return self.query(l, r, 0, 0, self.n - 1)

    # pylint: disable=too-many-positional-arguments
    # pylint: disable=too-many-arguments
    def update(self, index, updated_value, node, start, end):
        """
        Update value at given index.

        Args:
            index: Index to update
            updated_value: New value to set
            node: Current node index in tree
            start: Start index of current segment
            end: End index of current segment
        """
        if start == end:
            self.tree[node] = updated_value
        elif start <= index <= end:
            mid = (start + end) // 2
            if start <= index <= mid:
                self.update(index, updated_value, 2 * node + 1, start, mid)
            else:
                self.update(index, updated_value, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update_index(self, index, updated_value):
        """
        Public method to update value at given index.

        Args:
            index: Index to update
            updated_value: New value to set
        """
        self.update(index, updated_value, 0, 0, self.n - 1)


arr = [2, 5, 1, 6, 4, 10, 8, 9]
seg_tree = SegmentTree(arr)

print(seg_tree.query_range(1, 5))

seg_tree.update_index(2, 9)

print(seg_tree.query_range(1, 5))
