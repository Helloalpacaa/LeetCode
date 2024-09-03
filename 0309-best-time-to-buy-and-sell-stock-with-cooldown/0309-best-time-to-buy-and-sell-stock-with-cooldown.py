class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 4 for _ in range(n)]
        dp[0][0] = -prices[0]
        # dp[i][0]: hold the stock, either dp[i - 1][0], or purchase it at day i
        # dp[i][1]: not_hold the stock, after the cooldown, either dp[i - 1][1] or dp[i - 1][3]
        # dp[i][2]: sell at day i, so it can only be dp[i - 1][0] + price[i]
        # dp[i][3]: cooldown, can only be dp[i - 1][2]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][1], dp[i - 1][3]) - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = dp[i - 1][0] + prices[i]
            dp[i][3] = dp[i - 1][2]

        return max(dp[n - 1][1], dp[n - 1][2], dp[n - 1][3])