class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [[0] * 2 for _ in range(n)]
        # dp[0][0] = nums[0] # 0 = rob, 1 = not_rob
        rob = nums[0]
        not_rob = 0

        for i in range(1, len(nums)):
            # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + nums[i])
            # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0])
            tmp = rob
            rob = max(rob, not_rob + nums[i])
            not_rob = max(not_rob, tmp)
        
        # return max(dp[n - 1][0], dp[n - 1][1])
        return max(rob, not_rob)