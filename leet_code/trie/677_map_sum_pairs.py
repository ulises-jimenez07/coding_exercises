"""
Problem: Implement the MapSum data structure, which supports two main operations:
         1. `insert(key, val)`: Inserts a key-value pair, updating the value if the key already exists.
         2. `sum(prefix)`: Calculates the total sum of values for all keys previously inserted
            that start with the given prefix.

Approach:
- This problem is efficiently solved using a **Trie (Prefix Tree)** with a twist: each node stores a running sum (`score`).
- **TrieNode Structure:** Each node stores a `score` representing the aggregated value of all full keys
  that pass through this node (i.e., keys for which the prefix up to this node is part of the key).
- **Insert Operation:**
    1. First, determine the `delta` (the difference between the new value and the old value, if the key existed).
    2. Update the main Python dictionary (`self.map`) to store the new key-value mapping.
    3. Traverse the Trie using the `key`. For every node along the path, update its `score` by adding the calculated `delta`.
    4. This ensures that when a prefix is queried, the score at the prefix's ending node already holds the total sum.
- **Sum Operation:**
    1. Traverse the Trie based on the `prefix`.
    2. If the traversal reaches the end of the `prefix`, the `score` stored in the final node is returned immediately.
    3. If the path for the `prefix` does not exist, the sum is 0.

- Time Complexity:
    - `insert`: O(L), where L is the length of the key.
    - `sum`: O(P), where P is the length of the prefix.
- Space Complexity: O(N * L * D), where N is the number of keys, L is the average key length, and D is the alphabet size, plus O(N) for the auxiliary Python map.
"""

import unittest
from typing import (
    Dict,
)

# --- TrieNode Class ---


class TrieNode:
    """Represents a single node in the Trie for MapSum."""

    def __init__(self):
        # Dictionary to hold child nodes, mapped by the character they represent.
        self.childrens: Dict[str, "TrieNode"] = {}
        # The aggregated sum of values for all full keys passing through this node.
        self.score: int = 0
        # Flag to indicate if this node marks the end of a word (optional, mainly for traditional Trie use, but kept here).
        self.end_of_string: bool = False


# --- MapSum Class ---


class MapSum:
    """
    Implements a MapSum structure using a Trie to support prefix sum calculations.
    """

    def __init__(self):
        """Initializes the MapSum structure with a Trie and an auxiliary map."""
        self.root = TrieNode()
        # Auxiliary map to store the actual key-value pairs and easily find the old value during an update.
        self.map: Dict[str, int] = {}

    def insert(self, key: str, val: int) -> None:
        """
        Inserts a key-value pair and updates the scores in the Trie path.

        The use of `delta` handles both initial insertions and updates efficiently.
        """
        # 1. Calculate the change in value (delta).
        # If the key is new, map.get(key, 0) returns 0, so delta = val.
        # If the key is updated, delta = new_val - old_val.
        delta = val - self.map.get(key, 0)

        # 2. Update the auxiliary map with the new value.
        self.map[key] = val

        curr = self.root

        # 3. Update the root's score by the delta.
        curr.score += delta

        # 4. Traverse the key and update the score for every node along the path.
        for c in key:
            # Use setdefault to get the child node, creating it if it doesn't exist,
            # and automatically setting its score and end_of_string to defaults (0, False).
            curr = curr.childrens.setdefault(c, TrieNode())
            curr.score += delta

        # 5. Mark the end of the full key.
        curr.end_of_string = True

    def sum(self, prefix: str) -> int:
        """
        Returns the sum of values for all keys that start with the given prefix.
        """
        curr = self.root

        # 1. Traverse the Trie based on the prefix.
        for c in prefix:
            if c not in curr.childrens:
                # If the path is broken, no keys match the prefix.
                return 0
            curr = curr.childrens[c]

        # 2. The score at the final node of the prefix already holds the aggregated sum.
        return curr.score


# --- Unit Tests ---


class TestMapSum(unittest.TestCase):
    """Test cases for the MapSum implementation."""

    def test_basic_sum(self):
        """Test basic insertion and subsequent sum."""
        ms = MapSum()
        ms.insert("apple", 3)
        ms.insert("app", 2)
        # sum("ap") should be 3 ('apple') + 2 ('app') = 5
        self.assertEqual(ms.sum("ap"), 5)
        # sum("a") should be 5
        self.assertEqual(ms.sum("a"), 5)
        # sum("apple") should be 3
        self.assertEqual(ms.sum("apple"), 3)

    def test_update_value(self):
        """Test updating an existing key and verifying the sum update."""
        ms = MapSum()
        ms.insert("apple", 3)
        ms.insert("apricot", 5)
        self.assertEqual(ms.sum("a"), 8)

        # Update 'apple' from 3 to 10. Delta is 7.
        ms.insert("apple", 10)
        # New sum should be 10 ('apple') + 5 ('apricot') = 15
        self.assertEqual(ms.sum("a"), 15)
        # sum("ap") should be 10
        self.assertEqual(ms.sum("ap"), 10)
        self.assertEqual(ms.sum("app"), 10)

    def test_non_existent_prefix(self):
        """Test sum for a prefix not in the Trie."""
        ms = MapSum()
        ms.insert("hello", 10)
        self.assertEqual(ms.sum("world"), 0)
        self.assertEqual(ms.sum("hellow"), 0)
        self.assertEqual(ms.sum("h"), 10)

    def test_zero_value_insertion(self):
        """Test case with a zero value."""
        ms = MapSum()
        ms.insert("key1", 5)
        ms.insert("key2", 0)
        self.assertEqual(ms.sum("key"), 5)
        self.assertEqual(ms.sum("key1"), 5)
        self.assertEqual(ms.sum("key2"), 0)

    def test_negative_value_insertion(self):
        """Test case with negative values."""
        ms = MapSum()
        ms.insert("pos", 10)
        ms.insert("neg", -5)
        self.assertEqual(ms.sum("p"), 10)
        self.assertEqual(ms.sum("n"), -5)
        self.assertEqual(ms.sum(""), 5)  # Sum of all keys


# The Trie structure is essential for this problem because it allows the `sum` operation to be completed in O(P) time (where P is the prefix length). The running `score` in each node is the key optimization.

if __name__ == "__main__":
    # Using specific argv to avoid errors when running in environments like Jupyter/colab
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
