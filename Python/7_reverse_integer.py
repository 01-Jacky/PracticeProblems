import math
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            ans = int(str(x)[1:][::-1]) * -1
        else:
            ans = int(str(x)[::-1])

        return ans if -(2**31)-1 < ans < 2**31 else 0

    def reverse(self, x):
        negative = True if x < 0 else False
        x = abs(x)

        result = 0
        while x != 0:
            last_digit = x % 10
            result = result * 10 + last_digit
            x = x // 10

        if negative:
            result *= -1

        return result if -(2**31)-1 < result < 2**31 else 0


if __name__ == "__main__":
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(1534236469) == 0
    assert Solution().reverse(-2147483648) == 0
    assert Solution().reverse(-1534236469) == 0
