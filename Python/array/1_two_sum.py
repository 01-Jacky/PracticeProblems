class Solution(object):
    def twoSum(self, nums, target):
        """ Return indices """
        if len(nums) <= 1:
            return False

        table = {}                                  # Stores number -> index
        for i in range(len(nums)):
            val_required = target - nums[i]

            if val_required in table:
                return [table[val_required], i]
            else:
                table[nums[i]] = i

    def twoSum_return_values(self, nums, target):
        """ Return values """
        if len(nums) <= 1:
            return False

        bag = set()  # Stores number -> index
        for i in range(len(nums)):
            val_required = target - nums[i]

            if val_required in bag:
                return [val_required, nums[i] ]
            else:
                bag.add(nums[i])

print(Solution().twoSum_return_values([1,2,3,4,5],6))


