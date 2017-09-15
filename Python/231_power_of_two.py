"""
https://leetcode.com/problems/power-of-two/discuss/
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False;

        while n % 2 == 0:
            n /= 2

        return n == 1


if __name__ == "__main__":
    s = Solution()
    print Solution().isPowerOfTwo(4)