class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        # dp[i][j]: 从dungeon[i][j]出发需要的initial health point
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        # 我们从dp[m - 1][n - 1]出发，只需要初始化它下面的值和它右边的值
        # 走到其他点时，因为其他的cell都初始化为了正无穷，已经经过并赋值的点永远是更小的那一方
        dp[m][n-1] = dp[m-1][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 我们选择需要更小的initial health point
                # [-8, 5] -> 13，之后需要5，现在需要8，总共需要13
                # [8, 5] -> 1，之后需要5，现在能提供8，最小initial health point为1就能cover
                # [5, 5] -> 1 (initial health point最小值为1)
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = 1 if need <= 0 else need

        return dp[0][0]

