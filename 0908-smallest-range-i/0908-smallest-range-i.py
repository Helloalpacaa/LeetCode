class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if max(nums) - min(nums) <= k * 2:
            return 0
        else:
            return max(nums) - min(nums) - k * 2