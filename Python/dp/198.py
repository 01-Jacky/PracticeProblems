"""
1) Brute force try all combinations

2) Use DP
At each house we either current house + best at 2 before, or best at prev one
xxxxxC...
     ^ we're here. Two options
xxxxxC...
   ^ ^ At C we can rob it. Then best is C + best at 2 before.
xxxxxC...
    ^  At C we don't rob it. Then best is whatever the answer was at one before

3) Use DP and optimize it
We don't really need to keep the whole array. Just prev 2.
"""

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
        # print(maxProfit)

    return maxProfit[-1]

def rob(nums):
    n = len(nums)

    if n < 2:
        return 0 if n == 0 else nums[0]

    cur_maxProfit = max(nums[0], nums[1])
    prev_prev_maxProfit = nums[0]
    prev_maxProfit = max(nums[0], nums[1])

    for i in range(2,len(nums)):
        cur_maxProfit = max(
            prev_prev_maxProfit + nums[i],       # Current house or best at
            prev_maxProfit)

        prev_prev_maxProfit = prev_maxProfit
        prev_maxProfit = cur_maxProfit

    return cur_maxProfit


# print(rob([6,9,8,3,4,5,6,1,2,100,1]))
print(rob([100,9,1,3,5,7,1,100]))
# print(rob([100,1,1,200]))
# print(rob([1,3,1]))
