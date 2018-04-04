class Solution:
    def myPow(self, x, n):
        iterations = n
        if n == 0:
            return 1
        if n < 0:
            iterations = n*-1

        result = 1
        for _ in range(iterations):
            result *= x

        if n > 0:
            return result
        else:
            return 1/result


print(Solution().myPow(34.00515,-3))