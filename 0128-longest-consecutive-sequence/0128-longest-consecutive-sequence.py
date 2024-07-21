class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        ans = 0

        for num in nums:
            if num - 1 in numsSet:
                continue
            
            curr = num
            count = 1
            while curr + 1 in numsSet:
                count += 1
                curr += 1
            ans = max(ans, count)
        
        return ans