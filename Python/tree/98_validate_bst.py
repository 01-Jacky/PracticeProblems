# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
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

    def isValidBST_iterative(self, root):
        traversal = []
        stack = []
        cur = root

        # Do inorder traversal and store result in traversal
        while cur or stack:
            while cur:  # Push all left node to stack
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()  # Use the stack
            traversal.append(cur.val)
            cur = cur.right

        # check traversal for order. Could optimze it for early termination in our loop above
        prev = traversal[0]
        for i in range(1, len(traversal)):
            if prev >= traversal[i]:
                return False
            prev = traversal[i]
        return True
