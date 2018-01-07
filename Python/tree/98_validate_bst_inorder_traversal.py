# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        order = self.inorderTraversal(root)
        cur = order[0]
        for el in order[1:]:
            if cur >= el:
                return False
            cur = el
        return True

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

