class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心：取最左最小值，取最右最大值，那么得到的差就是最大利润
        profit = 0
        minValue = float('inf')

        for price in prices:
            minValue = min(minValue, price)
            profit = max(profit, price - minValue)

        return profit
