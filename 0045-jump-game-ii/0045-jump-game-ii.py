class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        furthest = 0
        end = 0

        for i in range(len(nums) - 1):
            furthest = max(furthest, nums[i] + i)
            if end == i:
                jumps += 1
                end = furthest
        
        return jumps