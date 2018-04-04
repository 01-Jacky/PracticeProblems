class Solution:
    def removeDuplicates(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] != nums[i - 1]:
                nums[i-count] = nums[i]     # If different, i
            else:
                count += 1                  # Else keep track of uniques

        return len(nums) - count


    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        i = 0
        j = 1
        while j < len(nums):
            # Use j to move up until the next non-duplicate
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]   # If j is ahead only by 1 this assignement doesn't change anything
                j += 1
            else:
                j += 1

        return i + 1

nums = [1,2,3,3,4,5,5,5,6]
print(Solution().removeDuplicates(nums))
print(nums)