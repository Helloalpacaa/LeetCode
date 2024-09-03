class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        
        # Initialize the two state variables
        not_holding = [0] * (k + 1)
        holding = [-float('inf')] * (k + 1)
        
        for price in prices:
            for i in range(1, k + 1):
                # Update holding state
                holding[i] = max(holding[i], not_holding[i-1] - price)
                
                # Update not_holding state
                not_holding[i] = max(not_holding[i], holding[i] + price)
        
        return not_holding[k]