class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if min(nums) + k >= max(nums) - k:
            return 0
        else:
            return max(nums) - min(nums) - 2 * k