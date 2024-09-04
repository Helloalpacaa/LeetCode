class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]: 以nums[i]为结尾的longest continuous increasing subsequence
        dp = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        
        return max(dp)
