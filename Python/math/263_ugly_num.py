"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""

import collections
def intersect(nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    z = a&b
    elements = (a&b).elements()
    return list((a & b).elements())

print(intersect([1,2,2,5], [5,2]))