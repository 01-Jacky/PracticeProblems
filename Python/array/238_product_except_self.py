class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = nums
        if len(arr)<2:
            return arr

        # build products before index
        products = [1]
        for i in range(1,len(arr)):
            products.append(products[i-1]*arr[i-1])

        # combine products before index with index after it
        curr_product = 1
        for i in range(len(arr)-1,-1,-1):
            products[i] *= curr_product
            curr_product *= arr[i]

        return products