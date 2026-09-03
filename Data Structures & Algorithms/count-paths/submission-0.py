class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个 m x n 的表格，初始值全部填0
        dp = [[0] * n for _ in range(m)]
        
        # 第一行和第一列，路径数都是1
        for i in range(m):
            dp[i][0] = 1        # 最左边一列
        for j in range(n):
            dp[0][j] = 1        # 最上面一行
        
        # 从(1,1)开始填表，因为第0行和第0列已经填好了
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # 右下角就是答案
        return dp[m-1][n-1]