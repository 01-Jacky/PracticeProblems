class Solution:
    """
    1) Math. Sum of consective nums = n*(n+1) / 2

    2) XOR
    1 2 3 ... 10
    Start with

    3) Incrementingally sum-subtract
    0 1 2 ... 10 iterativey add these
    [....]       iteratively subtract these
    """
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = int((n * (n + 1)) / 2)
        return expected_sum - sum(nums)


    def missingNumber(self, nums):
        missing = len(nums)             # Because the loop will xor 0,1,2... n-1. So we provide the n.
        for i in range(len(nums)):
            print(i)
            missing = missing ^ i ^ nums[i]
        return missing


    def missingNumber(self, nums):
        missing = len(nums)
        for i in range(len(nums)):
            missing = missing + i - nums[i]
        return missing

print(Solution().missingNumber([3,0,1]))