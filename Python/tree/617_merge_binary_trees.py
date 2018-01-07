# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        #         this waste memory
        #         if t1 is None:
        #             return t2
        #         if t2 is None:
        #             return t1

        #         node = TreeNode(t1.val + t2.val)
        #         node.left = self.mergeTrees(t1.left,t2.left)
        #         node.right = self.mergeTrees(t1.right,t2.right)
        #         return node

        # just copy over one of the trees
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1