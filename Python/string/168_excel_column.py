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
            n = n-1                         # -1 because using # of offset from A. A=0 offset from A,, B=2 offset From A...
            n = n // 26                     # Try to move a digit via base 26
            remain = n % 26
            ascii_code = ord('A')+remain
            ans.append(chr(ascii_code))     # convert remainder to char.
        return ''.join(ans[::-1])



# assert Solution().convertToTitle(28) == 'AB'
print(Solution().convertToTitle(1000))