"""
(]

"""
class Solution:
    def isValid(self, s):
        buffer = []
        brackets = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            # push open into buffer if open
            if ch in brackets.values():
                buffer.append(ch)

            # if not check what was last in the buffer
            if ch in brackets:
                if len(buffer) <= 0:
                    return False

                if brackets[ch] == buffer[-1]:
                    buffer.pop()
                else:
                    return False

        if buffer:
            return False
        else:
            return True


print(Solution().isValid('(])'))