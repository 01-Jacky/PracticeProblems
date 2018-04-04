def decrypt_string(string, mapping):
    int_string = ""
    for c in string:
        int_string += mapping[c]

    return int_string


def isCryptSolution(crypt, solution):
    mapping = {s: i for s, i in solution}
    s1_num = decrypt_string(crypt[0], mapping)
    s2_num = decrypt_string(crypt[1], mapping)
    s3_num = decrypt_string(crypt[2], mapping)

    check = [s1_num, s2_num, s3_num]  # Constraint: Check for leading zero if more than 1 ch
    for s in check:
        if len(s) > 1 and s[0] == '0':
            return False

    s3_check = int(s1_num) + int(s2_num)  # Solution check
    if str(s3_check) == s3_num:
        return True
    else:
        return False


