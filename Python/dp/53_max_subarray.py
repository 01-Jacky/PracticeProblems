class Solution(object):
    # Optimal Kadane
    # Time: O(n) Space: O(1)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_l = nums[0]
        max_g = nums[0]

        for i in range(1,len(nums)):
            max_l = max(nums[i], max_l + nums[i])
            max_g = max(max_g, max_l)
        return max_g

    # Brute force
    # Time: O(n^3) Space: O(1)
    # def maxSubArray(self, nums):
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
    #     max = nums[0]
    #     for i in range(0, len(nums)):
    #         sum = 0
    #         for j in range(i, len(nums)):
    #             sum +=  nums[j]
    #             if sum > max:
    #                 max = sum
    #     return max

    def maxSubArray_dp(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]

        max_so_far = nums[0]

        for i in range(1, len(nums)):
            # best at index i is either 1) we take num[i] + the best value we can do just before num[i], or just take num[i]
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_so_far = max(max_so_far, dp[i])         # see if we hit a new max

        return max_so_far

    def maxSubArray_dp_o1_space(self, nums):
        max_so_far = nums[0]
        prev_max = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(nums[i], nums[i] + prev_max)      # Dp formula: Either take nums[i] only or take it with previous max
            max_so_far = max(max_so_far, cur_max)           # Max record keeping
            prev_max = cur_max

        return max_so_far


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray_dp(arr))
print(Solution().maxSubArray_dp_o1_space(arr))
print(Solution().maxSubArray(arr))




# print(Solution().maxSubArray_dp([1,-2,3,-4,5]))