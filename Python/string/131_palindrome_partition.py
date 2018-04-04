class Solution():
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            substring_left = s[:i]
            substring_right = s[i:]
            if self.isPal(substring_left):
                self.dfs(substring_right, path+[substring_left], res)

    def isPal(self, s):
        return s == s[::-1]


print(Solution().partition('aab'))