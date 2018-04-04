class Solution(object):
    def findPeakElement(self, nums):
        return self._helper(nums, 0, len(nums)-1)

    def _helper(self, nums, lo, hi):
        if lo == hi:
            return nums[lo]

        mid = (lo+hi) // 2
        x = nums[mid]
        y = nums[mid+1]
        if nums[mid] < nums[mid+1]:     # peak must be to the right
            return self._helper(nums, mid+1, hi)
        else:
            return self._helper(nums, lo, mid)

arr = [1,3,9,8,4,30,34,3,1]

print(Solution().findPeakElement(arr))