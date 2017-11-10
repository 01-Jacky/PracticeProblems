def get_palindrome_gt_3(s):
    max_palindrome_length = len(s)
    palindrome_lst = []

    for palindrome_length in range(1, max_palindrome_length+1):
        print('Checking palindrome of length: ' + str(palindrome_length))
        for i in range(0,len(s)-palindrome_length+1):
            substring = s[i:i+palindrome_length]
            if is_palindrome(substring):
                print(substring + " is a palindrome")
                palindrome_lst.append(substring)
            else:
                print(substring + " is NOT a palindrome")
    return palindrome_lst


def is_palindrome(s):
    c1 = 0
    c2 = len(s) - 1

    while c1 <= c2:
        # skip non-alphanumeric characters
        while c1 < c2 and not s[c1].isalnum():
            c1 += 1
        while c1 < c2 and not s[c2].isalnum():
            c2 -= 1

        # Ignore case
        if s[c1].lower() != s[c2].lower():
            return False
        else:
            c1 += 1
            c2 -= 1
    return True

print(get_palindrome_gt_3('aabaabaa'))