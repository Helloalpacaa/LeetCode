class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            curr_max = 0

            for length in range(min(k, n - i)):
                curr_max = max(curr_max, arr[i + length])
                curr_sum = curr_max * (length + 1) + dp[i + length + 1]
                dp[i] = max(dp[i], curr_sum)
        
        return dp[0]