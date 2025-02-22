class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n) for _ in range(m)]
        dp[0][0] = 1

        for col in range(1, n):
            dp[0][col] = dp[0][col - 1] if obstacleGrid[0][col] == 0 else 0
        
        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] if obstacleGrid[row][0] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]


        
