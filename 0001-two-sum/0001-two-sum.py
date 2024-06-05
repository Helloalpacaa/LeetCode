class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
            
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in numsMap:
                return [i, numsMap[compliment]]
            numsMap[nums[i]] = i