class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        return sum(nums[i] == 0 for i in range(len(nums)))