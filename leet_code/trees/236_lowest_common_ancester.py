# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        Finds the lowest common ancestor (LCA) of two nodes in a binary tree.

        The LCA of two nodes p and q is the lowest node in the tree that has both p and q as descendants (where we allow a node to be a descendant of itself).

        Args:
            root: The root of the binary tree.
            p: One of the nodes to find the LCA for.
            q: The other node to find the LCA for.

        Returns:
            The TreeNode representing the LCA of p and q, or None if either p or q is not in the tree.

        """
        if root is None:
            return None  # Base case: empty tree
        if root.val == p.val or root.val == q.val:
            return root  # Base case: root is either p or q

        # Recursively search left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are on both sides of the root, then root is the LCA
        if left_lca and right_lca:
            return root

        # Otherwise check which side has a non-null LCA and return that
        return left_lca if left_lca else right_lca


import unittest


class TestLowestCommonAncestor(unittest.TestCase):
    def build_tree(self, values):
        """Helper function to build a binary tree from a list of values."""
        if not values:
            return None

        root = TreeNode(values[0])
        nodes = [root]
        i = 1
        while i < len(values):
            current = nodes.pop(0)
            if values[i] is not None:
                current.left = TreeNode(values[i])
                nodes.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                nodes.append(current.right)
            i += 1
        return root

    def test_lca(self):
        solution = Solution()

        # Test case 1: p and q are on opposite sides
        root1 = self.build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p1 = TreeNode(5)
        q1 = TreeNode(1)
        self.assertEqual(solution.lowestCommonAncestor(root1, p1, q1).val, 3)

        # Test case 2: p is a descendant of q
        root2 = self.build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p2 = TreeNode(5)
        q2 = TreeNode(4)
        self.assertEqual(solution.lowestCommonAncestor(root2, p2, q2).val, 5)

        # Test case 3: q is a descendant of p
        root3 = self.build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p3 = TreeNode(4)
        q3 = TreeNode(5)
        self.assertEqual(solution.lowestCommonAncestor(root3, p3, q3).val, 5)

        # Test case 4: p and q are the same
        root4 = self.build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p4 = TreeNode(5)
        q4 = TreeNode(5)
        self.assertEqual(solution.lowestCommonAncestor(root4, p4, q4).val, 5)

        # Test case 5: Empty tree
        self.assertIsNone(solution.lowestCommonAncestor(None, TreeNode(1), TreeNode(2)))

        # Test case 6: One node is not in the tree
        root6 = self.build_tree([1, 2])
        p6 = TreeNode(2)
        q6 = TreeNode(3)
        self.assertEqual(solution.lowestCommonAncestor(root6, p6, q6).val, 2)


if __name__ == "__main__":
    unittest.main()
