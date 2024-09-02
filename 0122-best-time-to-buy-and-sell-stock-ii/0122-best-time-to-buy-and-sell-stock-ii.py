class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            dp[i][0] = -prices[i] #买
            dp[i][1] = max(0, dp[i - 1][0] + prices[i])
        
        return sum(dp[i][1] for i in range(n))