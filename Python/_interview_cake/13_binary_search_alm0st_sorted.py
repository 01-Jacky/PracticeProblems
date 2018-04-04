"""
Find rotation point of an almost sorted array
e.g. [5,6,0,1,2,3,4]
"""

def find_rotation_point(words):
    first_word = words[0]

    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
        mid = floor_index + ((ceiling_index - floor_index) // 2)
        print('l: {} | h: {} | m: {} | 1st: {}'.format(words[floor_index], words[ceiling_index], words[mid],first_word))

        # if guess comes after first word or is the first word
        if words[mid] >= first_word:
            # go right
            print('words[mid] >= first_word, go right')
            floor_index = mid
        else:
            # go left
            print('words[mid] < first_word, go left')
            ceiling_index = mid

        # if floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            # between floor and ceiling is where we flipped to the beginning so ceiling is alphabetically first
            return ceiling_index


def bin_search(nums):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low+high)//2
        print('l: {} | h: {} | m: {}'.format(nums[low],nums[high], nums[mid]))
        if nums[mid] > nums[0]:        # Search value is smaller
            low = mid + 1
        elif nums[mid] < nums[0]:     # Search value is bigger
            high = mid - 1
    return low



nums = [7,8,0,1,2,3,4,5,6]
# nums = [3,4,5,6,7,8,0,1,2]

print(find_rotation_point(nums))
print(bin_search(nums))