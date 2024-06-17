class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        i = 0
        windowSum = 0
        
        for j in range(len(nums)):
            windowSum += nums[j]
            
            while windowSum >= target:
                ans = min(ans, j - i + 1)
                windowSum -= nums[i]
                i += 1
            
        return 0 if ans == float('inf') else ans