"""
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        s = s[::-1]
        for exponent, ch in enumerate(s):
            num_mapping = ord(ch) - ord('A') + 1        # A = 1, B = 2, etc...
            total += num_mapping * 26**exponent
        return total


print(Solution().titleToNumber('BA'))