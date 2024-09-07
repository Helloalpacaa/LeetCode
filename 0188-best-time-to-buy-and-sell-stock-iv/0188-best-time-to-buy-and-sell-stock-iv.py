class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        hold = [-prices[0]] * (k + 1)
        not_hold = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                hold[i] = max(hold[i], not_hold[i - 1] - price)
                not_hold[i] = max(not_hold[i], hold[i] + price)
        
        return not_hold[k]