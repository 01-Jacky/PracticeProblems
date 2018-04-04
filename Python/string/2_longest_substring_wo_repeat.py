"""
say each x is unique
start a tail pointer so the unique char substring is from ^ up to the char you're processing
xxxxxxx
^------
length of uniques is just from ^ to end

say we finally encounter a dup char, indicated as D
DxxxxxD
^------
If we kept track of indexes of each unique character, we lookup where ^ is and move it up 1.
DxxxxxD
 ^-----
New window is again ^ to end. The 1st appearance of the dup is now out of the window

xx....xDxxx...xxx
       ^---------
xx....xDxxx...xxxD
        ^---------
this works no matter where the dup is encountered

xxxDDD
     ^
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        index_map = {}        # ch -> index
        max_len = 0

        j = 0
        for i in range(len(s)):
            cur_char = s[i]

            if cur_char in index_map:               # If we encountered a duplicate, move window one pass the first occurance
                j = max(j, index_map[s[i]] + 1)

            index_map[s[i]] = i                     # Update the character's latest index
            cur_unique_substring_len = i-j+1
            max_len = max(max_len, cur_unique_substring_len)

        return max_len

# print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('abcada'))