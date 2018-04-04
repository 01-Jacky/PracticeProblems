class Solution:
    def threeSum(self, nums):
        if len(nums) <= 1:
            return []

        ans = []
        for i in range(len(nums)):
            a = nums[i]

            # Now do 2 sum where -a is the target because: a+b+c=0 -> b+c=-a -> c = -a - b
            bag = set()                             # Stores number -> index
            for j in range(i+1,len(nums)):
                val_required = -a - nums[j]

                if val_required not in bag:
                    bag.add(nums[j])
                else:
                    list_to_add = [a, nums[j], val_required]

                    exist = False
                    for existing_list in ans:
                        if set(list_to_add) == set(existing_list):
                            exist = True
                            break

                    if not exist:
                        ans.append(list_to_add)

        return ans


arr = [-1, 0, 1, 2, -1, -4]
Solution().threeSum(arr)