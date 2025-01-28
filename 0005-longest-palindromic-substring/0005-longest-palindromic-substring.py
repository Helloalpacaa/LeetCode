class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def palindrome(left, right) -> str:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        
        longest_palindrome = ""
        longest = 0
        for i in range(n):
            valid_palindrome = palindrome(i, i)
            
            if len(valid_palindrome) > longest:
                longest_palindrome = valid_palindrome
                longest = len(valid_palindrome)
            if i + 1 < n and s[i] == s[i + 1]:
                valid_palindrome = palindrome(i, i + 1)
                if len(valid_palindrome) > longest:
                    longest_palindrome = valid_palindrome
                    longest = len(valid_palindrome)

        return longest_palindrome