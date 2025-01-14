class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        max_reach = nums[0]
        i = 0

        while i in range(max_reach + 1):
            max_reach = max(max_reach, i + nums[i])
            print(max_reach)
            if max_reach >= len(nums) - 1:
                return True
            i += 1

        return False
