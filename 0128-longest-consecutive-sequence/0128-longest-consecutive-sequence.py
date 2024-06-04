class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        
        numsSet = set(nums)
            
        longest = 0
        
        for num in nums:
            if num - 1 in numsSet:
                continue
            
            currNum = num
            currLen = 1
            
            while currNum + 1 in numsSet:
                currNum += 1
                currLen += 1
            
            longest = max(longest, currLen)
        
        return longest