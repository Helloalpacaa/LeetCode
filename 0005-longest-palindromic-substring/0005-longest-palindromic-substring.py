class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ""
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)
            longestPalindrome = s1 if len(s1) > len(longestPalindrome) else longestPalindrome
            longestPalindrome = s2 if len(s2) > len(longestPalindrome) else longestPalindrome
        
        return longestPalindrome
        
        
    def palindrome(self, s: str, i: int, j: int) -> str:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        return s[i + 1: j]
            
            