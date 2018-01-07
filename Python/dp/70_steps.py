class Solution:
    """
    1) naive recursion
    Time O(2^n) Space O(2^n)
    2) recursion + memorization

    3) dp
    """

    # 1) naive recur
    def climbStairs(self, n):
        return self._climbStairs_helper(0, n)

    def _climbStairs_helper(self, i, n):
        if i == n:
            return 1
        if i > n:
            return 0

        return self._climbStairs_helper(i+1,n) + self._climbStairs_helper(i+2, n)

    # 2) memorization
    def climbStairs(self, n):
        mem = [0]*(n+1)
        return self._climbStairs_helper(0, n, mem)

    def _climbStairs_helper(self, i, n, mem):
        if i == n:
            return 1
        if i > n:
            return 0
        if mem[i] > 0:          # fetch memorization if possible
            return mem[i]

        mem[i] = self._climbStairs_helper(i+1,n,mem) + self._climbStairs_helper(i+2,n,mem)
        return mem[i]

    # 3) dp
    def climbStairs(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    # 3) dp
    def climbStairs(self, n):
        a = 1
        b = 1
        for i in range(n-1):
            a, b = b, a+b
        return b

print(Solution().climbStairs(2))
