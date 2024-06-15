class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sortedList = []
        i = 0
        
        for j in range(len(nums)):
            bisect.insort(sortedList, nums[j])
            
            if sortedList[-1] - sortedList[0] > limit:
                sortedList.pop(bisect.bisect(sortedList, nums[i]) - 1)
                i += 1
        
        return len(nums) - i
        