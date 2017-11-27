# 1 -> A
# 2 -> B
# 3 -> C
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB
class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        else:
            num = n-1 // 26
            print('num {}'.format(num))
            tmp = self.convertToTitle((n - 1) // 26)
            tmp2 = chr((n - 1) % 26 + ord('A'))
            return tmp + tmp2

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = []
        while n:
            n = n-1
            remain = n % 26
            ans.append(chr(ord('A')+remain))    # convert remainder to char. Add -1 because 1=A 2=B... so offset by -1
            n = n // 26
        return ''.join(ans[::-1])



# assert Solution().convertToTitle(28) == 'AB'
print(Solution().convertToTitle(700))