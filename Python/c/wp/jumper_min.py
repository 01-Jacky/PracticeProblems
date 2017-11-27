class Solution(object):
    def _get_min_jump(self, start, end, min_jump_arr):
        min = float('inf')
        for j in range(start+1, end+1):
            if min_jump_arr[j] < min:
                min = min_jump_arr[j]+1
        return min


    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_jumps = [None] * len(nums)
        min_jumps[-1] = 0

        for i in range(len(nums)-2,-1,-1):
            max_jump = nums[i]

            if max_jump == 0:
                min_jumps[i] = float('inf')
            else:
                farthest_index = min(len(nums)-1, i+max_jump)
                min_jumps[i] = self._get_min_jump(i, farthest_index, min_jumps)
                # print(min_jumps)

        return min_jumps[0]

# print(Solution().jump([2,3,1,1,4]))
# print(Solution().jump([1,2,0,1]))
import time

start = time.time()

x = [x for x in range(99999999,0,-1)]
# print(x)
print(Solution().jump([x for x in range(9,0,-1)]))

end = time.time()
print(end - start)
