# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        """
        Represents a node in a binary tree.

        Args:
            val: The value of the node.
            left: The left child node.
            right: The right child node.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        Performs a post-order traversal of a binary tree using two stacks.

        Post-order traversal visits nodes in the order: left subtree, right subtree, root.

        Args:
            root: The root of the binary tree.

        Returns:
            A list containing the values of the nodes in post-order.
        """
        ans = []  # Initialize the list to store the traversal result
        if not root:  # If the tree is empty, return an empty list
            return ans

        s1 = []  # First stack for intermediate processing
        s2 = []  # Second stack to store nodes in reverse post-order

        s1.append(root)  # Push the root onto the first stack
        while s1:  # While the first stack is not empty
            x = s1.pop()  # Pop the top node from the first stack
            s2.append(x)  # Push it onto the second stack
            if x.left:  # If the node has a left child
                s1.append(x.left)  # Push the left child onto the first stack
            if x.right:  # If the node has a right child
                s1.append(x.right)  # Push the right child onto the first stack

        while s2:  # While the second stack is not empty
            y = s2.pop()  # Pop the top node from the second stack
            ans.append(y.val)  # Append its value to the result list

        return ans  # Return the list of node values in post-order


import unittest


class TestPostorderTraversal(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(Solution().postorderTraversal(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(Solution().postorderTraversal(root), [1])

    def test_simple_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(Solution().postorderTraversal(root), [2, 3, 1])

    def test_complex_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(Solution().postorderTraversal(root), [4, 5, 2, 3, 1])

    def test_left_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(Solution().postorderTraversal(root), [3, 2, 1])

    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(Solution().postorderTraversal(root), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
