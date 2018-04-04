# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """ Too much copying to memory from slicing"""
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


    def sortedArrayToBST_v2(self, nums):
        if len(nums) == 0:
            return None
        return self._helper(nums, 0, len(nums)-1)


    def _helper(self, nums, lo, hi):
        if lo > hi:
            return None

        mid = (hi + lo) // 2

        root = TreeNode(nums[mid])
        root.left = self._helper(nums, lo, mid - 1)
        root.right = self._helper(nums, mid + 1, hi)

        return root
