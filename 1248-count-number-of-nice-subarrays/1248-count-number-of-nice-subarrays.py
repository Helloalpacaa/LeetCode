class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k) -> int:
            i = 0
            ans = 0
            oddNum = 0
            
            for j in range(len(nums)):
                if nums[j] % 2 != 0:
                    oddNum += 1
                
                while oddNum > k:
                    if nums[i] % 2 != 0:
                        oddNum -= 1
                    i += 1
                    
                ans += j - i + 1
            
            return ans
                
        return atMost(k) - atMost(k - 1)