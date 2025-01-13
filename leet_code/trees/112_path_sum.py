# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        Checks if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

        Args:
            root: The root of the binary tree.
            targetSum: The target sum.

        Returns:
             True if the tree has a root-to-leaf path with the target sum, False otherwise.
        """
        if not root:
            return False

        if not root.left and not root.right:  # Leaf node
            return root.val == targetSum

        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


import unittest


class TestHasPathSum(unittest.TestCase):
    def test_has_path_sum(self):
        solution = Solution()

        # Test case 1: Path exists
        root1 = TreeNode(5)
        root1.left = TreeNode(4)
        root1.right = TreeNode(8)
        root1.left.left = TreeNode(11)
        root1.left.left.left = TreeNode(7)
        root1.left.left.right = TreeNode(2)
        root1.right.left = TreeNode(13)
        root1.right.right = TreeNode(4)
        root1.right.right.right = TreeNode(1)
        self.assertTrue(solution.hasPathSum(root1, 22))

        # Test case 2: Path does not exist
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        self.assertFalse(solution.hasPathSum(root2, 5))

        # Test case 3: Empty tree
        root3 = None
        self.assertFalse(solution.hasPathSum(root3, 0))

        # Test case 4: Single node tree with matching target
        root4 = TreeNode(1)
        self.assertTrue(solution.hasPathSum(root4, 1))

        # Test case 5: Single node tree with non-matching target
        root5 = TreeNode(1)
        self.assertFalse(solution.hasPathSum(root5, 0))


if __name__ == "__main__":
    unittest.main()
