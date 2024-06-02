class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if nums:
            total = sum(nums)
            minNum = min(nums)
            m = total - minNum * len(nums)
        
        return m