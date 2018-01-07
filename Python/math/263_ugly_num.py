import collections
def intersect(nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    z = a&b
    elements = (a&b).elements()
    return list((a & b).elements())

print(intersect([1,2,2,5], [5,2,1,2]))