"""
1) For each pair, get shortest prefix
leetcode leetcore leeter lee
         leetc    leet   lee    return the lsat one
"""

class Solution:
    def _get_common_prefix(self, s1, s2):
        index = 0
        prefix = []

        while index < len(s1) and index < len(s2):
            if s1[index] == s2[index]:
                prefix.append(s1[index])
                index += 1
            else:
                break

        return ''.join(prefix)

    def longestCommonPrefix(self, strs):
        if len(strs) < 2:
            return strs[0]

        common_prefix = strs[0]
        for i in range(len(strs)-1):
            common_prefix = self._get_common_prefix(common_prefix, strs[i+1])
        return common_prefix

    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''

        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i][:len(prefix)] != prefix:
                prefix = prefix[:-1]
        return prefix

# print(Solution()._get_common_prefix('leet','leetcode'))
print(Solution().longestCommonPrefix(['leetsauce','leetcode','leetc']))

