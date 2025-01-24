class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occur = {}
        longest_substring = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in last_occur:
                left = last_occur[char] + 1
                del last_occur[char]
            
            last_occur[char] = right

            longest_substring = max(longest_substring, right - left + 1)
            
        return longest_substring