# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        Calculates the sum of values of all nodes with a value in the inclusive range [low, high].

        Args:
            root (TreeNode): The root of the BST.
            low (int): The lower bound of the range (inclusive).
            high (int): The upper bound of the range (inclusive).

        Returns:
            int: The sum of values in the specified range.
        """
        if not root:
            return 0  # Base case: empty tree, sum is 0

        ans_sum = 0

        # Check if current node's value is within the range
        if low <= root.val <= high:
            ans_sum += root.val

        # Recursively explore left subtree if it might contain values within the range
        if low < root.val and root.left:  # Optimization: avoid unnecessary recursion
            ans_sum += self.rangeSumBST(root.left, low, high)

        # Recursively explore right subtree if it might contain values within the range
        if root.val < high and root.right:  # Optimization: avoid unnecessary recursion
            ans_sum += self.rangeSumBST(root.right, low, high)

        return ans_sum


import unittest


class TestRangeSumBST(unittest.TestCase):
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

    def test_range_sum_bst(self):
        solution = Solution()

        # Test case 1: Example 1
        root1 = self.build_tree([10, 5, 15, 3, 7, None, 18])
        self.assertEqual(solution.rangeSumBST(root1, 7, 15), 32)

        # Test case 2: Example 2
        root2 = self.build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(solution.rangeSumBST(root2, 6, 10), 23)

        # Test case 3: Empty tree
        self.assertEqual(solution.rangeSumBST(None, 0, 100), 0)


if __name__ == "__main__":
    unittest.main()
