import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a new TreeNode.

        Args:
            val: The value of the node. Defaults to 0.
            left: The left child of the node. Defaults to None.
            right: The right child of the node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Checks if one binary tree is a subtree of another.

        A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T.
        The tree S could also be T itself.

        Args:
            root: The root of the main binary tree.
            subRoot: The root of the potential subtree.

        Returns:
            True if subRoot is a subtree of root, False otherwise.
        """

        def is_identical(node_1: Optional[TreeNode], node_2: Optional[TreeNode]) -> bool:
            """
            Compares two binary trees to check if they are identical.

            Two trees are identical if they have the same structure and the same node values.

            Args:
                node_1: The root of the first tree.
                node_2: The root of the second tree.

            Returns:
                True if the two trees are identical, False otherwise.
            """
            # If both nodes are None, they are identical (base case for reaching end of branch)
            if node_1 is None and node_2 is None:
                return True

            # If one of the nodes is None while the other is not, they are not identical
            if node_1 is None or node_2 is None:
                return False

            # Check if current node values are the same and recursively check left and right subtrees
            return (
                node_1.val == node_2.val
                and is_identical(node_1.left, node_2.left)
                and is_identical(node_1.right, node_2.right)
            )

        def dfs(node: Optional[TreeNode]) -> bool:
            """
            Performs a Depth-First Search (DFS) on the 'root' tree to find a node
            that is identical to 'subRoot'.

            Args:
                node: The current node in the 'root' tree being visited.

            Returns:
                True if an identical subtree is found, False otherwise.
            """
            # If the current node in the 'root' tree is None, we can't find subRoot here
            if node is None:
                return False

            # If the current node's subtree is identical to subRoot, we found it!
            if is_identical(node, subRoot):
                return True

            # Recursively search in the left and right subtrees of the current node
            # If either search finds the subRoot, return True
            return dfs(node.left) or dfs(node.right)

        # Start the DFS from the root of the main tree
        return dfs(root)


# -----------------------------------------------------------------------------
# Unit Tests
# -----------------------------------------------------------------------------


class TestIsSubtree(unittest.TestCase):
    def setUp(self):
        """
        Set up common tree structures for testing.
        """
        # Tree 1: [3,4,5,1,2]
        #      3
        #     / \
        #    4   5
        #   / \
        #  1   2
        self.root1 = TreeNode(3)
        self.root1.left = TreeNode(4)
        self.root1.right = TreeNode(5)
        self.root1.left.left = TreeNode(1)
        self.root1.left.right = TreeNode(2)

        # Subtree 1: [4,1,2] - Should be a subtree of root1
        #    4
        #   / \
        #  1   2
        self.subRoot1 = TreeNode(4)
        self.subRoot1.left = TreeNode(1)
        self.subRoot1.right = TreeNode(2)

        # Subtree 2: [3,4,5,1,2] - Should be a subtree (identical) of root1
        #      3
        #     / \
        #    4   5
        #   / \
        #  1   2
        self.subRoot2 = TreeNode(3)
        self.subRoot2.left = TreeNode(4)
        self.subRoot2.right = TreeNode(5)
        self.subRoot2.left.left = TreeNode(1)
        self.subRoot2.left.right = TreeNode(2)

        # Subtree 3: [4,1] - Not a complete subtree of root1
        #    4
        #   /
        #  1
        self.subRoot3 = TreeNode(4)
        self.subRoot3.left = TreeNode(1)

        # Tree 2: [1,2,3]
        #    1
        #   / \
        #  2   3
        self.root2 = TreeNode(1)
        self.root2.left = TreeNode(2)
        self.root2.right = TreeNode(3)

        # Subtree 4: [2] - Should be a subtree of root2
        #    2
        self.subRoot4 = TreeNode(2)

        # Empty Trees
        self.empty_tree = None
        self.single_node_tree = TreeNode(1)

    def test_example_case_true(self):
        """
        Test case from common examples where subRoot is a true subtree.
        """
        sol = Solution()
        self.assertTrue(sol.isSubtree(self.root1, self.subRoot1))

    def test_identical_trees(self):
        """
        Test case where the subRoot is identical to the root tree.
        """
        sol = Solution()
        self.assertTrue(sol.isSubtree(self.root1, self.subRoot2))

    def test_subroot_not_found(self):
        """
        Test case where subRoot is not present in the root tree.
        """
        sol = Solution()
        # Tree with a different structure at the 4 node
        self.assertFalse(sol.isSubtree(self.root1, self.subRoot3))

    def test_single_node_subtree(self):
        """
        Test with a single-node subtree.
        """
        sol = Solution()
        self.assertTrue(sol.isSubtree(self.root2, self.subRoot4))

    def test_subroot_larger_than_root(self):
        """
        Test case where subRoot is structurally larger than root.
        It should never be a subtree.
        """
        sol = Solution()
        # Create a larger subRoot to ensure it's not a subtree
        larger_subRoot = TreeNode(1)
        larger_subRoot.left = TreeNode(2)
        larger_subRoot.right = TreeNode(3)
        larger_subRoot.left.left = TreeNode(4)
        self.assertFalse(sol.isSubtree(self.single_node_tree, larger_subRoot))

    def test_complex_tree_no_match(self):
        """
        Test with more complex trees where no match exists.
        """
        # Root tree: [1,2,3,4,5,6,7]
        #        1
        #       / \
        #      2   3
        #     / \ / \
        #    4  5 6  7
        root_complex = TreeNode(1)
        root_complex.left = TreeNode(2)
        root_complex.right = TreeNode(3)
        root_complex.left.left = TreeNode(4)
        root_complex.left.right = TreeNode(5)
        root_complex.right.left = TreeNode(6)
        root_complex.right.right = TreeNode(7)

        # SubRoot: [2,8,9] (values don't match exactly where expected)
        #      2
        #     / \
        #    8   9
        subRoot_no_match = TreeNode(2)
        subRoot_no_match.left = TreeNode(8)
        subRoot_no_match.right = TreeNode(9)

        sol = Solution()
        self.assertFalse(sol.isSubtree(root_complex, subRoot_no_match))

    def test_complex_tree_with_match(self):
        """
        Test with more complex trees where a match exists.
        """
        # Root tree: [1,2,3,4,5,6,7] (same as above)
        #        1
        #       / \
        #      2   3
        #     / \ / \
        #    4  5 6  7
        root_complex = TreeNode(1)
        root_complex.left = TreeNode(2)
        root_complex.right = TreeNode(3)
        root_complex.left.left = TreeNode(4)
        root_complex.left.right = TreeNode(5)
        root_complex.right.left = TreeNode(6)
        root_complex.right.right = TreeNode(7)

        # SubRoot: [2,4,5] (matches a part of root_complex)
        #      2
        #     / \
        #    4   5
        subRoot_match = TreeNode(2)
        subRoot_match.left = TreeNode(4)
        subRoot_match.right = TreeNode(5)

        sol = Solution()
        self.assertTrue(sol.isSubtree(root_complex, subRoot_match))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
