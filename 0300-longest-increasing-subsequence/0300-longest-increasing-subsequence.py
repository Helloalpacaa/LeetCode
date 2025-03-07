class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [1] * n

        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        
        # return max(dp)

        sub = []
        
        for num in nums:
            idx = bisect_left(sub, num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        
        return len(sub)
