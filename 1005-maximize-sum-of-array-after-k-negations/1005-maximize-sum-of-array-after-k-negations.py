class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for _ in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] = -nums[min_index]
        
        return sum(nums)