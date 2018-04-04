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


def permute(s):
    # base case
    if len(s) == 1:
        return set([s])

    # call recursion to get permutations using all but last char
    permutations_except_1st = permute(s[1:])

    # for each returned permutation, insert the left out character into each place
    permutations = set()
    for permutation in permutations_except_1st:
        for i in range(len(permutation)+1):
            result = permutation[:i] + s[0] + permutation[i:]
            permutations.add(result)

    return permutations


# print(get_permutations('abc'))
print(permute('abc'))

# print(permute('cats'))