class Solution:
    def numDecodings(self, s: str) -> int:
        if s is None or s[0] == '0':
            return 0
        n = len(s)
        # dp[i] : the number of ways to decode s[:i]
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, n):
            if int(s[i]) > 0:
                dp[i + 1] += dp[i]
            if s[i - 1] != '0' and 1 <= int(s[i - 1: i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]
        
        print(dp)
        return dp[n]


