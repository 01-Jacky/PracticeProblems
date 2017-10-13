import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        ans = ''

        if str_x[0] == '-':
            ans += '-'
            str_x = str_x[1:]

        for ch in str_x[::-1]:
            ans += ch

        ans = int(ans)

        if math.fabs(ans) > math.pow(2,31)-1:   # Python won't overflow but guard against anyway
            ans = 0

        return int(ans)

if __name__ == "__main__":
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(1534236469) == 0
    assert Solution().reverse(-2147483648) == 0