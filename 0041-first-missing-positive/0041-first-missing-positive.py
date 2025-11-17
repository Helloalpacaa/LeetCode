class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # starting from 1, check if 1 .. n in the correct place in nums
        # while the current num is a number that shouldn't be here, switch them

        # the lowest positive numbers starting from [1, 2, 3 ... ]
        # correct position, if n == 3 -> index should be 2,  index = n - 1

        # 把[1, 2, 3 ... n]放在它正确的位置上
        # [3, 4, -1, 1]
        # [-1, 4, 3, 1]
        # [-1, 1, 3, 4]
        # [1, -1, 3, 4]
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
