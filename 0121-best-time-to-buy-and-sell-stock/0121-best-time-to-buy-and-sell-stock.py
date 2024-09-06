class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 只需要用两个parameter追踪，一个dp[0]代表卖的最低价，一个dp[1]代表最大的profit
        # dp[1]初始值为0，如果之后profit没有正数则保持0到最后
        dp = [0] * 2
        dp[0] = -prices[0]
        
        
        for i in range(1, n):
            dp[0] = max(dp[0], -prices[i])
            dp[1] = max(dp[1], dp[0] + prices[i])
        
        return dp[1]