class Solution:
    def canJump(self, nums: List[int]) -> bool:
        boundry = nums[0]

        i = 0
        while i <= boundry:
            boundry = max(boundry, i + nums[i])
            if boundry >= len(nums) - 1:
                return True
            i += 1
        
        return False