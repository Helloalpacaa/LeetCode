class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k) -> int:
            ans = 0
            i = 0
            diffInt = Counter()
            
            for j in range(len(nums)):
                diffInt[nums[j]] += 1
                
                while len(diffInt) > k:
                    diffInt[nums[i]] -= 1
                    if diffInt[nums[i]] == 0:
                        del diffInt[nums[i]]
                    i += 1
                
                ans += j - i + 1
            
            return ans
        
        return atMost(k) - atMost(k - 1)