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
    def zigzagLevelOrder(self, root):
        """
        Performs a zigzag level-order traversal of a binary tree.

        Zigzag level order traversal alternates between left-to-right and right-to-left traversal for each level.

        Args:
            root: The root of the binary tree.

        Returns:
            A list of lists, where each inner list represents a level in the tree and contains the values of the nodes at that level in zigzag order.
            Returns an empty list if the tree is empty.
        """
        if not root:  # If the tree is empty, return an empty list
            return []

        ans = []  # Initialize the result list
        q = [root]  # Initialize the queue with the root node
        level_index = 1  # Initialize level index (1 for left-to-right, 2 for right-to-left, and so on)

        while len(q) > 0:  # While the queue is not empty
            level = []  # Initialize a list to store the values of the current level
            q_len = len(q)  # Get the number of nodes in the current level

            # Iterate through all nodes in the current level
            for i in range(q_len):
                current = q.pop(0)  # Dequeue a node from the front
                level.append(
                    current.val
                )  # Add the node's value to the current level list

                # Enqueue the node's children (if any) for the next level
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)

            if level_index % 2 == 0:  # If the level index is even (right-to-left)
                ans.append(
                    level[::-1]
                )  # Reverse the level list before adding it to the result
            else:  # If the level index is odd (left-to-right)
                ans.append(level)  # Add the level list as is to the result

            level_index += 1  # Increment the level index

        return ans  # Return the zigzag level order traversal result


import unittest


class TestZigzagLevelOrder(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(Solution().zigzagLevelOrder(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(Solution().zigzagLevelOrder(root), [[1]])

    def test_simple_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        self.assertEqual(Solution().zigzagLevelOrder(root), [[3], [20, 9]])

    def test_complex_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().zigzagLevelOrder(root), [[3], [20, 9], [15, 7]])

    def test_left_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(Solution().zigzagLevelOrder(root), [[1], [2], [3]])

    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(Solution().zigzagLevelOrder(root), [[1], [2], [3]])


if __name__ == "__main__":
    unittest.main()
