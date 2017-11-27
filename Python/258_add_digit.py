"""
https://leetcode.com/problems/add-digits/description/
"""


class Solution(object):
    def addDigits(self, num):
        """R
        :type num: int
        :rtype: int
        """
        # while num >= 10:
        #     temp_sum = 0
        #     for digit_str in str(num):
        #         temp_sum += int(digit_str)
        #     num = temp_sum
        #
        # return num
        digits = [int(c) for c in str(num)]
        while len(digits) > 1:
            sum = 0
            for d in digits:
                sum += d
            digits = [int(c) for c in str(sum)]

        return digits[0]


if __name__ == "__main__":
    s = Solution()
    print(s.addDigits(103599))
