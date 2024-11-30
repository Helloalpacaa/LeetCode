class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        # Sort the array
        nums.sort()
        
        # Initialize min_score with the case where we either add k to all
        # or subtract k from all
        min_score = nums[-1] - nums[0]
        
        # Try all possibilities where we add k to nums[0:i] and 
        # subtract k from nums[i:]
        for i in range(len(nums) - 1):
            # For the left part (0 to i), we add k
            # For the right part (i+1 to end), we subtract k
            local_max = max(nums[i] + k, nums[-1] - k)
            local_min = min(nums[0] + k, nums[i + 1] - k)
            min_score = min(min_score, local_max - local_min)
            
        return min_score

 