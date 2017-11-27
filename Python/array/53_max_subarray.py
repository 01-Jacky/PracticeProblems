class Solution(object):
    # Optimal Kadane
    # Time: O(n) Space: O(1)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_l = max_g = nums[0]
        for i in range(1,len(nums)):
            max_l = max(nums[i], max_l + nums[i])
            max_g = max(max_g, max_l)
        return max_g

    # Brute force
    # Time: O(n^3) Space: O(1)
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     max = nums[0]
    #     for i in range(0, len(nums)):
    #         for j in range(i, len(nums)):
    #             sum = 0
    #             for k in range(i, j):
    #                 sum += nums[k]
    #             if sum > max:
    #                 max = sum
    #     return max

    # Brute force slightly better
    # Time: O(n^2) Space: O(1)
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     max = nums[0]
    #     for i in range(0, len(nums)):
    #         sum = 0
    #         for j in range(i, len(nums)):
    #             sum +=  nums[j]
    #             if sum > max:
    #                 max = sum
    #     return max

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([1,-2,3,-4,5]))