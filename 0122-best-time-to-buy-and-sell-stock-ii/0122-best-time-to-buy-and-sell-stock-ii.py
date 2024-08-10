class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] > minVal:
                profit += prices[i] - minVal
            minVal = prices[i]
        
        return profit