class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {val: idx for idx, val in enumerate(nums)}

        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in hm and hm[sub] != i:
                return [i, hm[sub]]
        