def reverse(x):
    result = 0

    if x < 0:                                   # Negatuve mod does weird shit in python
        x = x*-1
        negative_result = True

    while x != 0:                               # Say we have 123 to reverse
        tail_digit = x % 10                     # Strip the last digit. 3
        result = result * 10 + tail_digit       # result * 10 moves it over left 1 digit. Then plugs in the tail digit.
        x = x//10                               # shrinks the number to read from 123 to 12

    if result > 2**31:                          # overflow hack to act like other language
        return 0

    if negative_result:
        return result * -1
    else:
        return result


print(reverse(-123))