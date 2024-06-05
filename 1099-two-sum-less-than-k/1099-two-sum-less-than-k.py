class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        i = 0
        j = len(nums) - 1
        twoSumMax = -1
        
        while i < j:
            twoSum = nums[i] + nums[j]
            if twoSum < k:
                twoSumMax = max(twoSumMax, twoSum)
                i += 1
            else:
                j -= 1
        
        return twoSumMax