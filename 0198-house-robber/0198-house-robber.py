class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][0]:rob nums[i], which means you cannot rob nums[i - 1]
        # dp[i][1]: not rob nums[i], you can choose to rob nums[i - 1] or not
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = nums[0]
        dp[0][1] = 0

        for i in range(1, n):
            dp[i][0] = nums[i] + dp[i - 1][1]
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
        
        return max(dp[n - 1][0], dp[n - 1][1])

