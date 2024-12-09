class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        max_number = max(nums)
        freq = 0

        i = 0
        for j in range(len(nums)):
            if nums[j] == max_number:
                freq += 1
            
            while freq >= k:
                count += len(nums) - j
                if nums[i] == max_number:
                    freq -= 1
                i += 1
        
        return count