""" https://leetcode.com/problems/path-sum/description/ """

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        #return self.hasPathSum_recursive(root, sum)
        return self.hasPathSum_DFS(root, sum)

    def hasPathSum_recursive(self, root, sum):
        # base cases
        if root is None:
            return False
        if root.left is None and root.right is None:  # if leafnode and sum is down to 0 we fond the path
            return (sum - root.val) == 0

        # else not at leaf node
        return self.hasPathSum_recursive(root.left, sum - root.val) or \
               self.hasPathSum_recursive(root.right, sum - root.val)

    def hasPathSum_DFS(selfself, root, sum):
        if root is None:
            return False

        # DFS using a stack to hold tuple of (node, remaining sum)
        search_stack = [(root, sum)]

        while search_stack:
            popped     = search_stack.pop()
            node       = popped[0]
            sum_remain = popped[1] - node.val

            # Goal check
            if node.left is None and node.right is None:    # if leaf node
                if sum_remain == 0:
                    return True

            # Continue DFS
            if node.left:
                search_stack.append((node.left, sum_remain))
            if node.right:
                search_stack.append((node.right, sum_remain))

        return False
