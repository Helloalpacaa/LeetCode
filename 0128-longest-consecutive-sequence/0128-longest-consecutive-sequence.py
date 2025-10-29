class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in nums:
                continue
            
            y = num + 1
            while y in nums:
                y = y + 1

            longest = max(longest, y - num)
        
        return longest