class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]: 容量为i的背包，最少可以用几个硬币装满
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] == -1:
                    continue
                elif dp[i] == -1:
                    dp[i] = dp[i - coin] + 1
                else:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount]
                    
