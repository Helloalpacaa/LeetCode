class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        sign = 0
        count = 1

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1] and sign >= 0:
                count += 1
                sign = -1
            elif nums[i] > nums[i - 1] and sign <= 0:
                count += 1
                sign = 1
        
        return count