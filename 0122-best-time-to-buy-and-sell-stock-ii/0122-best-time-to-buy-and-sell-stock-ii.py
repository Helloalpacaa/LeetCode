class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minVal = prices[0]
        profit = 0

        for i in range(1, n):
            if prices[i] > minVal:
                profit += prices[i] - minVal
            
            minVal = prices[i]
        
        return profit