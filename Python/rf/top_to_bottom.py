# Given an array, get from top left to bottom right if you can only move down and right.
import math
def numberOfPaths(m, n):
    # Combination
    if m > n:
        tmp = n
        n = m
        m = tmp

    # Combiation nCr = n!/r!(n-r)!
    # _n = m+n-2
    # _r = n-1
    # return math.factorial(_n)/(math.factorial(_r)*(math.factorial(_n-_r)))

    # Permutation
    _n = m-1
    _r = n-1
    return math.factorial(_n) / math.factorial(_n - _r)


# Driver program to test above function
m = 6
n = 6
print(numberOfPaths(m, n))

# def numberOfPaths(m, n):
#     # If either given row number is first or given column number is first
#     if (m == 1 or n == 1):
#         return 1
#
#     return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)    # Num of path going down + Num of path going
#
#
# # Driver program to test above function
# m = 3
# n = 3
# print(numberOfPaths(m, n))

# from itertools import permutations
#
# def numberOfPaths(m, n):
#     if m == 1 or n == 1:
#         return 1
#
#     choices = ['R' for x in range(m-1)]
#     choices += ['D' for x in range(n-1)]
#     print(choices)
#     perm = permutations(choices, (m-1)+(n-1))
#
#     # Debug
#     unique_paths = set(perm)
#     return len(unique_paths)
#
# print(numberOfPaths(10,4))


# n=3
# r=3
# print(math.factorial(n)/math.factorial(n-r))