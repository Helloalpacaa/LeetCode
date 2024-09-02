class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
            
        # dp1: 从index 0到index (n - 2)
        dp1 = [[0] * 2 for _ in range(n - 1)]
        dp1[0][0] = nums[0] #抢
        # dp2: 从index 1到index (n - 1)
        dp2 = [[0] * 2 for _ in range(n - 1)]
        dp2[0][0] = nums[1] #抢

        for i in range(1, n - 1):
            dp1[i][0] = dp1[i - 1][1] + nums[i] #抢
            dp1[i][1] = max(dp1[i - 1][0], dp1[i - 1][1]) #不抢
             
        for i in range(2, n):
            dp2[i - 1][0] = dp2[i - 2][1] + nums[i]
            dp2[i - 1][1] = max(dp2[i - 2][0], dp2[i - 2][1])

        
        return max(dp1[n - 2][0], dp1[n - 2][1], dp2[n - 2][0], dp2[n - 2][1])


