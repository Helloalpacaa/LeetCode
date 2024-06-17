class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        ans = 0
        i = 0
        
        for j in range(len(s)):
            while counter[s[j]] > 0:
                counter[s[i]] -= 1
                i += 1
            
            counter[s[j]] += 1
            
            ans = max(ans, j - i + 1)
        
        return ans