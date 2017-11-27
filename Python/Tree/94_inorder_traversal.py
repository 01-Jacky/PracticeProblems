# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
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