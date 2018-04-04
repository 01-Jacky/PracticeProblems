class Solution:
    """
    nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

    1) sorting
    0 0 1 3 12
    move zeros
    1 3 12 0 0
    space n time nlogn :/

    2) use extra space and only copy over non zero
    0, 1, 0, 3, 12
    init new array full of 0
    0 0 0 0 0
    iterate once and only replace non zeros
    1 3 12 0 0
    time O(n) space O(n))

    3) find the first zero to swap with
    a=0
    i=1
    0, 1, 0, 3, 12
    swap
    1, 0, 0, 3, 12
    a=1
    i=4
    swap
    1 3 0 0 12
    a = 2
    i=5
    swap
    1 3 12 0 0
    Time O(n) Space O(1)

    4)move nums to the left using 2 pointers
    prev = 0
    0 1 0 3 12
    1 1 0 3 12      copied 1 into index 0
    prev = 1
    1 3 0 3 12      copied 3 into index 1
    prev = 2
    1 3 12 3 12     copied 12 into index 2
    prev = 3

    Done with 1st loop. Now start after where prev index left off and wipe it with 0s
    prev was index 3, so from 3 and on make everything 0
    1 3 12 0 0
    Time O(n) Space O(1)

    """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Use 2 pointers and move the numbers to the left
        last_non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1

        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0

    def moveZeroes(self, nums):
        """
        Swap if needed
        """
        # Use 2 pointers and move the numbers to the left
        last_non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index], nums[i] = nums[i], nums[last_non_zero_index], # swap
                last_non_zero_index += 1


arr = [0, 1, 0, 3, 12]
# arr = [2,1]
Solution().moveZeroes(arr)
print(arr)