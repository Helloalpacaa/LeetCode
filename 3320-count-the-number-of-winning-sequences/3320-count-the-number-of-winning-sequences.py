class Solution:
    def countWinningSequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        s = ['FWE'.find(c) for c in s] # convert string to list for indices

        # dp[i][j] is a Counter where:
        # - i is the current round
        # - j is Bob's current move(0: F, 1: W, 2: E)
        # - The Counter's key is the score difference, value is the number of ways to achieve it
        dp = [[Counter() for j in range(3)] for i in range(n)]

        for i in range(n):
            for j in range(3): # Bob's current move
                # Calculate score difference for this round
                # j - s[i]: calculate the difference between Bob's and Alice's moves
                # + 1: shift is added to ensure we always have a positive number before applying the module operation
                # % 3: wraps the result around to keep it in the range 0-2
                # -1: shifts the range to -1, 0, or 1
                d = (j - s[i] + 1) % 3 - 1

                if i == 0: # First round
                    dp[i][j][d] = 1
                else:
                    for j2 in range(3): # Bob's previous move
                        if j != j2: # Current move cannot be as same as previous move
                            # Iterates over all the score differences v and their counts from the previous round i -1 when Bob's last move was j2
                            for v, count in dp[i - 1][j2].items():
                                # 其实就是dp[i][j][v + d] += count
                                dp[i][j][v + d] = (dp[i][j][v + d] + count) % MOD
        
        ans = 0
        for j in range(3):
            for v in range(1, n + 1):
                ans += dp[n - 1][j][v]
        ans = ans % MOD

        return ans
