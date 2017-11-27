""" https://leetcode.com/problems/path-sum/description/ """


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # slow
        # for i in range(k % len(nums)):
        #     nums[:] = nums[-1:] + nums[:-1]

        # faster
        # [1,2,3,4] rotate n times means last n element get removed and put forward
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6,7,8,9,10]

    s.rotate(nums, 1)
    print nums
