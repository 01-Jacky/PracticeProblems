def bin_search(search_value, nums):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low+high)//2
        print('l: {} | h: {} | m: {}'.format(nums[low],nums[high], nums[mid]))
        if nums[mid] < search_value:        # Search value is smaller
            low = mid + 1
        elif nums[mid] > search_value :     # Search value is bigger
            high = mid - 1
        else:                               # Not bigger or smaller then it's exactly correct
            return mid
    return -1


nums = [i for i in range (0,9)]
print(bin_search(2,nums))