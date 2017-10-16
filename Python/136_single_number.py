class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = set()
        unique_nums.add(nums[0])

        for n in nums[1:]:
            if n in unique_nums:
                unique_nums.remove(n)
            else:
                unique_nums.add(n)

        return unique_nums.pop()

        # More clever solution
        # 2*(a+b+c) - (a+a+b+c+c) = b
        # return 2 * sum(set(nums)) - sum(nums)


assert Solution().singleNumber([1]) == 1
assert Solution().singleNumber([2,2,1]) == 1