class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][0]: 第i天持有股票的最大profit
        # dp[i][1]: 第i天不持有股票的最大profit
        # dp = [[0] * 2 for _ in range(n)]
        # dp[0][0] = -prices[0]

        # for i in range(1, n):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        
        # return dp[n - 1][1]

        hold = -prices[0]
        not_hold = 0

        for i in range(1, n):
            hold = max(hold, not_hold - prices[i])
            not_hold = max(not_hold, hold + prices[i])

        return not_hold