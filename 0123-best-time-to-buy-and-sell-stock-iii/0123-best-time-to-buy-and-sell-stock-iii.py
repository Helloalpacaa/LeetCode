class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 解法一，用二维dp数组
        # dp[i][0]: 截止到第i天第一次持有的最大利润
        # dp[i][1]: 截止到第i天第一次未持有的最大利润
        # dp[i][2]: 截止到第i天第二次持有的最大利润
        # dp[i][3]: 截止到第i天第二次未持有的最大利润
        n = len(prices)
        dp = [[0] * 4 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i][1] - prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i][2] + prices[i])
        
        return dp[n - 1][3]