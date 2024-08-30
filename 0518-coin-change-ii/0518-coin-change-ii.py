class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i]: 容量为i的amount有多少种方式组成
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]
        
        return dp[amount]