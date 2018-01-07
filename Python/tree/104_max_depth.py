# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """ Do a BFS """
        import collections

        q = collections.deque()
        depth = 0

        q.append(root)
        while q:
            levelSize = len(q)
            depth += 1
            for i in range(levelSize):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return depth


