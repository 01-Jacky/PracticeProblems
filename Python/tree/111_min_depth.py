# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque

        q = deque(root)
        level = 0
        children_at_level = 1
        inserted = 0

        while q:
            popped = q.popleft()

            if popped.left is None or popped.right is None:
                return level

            if popped.left is not None:


            children_at_level -= 1


            if children_at_level == 0
                level += 1


        q.append(root)
        print(q)

        return level


Solution().minDepth(None)