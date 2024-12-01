class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # [1, 10, 6, 9], k = 2
        # [3, 8, 4, 7]
        # [1, 6, 9, 10]
        nums.sort()
        min_score = nums[-1] - nums[0]

        for i in range(len(nums) - 1):
            local_min = min(nums[0] + k, nums[i + 1] - k)
            local_max = max(nums[-1] - k, nums[i] + k)
            min_score = min(min_score, local_max - local_min)
        
        return min_score