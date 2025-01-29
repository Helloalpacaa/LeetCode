class Solution:
    def canJump(self, nums: List[int]) -> bool:
        coverage = 0
        i = 0
        while i <= min(coverage, len(nums) - 1):
            coverage = max(coverage, i + nums[i])
            i += 1
            if coverage >= len(nums) - 1:
                return True
        
        return False