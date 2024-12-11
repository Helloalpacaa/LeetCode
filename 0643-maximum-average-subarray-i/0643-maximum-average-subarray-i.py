class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        ans = float('-inf')
        windowSum = 0
        
        for j in range(len(nums)):
            windowSum += nums[j]
            if j - i + 1 == k:
                ans = max(ans, windowSum / k)
                windowSum -= nums[i]
                i += 1
        
        return ans
        