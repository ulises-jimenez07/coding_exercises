"""
Problem: Serialize and deserialize a binary tree to/from string

Approach:
- Use preorder traversal with delimiters for serialization
- Mark null nodes with 'X' to preserve structure
- Deserialize using iterator to reconstruct tree
- Time complexity: O(n) for both operations
- Space complexity: O(n) for serialized string and recursion
"""

import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string using pre-order traversal."""
        if not root:
            return "X#"

        left_serialized = self.serialize(root.left)
        right_serialized = self.serialize(root.right)

        return str(root.val) + "#" + left_serialized + right_serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree."""

        def dfs(data_iter):
            val = next(data_iter)
            if val == "X":
                return None

            node = TreeNode(int(val))
            node.left = dfs(data_iter)
            node.right = dfs(data_iter)
            return node

        data_iter = iter(data.split("#"))
        return dfs(data_iter)


def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


class TestCodec(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def test_complex_tree(self):
        """Tests serialization and deserialization of a complex tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)

        serialized_data = self.codec.serialize(root)
        deserialized_root = self.codec.deserialize(serialized_data)

        self.assertEqual(serialized_data, "1#2#X#X#3#4#X#X#5#X#X#")
        self.assertTrue(is_same_tree(root, deserialized_root))

    def test_empty_tree(self):
        """Tests an empty tree."""
        serialized_data = self.codec.serialize(None)
        deserialized_root = self.codec.deserialize(serialized_data)

        self.assertEqual(serialized_data, "X#")
        self.assertIsNone(deserialized_root)

    def test_single_node_tree(self):
        """Tests a tree with a single node."""
        root = TreeNode(10)

        serialized_data = self.codec.serialize(root)
        deserialized_root = self.codec.deserialize(serialized_data)

        self.assertEqual(serialized_data, "10#X#X#")
        self.assertTrue(is_same_tree(root, deserialized_root))


if __name__ == "__main__":
    unittest.main()
