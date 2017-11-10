def _get_inserted_values(s, c_to_insert):
    """ Generate list of possible strings by inserting c in each possible from i to i_max"""
    res = []
    for i in range(len(s)+1):
        # or something like this perm[:i] + [n] + perm[i:]
        char_arr = list(s)
        char_arr.insert(i, c_to_insert)
        res.append(''.join(char_arr))
    return res


def perm(s):
    """
    Idea: Start answer (list of perms) as 1 string with the first char.
    For the next character, take each element in ans and get the perms
    generated from it (by inserting it in each possible place).
    Given [1,2,3]
    [1]
    [21] [12] <--- take [1] and insert 2 into all possible indexes 0, 1 (e.g. [_1] [1_])
    [321] [231] [213] [312] [132] [123] <--- take [21] and insert 3 in each possible place. Do same for [12]
    etc.

    Time:   O(n^3)?
    Space:  O(n)
    """
    if len(s) <= 1:
        return [s]

    ans = [[s[0]]]
    for i in range(1, len(s)):
        tmp_ans = []                                    # print('inserting {} into indexes 0 to i={}'.format(s[i],i))
        for e in ans:
            perm_of_e = _get_inserted_values(e, s[i])   # e.g. given '12' and '3', insert 3 into all possible index in '12'
            tmp_ans.extend(perm_of_e)
    ans = tmp_ans                                       # print(tmp_ans)

    return ans


s = '123'
print(perm([c for c in s]))
g