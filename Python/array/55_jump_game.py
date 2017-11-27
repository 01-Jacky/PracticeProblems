import math

class Solution(object):
    # Approach 1
    # def canJump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     jumps_remain = 0
    #     for k, el in enumerate(nums):
    #         if el >= jumps_remain:
    #             jumps_remain = el
    #         else:
    #             jumps_remain -= 1
    #
    #         if jumps_remain <= 0 and k != len(nums)-1:
    #             return False
    #     return True

    #Approach 2
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable_index = 0
        for i, el in enumerate(nums):
            reachable_index = max(reachable_index, i+el)
            if i >= reachable_index and i != len(nums)-1:
                return False
        return True

assert Solution().canJump([2,3,1,1,4]) == True
assert Solution().canJump([3,2,1,0,4]) == False
assert Solution().canJump([2,0]) == True
assert Solution().canJump([2,0,0]) == True
assert Solution().canJump([1,2]) == True
assert Solution().canJump([0,1]) == False
assert Solution().canJump([1,1,1,0]) == True
# 01234
# 23114
# 2434
#
# max = 4