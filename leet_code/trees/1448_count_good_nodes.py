import unittest


# Definition for a binary tree node.
# This class is provided as part of the problem setup.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solves the 'Good Nodes in Binary Tree' problem using a recursive approach.
    A node is considered 'good' if the path from the root to the node
    contains no node with a value greater than the current node's value.
    """

    def goodNodes(self, root: TreeNode) -> int:
        """
        Main method to initiate the search for good nodes.
        It initializes a counter and calls the recursive helper function.
        """
        self.count = 0
        # Start the traversal from the root with the initial max_till_parent as negative infinity.
        self.count_nodes(root, float("-inf"))
        return self.count

    def count_nodes(self, node, max_till_parent):
        """
        A recursive helper function to traverse the tree and count good nodes.

        Args:
            node: The current TreeNode being visited.
            max_till_parent: The maximum value found in the path from the root
                             to the current node's parent.
        """
        # Base case: If the current node is None, we've reached a leaf and stop the recursion.
        if node:
            # max_till_me will store the maximum value encountered so far on the path to this node.
            # We initialize it with the current node's value.
            max_till_me = node.val

            # Check if the current node is a 'good' node.
            # The first node (root) is always 'good', as there's no path above it.
            if max_till_parent == float("-inf"):
                self.count += 1
            else:
                # If the current node's value is greater than or equal to the maximum
                # value in its path from the root, it's a good node.
                if node.val >= max_till_parent:
                    self.count += 1
                # Update the maximum value for the path to be passed down to children.
                # This is the greater of the current node's value and the parent's max.
                max_till_me = max(max_till_me, max_till_parent)

            # Recursively call the function for the left and right children,
            # passing the updated maximum value for their respective paths.
            self.count_nodes(node.left, max_till_me)
            self.count_nodes(node.right, max_till_me)


# Unit test class to verify the solution
class TestSolution(unittest.TestCase):
    def test_good_nodes_simple_case(self):
        """
        Test case for a simple binary tree.
        Tree:
        """
        #       3
        #      / \
        #     1   4
        #    /   / \
        #   3   1   5
        # Good nodes are 3 (root), 4, 5, and 3 (leftmost leaf). Expected count is 4.
        # Construct the binary tree
        root = TreeNode(3)
        root.left = TreeNode(1, TreeNode(3))
        root.right = TreeNode(4, TreeNode(1), TreeNode(5))

        # Instantiate the solution and run the test
        solution = Solution()
        result = solution.goodNodes(root)

        # Assert that the result matches the expected output
        self.assertEqual(result, 4, "The number of good nodes should be 4")

    def test_good_nodes_all_good(self):
        """
        Test case where all nodes are good.
        Tree:
              1
             / \
            2   3
        Expected count is 3.
        """
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        solution = Solution()
        result = solution.goodNodes(root)
        self.assertEqual(result, 3, "All nodes should be good")

    def test_good_nodes_all_bad_except_root(self):
        """
        Test case where only the root is good.
        Tree:
              5
             / \
            2   4
        Expected count is 1.
        """
        root = TreeNode(5, TreeNode(2), TreeNode(4))
        solution = Solution()
        result = solution.goodNodes(root)
        self.assertEqual(result, 1, "Only the root should be good")

    def test_good_nodes_single_node(self):
        """
        Test case for a single-node tree.
        Expected count is 1.
        """
        root = TreeNode(10)
        solution = Solution()
        result = solution.goodNodes(root)
        self.assertEqual(result, 1, "A single node tree should have 1 good node")

    def test_good_nodes_empty_tree(self):
        """
        Test case for an empty tree.
        Expected count is 0.
        """
        root = None
        solution = Solution()
        result = solution.goodNodes(root)
        self.assertEqual(result, 0, "An empty tree should have 0 good nodes")


# This block allows the script to be run directly to execute the tests.
if __name__ == "__main__":
    unittest.main()
