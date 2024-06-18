class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            ans = 0
            counter = Counter()
            i = 0
            
            for j in range(len(nums)):
                counter[nums[j]] += 1
                
                while len(counter) > k:
                    counter[nums[i]] -= 1
                    if counter[nums[i]] == 0:
                        del counter[nums[i]]
                    i += 1
                
                ans += j - i + 1
            
            return ans
        
        return atMost(k) - atMost(k - 1)