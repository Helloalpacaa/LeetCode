class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest_substring = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            while char in window:
                window.remove(s[left])
                left += 1
            
            window.add(char)

            longest_substring = max(longest_substring, right - left + 1)
        
        return longest_substring