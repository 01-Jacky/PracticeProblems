class Solution(object):
    def _get_next(self, s):
        ans = ''
        digit = s[0]
        count = 1

        for c in s[1:]:                     # Count repeats and flush when it's no longer a repeat
            if c == digit:
                count += 1
            else:
                ans += str(count) + digit
                digit = c
                count = 1

        ans += str(count) + digit           # Flush last sequence at the end
        return ans

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'
        for x in range(n - 1):
            start = self._get_next(start)
        return start

print(Solution().countAndSay(5))