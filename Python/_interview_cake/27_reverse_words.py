"""
1) Find indexes of the two words to swap, and scott them over as needed
Note: String are inmutable so we must pass in an array of ch if we want to do it inplace
Time: O(n^2)    Space:O(1)
"""

def reverse_words(arr):
    reverse_inplace(arr, 0, len(arr)-1)

    index_start = 0
    for index_end in range(len(arr) + 1):
        if (index_end == len(arr)) or (arr[index_end] == ' '):
            reverse_inplace(arr, index_start, index_end - 1)
            index_start = index_end + 1


def reverse_inplace(ch_arr, beg, end):
    if end - beg < 1:
        return ch_arr

    while beg < end:
        tmp = ch_arr[beg]
        ch_arr[beg] = ch_arr[end]
        ch_arr[end] = tmp

        beg += 1
        end -= 1


arr = list("I am dog")
reverse_words(arr)

print(''.join([ch for ch in arr]))