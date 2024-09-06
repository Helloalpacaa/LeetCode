class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心：取最左最小值，取最右最大值，那么得到的差就是最大利润
        # profit = 0
        # minValue = float('inf')

        # for price in prices:
        #     minValue = min(minValue, price)
        #     profit = max(profit, price - minValue)

        # return profit

        # dp[i][0]: 第i天持有股票的利润
        # dp[i][1]: 第i天不持有股票的利润
        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n)]
        # dp[0][0] = -prices[0]

        # for i in range(1, n):
        #     dp[i][0] = max(dp[i - 1][0], - prices[i])
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        
        # return dp[n - 1][1]

        hold = -prices[0]
        not_hold = 0

        for i in range(1, len(prices)):
            hold = max(hold, -prices[i])
            not_hold = max(not_hold, hold + prices[i])

        return not_hold

