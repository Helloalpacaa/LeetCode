class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            else:
                nums[count] = nums[i]
                count += 1
        
        return count