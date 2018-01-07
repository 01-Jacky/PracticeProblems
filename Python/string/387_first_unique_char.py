class Solution:
    def firstUniqChar(self, s):
        """
        1) Brute force
        Time O(N^2) Space O(1)

        2) Sort and check
        Time O(nlgn) Space O(n)

        3) Set
        Time O(N) Space O(1)
        """
        freq = [0]*26

        # Count freq
        for ch in s:
            index = ord(ch) - ord('a')      # 0=a, 1=b, etc.
            freq[index] += 1

        # Return first unique char
        for i, ch in enumerate(s):
            index = ord(ch) - ord('a')      # 0=a, 1=b, etc.
            if freq[index] == 1:
                return i

        return -1

print(Solution().firstUniqChar('leetcode'))
print(Solution().firstUniqChar('loveleetcode'))


