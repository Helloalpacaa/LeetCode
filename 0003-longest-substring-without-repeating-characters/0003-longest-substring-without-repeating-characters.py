class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = set()

        left = 0
        for right in range(len(s)):
            char = s[right]
            while char in window:
                window.remove(s[left])
                left += 1
            
            window.add(char)
            longest = max(longest, right - left + 1)
        
        return longest