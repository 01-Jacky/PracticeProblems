from collections import deque
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        max_reach = nums[i]
        jumps = 0

        while i < len(nums)-1:
            jumps += 1
            start = i+1
            end = min(max_reach+1, len(nums))

            for x in range(start, end):
                i += 1
                if x+nums[x] > max_reach:
                    max_reach = x + nums[x]

        return(jumps)

# print(Solution().jump([5,6,0,4,2,4,1,0,0,4]))
print(Solution().jump([5,6,0,4,2,4,1,0,0,4]))
# print(Solution().jump([2,3,1,1,2,4,2,0,1,1]))
# Solution().jump([1,3,1,1,4])
# print(Solution().jump([1,1,1,1,1,1]))
# print(Solution().jump([2,1]))
# print(Solution().jump([1,2,3]))

