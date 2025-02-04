class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = 0
        max_sub = float('-inf')

        for num in nums:
            sub += num
            max_sub = max(max_sub, sub)

            if sub < 0:
                sub = 0
            
        return max_sub