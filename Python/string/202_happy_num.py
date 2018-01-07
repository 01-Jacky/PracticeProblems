"""
A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

There could be a loop
"""

class Solution:

    def _get_digit_square_sums(self, n):
        total = 0
        for digit_ch in str(n):
            total += int(digit_ch)**2
        return total


    def isHappy(self, n):
        n = str(n)
        seen = set()

        while n not in seen:
            seen.add(n)
            total = self._get_digit_square_sums(n)
            if total == 1:
                return True
            else:
                n = total

        return False

print(Solution().isHappy(19))


