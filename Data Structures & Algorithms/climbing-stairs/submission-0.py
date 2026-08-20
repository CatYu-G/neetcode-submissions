class Solution:
    def climbStairs(self, n: int) -> int:
        #状态转移方程，看这个那我们就看前一个要多久
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        #4
        #0 0 0 0 0
        #0 1 2
        return dp[n]