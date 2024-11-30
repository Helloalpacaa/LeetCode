class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        count = 0

        frequency = 0
        i = 0
        for j in range(len(nums)):
            char = nums[j]
            if nums[j] == max_element:
                frequency += 1
            while frequency >= k:
                count += (len(nums) - j)
                if nums[i] == max_element:
                    frequency -= 1
                i += 1
                
        return count