class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        total = 0

        for i in range(len(nums)):
            if nums[i] >= total and total < 0:
                total = nums[i]
            else:
                total += nums[i]

            ans = max(ans, total)
        
        return ans