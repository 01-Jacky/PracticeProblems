# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBST_helper(root, float("-inf"), float("inf"))

    def isValidBST_helper(self, root, min, max):
        if root is None:
            return True

        return min < root.val < max and \
               self.isValidBST_helper(root.left, min, root.val) and \
               self.isValidBST_helper(root.right, root.val, max)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        order = []

        if root is None:
            return order

        order.extend(self.inorderTraversal(root.left))
        order.append(root.val)
        order.extend(self.inorderTraversal(root.right))

        return order