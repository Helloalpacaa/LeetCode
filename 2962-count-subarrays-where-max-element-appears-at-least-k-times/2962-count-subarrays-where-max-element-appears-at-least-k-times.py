class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        count = 0

        window = {}
        i = 0
        for j in range(len(nums)):
            char = nums[j]
            window[char] = window.get(char, 0) + 1
            while max_element in window and window[max_element] >= k:
                count += (len(nums) - j)
                window[nums[i]] -= 1
                i += 1
                
        
        return count