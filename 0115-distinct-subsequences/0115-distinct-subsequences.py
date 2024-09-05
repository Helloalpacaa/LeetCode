class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for col in range(n + 1):
            dp[0][col] = 1

        for i in range(m):
            for j in range(n):
                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        
        return dp[m][n]