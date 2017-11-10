def is_alphanumeric(c):
    valid = set()

    for i in range(10):
        valid.add(str(i))

    start_ascii_int = ord('a')
    for x in range(start_ascii_int, start_ascii_int+26):
        valid.add(chr(x))

    if c in valid:
        return True
    else:
        return False

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

if __name__ == "__main__":
    assert is_palindrome('aba') is True
    assert is_palindrome('abc') is False
    assert is_palindrome('abba') is True
    assert is_palindrome('abcba') is True
    assert is_palindrome('aaddbb') is False
    assert is_palindrome('aaddaa') is True
    assert is_palindrome('a.') is True
    assert is_palindrome(' ') is True
    assert is_palindrome('.,') is True


z = '0'
print(is_alphanumeric(z))

