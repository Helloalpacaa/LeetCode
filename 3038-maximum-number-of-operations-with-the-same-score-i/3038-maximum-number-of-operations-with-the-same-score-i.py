class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0] + nums[1]
        operation = 1

        for i in range(2, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] == score:
                operation += 1
            else:
                break
        
        return operation
