def houseRobber(nums):
    if len(nums) == 0:
        return 0
    if len(nums) < 2:
        return max(nums)

    # Build up answer bottom up
    dp = [0] * len(nums)
    for i in range(len(nums)):
        cur_house_value = nums[i]

        value_rob = cur_house_value + dp[i-2]
        value_not_rob = dp[i-1]

        dp[i] = max(value_rob, value_not_rob)

    return dp[-1]

arr = [1, 3, 1, 3, 100]     # ans = 103
arr = []
print(houseRobber(arr))