class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        twoSum = -1
        
        while i < j:
            total = nums[i] + nums[j]
            if total < k:
                twoSum = max(twoSum, total)
                i += 1
            else:
                j -= 1
        
        return twoSum