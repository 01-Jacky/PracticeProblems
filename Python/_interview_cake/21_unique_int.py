# In an array where ints appear twice except for 1 of them, find that unique int

"""
1) Naive, for each el check the rest of the array
Time: O(n^2)    Space: O(1)

2) Use a set/dict to keep track
Time: O(n)    Space: O(n)

3) Each # xor with another will cancel
Time: O(1)    Space: O(1)

"""

def find_single(arr):
    num = 0
    for el in arr:
        num = num ^ el
    return num


arr = [1,4,2,3,1,2,4]
print(find_single(arr))