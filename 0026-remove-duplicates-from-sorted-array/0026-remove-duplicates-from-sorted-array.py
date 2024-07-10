class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                nums[count] = nums[i]
                count += 1
        
        return count