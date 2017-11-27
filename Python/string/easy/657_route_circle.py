class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0

        for c in moves:
            if c == 'R':
                x += 1
            elif c == 'L':
                x -= 1
            elif c == 'U':
                y += 1
            elif c == 'D':
                y -= 1

        return x == 0 and y == 0


assert Solution().judgeCircle('UDLR') is True
assert Solution().judgeCircle('UDL') is False
assert Solution().judgeCircle('') is True
assert Solution().judgeCircle('UUUDDD') is True