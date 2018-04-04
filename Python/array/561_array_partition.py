"""
1) Sort and see
1 4 3 2
if we sort it
1 2 3 4
For 1, the best option is to take the next smallest number so we don't "waste" it
(1 2) (3 4)
(1,2) (3,4)
"""

class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()

        sum = 0
        for i in range(0,len(nums),2):
            sum += min(nums[i], nums[i+1])
        return sum(nums[::2])

    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])
