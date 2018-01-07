"""
1) Use 2 references
Note: String are inmutable so we must pass in an array of ch if we want to do it inplace
Time: O(n)    Space:O(1)
"""

def reverse_inplace(ch_arr):
    if len(ch_arr) < 2:
        return ch_arr

    beg = 0
    end = len(ch_arr) - 1

    while beg < end:
        tmp = ch_arr[beg]
        ch_arr[beg] = ch_arr[end]
        ch_arr[end] = tmp

        beg += 1
        end -= 1



arr = list("hello world")
reverse_inplace(arr)


print(''.join([ch for ch in arr]))