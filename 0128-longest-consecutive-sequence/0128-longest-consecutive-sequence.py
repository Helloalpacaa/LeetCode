class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        
        longest = 0
        length = 0
        for num in numsSet:
            if num - 1 in numsSet:
                continue
                
            length = 1
            currNum = num
            while currNum + 1 in numsSet:
                length += 1
                currNum += 1
            
            longest = max(longest, length)
        
        return longest
            