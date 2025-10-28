class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if len(nums) == 1:
        #     return True

        target = len(nums) - 1
        coverage = 0
        i = 0

        while i < len(nums) and i <= coverage:
            coverage = max(coverage, i + nums[i])
            if coverage >= target:
                return True
            i += 1
        
        return False