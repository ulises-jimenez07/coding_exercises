# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root) -> None:
        """
        Flattens a binary tree to a linked list in-place.

        The flattening is done such that the original left child becomes the right child of the node,
        and the original right child becomes the right child of the former left child. The left child
        of the flattened tree is always None.

        Do not return anything, modify root in-place instead.
        """

        def flatten_tree(node):
            print(
                f"Entering flatten_tree with node: {node.val if node else None}"
            )  # Print current node

            if not node:
                print("Base case: empty node, returning None")  # Print base case
                return None
            if not node.left and not node.right:
                print(
                    f"Base case: leaf node {node.val}, returning itself"
                )  # Print leaf case
                return node

            print(f"Processing node: {node.val}")  # Print processing node

            left_tail = flatten_tree(node.left)  # Recursively flatten left subtree
            print(
                f"Returned from left subtree of {node.val}, left_tail: {left_tail.val if left_tail else None}"
            )

            right_tail = flatten_tree(node.right)  # Recursively flatten right subtree
            print(
                f"Returned from right subtree of {node.val}, right_tail: {right_tail.val if right_tail else None}"
            )

            if left_tail:
                print(
                    f"Attaching right subtree of {node.val} to the end of left subtree"
                )  # Print attachment
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            print(
                f"Returning from {node.val}, tail: {(right_tail.val if right_tail else (left_tail.val if left_tail else None))}"
            )

            return (
                right_tail if right_tail else left_tail
            )  # Return tail of the flattened subtree

        flatten_tree(root)


# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)


solution = Solution()
solution.flatten(root)

# The flattened tree should now look like a linked list:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
current = root
while current:
    print(current.val, end=" -> ")
    current = current.right
print("None")
