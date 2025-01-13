# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    Serializes and deserializes a binary tree.

    Serialization represents the tree as a string, and deserialization reconstructs the tree from the string.
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "X#"  # Use 'X' to represent null nodes and '#' as a delimiter

        left_serialized = self.serialize(
            root.left
        )  # Recursively serialize left subtree
        right_serialized = self.serialize(
            root.right
        )  # Recursively serialize right subtree

        # Combine the value of the current node with its serialized subtrees
        return str(root.val) + "#" + left_serialized + right_serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs():
            """
            Recursive depth-first search helper function for deserialization.
            This uses an iterator to efficiently process the serialized string.
            """
            val = next(data)  # Get next value from iterator
            if val == "X":
                return None  # Return null node for 'X'

            node = TreeNode(int(val))  # Create a new node
            node.left = dfs()  # Recursively deserialize left subtree
            node.right = dfs()  # Recursively deserialize right subtree
            return node  # Return deserialized node

        data = iter(data.split("#"))  # Create iterator for serialized data split by '#'
        return dfs()  # Start deserialization using DFS


import unittest


class TestCodec(unittest.TestCase):
    def test_serialize_deserialize(self):
        codec = Codec()

        # Test case 1: Simple tree
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root1.right.left = TreeNode(4)
        root1.right.right = TreeNode(5)
        serialized1 = codec.serialize(root1)
        deserialized1 = codec.deserialize(serialized1)
        self.assertEqual(serialized1, "1#2#X#X#3#4#X#X#5#X#X#")
        self._assert_trees_equal(root1, deserialized1)

        # Test case 2: Null tree
        root2 = None
        serialized2 = codec.serialize(root2)
        deserialized2 = codec.deserialize(serialized2)
        self.assertEqual(serialized2, "X#")
        self.assertIsNone(deserialized2)

        # Test case 3: Single node tree
        root3 = TreeNode(10)
        serialized3 = codec.serialize(root3)
        deserialized3 = codec.deserialize(serialized3)
        self.assertEqual(serialized3, "10#X#X#")
        self._assert_trees_equal(root3, deserialized3)

    def _assert_trees_equal(self, root1, root2):
        """Helper function to assert that two trees are structurally and valuely equal."""
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return self._assert_trees_equal(
            root1.left, root2.left
        ) and self._assert_trees_equal(root1.right, root2.right)


if __name__ == "__main__":
    unittest.main()
