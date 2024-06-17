class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = Counter()
        ans = 0
        i = 0
        
        for j in range(len(s)):
            counter[s[j]] += 1
            
            while len(counter) > 2:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
            
            ans = max(ans, j - i + 1)
            
        return ans
                
                