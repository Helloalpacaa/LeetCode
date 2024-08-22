class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j]: 容量为i个0，j个1的背包，最多能放多少个subset
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for str in strs:
            zero = str.count('0')
            one = str.count('1')
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        
        return dp[m][n]
