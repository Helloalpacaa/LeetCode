class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            if i > k * 2:
                curr_sum -= nums[i - k * 2 - 1]
            
            if i >= k * 2:
                ans[i - k] = curr_sum // (k * 2 + 1)
        
        return ans
            