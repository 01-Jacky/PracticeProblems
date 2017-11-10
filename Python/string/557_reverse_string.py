class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # list comprehension
        # reversed = [word[::-1] for word in s.split(' ')]
        # return ' '.join(reversed)

        # map and lambda
        # reversed_list = map((lambda word:word[::-1]), s.split(' '))
        # return ' '.join(reversed_list)

        # map and a helper
        # def _reverse(s):
        #     return s[::-1]
        #
        # reversed_list = map(_reverse, s.split(' '))
        # return ' '.join(reversed_list)

print(Solution().reverseWords('ab"c def xyz'))