class Solution:
    def canJump(self, nums: List[int]) -> bool:
        coverage = nums[0]
        i = 0

        while i <= coverage:
            coverage = max(coverage, i + nums[i])
            if coverage >= len(nums) - 1:
                return True
            i += 1

        return False
