class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # dp[i][j]: the maximum score of the first i elements dividing in k groups
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Initialize the largest sum when k == 1
        for i in range(1, n + 1):
            dp[i][1] = prefix_sum[i] / i
        
        # fill in the dp array
        for k in range(2, k + 1):
            for i in range(k, n + 1):
                for j in range(1, i):
                    curr_max = dp[j][k - 1] + (prefix_sum[i] - prefix_sum[j]) / (i - j)
                    dp[i][k] = max(dp[i][k], curr_max)
        
        return dp[n][k]

