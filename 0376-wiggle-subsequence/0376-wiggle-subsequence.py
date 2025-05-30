class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [1] * n
        down = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = up[i - 1] + 1
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        
        return max(up[n - 1], down[n - 1])



        # up = 1
        # down = 1

        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i - 1]:
        #         up = down + 1
        #     elif nums[i] < nums[i - 1]:
        #         down = up + 1
        
        # return max(up, down)
            