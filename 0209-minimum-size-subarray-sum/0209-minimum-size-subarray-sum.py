class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        subArraySum = 0
        minSubArrayLen = sys.maxsize
        for j in range(len(nums)):
            subArraySum += nums[j]
            if subArraySum >= target:
                while subArraySum - nums[i] >= target:
                    subArraySum -= nums[i]
                    i += 1
                minSubArrayLen = min(minSubArrayLen, j - i + 1)
        
        return 0 if minSubArrayLen == sys.maxsize else minSubArrayLen