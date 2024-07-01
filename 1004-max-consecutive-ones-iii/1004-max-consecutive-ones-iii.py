class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        i = 0
        
        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            
            while k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            
            ans = max(ans, j - i + 1)
        
        return ans