class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var max_profit = 0
        var min_price = prices[0]

        for price in prices {
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        }

        return max_profit
        
    }
}