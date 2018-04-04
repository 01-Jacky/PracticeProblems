class Solution:
    def uniquePaths(self, m, n):
        """ DFS """
        stack = []
        count = 0
        stack.append((0,0))

        while stack:
            popped = stack.pop()
            if popped == (m-1, n-1):
                count += 1

            row, col = popped
            if col < n:
                stack.append((row, col+1))
            if row < m:
                stack.append((row+1, col))

        return count


    def uniquePaths(self, m, n):
        """ Math """
        import math
        if m > n:
            m, n = n, m

        # Combiation nCr = n!/r!(n-r)!
        _n = m+n-2
        _r = n-1
        return math.factorial(_n)/(math.factorial(_r)*(math.factorial(_n-_r)))

    def uniquePaths(self, m, n):
        """ DP """
        dp = [[None] * n for _ in range(m)]

        row = m
        col = n

        # Fill right most col and bottom most row
        for i in range(row):
            dp[i][col-1] = 1
        for i in range(col):
            dp[m-1][i] = 1

        # Fill out dp
        for i in range(col-2, -1, -1):
            for j in range(row-2, -1, -1):
                dp[j][i] = dp[j][i+1] + dp[j+1][i]

        return dp[0][0]

    def uniquePaths(self, m, n):
        """ DP more optimized by init everything as 1"""
        dp = [[1] * n for _ in range(m)]
        row = m
        col = n

        # Fill out dp
        for i in range(col-2, -1, -1):
            for j in range(row-2, -1, -1):
                dp[j][i] = dp[j][i+1] + dp[j+1][i]

        return dp[0][0]

print(Solution().uniquePaths(23,12))
