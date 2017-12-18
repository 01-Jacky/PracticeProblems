class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c1 = 0
        c2 = len(s) - 1

        while c1 <= c2:
            # skip non-alphanumeric characters
            while c1 < c2 and not s[c1].isalnum():
                c1 += 1
            while c1 < c2 and not s[c2].isalnum():
                c2 -= 1

            if s[c1].lower() != s[c2].lower():
                return False
            else:
                c1 += 1
                c2 -= 1

        return True

    # def isPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     if len(s) % 2 == 0:
    #         center = len(s) // 2
    #         print(s[:center])
    #         print(s[:center] == s[center:][::-1])
    #     else:
    #         center = (len(s) // 2)
    #         print(s[:center] == s[center+1:][::-1])

Solution().isPalindrome('aabaa')