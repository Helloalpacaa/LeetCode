class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        ans = ""
        for i in range(len(s)):
            if len(self.expand(s, i, i)) > maxLength:
                maxLength = len(self.expand(s, i, i))
                ans = self.expand(s, i, i)
            if i + 1 < len(s) and len(self.expand(s, i, i + 1)) > maxLength:
                maxLength = len(self.expand(s, i, i + 1))
                ans = self.expand(s, i, i + 1)
        
        return ans
    
    def expand(self, s: str, i: int, j: int) -> str:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
            
        return s[i + 1: j]
            