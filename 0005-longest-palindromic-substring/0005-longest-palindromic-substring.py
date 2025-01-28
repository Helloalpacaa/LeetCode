class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def palindrome(left, right) -> str:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        
        longest_palindrome = ""
        for i in range(n):
            palindrome1 = palindrome(i, i)
            palindrome2 = palindrome(i, i + 1)
            longest_palindrome = palindrome1 if len(palindrome1) > len(longest_palindrome) else longest_palindrome
            longest_palindrome = palindrome2 if len(palindrome2) > len(longest_palindrome) else longest_palindrome

        return longest_palindrome