class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n):
            dp[i + 1][0] = dp[i][1] + nums[i] #抢
            dp[i + 1][1] = max(dp[i][0], dp[i][1]) #不抢
        
        return max(dp[n][0], dp[n][1])
