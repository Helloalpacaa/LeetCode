class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(i: int, j: int) -> str:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            return s[i + 1: j]
        
        ans = ""
        for i in range(len(s)):
            s1 = palindrome(i, i)
            s2 = palindrome(i, i + 1)
            ans = s1 if len(s1) > len(ans) else ans
            ans = s2 if len(s2) > len(ans) else ans
        
        return ans
            