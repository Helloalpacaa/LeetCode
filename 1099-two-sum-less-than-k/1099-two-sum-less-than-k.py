class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        maxSum = -1
        
        while i < j:
            currSum = nums[i] + nums[j]
            if currSum < k:
                maxSum = max(currSum, maxSum)
                i += 1
            else:
                j -= 1
        
        return maxSum
        