class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        # 0: max profit of buy in day 1
        # 1: max profit of sell in day 1
        dp[0][0] = -prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        
        print(dp)
        return dp[n - 1][1]