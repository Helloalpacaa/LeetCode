class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # left代表未经被改变符号的部分
        # right代表符号被改变了的部分
        # left + right = target
        # left - right = sum(nums)
        if (target + sum(nums)) % 2 != 0:
            return 0

        left = (target + sum(nums)) // 2
        if left < 0:
            return 0
            
        # dp[i]: 装满背包容量为i有多少种方法
        dp = [0] * (left + 1)
        dp[0] = 1

        for num in nums:
            for i in range(left, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[left]

        
