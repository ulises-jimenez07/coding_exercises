from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Represents a node in a binary tree.

        :param val: The value of the node. Defaults to 0.
        :param left: The left child node. Defaults to None.
        :param right: The right child node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum depth (height) of a binary tree.

        :param root: The root node of the binary tree.
        :return: The maximum depth of the tree. Returns 0 if the tree is empty.
        """
        if not root:
            return 0  # Base case: Empty tree has depth 0

        # Recursively calculate the depth of the left and right subtrees.
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)

        # The depth of the current node is 1 plus the maximum depth of its children.
        return 1 + max(depth_left, depth_right)


# Test cases
def test_maxDepth():
    solution = Solution()

    # Test case 1: Empty tree
    root1 = None
    assert solution.maxDepth(root1) == 0

    # Test case 2: Single node tree
    root2 = TreeNode(1)
    assert solution.maxDepth(root2) == 1

    # Test case 3: Balanced tree
    root3 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solution.maxDepth(root3) == 3

    # Test case 4: Skewed left tree
    root4 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert solution.maxDepth(root4) == 4

    # Test case 5: Skewed right tree
    root5 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert solution.maxDepth(root5) == 4

    print("All test cases passed!")


test_maxDepth()
