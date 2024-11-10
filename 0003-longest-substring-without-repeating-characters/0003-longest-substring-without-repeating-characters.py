class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        ans = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            while char in window:
                window[s[left]] = window.get(s[left]) - 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            
            window[char] = window.get(char, 0) + 1
            ans = max(ans, right - left + 1)
            
        return ans
