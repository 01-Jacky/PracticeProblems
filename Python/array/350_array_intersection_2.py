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



class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        1) Use Counter object
        2) Use hashmap to account for 1st array. Then 2nd array has intersect only if it is in the 1st.
        """
        map = {}
        for num in nums1:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        intersect = []
        for num in nums2:
            if num in map and map[num] > 0:
                intersect.append(num)
                map[num] -= 1

        return intersect

print(Solution().intersect([1,2,2,3],[2,2]))