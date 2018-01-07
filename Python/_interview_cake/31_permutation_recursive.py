"""
Solution:
1) Recursively reduce to base case and then insert new char
"""

def get_permutations(s):
    # base case
    if len(s) <= 1:
        return set([s])

    chars_except_last = s[:-1]
    last_char = s[-1]

    # recursive call: get all possible permutations for all chars except last
    permutations_except_last_ch = get_permutations(chars_except_last)
    print(permutations_except_last_ch)

    # insert last char in all possible positions for each of the above permutations
    permutations = set()
    for permutation_except_last_ch in permutations_except_last_ch:
        for position in range(len(chars_except_last) + 1):  # for each position
            permutation = permutation_except_last_ch[:position] + last_char + permutation_except_last_ch[position:]
            permutations.add(permutation)

    return permutations


# def permute(nums):
#     res = []
#     dfs(nums, [], res)
#     return res
#
# def dfs(nums, path, res):
#     if not nums:
#         res.append(path)
#         # return # backtracking
#     for i in range(len(nums)):
#         dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
#     return res


print(get_permutations('abc'))

# print(permute('cats'))