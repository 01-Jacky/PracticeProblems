class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        res = []
        for n in range(left, right + 1):
            if self.is_self_dividing(n):
                res.append(n)
        return res


    def is_self_dividing(self, n):
        for c in str(n):
            if c == '0' or n % int(c) != 0:
                return False
        return True



print(Solution().selfDividingNumbers(1,22))