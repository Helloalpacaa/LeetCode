class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # left + right = sum
        # left - right = target
        if (sum(nums) + target) % 2 != 0:
            return 0
        
        if sum(nums) + target < 0:
            return 0

        left = (sum(nums) + target) / 2
    
        # dp[j]: 容量为j的背包，有多少种方式填满
        left = int(left)
        dp = [0] * (left + 1)
        dp[0] = 1
        for num in nums:
            for j in range(left, num - 1, -1):
                dp[j] += dp[j - num]
        
        print(dp)
        
        return dp[left]