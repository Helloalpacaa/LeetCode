class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        while i < len(nums) and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        
        minVal = float('inf')
        for num in nums:
            minVal = min(minVal, num)
        
        return sum(nums) - (k % 2) * minVal * 2

        
