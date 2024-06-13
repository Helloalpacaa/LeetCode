class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        subArraySum = 0
        minSubArrayLen = float('inf')
        
        for j in range(len(nums)):
            subArraySum += nums[j]
            
            while subArraySum >= target:
                minSubArrayLen = min(minSubArrayLen, j - i + 1)
                subArraySum -= nums[i]
                i += 1

        return 0 if minSubArrayLen == float('inf') else minSubArrayLen