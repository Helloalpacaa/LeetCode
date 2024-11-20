class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        # dp[i][j]: minimum number os steps to make s[i: j] palindrome
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        
        return dp[0][n - 1]