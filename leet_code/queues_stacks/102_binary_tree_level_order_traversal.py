# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        Performs a level-order traversal of a binary tree.

        Args:
            root: The root of the binary tree.

        Returns:
            A list of lists, where each inner list represents a level in the tree and contains the values of the nodes at that level.
            Returns an empty list if the tree is empty.
        """
        if not root:
            return []

        queue = [root]  # Initialize the queue with the root node
        ans = []  # Initialize the result list

        while queue:
            level_size = len(queue)  # Get the number of nodes in the current level
            level = []  # Initialize a list to store the values of the current level

            # Iterate through all nodes in the current level
            for _ in range(level_size):
                node = queue.pop(0)  # Dequeue a node from the front
                level.append(node.val)  # Add the node's value to the current level list

                # Enqueue the node's children (if any) for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level)  # Add the current level's list to the result list

        return ans


import unittest


class TestLevelOrder(unittest.TestCase):
    def test_level_order(self):
        solution = Solution()

        # Test case 1: Empty tree
        self.assertEqual(solution.levelOrder(None), [])

        # Test case 2: Single node tree
        root2 = TreeNode(1)
        self.assertEqual(solution.levelOrder(root2), [[1]])

        # Test case 3: Complete binary tree
        root3 = TreeNode(3)
        root3.left = TreeNode(9)
        root3.right = TreeNode(20)
        root3.right.left = TreeNode(15)
        root3.right.right = TreeNode(7)
        self.assertEqual(solution.levelOrder(root3), [[3], [9, 20], [15, 7]])

        # Test case 4: Incomplete binary tree
        root4 = TreeNode(1)
        root4.left = TreeNode(2)
        root4.right = TreeNode(3)
        root4.left.left = TreeNode(4)
        self.assertEqual(solution.levelOrder(root4), [[1], [2, 3], [4]])

        # Test case 5: Skewed tree
        root5 = TreeNode(1)
        root5.right = TreeNode(2)
        root5.right.right = TreeNode(3)
        self.assertEqual(solution.levelOrder(root5), [[1], [2], [3]])


if __name__ == "__main__":
    unittest.main()
