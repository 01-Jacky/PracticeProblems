# def _get_1s(n):
#     count = 0
#     binary = "{0:b}".format(n)
#     for c in binary:
#         if c == '1':
#             count += 1
#     return count
#
#
# def rearrange(nums):
#     # Python sorted uses a stable sort
#     # nums = sorted(nums)
#     return sorted(nums, key=_get_1s)
#
# print(rearrange([1,2,3]))
# print(rearrange([5,3,7,10,14]))

def _get_1s(n):
    count = 0
    binary = "{0:b}".format(n)

    for c in binary:
        if c == '1':
            count += 1
    return count


def rearrange(nums):
    # First sort by count of binary 1 of num, then by decimal value of num
    return sorted(nums, key=lambda num: (_get_1s(num), num))


print(rearrange([1,2,3]))
print(rearrange([5,3,7,10,14]))