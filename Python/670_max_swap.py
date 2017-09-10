"""
https://leetcode.com/problems/add-digits/description/
"""


class Solution(object):
    def addDigits(self, num):
        """R
        :type num: int
        :rtype: int
        """
        while num >= 10:
            temp_sum = 0
            for digit_str in str(num):
                temp_sum += int(digit_str)
            num = temp_sum

        return num


if __name__ == "__main__":
    s = Solution()
    print s.addDigits(38)
