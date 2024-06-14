class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        charHm = {}
        i = 0
        ans = 0
        
        for j in range(len(s)):
            charHm[s[j]] = charHm.get(s[j], 0) + 1
            
            if len(charHm) <= k:
                ans = max(ans, j - i + 1)
                         
            while len(charHm) > k:
                charHm[s[i]] -= 1
                if charHm[s[i]] == 0:
                    del charHm[s[i]]
                i += 1
        
        return ans