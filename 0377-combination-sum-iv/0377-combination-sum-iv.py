class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i]: 容量为target的背包有多少种方式装满
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(len(dp)):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]
