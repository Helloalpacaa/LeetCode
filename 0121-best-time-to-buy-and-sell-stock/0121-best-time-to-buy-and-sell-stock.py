class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        
        return max_profit