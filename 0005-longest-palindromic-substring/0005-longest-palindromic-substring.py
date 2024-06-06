class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            s1 = self.palindromeLength(s, i, i)
            s2 = self.palindromeLength(s, i, i + 1)
            ans = ans if len(ans) > len(s1) else s1
            ans = ans if len(ans) > len(s2) else s2
        
        return ans
    
    def palindromeLength(self, s: str, i: int, j: int) -> str:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        return s[i + 1: j]