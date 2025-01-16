class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1) # dp[i] represents max sum from index i to end

        for i in range(n - 1, -1, -1):
            # Try all possible lengths from 1 to k
            curr_max = 0
            for length in range(min(k, n - i)):
                # Find maximum in current window
                curr_max = max(curr_max, arr[i + length])
                # Calculate sum for this partition and add remaining best sum
                curr_sum = curr_max * (length + 1) + dp[i + length + 1]
                dp[i] = max(dp[i], curr_sum)
        
        return dp[0]