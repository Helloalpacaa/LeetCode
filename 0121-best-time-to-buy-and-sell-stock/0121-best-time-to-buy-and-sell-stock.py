class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minValue = prices[0]

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minValue)
            minValue = min(minValue, prices[i])
        
        return maxProfit