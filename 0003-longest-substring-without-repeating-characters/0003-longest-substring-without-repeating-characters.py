class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        longest = 0
        for end in range(len(s)):
            while s[end] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[end])
            longest = max(longest, len(window))
        
        return longest