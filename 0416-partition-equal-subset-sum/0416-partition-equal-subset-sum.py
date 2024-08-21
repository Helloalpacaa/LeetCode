class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        # 背包容量为target，遍历nums，最多能装多少
        n = len(nums)
        dp = [0] * (target + 1)

        for num in nums:
            for j in range(target, -1, -1):
                if j >= num:
                    dp[j] = max(dp[j], dp[j - num] + num)

        return dp[target] == target