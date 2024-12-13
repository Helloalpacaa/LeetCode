class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            if nums[i] == 0:
                count += 1
        
        return count