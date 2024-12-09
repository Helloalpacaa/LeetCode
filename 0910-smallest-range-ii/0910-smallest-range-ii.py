class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        nums.sort()
        score = nums[-1] - nums[0]

        for i in range(len(nums) - 1):
            max_number = max(nums[-1] - k, nums[i] + k)
            min_number = min(nums[0] + k, nums[i + 1] - k)
            score = min(score, max_number - min_number)
        
        return score