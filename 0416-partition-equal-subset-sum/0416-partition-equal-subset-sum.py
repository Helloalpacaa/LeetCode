class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        # 背包容量为target，遍历nums，能填满就return True
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target] == target