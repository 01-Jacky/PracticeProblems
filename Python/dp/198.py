def rob(nums):
    n = len(nums)

    if n < 2:
        return 0 if n == 0 else nums[0]

    maxProfit = [0]*len(nums)
    maxProfit[0] = nums[0]
    maxProfit[1] = max(nums[0], nums[1])

    for i in range(2,len(nums)):
        maxProfit[i] = max(
            maxProfit[i-2] + nums[i],       # Current house or best at
            maxProfit[i-1])
        print(maxProfit)

    return maxProfit[-1]

# print(rob([6,9,8,3,4,5,6,1,2,100,1]))
print(rob([100,9,1,3,5,7,1,100]))
# print(rob([100,1,1,200]))