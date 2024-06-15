class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sortedList = [] # sorted list to continuesly adding nums and sort them
        i = 0
        
        for j in range(len(nums)):
            # use binary search to insert num
            bisect.insort(sortedList, nums[j])
            
            # when max - min >limit
            if sortedList[-1] - sortedList[0] > limit:
                # move i, so we need to pop nums[i] from sortedList
                # use bisect.bisect to find the index of nums[i]
                sortedList.pop(bisect.bisect(sortedList, nums[i]) - 1)
                # move i one step, because we moved j, if the condition is not meet and we move i, the length of longest subarray won't change
                i += 1
        
        return len(nums) - i
        