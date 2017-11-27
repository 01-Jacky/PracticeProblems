from collections import deque
class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        steps = 0

        while j < len(nums):
            endj = min(nums[i]+i+1, len(nums))          # Get next start or end of array
            while j < endj:
                if nums[j] + j > nums[i] + i:
                    i = j
                j += 1
            steps += 1
        return steps

print(Solution().jump([2,3,1,1,4]))
# print(Solution().jump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
