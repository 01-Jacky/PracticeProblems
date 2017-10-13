""" https://leetcode.com/problems/path-sum/description/ """

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = self._int2bin(x)            # Self defined way
        y = '{:b}'.format(y)            # Python built in way to get a binary string

        len_dif = abs(len(x)-len(y))    # Pad shorter string with zeros on the left
        if len(x) > len(y):
            for i in range(len_dif):
                y = '0' + y
        else:
            x = x.zfill(len(y))         # Alternative way to pad string with 0's

        distance = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                distance += 1

        return distance

    def _int2bin(self, i):
        """ Use bitwise operation to generate binary representation"""
        if i == 0:
            return "0"

        s = ''
        while i:
            if i & 1 == 1:
                s = "1" + s
            else:
                s = "0" + s
            i = i/2                         # shifts bits down one, e.g. 101 -> 10

        return s


if __name__ == "__main__":
    s = Solution()
    print(s.hammingDistance(4, 10))
