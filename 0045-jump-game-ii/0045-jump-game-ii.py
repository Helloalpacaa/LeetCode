class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        end = 0
        furthest = 0

        for i in range(len(nums)):
            furthest = max(furthest, i + nums[i])
            if i == end:
                jumps += 1
                end = furthest
                if end >= len(nums) - 1:
                    break
        
        return jumps
