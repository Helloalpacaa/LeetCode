class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        for i in range(0, len(nums)):
            coverage = i + nums[i]
            for c in range(i + 1, min(coverage + 1, len(nums))):
                dp[c] = min(dp[c], dp[i] + 1)
        
        return dp[len(nums) - 1]