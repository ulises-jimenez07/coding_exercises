# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        Checks if a binary tree is symmetric around its center.

        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True  # An empty tree is symmetric
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, t1, t2):
        """
        Recursively checks if two subtrees are mirror images of each other.

        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: bool
        """
        if t1 is None and t2 is None:
            return True  # Both subtrees are empty, so they are mirrors
        if t1 is None or t2 is None:
            return False  # One subtree is empty and the other isn't, so not mirrors

        # Check if the values of the current nodes are equal and if their children are mirrors
        first_mirror = self.is_mirror(t1.right, t2.left)  # Compare outer children
        second_mirror = self.is_mirror(t1.left, t2.right)  # Compare inner children
        return (
            first_mirror and second_mirror and t1.val == t2.val
        )  # All conditions must be true


# Test cases
def test_isSymmetric():
    solution = Solution()

    # Test case 1: Symmetric tree
    root1 = TreeNode(
        1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))
    )
    assert solution.isSymmetric(root1) == True

    # Test case 2: Non-symmetric tree
    root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert solution.isSymmetric(root2) == False

    # Test case 3: Empty tree
    root3 = None
    assert solution.isSymmetric(root3) == True

    # Test case 4: Single node tree
    root4 = TreeNode(1)
    assert solution.isSymmetric(root4) == True

    # Test case 5: Tree with unequal values at mirrored positions
    root5 = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(4)))
    assert solution.isSymmetric(root5) == False

    print("All test cases passed!")


test_isSymmetric()
