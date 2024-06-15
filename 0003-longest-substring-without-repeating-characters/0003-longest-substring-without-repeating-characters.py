class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        i = 0
        ans = 0
        for j in range(len(s)):
            if s[j] in last and i <= last[s[j]]:
                i = last[s[j]] + 1
                
            print(i, j)
            ans = max(ans, j - i + 1) 
            last[s[j]] = j
        
        return ans