"""
4 hello
2 ll
4-2 = 2
"""


class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0

        for i in range((len(haystack) - len(needle) + 1)):
            # Might have found a needle
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        break

                    # If all the ch in the needle matches
                    if j == len(needle)-1:
                        return i

        return -1


print(Solution().strStr('"mississippi','issip'))