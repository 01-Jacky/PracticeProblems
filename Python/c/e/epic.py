# You will be given a string, containing both uppercase and lowercase alphabets(numbers are not allowed).
# You have to print all permutations of string with the added constraint that you can’t
# change the uppercase alphabets positions.

def get_perm(s):
    perms = []
    for i in range(len(s)):
        perms.append(s[i])

    return perms

# DFS
def valid_perm(s, nums, captial_indexes):
    for i in captial_indexes:
        if s[i] != nums[i]:
            return False
    return True

def permute(nums):
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        dfs(nums[:i] + nums[i + 1:],
            path + [nums[i]],
            res)

x = 'aACzdz'
captial_indexes = [i for i in range(len(x)) if 'A' <= x[i] <= 'Z']
x = [x for x in x]

ans = []
for e in permute(x):
    if valid_perm(e,x,captial_indexes):
        ans.append(e)

for e in ans:
    print(e)