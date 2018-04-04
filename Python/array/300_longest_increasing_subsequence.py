class Solution(object):
    # def bin_search(self, nums):

    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0

        for x in nums:
            i = 0
            j = size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
            print(tails)

        return size

arr = [4,5,6,3]
# arr = [1,3,5,2,8,9,4,6]
print(Solution().lengthOfLIS(arr))