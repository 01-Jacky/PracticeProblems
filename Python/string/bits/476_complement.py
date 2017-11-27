class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = "{0:b}".format(num)
        complement = ''.join(['1' if bit == '0' else '0' for bit in binary])
        return int(complement,2)

print(Solution().findComplement(2))