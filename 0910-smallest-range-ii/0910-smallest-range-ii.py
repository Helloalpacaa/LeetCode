class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        nums.sort()
        min_score = nums[-1] - nums[0]

        for i in range(len(nums) - 1):
            local_max = max(nums[-1] - k, nums[i] + k)
            local_min = min(nums[0] + k, nums[i + 1] - k)
            min_score = min(min_score, local_max - local_min)
            print(local_max, local_min, min_score)
        
        return min_score