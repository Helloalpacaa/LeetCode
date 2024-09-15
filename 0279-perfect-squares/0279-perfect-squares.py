class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = i
        
        for i in range(int(sqrt(n)) + 1):
            dp[i * i] = 1
        
        for i in range(n + 1):
            for j in range(int(sqrt(i)) + 1):
                perfectSquare = j * j
                dp[i] = min(dp[i], dp[i - perfectSquare] + 1)

        return dp[n]